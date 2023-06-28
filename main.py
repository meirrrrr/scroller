import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("")
time.sleep(2)
scroll_pause_time = 0.5
screen_height = driver.execute_script("return window.screen.height;")
i = 1

while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if screen_height * i > scroll_height:
        break
