class InternetSpeedTwitterBot:

    def __init__(self, driver, down, up):
        self.driver = driver
        self.down = down
        self.up = up
        self.__secret__ = "this is secret message."

    def get_internet_speed(self):
        print("internet speed is ...")
        print(self.__dict__)

    def tweet_at_provider(self):
        print("tweet...")


# --- below is testing code
# bot = InternetSpeedTwitterBot("driver path", -4.5, 48)
# bot.get_internet_speed()
# bot.tweet_at_provider()
# print(bot.__secret__)
