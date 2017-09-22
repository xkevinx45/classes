import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.marinenet.usmc.mil/')
#time.sleep(2) # Let the user actually see something!
driver.find_element_by_id("btn").click()
#time.sleep(2)
UserName = driver.find_element_by_name('ctl00$content$Login1$UserName')
UserName.send_keys('kevin.r.neely')
Password = driver.find_element_by_name('ctl00$content$Login1$Password')
Password.send_keys('ZZZZZzzzzz!!!!!11111')
#time.sleep(2)
driver.find_element_by_id("ctl00_content_Login1_LoginButton").click()
driver.find_element_by_id('ctl00_content_ucTranscript_grdTranscripts_ctl03_btnLaunchCourse').click()
driver.find_element_by_id('ctl00_content_btnGo').click()
driver.execute_script('javascript:buttonHandler(NextBtn,NextBtn.disabled ); return false;')
