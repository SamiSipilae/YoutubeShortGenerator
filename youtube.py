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

from selenium.webdriver.firefox.options import Options
import logging




def upload(file, description, tags, title):
    options = Options()
    options.headless = True

    browser = webdriver.Firefox(options=options)
    browser.get("https://www.youtube.com/")
    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//button[contains(@aria-label,"Accept the use of cookies and other data for the purposes described")]'))).click()
    except:
        pass
    # retrieve cookies from a json file
    for cookie in json.loads(Path('cookies.json').read_text()):
        browser.add_cookie(cookie)

    browser.get("https://www.youtube.com/upload")

    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[.="Continue"]'))).click()
    except:
        pass
    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//input[@name="Filedata"]'))).send_keys(os.path.abspath(file))
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[.="Next"]')))
        titleField = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@aria-label,"Add a title that describes your video")]')))
        titleField.send_keys(Keys.CONTROL, 'a')
        titleField.send_keys(title)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"Description")]/following-sibling::div[1]/div/ytcp-social-suggestion-input/div'))).send_keys(description)
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
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//ytcp-button[@id="close-button"]'))).click()
        Path('cookies.json').write_text(
        json.dumps(browser.get_cookies(), indent=2))
        browser.close()
    except:
        logging.exception("Exception while uploading file:")
        breakpoint()





