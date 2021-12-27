from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "/usr/local/bin/geckodriver"

browser = webdriver.Firefox(executable_path=PATH)
url = "https://www.techwithtim.net/"

browser.get(url=url)

search = browser.find_element_by_name("s") #get viels with name 's' (it's search)
search.send_keys("test") #put python to this search
search.send_keys(Keys.RETURN) #when we press enter it'll find all info with 'python'

try:
    

    main = WebDriverWait(browser, 10).until( #wait until it gets all info
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text) #print all data from teg with id = 'main'
    # articles = main.find_elements_by_tag_name("article")
    # for article in articles:

    #     header = article.find_element_by_class_name("entry-header")
    #     print(header.text)
except Exception as ex:
    print(ex)
    browser.quit()

finally:
    browser.quit()

