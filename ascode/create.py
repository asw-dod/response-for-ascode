from selenium import webdriver

def driver_create():
    options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    options.add_argument('user-agent=' + user_agent)
    options.add_argument("window-size=1920x1080") # 화면크기(전체화면)
    options.add_argument('--start-maximized') #브라우저가 최대화된 상태로 실행됩니다.
    options.add_argument('--start-fullscreen') #브라우저가 풀스크린 모드(F11)로 실행됩니다.
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu") 
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    
    return driver