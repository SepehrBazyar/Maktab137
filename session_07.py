import logging


# logging.basicConfig(
#     level=logging.INFO,
#     format="%(name)s - %(asctime)s - %(levelname)s - %(message)s",
#     # filename="log.txt",
#     # filemode="a",
# )

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler(
    filename="log.txt",
    mode="a",
)

stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.INFO)


brief_format = logging.Formatter("%(levelname)s - %(message)s")
detail_format = logging.Formatter("%(name)s - %(levelname)s - %(lineno)d -%(message)s")



stream_handler.setFormatter(brief_format)
file_handler.setFormatter(detail_format)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


result = 0
for _ in range(3):
    number = input("Please Enter Your Number: ")
    try:
        number = int(number)
    except:
        logger.warning("Invalid Value")
        number = 0

    result += number
    logger.info("Added New Number")
    logger.warning("SFEFEWFEWFEFFEFEFEFEFEWJF9EUFOPEWU90FE")


print(f"{result=}")
