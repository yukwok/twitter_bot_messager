import time
from selenium import webdriver
from selenium.webdriver.common import keys


PROMISED_DOWNLOAD = 150
PROMISED_UPLOAD = 10
CHROME_DRIVER_PATH = "/Users/prog/VScode/python/webdev/chromedriver"
TWITTER_EMAIL = "billynyk@gmail.com"
TWITTER_PASSWORD = "abcde12345()"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0
        self.__secret__ = "this is secret message."

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")

        go_button = self.driver.find_element_by_css_selector(".start-button a")

        go_button.click()

        print("sleep for 1 minute")
        time.sleep(60)
        # "//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span"
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        print(f"internet speed is ...dn:{self.down}, up:{self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')

        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(5)

        password.send_keys(keys.Keys.ENTER)

        for x in range(30):
            time.sleep(1)
            print(x)
        print("tweet...")

        what_happening = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        what_happening.send_keys("Hello Twitter")


# --- below is testing code
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
# bot.get_internet_speed()
bot.tweet_at_provider()
