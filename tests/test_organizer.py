"""
Tests for the File Organizer.
"""

from pathlib import Path

import pytest

from src.file_handler import FileHandler
from src.organizer import FileOrganizer


@pytest.fixture
def sample_config():
    return {
        "categories": {
            "images": {"extensions": [".jpg", ".png"], "description": "Image files"},
            "documents": {
                "extensions": [".pdf", ".doc"],
                "description": "Document files",
            },
        }
    }


def test_file_handler_category_detection(sample_config):
    handler = FileHandler(sample_config)

    # Test image detection
    assert handler.get_category(Path("test.jpg")) == "images"
    assert handler.get_category(Path("test.png")) == "images"

    # Test document detection
    assert handler.get_category(Path("test.pdf")) == "documents"
    assert handler.get_category(Path("test.doc")) == "documents"

    # Test unknown file type
    assert handler.get_category(Path("test.xyz")) == "others"
