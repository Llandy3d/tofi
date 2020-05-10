import pytest

from tofi.config import ensure_config_paths, get_or_create_config


@pytest.fixture
def mock_paths(monkeypatch, tmp_path):
    BASE_PATH = tmp_path / '.config/tofi'
    SECRETS_PATH = BASE_PATH / '.secrets'
    monkeypatch.setattr('tofi.config.BASE_PATH', BASE_PATH)
    monkeypatch.setattr('tofi.config.SECRETS_PATH', SECRETS_PATH)

    return BASE_PATH, SECRETS_PATH


def test_ensure_config_paths_creates_paths(mock_paths):
    ensure_config_paths()

    assert all(path.exists() for path in mock_paths)


def test_ensure_config_path_not_fail_if_paths_exists(mock_paths):
    for path in mock_paths:
        path.mkdir(parents=True)

    ensure_config_paths()

    assert all(path.exists() for path in mock_paths)


def test_get_or_create_creates_config(monkeypatch, tmp_path):
    CONFIG_PATH = tmp_path / 'tofi.ini'
    monkeypatch.setattr('tofi.config.CONFIG_PATH', CONFIG_PATH)

    get_or_create_config()

    assert CONFIG_PATH.exists()


def test_get_or_create_retrieves_config(monkeypatch, tmp_path):
    CONFIG_PATH = tmp_path / 'tofi.ini'
    monkeypatch.setattr('tofi.config.CONFIG_PATH', CONFIG_PATH)

    data = """[test]
              data = data
    """

    with open(CONFIG_PATH, 'w') as f:
        f.write(data)

    config = get_or_create_config()

    assert config.sections()[0] == 'test'
    assert config['test']['data'] == 'data'
