import os
from dotenv import load_dotenv
from ascode import *
import logging

logging.basicConfig(format='[main] %(levelname)s : %(message)s ', level=logging.DEBUG)

load_dotenv(override=True)

ascode_id = os.getenv('ASCODE_USERID')
ascode_pw = os.getenv('ASCODE_USERPW')
duration = os.getenv('DURATION_PER_CHECK')

if __name__ == "__main__":
    while True:
        driver = driver_create()
        login(driver, ascode_id, ascode_pw)
        items = get_discuss_list(driver, ascode_id)

        for item in items:
            logging.info(item)
            write_error_message_to_discuss(driver, item)

        driver.quit()
        time.sleep(float(duration))
