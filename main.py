from classes import PhantomBot

BOT = PhantomBot()

if __name__ == "__main__":
    driver = BOT.setupDriver()

    driver.get("https://www.magiceden.io/")

    driver.maximize_window()

    BOT.initWallet(driver)
    BOT.selectWallet(driver)
    BOT.startBidding(driver)