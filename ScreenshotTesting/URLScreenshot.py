from selenium import webdriver
import time

DRIVER = 'E:/hackaton/ScreenshotTesting/Drivers/chromedriver.exe'
browser = webdriver.Chrome(DRIVER)

def getScreenshot(url):
    browser.maximize_window()
    browser.get(url)
    browser.save_screenshot("firstScreenshot.png")
    image = Image.open('E:/hackaton/ScreenshotTesting/firstScreenshot.png')
    return image
