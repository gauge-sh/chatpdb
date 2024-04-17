import pytest
from unittest.mock import MagicMock, patch
from chatpdb.debugger import handle_chat_pdb
from chatpdb.frame import FrameData
import inspect


# Test suite for debugger.py
@pytest.fixture
def mock_console():
    with patch("chatpdb.debugger.console") as mock:
        yield mock


@pytest.fixture
def mock_chat():
    with patch("chatpdb.debugger.ask") as mock_ask, patch(
        "chatpdb.debugger.explain"
    ) as mock_explain:
        yield mock_ask, mock_explain


@pytest.fixture
def sample_frame():
    return inspect.currentframe()


def test_handle_chat_pdb_with_valid_frame(mock_console, mock_chat, sample_frame):
    handle_chat_pdb(sample_frame, "ask something")
    mock_chat[0].assert_called_once()


def test_handle_chat_pdb_with_no_frame(mock_console):
    handle_chat_pdb(None, "")
    mock_console.print.assert_called_once_with("ChatPDB: No frame available")


# Test suite for frame.py
def test_frame_data_from_valid_frame():
    frame = inspect.currentframe()
    frame_data = FrameData.from_frame(frame)
    assert frame_data.frame is frame
    assert isinstance(frame_data.source_code, str)
    assert "test_frame_data_from_valid_frame" in frame_data.source_code


def test_frame_data_from_none():
    with pytest.raises(TypeError):
        FrameData.from_frame(None)
