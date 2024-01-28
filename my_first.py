from selenium import webdriver

PATH = "/Users/dongchengen/Desktop/chromedriver_mac/"
driver = webdriver.Safari(PATH)
driver.get("https://google.com")