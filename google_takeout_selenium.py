from selenium import webdriver
from bs4 import BeautifulSoup
import time




options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('/home/dell/Documents/Aha-Loans/Practicing/Selenium/IncomeTaxAutoamtion/chromedriver', options = options)
driver.set_window_size(1024,600)
driver.maximize_window()
driver.delete_all_cookies()
print("Wroking")
# time.sleep(20)
driver.get('https://accounts.google.com/signin/v2/identifier?passive=1209600&osid=1&continue=https%3A%2F%2Ftakeout.google.com%2F&followup=https%3A%2F%2Ftakeout.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.find_element_by_id('identifierId').send_keys('prathvi16.ps@gmail.com')
print("User ID")
driver.find_element_by_xpath('//*[@id="identifierNext"]/content').click()
print("Clicked next")
# driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('prathvishakti')
time.sleep(5)
driver.find_element_by_css_selector("input.whsOnd.zHQkBf").send_keys('sunshine@16')

driver.find_element_by_xpath('//*[@id="passwordNext"]/content').click()
time.sleep(5)

# driver.find_element_by_xpath("//*[@span='Select none']").click()

print("Executed Next")
driver.find_element_by_xpath('//*[@id="i4"]/div[1]/div/table/thead/tr/th[3]/div/div').click()
print("Executed Select None")
time.sleep(5)

driver.find_element_by_xpath('//*[@id="i70"]/tr[1]/td[6]').click()
print("Location History")
time.sleep(5)

driver.find_element_by_xpath('//*[@id="i4"]/div[2]/div[1]').click()
# driver.find_element_by_css_selector("div.U26fgb.O0WRkf.zZhnYe.e3Duub.C0oVfc.M9Bg4d").click()
print("Executed Next")
time.sleep(5)

driver.find_element_by_xpath('//*[@id="i104"]/div[2]/div').click()

print("Executed Create Archive")

time.sleep(30)
driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/c-wiz/div[2]/div/div[3]/div[1]/table/tbody[1]/tr[1]/td[7]/div/div').click()
print("Executed Download Archive")


# driver.close()