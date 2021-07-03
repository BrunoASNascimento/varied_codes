from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from common import Setup


def getOptions():
    chromeOptions = Options()
    chromeOptions.add_experimental_option("prefs", {"download.default_directory":  "C:/Users/bruno/Documents/",
                                          "download.prompt_for_download": False, "download.directory_upgrade": True, "safebrowsing.enabled": True})
    return chromeOptions


chromedriver = "D:/developer/github.com/kroton/kbots_dga/DGA-319/utils/chromedriver_90.exe"

driver = webdriver.Chrome(
    executable_path=chromedriver, options=Setup.getOptions())
driver.get(
    "https://selenium-release.storage.googleapis.com/3.150/IEDriverServer_Win32_3.150.1.zip")
