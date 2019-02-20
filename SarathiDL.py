from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import json


def scrapping_data(DL_no, DOB):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(
        '/home/ahaloans/Documents/AhaLoans/Production/Selenium/DrivingLicenseSarathi/Selenium-Google-Takeout/chromedriver',
        options=options)
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    driver.delete_all_cookies()
    print("Working")

    try:
        driver.get('https://sarathi.nic.in:8443/nrportal/sarathi/DlDetRequest.jsp')
        # driver.find_element_by_id('dlform:DLNumber').send_keys('Up8720140002671')
        # driver.find_element_by_id('dlform:dob').send_keys('06/07/1989')

        driver.find_element_by_id('dlform:DLNumber').send_keys('Up6320140016332')
        driver.find_element_by_id('dlform:dob').send_keys('20/07/1994')

        # driver.find_element_by_id('dlform:DLNumber').send_keys(DL_no)
        # driver.find_element_by_id('dlform:dob').send_keys(DOB)

        driver.find_element_by_id('dlform:sub').click()
        html = driver.page_source
        soup = BeautifulSoup(html)

        result = dict()
        result_inner = dict()

        form_fetch = soup.find_all('table')
        ### Driving Licence Details
        ##Details of Driving Licence

        row_fetch = form_fetch[1].find_all('tr')
        data_fetch = row_fetch[0].get_text()
        data = data_fetch.split('\n')[1].split(':')
        result_inner[data[0]] = data[1]
        title = data[0]

        ## Status

        row_fetch = form_fetch[2].find_all('tr')
        data_fetch = row_fetch[0].get_text()
        data = data_fetch.split('\n')
        result_inner[data[2][:-2]] = data[3]

        ## Last Transacted
        row_fetch = form_fetch[3].find_all('td')
        array_text = []
        for data in row_fetch:
            array_text.append(data.get_text())
        result_inner[array_text[0][1:-2]] = array_text[1]
        result_inner[array_text[2][1:-2]] = array_text[3]

        row_fetch = form_fetch[4].find_all('td')
        result_inner[row_fetch[0].get_text()[1:-2]] = row_fetch[1].get_text()
        result[title] = result_inner

        ### DL Validity
        title = 'DL Validity'
        result_inner = dict()
        result_inner_text = dict()
        row_fetch = form_fetch[5].find_all('td')
        array_text = []
        array_text = row_fetch[0].get_text()
        array_text = array_text.split('\n')[4:-21]
        # array_text = filter(bool, array_text) # fastest

        result_inner_text[array_text[2][:-2]] = array_text[3]
        result_inner_text[array_text[5][:-2]] = array_text[6]
        result_inner[array_text[0][:-2]] = result_inner_text

        result_inner_text = dict()
        result_inner_text[array_text[12][:-2]] = array_text[13]
        result_inner_text[array_text[15][:-2]] = array_text[16]
        result_inner[array_text[10][:-1]] = result_inner_text

        result_inner[array_text[20][:-2]] = array_text[21]
        result_inner[array_text[23][:-2]] = array_text[24]
        result[title] = result_inner

        ## COV Details

        row_fetch = form_fetch[7].get_text().split('\n')
        title = row_fetch[3][:-3]
        result_inner = dict()
        result_inner_text = dict()
        list_inner = list()

        result_inner_text[row_fetch[10]] = row_fetch[17]
        result_inner_text[row_fetch[11]] = row_fetch[18]
        result_inner_text[row_fetch[12]] = row_fetch[19]
        list_inner.append(result_inner_text)
        result_inner_text = dict()
        result_inner_text[row_fetch[10]] = row_fetch[22]
        result_inner_text[row_fetch[11]] = row_fetch[23]
        result_inner_text[row_fetch[12]] = row_fetch[24]
        list_inner.append(result_inner_text)
        result[title] = list_inner

        ## Badge Details

        result_inner_text = dict()
        row_fetch = form_fetch[9].get_text().split('\n')
        title = row_fetch[3][:-3]
        result_inner_text[row_fetch[10][:-1]] = row_fetch[17]
        result_inner_text[row_fetch[11][:-1]] = row_fetch[18]
        result_inner_text[row_fetch[12][:-1]] = row_fetch[19]
        result[title] = result_inner_text

        json_result = json.dumps(result)
        print(json_result)

    except:
        print("Data Not Found")

if __name__ == '__main__':
    DL_no = 'Up8720140002671'
    DOB = '06/07/1989'

    scrapping_data(DL_no, DOB)