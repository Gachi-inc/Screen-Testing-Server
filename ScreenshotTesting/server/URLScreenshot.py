from selenium import webdriver

DRIVER = 'C:/Users/79827/Desktop/python/projectH/Screen-Testing-Server-main/server/Drivers/chromedriver.exe'


def getScreenshot(url):
    browser = webdriver.Chrome(DRIVER)
    browser.maximize_window()
    browser.get(url)
    browser.save_screenshot("firstScreenshot.png")
    return "firstScreenshot.png"
