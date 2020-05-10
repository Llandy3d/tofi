import configparser
from pathlib import Path


BASE_PATH = Path('~/.config/tofi').expanduser()
SECRETS_PATH = BASE_PATH / '.secrets'
CONFIG_PATH = BASE_PATH / 'tofi.ini'


def ensure_config_paths():
    """Ensures that all config paths needed for execution are created."""
    BASE_PATH.mkdir(parents=True, exist_ok=True)
    SECRETS_PATH.mkdir(exist_ok=True)


def get_or_create_config():
    """Returns the config if it exists, else creates a new file and returns the config."""
    config = configparser.ConfigParser()

    if CONFIG_PATH.exists():
        config.read(CONFIG_PATH)
        return config

    config['backup'] = {
        'enabled': 'false',
        'repository': '',
    }

    with open(CONFIG_PATH, 'w') as f:
        config.write(f)

    return config
