import json
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import os
import time


def upload(file, description, tags, title):

    browser = webdriver.Firefox()
    browser.get("https://www.youtube.com/")
    # retrieve cookies from a json file
    for cookie in json.loads(Path('cookies.json').read_text()):
        browser.add_cookie(cookie)

    browser.get("https://www.youtube.com/upload")

    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[.="Continue"]'))).click()
    except:
        pass

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@name="Filedata"]'))).send_keys(os.path.abspath(file))
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[.="Next"]')))
    titleField = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Add a title that describes your video"]')))
    titleField.send_keys(Keys.CONTROL, 'a')
    titleField.send_keys(title)
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Tell viewers about your video"]'))).send_keys(description)
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]'))).click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[.="Show more"]'))).click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Add tag"]'))).click()
    tagField = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Add tag"]')))
    for tag in tags:
        tagField.send_keys(tag+',')
        time.sleep(0.1)
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[.="Video language"]'))).click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//yt-formatted-string[.="English"]'))).click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[.="Next"]'))).click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//h3[.="Add subtitles"]')))
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[.="Next"]'))).click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[.="Copyright"]')))
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[.="Next"]'))).click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[.="Public"]'))).click()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[.="Publish"]'))).click()










