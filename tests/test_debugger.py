from chatpdb.debugger import handle_chat_pdb
from tests.test_fixtures import mock_chat, mock_console, sample_frame  # noqa: F401


def test_handle_chat_pdb_with_valid_frame(mock_console, mock_chat, sample_frame):
    handle_chat_pdb(sample_frame, "ask something")
    mock_chat[0].assert_called_once()


def test_handle_chat_pdb_with_no_frame(mock_console):
    handle_chat_pdb(None, "")
    mock_console.print.assert_called_once_with("ChatPDB: No frame available")
