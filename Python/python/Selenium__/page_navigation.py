from selenium import webdriver

PATH = "/usr/local/bin/geckodriver"

browser = webdriver.Firefox(executable_path=PATH)
url = "http://127.0.0.1:8000/"

browser.get(url=url)
    
link = browser.find_element_by_link_text("Read more")
link.click()    