"""
Kleines Script um die potentielle Bitrate, um auf Twitch streamen zu koennen, automatisiert berechnen und auswerten zu lassen.
Idee zur Coding-Challenge vom Video: https://www.youtube.com/watch?v=M2QP6qtP6Rg
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

##--------DRIVER CONFIG--------##
driver_path = "C:/dev/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

def main():

    def navigate_page(driver) -> str:
        cookies_accept_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookies_accept_button.click()
        time.sleep(2)

        go_button = driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        time.sleep(45)

        return str(driver.page_source)

    def calc_bitrate(upload_speed : float) -> float:
        upload_speed = upload_speed * 1000

        return upload_speed * 0.8

    def analyze_bitrate_to_stream(bitrate : float) -> str:
        if bitrate < 3000:
            return "Kein Streaming moeglich..."
        elif bitrate >= 3000 and bitrate < 4500:
            return "Streaming auf 720p mit 30fps moeglich."
        elif bitrate >= 4500 and bitrate < 6000:
            return "Streaming auf 720p mit 60fps oder 1080p mit 30fps moeglich."
        else:
            return "Streaming auf 1080p mit 60fps moeglich."

    driver.get("https://www.speedtest.net/")

    time.sleep(5)

    can_continue = True

    try:
        html = navigate_page(driver)
    except Exception as e:
        can_continue = False
        print(f"Eine Fortfuehrung des Programms ist nicht moeglich, da die Uploadrate auf speedtest.net nicht abgefragt werden konnte.\n{e}")

    if can_continue:
        upload_speed = float(html[html.index("Your upload speed is ") + len("Your upload speed is ") : html.index("Your upload speed is ") + len("Your upload speed is ") + 12].split(",")[0])

        bitrate = calc_bitrate(upload_speed)

        print(f"Du hast eine Streaming-Bitrate von {bitrate}.")

        print(analyze_bitrate_to_stream(bitrate))

if __name__ == '__main__':
    main()
