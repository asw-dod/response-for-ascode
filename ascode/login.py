import time
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import html
import re

def login(driver, id: str, pw: str):
    driver.get("http://ascode.org/index.php")
    time.sleep(0.5)
    driver.find_element(By.LINK_TEXT, "로그인").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, u"//a[contains(text(),'로그인')]").click()
    time.sleep(0.5)
    driver.find_element(By.NAME, "user_id").click()
    driver.find_element(By.NAME, "user_id").clear()
    driver.find_element(By.NAME, "user_id").send_keys(id)
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(pw)
    driver.find_element(By.NAME, "submit").click()
    time.sleep(0.5)
    driver.refresh()

def get_discuss_list(driver, host_id: str, url = 'http://ascode.org/discuss3/discuss.php'):
    driver.get(url)
    data = driver.find_elements(By.XPATH, '/html/body/div[1]/div/center/div/table/tbody/tr')
    result = []
    for item in data[1:]:
        d = item.find_elements(By.XPATH, 'td')
        elem = {
            'id': d[2].text,
            'author': d[3].text,
            'title': d[4].text,
            'post-date': d[5].text,
            'url': d[4].find_element(By.XPATH, "a").get_attribute('href')
        }

        norm = filter_data(elem)
        if norm != None:
            elem['issue'] = norm
            result.append(elem)
            
    result = list(filter(lambda x: check_answer(driver, host_id, x['url']), result))
    return result

def filter_data(x):
    now = datetime.now()
    dt = datetime.strptime(x['post-date'], "%Y-%m-%d")
    delta = now - dt
    hour = delta.total_seconds() / 3600
    if hour >= 72:
        return None
    numbers = re.findall(r"\[(\d+)\]", x['title'])
    if len(numbers) != 1:
        return None
    
    # print(numbers)  # 결과: ['숫자']
    return numbers[0]

def check_answer(driver, host_id: str, x: str):
    driver.get(x)
    data = driver.find_elements(By.XPATH, '/html/body/div[1]/div/center/div/table/tbody/tr')
    d = data[1:]
    for row in d: 
        p = row.find_element(By.XPATH, 'td/div[1]')
        id = p.text.split('@')[0].strip()
        if host_id == id:
            return False # Exist
    return True
        

def get_code(driver):
    code = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/table/tbody/tr/td[2]/div')
    code = code.text.split('/**************************************************************')[1]
    code = code.split('****************************************************************/')[0]
    code = code.split('User: ')[1].split("Language")[0].strip()
    return code

def get_error(driver):
    a = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/table/tbody/tr/td[2]')
    text = html.escape(a.text)
    text = text.replace("\\n", "\n")
    return text

def write_error_message_to_discuss(driver, item):
    driver.get('http://ascode.org/ceinfo.php?sid={0}'.format(item['issue']))
    time.sleep(0.5)
    if item['author'] == get_code(driver):
        err = get_error(driver)
        driver.get(item['url'])
        time.sleep(0.5)
        driver.find_element(By.ID, "replyContent").click()
        driver.find_element(By.ID, "replyContent").clear()
        driver.find_element(By.ID, "replyContent").send_keys(err)
        driver.find_element(By.XPATH, "//input[@value='Submit']").click()