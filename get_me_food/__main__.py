import logging
import sys

from get_me_food.commons import common_logger
from get_me_food.commons.cmd_arguments import CMDArguments
from get_me_food.get_me_food import GetMeFood

console_logger = logging.getLogger('console')
info_logger = logging.getLogger('info_file')
error_logger = logging.getLogger('error_file')


def main(argv: list) -> None:
    """Main function."""
    common_logger.setup_logger()

    cmd_arguments = CMDArguments(argv)
    get_me_food = GetMeFood(cmd_arguments.ingredients())
    print(get_me_food)

if __name__ == "__main__":
    main(sys.argv[1:])
    info_logger.info("Finished.")
