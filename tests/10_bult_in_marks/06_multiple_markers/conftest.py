def pytest_configure(config):
    config.addinivalue_line("markers", "fast")
    config.addinivalue_line("markers", "furious")