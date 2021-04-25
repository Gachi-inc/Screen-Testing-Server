from PIL import Image
from selenium import webdriver
import time

DRIVER = 'C:/Users/79827/Documents/GitHub/Screen-Testing-Server/ScreenshotTesting/Driverschromedriver.exe'
browser = webdriver.Chrome(DRIVER)

def getScreenshot(url):
    browser.maximize_window()
    browser.get(url)
    browser.save_screenshot("firstScreenshot.png")
    image = Image.open('C:/Users/79827/Documents/GitHub/Screen-Testing-Server/ScreenshotTesting/firstScreenshot.png')
    return image
