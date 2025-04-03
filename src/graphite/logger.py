import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(module)s:: !> %(message)s",
    handlers=[
        logging.FileHandler("sysgraph.log"),  # Log to a file
        logging.StreamHandler(),  # Also output to console
    ],
)
