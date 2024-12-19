import logging


def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create console handler with a specific format
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    if not logger.handlers:  # Prevent adding multiple handlers
        logger.addHandler(console_handler)

    return logger


class CustomFormatter(logging.Formatter):
    def format(self, record):
        return f"{record.levelname}:     {record.message}"


def setup_custom_logger():
    logger = logging.getLogger("uvicorn.access")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        handler = logging.StreamHandler()
        handler.setFormatter(CustomFormatter())
        logger.addHandler(handler)

    # Ensure logger does not expect args for messages
    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")
