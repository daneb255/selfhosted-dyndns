import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

PDNS_API_KEY = os.getenv("PDNS_API_KEY")
PDNS_API_URL = os.getenv("PDNS_API_URL")

LOG_ROOT_DIR = os.getenv("LOG_ROOT_DIR")

DYNDNS_FILE = os.getenv("DYNDNS_FILE")
DYNDNS_USER = os.getenv("DYNDNS_USER")
DYNDNS_PASSWORD = os.getenv("DYNDNS_PASSWORD")


# define domains to update in powerdns
RECORDS = []
