import inspect

import pytest

from chatpdb.frame import FrameData


def test_frame_data_from_valid_frame():
    frame = inspect.currentframe()
    frame_data = FrameData.from_frame(frame)
    assert frame_data.frame is frame
    assert isinstance(frame_data.source_code, str)
    assert "test_frame_data_from_valid_frame" in frame_data.source_code


def test_frame_data_from_none():
    with pytest.raises(TypeError):
        FrameData.from_frame(None)
