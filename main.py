from selenium import webdriver
from fje import login_gmail
from fje import remove_security
import fje
import time
import csv


class mail_obj():
    def __init__(self, Email, Password, Secret):
       self.Email = Email
       self.Password = Password
       self.Secret = Secret

webdriver_location = 'C:\gekodriver\geckodriver.exe'
with open ('emails.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        #print(row)
        i = mail_obj(row[0], row[1], row[2])

        with  webdriver.Firefox(executable_path=webdriver_location) as driver:
            login_gmail(i, driver)
            #remove_security(i, driver)

            More = driver.find_element_by_xpath("//div[@class='n6']")
            More.click()
            time.sleep(5)
            AllMail = driver.find_element_by_xpath("//div[@class='TN bzz aHS-aHO']")
            AllMail.click()
            time.sleep(30)


            next_button = driver.find_element_by_xpath('//*[@id=":12q"]')
            print(next_button)
            print(next_button.get_attribute('class'))



            donja = driver.find_element_by_xpath('/html[1]/body[1]/div[7]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/span[1]/span[2]')
            print(donja)
            print(donja.text)



            gornja = driver.find_element_by_xpath('/html[1]/body[1]/div[7]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/span[2]')
            print(gornja)
            print(gornja.text)



            donja_granica = int(donja.text)
            gornja_granica = int(gornja.text)
            fje.email_check(i, driver)
            while (donja_granica != gornja_granica):
                fje.email_check(i, driver)
                next_button.click()
                time.sleep(10)
                donja = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/span/div[1]/span/span[1]/span[2]')
                gornja = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/span/div[1]/span/span[2]')
                donja_granica = int(donja.text)
                gornja_granica = int(gornja.text)

            time.sleep(10)

            driver.find_element_by_xpath("//div[@class='TN bzz aHS-bnv']").click()# spam button click
            time.sleep(10)

            next_button = driver.find_element_by_xpath("//div[@id=':pp']")
            print(next_button)
            print(next_button.get_attribute('class'))

            donja = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/span/div[1]/span/span[1]/span[2]')
            print(donja)
            print(donja.text)

            gornja = driver.find_element_by_xpath('/html[1]/body[1]/div[7]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/span[2]')
            print(gornja)
            print(gornja.text)

            fje.spam_check(i, driver)
            while (donja_granica != gornja_granica):
                fje.spam_check()(i, driver)
                next_button.click()
                time.sleep(10)
                donja = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/span/div[1]/span/span[1]/span[2]')
                gornja = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/span/div[1]/span/span[2]')
                donja_granica = int(donja.text)
                gornja_granica = int(gornja.text)

            driver.quit()


