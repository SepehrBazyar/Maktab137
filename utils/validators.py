import logging
import re as regex


PATTERN = r"^\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b$"


def is_valid_email(email: str) -> bool:
    logging.debug("CALLED")
    return bool(regex.search(PATTERN, email))


if __name__ == "__main__":
    print(is_valid_email("@@@@@@@"))
    print(is_valid_email("akbar@gmail"))
    print(is_valid_email("akbar@gmail.com"))
    print(is_valid_email("akbar@gmail.ir"))
