import logging

# Configure the logger


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
