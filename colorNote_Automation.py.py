from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "Galaxy A50",
    "appPackage": "com.socialnmobile.dictapps.notepad.color.note",
    "appActivity": "com.socialnmobile.colornote.activity.Main",
    "udid": "RR8M40VQHAA"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# add new note
el1 = driver.find_element(
    by=AppiumBy.ID, value="com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip")
el1.click()
time.sleep(2)
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add")
el2.click()
time.sleep(2)
el3 = driver.find_element(
    by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.ImageView")
el3.click()
time.sleep(2)
el4 = driver.find_element(
    by=AppiumBy.ID, value="com.socialnmobile.dictapps.notepad.color.note:id/edit_title")
el4.send_keys("Shopping List")
time.sleep(2)
el5 = driver.find_element(
    by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView")
el5.click()
time.sleep(2)
el6 = driver.find_element(
    by=AppiumBy.ID, value="com.socialnmobile.dictapps.notepad.color.note:id/edit")
el6.send_keys("Snack")
time.sleep(2)
el7 = driver.find_element(by=AppiumBy.ID, value="android:id/button3")
el7.click()
time.sleep(2)
el8 = driver.find_element(
    by=AppiumBy.ID, value="com.socialnmobile.dictapps.notepad.color.note:id/edit")
el8.send_keys("Tissue")
el9 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
el9.click()
el10 = driver.find_element(
    by=AppiumBy.ID, value="com.socialnmobile.dictapps.notepad.color.note:id/back_btn")
el10.click()
el11 = driver.find_element(
    by=AppiumBy.ID, value="com.socialnmobile.dictapps.notepad.color.note:id/back_btn")
el11.click()
time.sleep(2)

# search note
el12 = driver.find_element(
    by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@content-desc=\"Search\"]/android.widget.ImageView")
el12.click()
el13 = driver.find_element(
    by=AppiumBy.ID, value="com.socialnmobile.dictapps.notepad.color.note:id/edit_search")
el13.send_keys("Shopping List")
el13.click()
el14 = driver.find_element(
    by=AppiumBy.ID, value="com.socialnmobile.dictapps.notepad.color.note:id/title")
el14.click()
el15 = driver.find_element(
    by=AppiumBy.ID, value="com.socialnmobile.dictapps.notepad.color.note:id/back_btn")
el15.click()
time.sleep(2)
el16 = driver.find_element(
    by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="Notes"]/android.widget.ImageView')
el16.click()
time.sleep(2)
# delete note
el17 = driver.find_element(
    by=AppiumBy.ID, value="com.socialnmobile.dictapps.notepad.color.note:id/title")
el17.click()
el18 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="More")
el18.click()
time.sleep(2)
el19 = driver.find_element(
    by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.ImageView")
el19.click()
time.sleep(2)
el20 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
el20.click()

driver.quit()
