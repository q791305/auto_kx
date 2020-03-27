from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

mail=os.popen('cat /root/auto_python/file3').read().replace("\n", "")
account=os.popen('cat /root/auto_python/.file1').read().replace("\n", "")
key=os.popen('cat /root/auto_python/.file2').read().replace("\n", "")
try:

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome("/root/auto_python/chromedriver", options=chrome_options)
  
    driver.get("https://eip.kx.com.tw/kxeip/") #先進入擎昊網頁
    driver.find_element_by_name("txtAccount").send_keys(account)
    driver.find_element_by_name("txtPassword").send_keys(key)
    driver.find_element_by_id("btnLogin").click()

    driver.get("https://eip.kx.com.tw/KxEIP/Modules/Personal/PersonalWorkLog")
    driver.find_element_by_class_name("btnBatchFix").click()


    time.sleep(3)  #停止3秒
    driver.close()  #關閉網頁

except:
    os.system('echo "打卡處理失敗" | mailx -r "python@auto" -S smtp="{0}" -s "[ERROR]打卡失敗" {1}@kx.com.tw'.format(mail,account))
  
else:
    os.system('echo "打卡成功" | mailx -r "python@auto" -S smtp="{0}" -s "[SUCCESS]打卡成功" {1}@kx.com.tw'.format(mail,account))
  
