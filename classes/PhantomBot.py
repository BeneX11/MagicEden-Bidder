import os
import time

from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from helpers.utils import cPrint, get_nft_xpath

from config import SEED_PHRASE, PASSWORD, COLLECTION_URL, ELEMENTS, BID_PRICE, CLOSE_BROWSER, EXTENSION_PATH
from helpers.utils import is_element_exists


class PhantomBot:
    def __init__(self):
        self.elements = ELEMENTS

    @staticmethod
    def setupDriver() -> webdriver.Chrome:
        options = Options()

        options.add_extension(EXTENSION_PATH)
        options.add_argument("--disable-gpu")

        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        os.environ['WDM8LOCAL'] = '1'

        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

        return driver

    @staticmethod
    def __selectElement(xpath: str, toBeClicked: bool, driver: webdriver.Chrome, input_key: str = "") -> None:
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, xpath)))
        el = driver.find_element(By.XPATH, xpath)

        if input_key != "":
            el.send_keys(input_key)
            toBeClicked = False

        if toBeClicked:
            el.click()

    @staticmethod
    def __selectElements(xpath: str, driver: webdriver.Chrome) -> list[WebElement]:
        WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        el = driver.find_elements(By.XPATH, xpath)

        return el

    @staticmethod
    def __scroll_down(driver):

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(4)

            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

    def initWallet(self, driver: webdriver.Chrome) -> None:
        cPrint("Init wallet...", Fore.YELLOW)

        driver.switch_to.window(driver.window_handles[1])

        self.__selectElement(self.elements['phantom']['importButton'], True, driver)

        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//*[@id='word_0']")))
        for i in range(0, 12):
            driver.find_element(By.XPATH, f"//*[@id='word_{i}']").send_keys(SEED_PHRASE.split(' ')[i])

        self.__selectElement(self.elements['phantom']['submitButton'], True, driver)

        time.sleep(5)
        self.__selectElement(self.elements['phantom']['submitButton'], True, driver)

        self.__selectElement(self.elements['phantom']['passwordField'], False, driver,
                             input_key=PASSWORD)
        self.__selectElement(self.elements['phantom']['confirmPasswordField'], False, driver,
                             input_key=PASSWORD)
        self.__selectElement(self.elements['phantom']['checkbox'], True, driver)
        self.__selectElement(self.elements['phantom']['submitButton'], True, driver)

        time.sleep(5)
        self.__selectElement(self.elements['phantom']['continueButton'], True, driver)

        time.sleep(5)
        self.__selectElement(self.elements['phantom']['continueButton'], True, driver)

        driver.switch_to.window(driver.window_handles[0])

        cPrint("Done\n", Fore.YELLOW)

    def selectWallet(self, driver: webdriver.Chrome) -> None:
        cPrint("Selecting wallet...", Fore.YELLOW)

        self.__selectElement(self.elements['magiceden']['connectWallet'], True, driver)

        time.sleep(2)
        self.__selectElement(self.elements['magiceden']['phantomWallet'], True, driver)
        time.sleep(2)

        if len(driver.window_handles) >= 2:
            WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(2))
            driver.switch_to.window(driver.window_handles[1])

            time.sleep(2)
            self.__selectElement(self.elements['magiceden']['popup']['connectButton'], True, driver)

            driver.switch_to.window(driver.window_handles[0])
        cPrint("Done\n", Fore.YELLOW)

    def startBidding(self, driver: webdriver.Chrome) -> None:
        try:
            cPrint("Start Bidding...", Fore.YELLOW)
            driver.get(COLLECTION_URL)

            if is_element_exists(driver, self.elements['magiceden']['connectWallet']):
                self.selectWallet(driver)

            time.sleep(3)

            cPrint("Scrolling to the bottom to get all listed NFTs...", Fore.YELLOW)
            self.__scroll_down(driver)

            NFTs = self.__selectElements(self.elements['magiceden']['nftTable'], driver)[1::]

            cPrint(f"Total NFTs: {len(NFTs)}", Fore.GREEN)
            cPrint("Scrolling up...", Fore.YELLOW)

            driver.execute_script("window.scrollTo(0, 220)")
            time.sleep(5)
            self.__selectElement(self.elements["magiceden"]["bidButton"], True, driver)

            totalCount = 0
            prevIndex = 0
            while True:
                if totalCount >= len(NFTs):
                    break

                count = 0
                for i in range(prevIndex, len(NFTs)):
                    if (count == 50) or (totalCount >= len(NFTs)):
                        break

                    prevIndex = i

                    xpath = get_nft_xpath(i + 2)
                    nft = driver.find_element(By.XPATH, xpath)

                    driver.execute_script("arguments[0].scrollIntoView(true);", nft)

                    time.sleep(0.05)

                    self.__selectElement(xpath, True, driver)

                    cPrint(f"Selecting nft...{totalCount + 1}/{len(NFTs)}", Fore.YELLOW)

                    count += 1
                    totalCount += 1

                cPrint(f"Making bid...", Fore.GREEN)
                self.__selectElement(self.elements["magiceden"]["bidInput"], False, driver, input_key=BID_PRICE)
                self.__selectElement(self.elements["magiceden"]["bidNow"], True, driver)

                WebDriverWait(driver, 120).until(EC.number_of_windows_to_be(2))
                driver.switch_to.window(driver.window_handles[1])

                self.__selectElement(self.elements['magiceden']['popup']['approveButton'], True, driver)

                WebDriverWait(driver, 120).until(EC.number_of_windows_to_be(1))
                driver.switch_to.window(driver.window_handles[0])

                time.sleep(1)

                WebDriverWait(driver, 120).until(
                    EC.element_to_be_clickable((By.XPATH, self.elements["magiceden"]["clearButton"])))
                self.__selectElement(self.elements["magiceden"]["clearButton"], True, driver)

                cPrint(f"Continue select NFT...", Fore.YELLOW)

            cPrint("All bids were done!\n", Fore.GREEN)
        except Exception as err:
            cPrint(f"An error has occurred: {err}", Fore.RED)
        finally:
            if CLOSE_BROWSER:
                cPrint("Closing browser...\n", Fore.YELLOW)

                driver.close()

            exit()

    def cancelBids(self, driver: webdriver.Chrome) -> None:
        try:
            cPrint("Start...", Fore.YELLOW)

            driver.get("https://www.magiceden.io/me?tab=offers-made&filter=tradeable")
            if is_element_exists(driver, self.elements['magiceden']['connectWallet']):
                self.selectWallet(driver)

            try:
                while True:
                    NFTs = self.__selectElements(self.elements['magiceden']['offersTable'], driver)
                    for nft in NFTs:
                        nft.find_element(By.XPATH, "//td[6]/div/button[1]").click()

                    driver.refresh()
            except Exception as err:
                pass
            finally:
                cPrint("Done\n", Fore.YELLOW)

        except Exception as err:
            cPrint(f"An error has occurred: {err}", Fore.RED)
        finally:
            if CLOSE_BROWSER:
                cPrint("Closing browser...\n", Fore.YELLOW)

                driver.close()

            exit()

