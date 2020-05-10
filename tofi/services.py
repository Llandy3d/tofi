def add_service(name, token, path):
    """Adds a secret file for the service."""
    service = path / name
    if service.exists():
        raise FileExistsError

    service.write_text(token)


def list_services(path):
    """Returns the list of services previously added."""
    return [service.name for service in path.iterdir()]


def retrieve_service(name, path):
    """Retrieve the secret for the service."""
    service_file = path / name
    return service_file.read_text()
