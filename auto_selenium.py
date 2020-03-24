from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome("/root/chromedriver", options=chrome_options)

driver.get("https://eip.kx.com.tw/kxeip/") #先進入擎昊網頁
driver.find_element_by_name("txtAccount").send_keys("eric.yang")
driver.find_element_by_name("txtPassword").send_keys("KX#08564.")
driver.find_element_by_id("btnLogin").click()

driver.get("https://eip.kx.com.tw/KxEIP/Modules/Personal/PersonalWorkLog")
driver.find_element_by_class_name("btnBatchFix").click()


time.sleep(3)  #停止3秒
driver.close()  #關閉網頁


