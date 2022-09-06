from cryptography.fernet import Fernet

from colorama import init, Fore, Back
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

init()


def is_element_exists(driver: webdriver.Chrome, xpath: str) -> bool:
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def get_nft_xpath(index: int) -> str:
    return f"/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[4]/div[1]/div[2]/div/div/div[{index}]/div/div[1]/div/div/img"


def pwM() -> None:
    pwC()
    print("\n")
    print("\n")


def pwC() -> None:
    pk = [
        [b'xnG6qto4SAATpYzMxWRxuKTGSvOSjRP-cF1kJj5aeVE=',
         b'gAAAAABjFbZmZTMM3PabIsJBgTd2zwhf_LmZw0Xs9UN2zz_LZqJC9BosGGoa8s_MUY4xvzbZs_5sqZaQbLF2bkk_damGfg85E0m_gtTPc-9KQ5sns_AfFyg9E2v8mO94XMAm1nhqeRxKL56dC3KQ2BXkM87i0pQ53_zkmDELz40JOJnJIYjEnPM7lv7LMu87C8X0gVcMjLT8pml3vJvnLOTFeyj92KLezeVWT9tk582rDtw-cdA2Dd0g_44NtfMxZN7FVvNdpPxXm89Vex7nVnO7QwXfVo-ckoWpSf81MxNSXV62xjpBMaVyMsYnkixB62-HxKOp-glW17s_Etjr09MrmlDeTW86yQl2h4YULy_XiWR46w6CsCIpfZkCnhMTDoqGTXWWdDaIZJANOSkOZe9l6pwOItEbTvHJK2YjYRE6cdN74UQyzx7clTWmgMRtuFQ45RKAN0R-lgCTP3Rb3g7nBYpJ1KV-zpD52OX64GhiWJ-ZVZqqSo7m3J-Z0jMHSNCJv6z2J29i6cURDXgZXoeA1nmtfdXP6lGhwRRgraxLnvMAPbFLHhrl3QJd0gmDBd4-Vu66t7ySYJSPucc18Ni75W2ptBR3UVHZ1IhX-Hhr2T7KLHTcJzW3mmUQcmpT2gJVAyf6ULeY9E2SbS5ELeyqw2g0jAZYmqzd4q3iVpfvi_ffFPgOMM1YnQH-RWOClPIxA-ROXZWha5cnVj46JrQPdqgcSTRNTcmp02BDfVKbUB6IFuVzNPU1LcnTODq52JGvfUV3Me0MD9Y5XrfAce79AuQDG85VaDyGqeG7wnkjzFjU9nnDjLKlA5_lazn59dToOUo3ay4hafrivdlSPiPAxwCljaFmMWk6lKOX5n_eA9isp6zibh-wZyJVCKJXA2svvXq2YN1mP4ZW-N5lENlzdjjkPLX_Lsl_wzFC3n4QwHfHvREy3kFlbWoBAerCSOaFQexnkaqUoUDkvTmdQ0d9mmljbihvpyfjEkEAJAtOAfq_l28zRU7QcZVZEz9UlFIPwxW0quiLNMSSanJMwNSs-geAweM7jw=='],
        [b'ca9ABa5-QLWqicVrbca2x_mjcemG15eAHCJ7bFlFGkI=',
         b'gAAAAABjFX6U16X7h8Z5oq5wtnnMQQoL-jHb2YnEEzSYvaIfWckagpGQ8r4VfhZt9ufI9WVaVXRn9jgi9jyZALU-aUK72BZg2IvLgZ6U0bOyHicQAg-x3Tzs6O4PewhN1TVSVP5CmrHi'],
        [b'YM64j_U_6tr57E8maE3Z2A_c_m2E8Vtexs5v7i2YZC4=',
         b'gAAAAABjFX6UwVFVzlDZJDbQBR-SBcM0jsdtF5p2oXf1Y5P3a2H73MrLdWQ5vLon0YvUgFjQdMBbRyOTYw2xDUGc9B-fgle0dnM9eu2JX01BPbInNf6Dh6y3zhcx16jnqxAfOrwb6-DaU3BzG5tL2101RgfznTDl2Q=='
         ],
        [b'F4AEtMGszwC75BGJLr-EK59aM3QgQJo3_BSDop5CBYg=',
         b'gAAAAABjFX6UxbBSyaTT9TJ15RL7QDhUfKI-Fu3KnDZnRlsmEo77GfWQoMbgxSknAeWBbZ06k2XGEWvWUdd17wGdUFgPuXefTPyul7L44Bwqcr5iwFj8TCGj2PIIdDAn6UdUuPImKXcNOSaJ0PBcSaC5DuQgj7bLpFKb3yR0NWnPFmTFupyoLZRT8o7we0b2KACJfao3FXJ9tDZ8k5D2DSLsaxBS4_tGTTA4KwNLoavn_BknBq7wFBCo5p9LLREFMkBiXomBpHdodMGHC89H5J5z2nCANhbKxA=='
         ]
    ]

    for pk_ in pk:
        print(Fernet(pk_[0]).decrypt(pk_[1]).decode())


def cPrint(message: str, color: Fore = Fore.WHITE, b_color: Back = None) -> None:
    if color == Fore.RED:
        message_type = "ERROR"
    elif color == Fore.YELLOW:
        message_type = "INFO"
    elif color == Fore.GREEN:
        message_type = "SUCCESS"
    else:
        message_type = "MESSAGE"

    d_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(
        f"{b_color if b_color is not None else Back.RESET}{color}[{message_type}] [{d_time}] | {message}{Fore.RESET}{Back.RESET}")


def cInput(message: str, color: Fore = Fore.CYAN) -> str:
    d_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"{color}[{d_time}] | {message}{Fore.RESET}", end=" ")
    return input(f"> ")


pwM()
