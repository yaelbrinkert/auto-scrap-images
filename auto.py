from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
import os

CHROME_BINARY_PATH = "/Users/macm1/Downloads/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
DOWNLOADS_DIR = os.path.expanduser("~/Downloads")

list = ["4.0",
    "4.1",
    "4.2",
    "4.3",
    "4.4",
    "4.5"]

options = Options()
options.binary_location = CHROME_BINARY_PATH
# options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# startNumber = 3.7

def startDection(startNumber):
    url = f'https://fortnite.gg/img/maps/{startNumber}.jpg'
    print('started')
    driver.get(url)
    time.sleep(1)
    # driver.implicitly_wait(1.3)
    filename = f"{startNumber}.jpg"
    exists = os.path.join(DOWNLOADS_DIR, filename)
    if driver.current_url == url:
        try: 
            if os.path.exists(exists):
                print("File is already saved")
                return
            if "Page Not Found - Fortnite.GG" in driver.title or "404" in driver.title:
                print(f"❌ {filename} → Page Not Found (URL invalide)")
                return
            try: 
                pyautogui.hotkey('command', 's')
                time.sleep(1)
                pyautogui.press('enter')
                print("Saved "+startNumber+" version")
            except Exception as e:
                print("Error:", e)
        except Exception as e:
            print('Error :', e)

for l in list:
    startDection(l)

