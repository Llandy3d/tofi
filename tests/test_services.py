import pytest

from tofi.services import add_service, list_services, retrieve_service
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


def test_list_services_empty(mock_config_paths):
    ensure_config_paths()

    assert list_services(mock_config_paths[1]) == []


def test_list_services_with_a_service(mock_config_paths):
    ensure_config_paths()
    add_service('test', 'secret_test', mock_config_paths[1])

    assert list_services(mock_config_paths[1]) == ['test']


def test_retrieve_service_with_existing_secret(mock_config_paths):
    ensure_config_paths()
    add_service('test', 'secret_test', mock_config_paths[1])

    assert retrieve_service('test', mock_config_paths[1]) == 'secret_test'


def test_retrieve_service_without_existing_secret(mock_config_paths):
    ensure_config_paths()

    with pytest.raises(FileNotFoundError):
        retrieve_service('test', mock_config_paths[1])
