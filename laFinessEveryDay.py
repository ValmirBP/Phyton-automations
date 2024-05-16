from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

indexDate = 0
indexDuration = 3
span_text =''
desired_time = '04:30 PM'

# LOGIN
# -----------------------------------------------------------------------------------------------

service = Service(ChromeDriverManager().install())

browser=  webdriver.Chrome(service=service)

browser.get('https://www.lafitness.com/Pages/login.aspx')

browser.find_element('xpath', '//*[@id="txtUser"]').send_keys('Valmir124')
browser.find_element('xpath', '//*[@id="txtPassword"]').send_keys('skdlvnjçsjfnwi!S4S')
browser.find_element('xpath', '//*[@id="ctl00_MainContent_Login1_btnLogin"]').click()


# COURT RESERVATIONS
# -----------------------------------------------------------------------------------------------

browser.get('https://www.lafitness.com/Pages/RacquetballReservation.aspx')
sleep(1)

# select date of court
while span_text != 'There are no courts available for your selection. Please change your selection.' :
    dropdown_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ddlDates"]'))
    )
    dropdown = Select(dropdown_element)
    dropdown.select_by_index(indexDate)

# Select duration of court 120 min
    dropdown_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ddlDuration"]'))
    )
    dropdown = Select(dropdown_element)
    dropdown.select_by_index(indexDuration)

    sleep(1)

    try:
        span_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="lblErrorMessage"]'))
        )
        span_text = span_element.text

        print('NO Option this time 120 ')

# if  no time for 120 go to 90
        if span_text == 'There are no courts available for your selection. Please change your selection.':

            dropdown_element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="ddlDuration"]'))
            )
            dropdown = Select(dropdown_element)
            dropdown.select_by_index(indexDuration - 1)

            sleep(1)

            span_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="lblErrorMessage"]'))
            )
            span_text = span_element.text
            print('NO Option this time 90 ')

            indexDate += 1
            span_text = ''

    except TimeoutException:
         print("The span element did not appear within the specified time.")

# time search
    try:
        dropdown_element = WebDriverWait(browser, 10).until(
         EC.presence_of_element_located((By.XPATH, '//*[@id="cboSearByTimeList"]'))
        )

        dropdown = Select(dropdown_element)
        options = [option.text for option in dropdown.options]

        for option in options:
            if desired_time in options:
                print(f"Option {desired_time} has been selected.")
                dropdown.select_by_value(desired_time)
                browser.find_element('xpath', '//*[@id="btnSaveReservation"]').click()
            else:
                print("Option 'Your Option Text' is not available in the dropdown.")

        indexDate += 1
        span_text = ''


    except TimeoutException:
        print("The dropdown element did not appear within the specified time.")

# -----------------------------------------------------------------------------------------------


