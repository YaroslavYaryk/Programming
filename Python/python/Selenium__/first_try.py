from selenium import webdriver
from time import sleep

option = webdriver.FirefoxOptions()
option.add_argument("user-agent=HelloWorld:)")

PATH = "/usr/local/bin/geckodriver"

browser = webdriver.Firefox(executable_path=PATH)
url = "https://www.facebook.com/"

try:
    browser.get(url=url)
    print(browser.title) #show title of the page
    sleep(10)
    # browser.refresh() #reload beowser window
    # browser.get_screenshot_as_file("1.png")

except Exception as ex:
    print(ex)


finally:
    browser.quit()


