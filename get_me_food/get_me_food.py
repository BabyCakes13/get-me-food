"""Module which implements the logic of the application."""
import logging
console_logger = logging.getLogger('console')
info_logger = logging.getLogger('info_file')
error_logger = logging.getLogger('error_file')


class GetMeFood:
    """Entrypoint of the application."""

    def __init__(self) -> None:
        console_logger.debug("Setup GetMeFood class.")

    def __str__(self) -> str:
        return "GetMeFood[]"
