# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
import time
import csv


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# this is a comment



num = 0
with open('aaa.csv', 'r') as fd:
    data = list(csv.reader(fd))
num = len(data)

i = 0
a = []

driver.get(
    "http://wcmsdev:81/wcms/Main.aspx")
time.sleep(1)
driver.find_element_by_id(
    "txtUserName").send_keys("------")
driver.find_element_by_id(
    "txtPassword").send_keys("------")
driver.find_element_by_id(
    "btnLogin").click()
print("Logging on", end="")
for z in range(6):
    print(".", end='', flush=True)
    time.sleep(0.5)
print("\nDone!")


def search():
    driver.get(
        "http://wcmsdev:81/wcms/SectionManager.aspx")
    iframe = driver.find_element_by_id(
        'frameContent')
    driver.switch_to.frame(iframe)
    driver.find_element_by_id(
        "FunctionContent_PublishContent_ascx_txtContentIDSearch").send_keys(data[i])
    driver.find_element_by_xpath(
        "/html/body/form/div[3]/table/tbody/tr/td[4]/div/table/tbody/tr/td[2]/div[1]/div[1]/table/tbody/tr[4]/td/a/span").click()
    print("Searching", end="")
    for z in range(3):
        print(".", end='', flush=True)
        time.sleep(0.5)
    print("\nDone!")


def work():
    time.sleep(1)
    driver.find_element_by_xpath(
        "/html/body/form/div[3]/table/tbody/tr/td[4]/div/table/tbody/tr/td[2]/div[3]/div[2]/div[2]/a[1]/span/span/span").click()

    time.sleep(1)
    driver.find_element_by_xpath(
        "/html/body/form/div[3]/table/tbody/tr/td[4]/div/table/tbody/tr/td[2]/div[2]/div[2]/table/tbody/tr/td[1]/a/span/span/span").click()

    time.sleep(1)
    driver.find_element_by_xpath(
        "/html/body/form/div[3]/table/tbody/tr/td[4]/div/table/tbody/tr/td[2]/div[3]/div[2]/div[2]/a[5]/span").click()

    time.sleep(1)
    driver.find_element_by_xpath(
        "/html/body/form/div[3]/div/a[1]/span").click()
    print("Finalizing", end="")
    for z in range(2):
        print(".", end='', flush=True)
        time.sleep(0.5)
    print("\nDone!")


# become var?
i = 0
while i < num:
    # try:
    search()
    # except:
    #     driver.switch_to.alert.accept()
    #     a.apend(data[i])
    #     print(a)
    #     time.sleep(1)
    #     i += 1
    # finally:
    work()
    i += 1
    answer = str(round(i / num * 100, 2))
    print(answer + "%", "work done!")
#  Tried error handling but its not worth the time xD
