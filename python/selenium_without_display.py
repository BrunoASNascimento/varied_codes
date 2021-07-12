from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


# Links

# https://medium.com/@pyzzled/running-headless-chrome-with-selenium-in-python-3f42d1f5ff1d
# https://stackoverflow.com/questions/50642308/webdriverexception-unknown-error-devtoolsactiveport-file-doesnt-exist-while-t
# https://stackoverflow.com/questions/53073411/selenium-webdriverexceptionchrome-failed-to-start-crashed-as-google-chrome-is
# https://stynxh.github.io/2020-06-21-install-google-chrome-on-ubuntu-linux-from-command-line-eng/
# https://stynxh.github.io/2019-10-09-how-to-run-chromedriver-in-selenium-in-docker-with-python3/
# https://hub.docker.com/r/selenium/node-chrome/dockerfile/
# https://stackoverflow.com/questions/43665276/how-to-run-google-chrome-headless-in-docker


# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-dev-shm-usage")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = 'data/chromedriver.exe'
# go to Google and click the I'm Feeling Lucky button
driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path=chrome_driver)
driver.get("https://www.google.com")
lucky_button = driver.find_element_by_xpath('//*[@id="gb"]/div/div[2]/a')
lucky_button.click()

# capture the screen
driver.get_screenshot_as_file("capture.png")
driver.close()
