import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(asctime)s - %(message)s",
    filename="log.txt",
    filemode="a",
)

# open("log.txt", "a")

from utils import is_valid_email


email = input("Please Enter Your Email Address: ")

try:
    assert is_valid_email(email), "INVALID EMAIL ADDRESS!"
except AssertionError:
    logging.warning("INVALID DATA")
