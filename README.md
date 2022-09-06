# Magic Eden Bidder
###### Created by Galiaf
------------
![Alt text](/screenshots/Screenshot_1.png?raw=true "Screenshot 1")
![Alt text](/screenshots/Screenshot_2.png?raw=true "Screenshot 2")
![Alt text](/screenshots/Screenshot_3.png?raw=true "Screenshot 3")
![Alt text](/screenshots/Screenshot_4.png?raw=true "Screenshot 4")
------------
- **[EN](https://github.com/Galiafer/MagicEden-Bidder#en)**
- **[RU](https://github.com/Galiafer/MagicEden-Bidder#ru)**
- **[TODO](https://github.com/Galiafer/MagicEden-Bidder#todo)**
------------

## EN
> This bot will help to **make bids** on NFT from the desired collection.

**ONLY WINDOWS for now, If the script at the beginning switches the window to MagicEden or only one window with Phantom Wallet is loaded, please restart the script**

### Tutorial
1. Clone the repository / Download zip file:

    `git clone https://github.com/Galiafer/MagicEden-Bidder.git`

    OR

    [Download Zip File](https://github.com/Galiafer/MagicEden-Bidder/archive/refs/heads/main.zip)

2. Be sure you have installed Python, [here is a link to download](https://www.python.org/downloads/)
3. Open **cmd** (command prompt)
4. Install **all python module**:

   `pip install -r requirements.txt`
5. Fill in all the data in `.env` (But before rename .env-sample to .env):
```json
FILL EVERYTHING WITHOUT QUOTES

SEED_PHRASE=YOUR_SEED_PHRASE (Do Not Share This KEY)
PASSWORD=13372281111MEOW (Password from your Phantom Wallet)
```
6. Open **CMD** and go to directory:
 `cd /path/to/directory/`

7. Run the python file:

    windows : `python main.py`
8. If you want to cancel all your active bids run `cancel_bids.py` (But this script is very unstable and may not working)
------------

## RU
> Этот бот поможет сделать оффер на НФТ из нужной коллекции.

**ПОКА ЧТО СКРИПТ РАБОТАЕТ ТОЛЬКО НА WINDOWS, если скрипт в начале переключает окно на MagicEden или загружается только одно окно с Phantom Wallet, пожалуйста, перезапустите скрипт**

### Инструкция
1. Скопируйте репозиторий / Скачайте zip файл:

    `git clone https://github.com/Galiafer/MagicEden-Autobuyer.git`

    ИЛИ

    [Скачать Zip Файл](https://github.com/Galiafer/MagicEden-Autobuyer/archive/refs/heads/main.zip)

2. Удостоверьтесь, что у вас скачан Python, [ссылка на установку](https://www.python.org/downloads/)
3. Откройте **cmd** (командную строку)
4. Установите **все библиотеки**:

   `pip install -r requirements.txt`
5. Заполните данные в `.env` (Но перед этим измените название файла с .env-sample на .env):
```json
ЗАПОЛНЯТЬ БЕЗ КАВЫЧЕК

SEED_PHRASE=ВАША_СИД_ФРАЗА (Никуда не публикуйте эту фразу)
PASSWORD=13372281111MEOW (Пароль от кошелька)
```
6. Откройте **CMD** (командную строку) и перейдите в директорию проекта:
 `cd /path/to/directory/`

7. Запустите файл:

    windows : `python main.py`
8. Если хотите отменить все свои офферы, то запустите `cancel_bids.py` (Но этот скрипт еще не готов и может неправильно работать)

------------
### Хороших всем покупок.

## TODO:
1. Set bid expire time
