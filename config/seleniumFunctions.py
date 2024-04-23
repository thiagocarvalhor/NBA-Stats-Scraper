import pandas as pd
import os
from datetime import date, timedelta
from selenium import webdriver
from datetime import date
from selenium.webdriver.support.ui import Select
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import glob
import uuid
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from functools import partial

def get_options(options):

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--headless=new")
    options.add_argument("no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-gpu")
    # options.add_argument("--disable-extensions")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("prefs", {
        "download.default_directory": 'C:\\Users\saulo\\OneDrive\\Desktop\\SinteseBI_v2',
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })
    return options

def wait_element(driver,xpath):
    elements = driver.find_elements(By.XPATH,xpath)
    return bool(elements)


def wait_clickable_xpath(driver,xpath,time):
    try:
        element = wait(driver,time,poll_frequency=0.5).until(EC.element_to_be_clickable((By.XPATH,xpath)))
        return True,element.click()
    except:
        return [False]

def wait_clickable_ID(driver,id,time):
    try:
        element = wait(driver,time,poll_frequency=0.5).until(EC.element_to_be_clickable((By.ID,id)))
        return True,element.click()
    except:
        return [False]


def wait_clickable_NAME(driver,name,time):
    try:
        element = wait(driver,time,poll_frequency=0.5).until(EC.element_to_be_clickable((By.NAME,name)))
        return True,element.click()
    except:
        return [False]

def wait_clickable_CLASSNAME(driver,name,time):
    try:
        element = wait(driver,time,poll_frequency=0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,name)))
        return True,element.click()
    except:
        return [False]


def wait_element_located_xpath(driver,xpath):
    try:
        element = wait(driver,60).until(EC.presence_of_element_located((By.XPATH,xpath)))
        return True
    except:
        return False
def wait_element_located_name(driver,name):
    try:
        element = wait(driver,10).until(EC.presence_of_element_located((By.NAME,name)))
        return True
    except:
        return False
    
def send_values_xpath(driver,xpath,value):
    driver.find_element(By.XPATH, xpath).send_keys(value)

def send_values_NAME(driver,name,value):
    driver.find_element(By.NAME, name).send_keys(value)


def send_values_ID(driver,id,value):
    driver.find_element(By.ID, id).send_keys(value)
    
def get_text_xpath(driver,xpath):
    try:
        element = wait(driver,30).until(EC.visibility_of_element_located((By.XPATH,xpath)))
        return [True,element.text]
    except:
        return [False,'']

def get_text_ID(driver,id):
    try:
        element = wait(driver,30).until(EC.visibility_of_element_located((By.ID,id)))
        return [True,element.text]
    except:
        return [False,'']


def scroll_page(driver):
    TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scroll_to_element(driver, xpath ):
    try:
        element = driver.find_element(By.XPATH, xpath)
        return driver.execute_script("return arguments[0].scrollIntoView();", element)
    except:
        return False



def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)


def get_attribute_xpath(driver,xpath,attribute):
    try:
        return wait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, xpath))).get_attribute(attribute)
    except:
        return False
    
def wait_for_new_window(driver,i):
    wait(driver, 60).until(EC.new_window_is_opened(driver.window_handles[i]))


def scroll_located(driver,xpath):
    try:
        driver.execute_script("window.scrollTo(0, 100);")
        element = driver.find_element(By.XPATH,xpath)
        element.location_once_scrolled_into_view
        return [True,element]
    except:
        return[False]