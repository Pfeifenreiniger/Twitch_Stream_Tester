"""
Kleines Script um die potentielle Bitrate, um auf Twitch streamen zu koennen, automatisiert berechnen und auswerten zu lassen.
Idee zur Coding-Challenge vom Video: https://www.youtube.com/watch?v=M2QP6qtP6Rg
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "C:/dev/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.speedtest.net/")

time.sleep(5)

cookies_accept_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
cookies_accept_button.click()
time.sleep(2)

go_button = driver.find_element(By.CLASS_NAME, "start-text")
go_button.click()

time.sleep(45)

html = driver.page_source

upload_speed = float(html[html.index("Your upload speed is ") + len("Your upload speed is ") : html.index("Your upload speed is ") + len("Your upload speed is ") + 12].split(",")[0])

upload_speed = upload_speed * 1000

bitrate = upload_speed * 0.8

print(f"Du hast eine Streaming-Bitrate von {bitrate}.")

if bitrate < 3000:
    print("Kein Streaming moeglich...")
elif bitrate >= 3000 and bitrate < 4500:
    print("Streaming auf 720p mit 30fps moeglich.")
elif bitrate >= 4500 and bitrate < 6000:
    print("Streaming auf 720p mit 60fps oder 1080p mit 30fps moeglich.")
else:
    print("Streaming auf 1080p mit 60fps moeglich.")
