def pytest_configure(config):
    config.addinivalue_line(
        "markers", "specific_setup"
    )