from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome('/home/ahaloans/Documents/AhaLoans/Production/Selenium/DrivingLicenseSarathi/Selenium-Google-Takeout/chromedriver')
driver.set_window_size(1024,600)
driver.maximize_window()
driver.delete_all_cookies()
print("Working")

driver.get('https://sarathi.nic.in:8443/nrportal/sarathi/DlDetRequest.jsp')
driver.find_element_by_id('dlform:DLNumber').send_keys('Up8720140002671')
driver.find_element_by_id('dlform:dob').send_keys('06/07/1989')
driver.find_element_by_id('dlform:sub').click()


