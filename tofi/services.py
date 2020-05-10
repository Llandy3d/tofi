def add_service(name, token, path):
    """Adds a secret file for the service."""
    service = path / name
    if service.exists():
        raise FileExistsError

    service.write_text(token)
