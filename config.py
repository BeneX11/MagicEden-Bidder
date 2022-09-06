import json

from dotenv import load_dotenv
import os

from helpers.utils import cInput

load_dotenv()

ELEMENTS = json.load(open('helpers/elements.json'))

SEED_PHRASE = os.getenv("SEED_PHRASE")
PASSWORD = os.getenv("PASSWORD")

CLOSE_BROWSER = True
EXTENSION_PATH = "./helpers/Phantom.crx"

COLLECTION_URL = str(cInput("Enter Collection URL"))
BID_PRICE = float(cInput("Enter Bid Price [in SOL]"))
