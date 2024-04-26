import os

from ascode import *
from dotenv import load_dotenv

driver = driver_create()

load_dotenv()
ascode_id = os.environ['ASCODE_USERID']
ascode_pw = os.environ['ASCODE_USERPW']

login(driver, ascode_id, ascode_pw)
items = get_discuss_list(driver, ascode_id)

for item in items:
    write_error_message_to_discuss(driver, item)
