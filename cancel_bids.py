from colorama import Fore

from helpers.utils import cPrint

cPrint("YOU ARE IN CANCEL MODE, ENTER ANY DATA IN INPUTS IT DOESN`T MATTER", Fore.RED)

if __name__ == "__main__":
    from classes import PhantomBot

    BOT = PhantomBot()

    driver = BOT.setupDriver()

    driver.get("https://www.magiceden.io/")

    driver.maximize_window()

    BOT.initWallet(driver)
    BOT.selectWallet(driver)

    BOT.cancelBids(driver)