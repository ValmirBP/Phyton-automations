import os
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from colorama import Fore
from time import sleep

load_dotenv()
desired_time = '05:30 PM'
desired_duration_1 = '120 minutes'
desired_duration_2 = '90  minutes'
desired_duration_3 = '60  minutes'
desired_court_1 = '3 SQUASH COURT 3'
desired_court_2 = '4 SQUASH COURT 4'
username =  os.getenv("USER")
password = os.getenv("PASSWORD")

'2 SQUASH COURT 2'

# LOGIN
# -----------------------------------------------------------------------------------------------

def login (username, password ):

    service = Service(ChromeDriverManager().install())
    browser=  webdriver.Chrome(service=service)
    browser.get('https://www.lafitness.com/Pages/login.aspx')
    browser.find_element('xpath', '//*[@id="txtUser"]').send_keys(username)
    browser.find_element('xpath', '//*[@id="txtPassword"]').send_keys(password)
    browser.find_element('xpath', '//*[@id="ctl00_MainContent_Login1_btnLogin"]').click()
    return browser

# Date selection
# -----------------------------------------------------------------------------------------------
def select_dates(browser):

    dropdown_dates = browser.find_element('xpath','//*[@id="ddlDates"]')
    dates = Select(dropdown_dates)
    all_dates = [option.text for option in dates.options]
    # print('Dates:')
    # print("----" * 15)
    # print(all_dates)
    return all_dates

# Date selection
# -----------------------------------------------------------------------------------------------
def select_durations(browser):

    dropdown_duration = browser.find_element('xpath','//*[@id="ddlDuration"]')
    durations = Select(dropdown_duration)
    all_options = [option.text for option in durations.options]
    # print('Durations:')
    # print("----" * 15)
    # print(all_options)
    return all_options

# Date selection
# -----------------------------------------------------------------------------------------------
def select_times(browser):

    dropdown_times = browser.find_element('xpath','//*[@id="cboSearByTimeList"]')
    times = Select(dropdown_times)
    all_times = [option.text for option in times.options]
    # print('Times:')
    # print("----" * 15)
    # print(all_times)
    return all_times

# Date selection
# -----------------------------------------------------------------------------------------------
def select_courts (browser):

    dropdown_courts = browser.find_element('xpath','//*[@id="cboCourtByTime"]')
    courts = Select(dropdown_courts)
    all_courts = [option.text for option in courts.options]
    # print('Courts:')
    # print("----" * 15)
    # print(all_courts)
    return all_courts

def is_error_message_present(browser):
    try:
        error_message = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="lblErrorMessage"]'))
        )
        return error_message.text == "There are no courts available for your selection. Please change your selection."
    except:
        return False
# main
# -----------------------------------------------------------------------------------------------
def main():


    # Log in
    browser = login(username, password)
    browser.get('https://www.lafitness.com/Pages/RacquetballReservation.aspx')

    # Select dates
    all_dates = select_dates(browser)

    # Loop through each date
    for date in all_dates:
        print(Fore.GREEN +  "Date:", date, Fore.RESET)
        dropdown_dates = browser.find_element('xpath', '//*[@id="ddlDates"]')
        dates = Select(dropdown_dates)
        dates.select_by_visible_text(date)

        sleep(1)

        # Select durations
        all_durations = select_durations(browser)

        # 120 minutes
        if desired_duration_1 in all_durations:
                dropdown_duration = browser.find_element('xpath', '//*[@id="ddlDuration"]')
                durations = Select(dropdown_duration)
                durations.select_by_visible_text(desired_duration_1)
                print(Fore.GREEN ,f'selected {desired_duration_1}',Fore.RESET)

                sleep(1)

                if is_error_message_present(browser):
                    print( Fore.RED + "Error message is present, changing duration", Fore.RESET)

                else:
                    print(Fore.GREEN + "Error message is not present",Fore.RESET)
                    all_times = select_times(browser)

                    if desired_time in all_times:
                        # Select the current time
                        dropdown_times = browser.find_element('xpath', '//*[@id="cboSearByTimeList"]')
                        times = Select(dropdown_times)
                        times.select_by_visible_text(desired_time)

                        sleep(1)

                        all_courts = select_courts(browser)

                        if desired_court_1 in all_courts:
                            dropdown_courts = browser.find_element('xpath', '//*[@id="cboCourtByTime"]')
                            courts = Select(dropdown_courts)
                            courts.select_by_visible_text(desired_court_1)
                            browser.find_element('xpath', '//*[@id="btnSaveReservation"]').click()
                            print(Fore.GREEN,f'reservation made on {date}, at {desired_time}, for{desired_duration_1} at court {desired_court_1}',Fore.RESET)

                            sleep(1)

                        elif desired_court_2 in all_courts:
                            dropdown_courts = browser.find_element('xpath', '//*[@id="cboCourtByTime"]')
                            courts = Select(dropdown_courts)
                            courts.select_by_visible_text(desired_court_2)
                            browser.find_element('xpath', '//*[@id="btnSaveReservation"]').click()
                            print(Fore.GREEN,f'reservation made on {date}, at {desired_time}, for{desired_duration_1} at court {desired_court_2}',Fore.RESET)
                            sleep(1)

                        else:
                            browser.find_element('xpath', '//*[@id="btnSaveReservation"]').click()
                            print(Fore.GREEN,f'reservation made on {date}, at {desired_time}, for{desired_duration_1} at any court',Fore.RESET)
                            sleep(1)
                    else:
                        print(Fore.RED , f' At Date: {date} Time, {desired_time} not available for {desired_duration_1}',Fore.RESET)


        # 90 minutes
        if desired_duration_2 in all_durations:
            dropdown_duration = browser.find_element('xpath', '//*[@id="ddlDuration"]')
            durations = Select(dropdown_duration)
            durations.select_by_visible_text(desired_duration_2)
            print(Fore.GREEN ,f'selected {desired_duration_2}')

            sleep(1)

            if is_error_message_present(browser):
                print(Fore.RED +"Error message is present, changing duration")

            else:
                    print(Fore.GREEN + "Error message is not present")
                    all_times = select_times(browser)

                    if desired_time in all_times:
                        # Select the current time
                        dropdown_times = browser.find_element('xpath', '//*[@id="cboSearByTimeList"]')
                        times = Select(dropdown_times)
                        times.select_by_visible_text(desired_time)

                        all_courts = select_courts(browser)

                        if desired_court_1 in all_courts:
                            dropdown_courts = browser.find_element('xpath', '//*[@id="cboCourtByTime"]')
                            courts = Select(dropdown_courts)
                            courts.select_by_visible_text(desired_court_1)
                            browser.find_element('xpath', '//*[@id="btnSaveReservation"]').click()
                            print(Fore.GREEN,f'reservation made on {date}, at {desired_time}, for {desired_duration_2} at court {desired_court_1}',Fore.RESET)
                            sleep(1)

                        elif desired_court_2 in all_courts:
                            dropdown_courts = browser.find_element('xpath', '//*[@id="cboCourtByTime"]')
                            courts = Select(dropdown_courts)
                            courts.select_by_visible_text(desired_court_2)
                            browser.find_element('xpath', '//*[@id="btnSaveReservation"]').click()
                            print(Fore.GREEN,f'reservation made on {date}, at {desired_time}, for {desired_duration_2} at court {desired_court_2}',Fore.RESET)
                            sleep(1)

                        else:
                            browser.find_element('xpath', '//*[@id="btnSaveReservation"]').click()
                            print(Fore.GREEN,f'reservation made on {date}, at {desired_time}, for {desired_duration_2} at any court',Fore.RESET)
                            sleep(1)

                    else:
                        print(Fore.RED ,f' At Date: {date} Time, {desired_time} not available for {desired_duration_2} ',Fore.RESET)

        # 60 minutes
        if desired_duration_3 in all_durations:
            dropdown_duration = browser.find_element('xpath', '//*[@id="ddlDuration"]')
            durations = Select(dropdown_duration)
            durations.select_by_visible_text(desired_duration_3)
            print(Fore.GREEN ,f'selected {desired_duration_3}',Fore.RESET)

            sleep(1)

            if is_error_message_present(browser):
                print(Fore.RED + "Error message is present, changing day",Fore.RESET)

            else:
                print(Fore.GREEN + "Error message is not present",Fore.RESET)
                all_times = select_times(browser)

                if desired_time in all_times:
                    # Select the current time
                    dropdown_times = browser.find_element('xpath', '//*[@id="cboSearByTimeList"]')
                    times = Select(dropdown_times)
                    times.select_by_visible_text(desired_time)

                    sleep(1)

                    all_courts = select_courts(browser)

                    if desired_court_1 in all_courts:
                        dropdown_courts = browser.find_element('xpath', '//*[@id="cboCourtByTime"]')
                        courts = Select(dropdown_courts)
                        courts.select_by_visible_text(desired_court_1)
                        browser.find_element('xpath', '//*[@id="btnSaveReservation"]').click()
                        print(Fore.GREEN,f'reservation made on {date}, at {desired_time}, for {desired_duration_3} at court {desired_court_1}',Fore.RESET)
                        sleep(1)

                    elif desired_court_2 in all_courts:
                        dropdown_courts = browser.find_element('xpath', '//*[@id="cboCourtByTime"]')
                        courts = Select(dropdown_courts)
                        courts.select_by_visible_text(desired_court_2)
                        browser.find_element('xpath', '//*[@id="btnSaveReservation"]').click()
                        print(Fore.GREEN,f'reservation made on {date}, at {desired_time}, for {desired_duration_3} at court {desired_court_2}',Fore.RESET)
                        sleep(1)

                    else:
                        browser.find_element('xpath', '//*[@id="btnSaveReservation"]').click()
                        print(Fore.GREEN,f'reservation made on {date}, at {desired_time}, for {desired_duration_3} at any court',Fore.RESET)
                        sleep(1)

                else:
                    print(Fore.RED ,f' At Date: {date} Time, {desired_time} not available for {desired_duration_3}',Fore.RESET)

    browser.quit()


main()


