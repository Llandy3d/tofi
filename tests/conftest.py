import pytest


@pytest.fixture
def mock_config_paths(monkeypatch, tmp_path):
    BASE_PATH = tmp_path / '.config/tofi'
    SECRETS_PATH = BASE_PATH / '.secrets'
    monkeypatch.setattr('tofi.config.BASE_PATH', BASE_PATH)
    monkeypatch.setattr('tofi.config.SECRETS_PATH', SECRETS_PATH)

    return BASE_PATH, SECRETS_PATH
