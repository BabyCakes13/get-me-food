from get_me_food.commons import common_logger
from get_me_food.get_me_food import GetMeFood


import logging
console_logger = logging.getLogger('console')
info_logger = logging.getLogger('info_file')
error_logger = logging.getLogger('error_file')

def main() -> None:
    """Main function."""
    common_logger.setup_logger()
    get_me_food = GetMeFood()


if __name__ == "__main__":
    main()
    info_logger.info("Finished.")

    try:
        raise ValueError('A very specific bad thing happened.')
    except ValueError:
        error_logger.error("Error")
