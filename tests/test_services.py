import pytest

from tofi.services import add_service
from tofi.config import ensure_config_paths


def test_add_service_creates_new_secret_file(mock_config_paths):
    ensure_config_paths()
    secret_file = mock_config_paths[1] / 'test'

    add_service('test', 'secret_test', mock_config_paths[1])

    assert secret_file.exists()
    assert secret_file.read_text() == 'secret_test'


def test_add_service_raises_if_file_exists(mock_config_paths):
    ensure_config_paths()
    secret_file = mock_config_paths[1] / 'test'
    secret_file.write_text('test data')

    with pytest.raises(FileExistsError):
        add_service('test', 'secret test', mock_config_paths[1])
