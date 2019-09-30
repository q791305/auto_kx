from selenium.webdriver import Chrome #設定用python控制網頁的函式庫
import time

driver = Chrome("./chromedriver")
driver.get("https://eip.kx.com.tw/kxeip/") #先進入擎昊網頁
driver.find_element_by_name("txtAccount").send_keys("")
driver.find_element_by_name("txtPassword").send_keys("")
driver.find_element_by_id("btnLogin").click()

driver.get("https://eip.kx.com.tw/KxEIP/Modules/Personal/PersonalWorkLog")
driver.find_element_by_class_name("btnBatchFix").click()


time.sleep(3)  #停止3秒
driver.close()  #關閉網頁

