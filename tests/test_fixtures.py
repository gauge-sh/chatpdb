import inspect
from unittest.mock import patch

import pytest


@pytest.fixture
def mock_console():
    with patch("chatpdb.debugger.main.console") as mock:
        yield mock


@pytest.fixture
def mock_chat():
    with patch("chatpdb.debugger.main.ask") as mock_ask, patch(
        "chatpdb.debugger.main.explain"
    ) as mock_explain:
        yield mock_ask, mock_explain


@pytest.fixture
def sample_frame():
    return inspect.currentframe()
