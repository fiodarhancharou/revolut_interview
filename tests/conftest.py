import logging
import sys

import pytest


@pytest.fixture
def some_fixture() -> object:
    yield object
