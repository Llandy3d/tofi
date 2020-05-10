from pathlib import Path


BASE_PATH = Path('~/.config/tofi').expanduser()
SECRETS_PATH = BASE_PATH / '.secrets'
CONFIG_PATH = BASE_PATH / 'tofi.ini'


def ensure_config_paths():
    """Ensures that all config paths needed for execution are created."""
    BASE_PATH.mkdir(parents=True, exist_ok=True)
    SECRETS_PATH.mkdir(exist_ok=True)
