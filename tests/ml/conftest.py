import os

import pytest


def pytest_runtest_setup(item):
    if "ml" in item.keywords:
        if os.getenv("APP_ENV") != "local":
            pytest.skip("ML tests run only when APP_ENV=local")
