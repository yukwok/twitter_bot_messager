from selenium import webdriver


# --- This is the bot to check the internet speed and post the results
# --- to the Twitter services
PROMISED_DOWNLOAD = 150
PROMISED_UPLOAD = 10
CHROME_DRIVER_PATH = ""
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


sample_element = '<span data-download-status-value="0.07" class="result-data-large number result-data-value download-speed">71.49</span>'


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0
