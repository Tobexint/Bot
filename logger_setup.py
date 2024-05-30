import logging


def setup_logger(log_file):
    """
    Set up a logger with both file and stream handlers.

    Args:
        log_file (str): The filename for the log file.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger with the name 'AlJazeeraBot'
    logger = logging.getLogger("AlJazeeraBot")
    logger.setLevel(logging.DEBUG)

    # Create a formatter that includes the timestamp, log level, and message
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Create a file handler for logging to a file
    file_handler = logging.FileHandler(log_file)
    # Set the file handler level to DEBUG
    file_handler.setLevel(logging.DEBUG)
    # Add the formatter to the file handler
    file_handler.setFormatter(formatter)
    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Create a stream handler for logging to the console
    stream_handler = logging.StreamHandler()
    # Set the stream handler level to INFO
    stream_handler.setLevel(logging.INFO)
    # Add the formatter to the stream handler
    stream_handler.setFormatter(formatter)
    # Add the stream handler to the logger
    logger.addHandler(stream_handler)


    return logger
