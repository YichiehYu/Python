
import os
import time
from datetime import datetime

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
current_date = datetime.today().strftime('%Y%m%d')

#1. 使用Chrome App到國泰世華銀行官網(https://www.cathaybk.com.tw/cathaybk/)並將畫面截圖。
desired_cap = {}
desired_cap['platformName'] = 'Android'
desired_cap['deviceName'] = 'Android'
desired_cap['appPackage'] = 'com.android.chrome'
desired_cap['appActivity'] = 'org.chromium.chrome.browser.ChromeTabbedActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)


try:
    component = WebDriverWait(driver, 5).until(
        lambda driver: driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/terms_accept'))
    component.click()

    component = WebDriverWait(driver, 5).until(
        lambda driver: driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/negative_button'))
    component.click()
except:
    pass

driver.get("https://www.cathaybk.com.tw/cathaybk/")

component = WebDriverWait(driver, 10).until(
    lambda driver: driver.find_element(by=AppiumBy.XPATH, value='(//android.view.View[@content-desc=" "])[1]'))
# screenshot
baseName = os.path.basename(__file__)
driver.save_screenshot(baseName+'1'+'.png')

#2. 點選左上角選單，進入 個人金融 > 產品介紹 > 信用卡列表，需計算有幾個項目並將畫面截圖。

component = WebDriverWait(driver, 5).until(
    lambda driver: driver.find_element(by=AppiumBy.XPATH, value='(//android.view.View[@content-desc=" "])[1]'))
component.click()

component = WebDriverWait(driver, 5).until(
    lambda driver: driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="產品介紹"]'))
component.click()

component = WebDriverWait(driver, 5).until(
    lambda driver: driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="信用卡"]'))
component.click()

component = WebDriverWait(driver, 5).until(
    lambda driver: driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View'))

time.sleep(6)
count=0
for list in component:
    count += 1
print('計算有幾項目在信用卡選單下面:',count-1)
# screenshot
baseName = os.path.basename(__file__)
driver.save_screenshot(baseName+'2'+'.png')

#3. 個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 計算頁面上所有(停發)信用卡數量並截圖
component = WebDriverWait(driver, 5).until(
    lambda driver: driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='卡片介紹'))
component.click()

time.sleep(5)


for x in range(9):
    deviceSize = driver.get_window_size()
    screenWidth = deviceSize['width']
    screenHeight = deviceSize['height']

    ###### Swipe from Bottom to Top  #######
    startx = screenWidth / 2
    endx = screenWidth / 2
    starty = screenHeight * 6 / 9
    endy = screenHeight / 9

    actions = TouchAction(driver)
    actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()



component = WebDriverWait(driver, 5).until(
    lambda driver: driver.find_elements(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[7]/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.Button'))
component_len = len(component)
count=0
for list in range(1,component_len+1):
    count += 1

    component2 = WebDriverWait(driver, 5).until(
        lambda driver: driver.find_element(by=AppiumBy.XPATH,
                                            value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[7]/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.Button[' + str(
                                                count) + ']'))
    component2.click()

    component = WebDriverWait(driver, 5).until(
        lambda driver: driver.find_elements(by=AppiumBy.XPATH,
                                            value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[7]/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.Button['+str(count)+']'))

    # screenshot
    baseName = os.path.basename(__file__)
    driver.save_screenshot(baseName + 'card'+ str(count) + '.png')
print('信用卡列表選單後計算(停發)信用卡數量:',count)
