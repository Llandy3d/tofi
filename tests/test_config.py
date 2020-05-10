import pytest

from tofi.config import ensure_config_paths


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
