"""
Utility functions for the File Organizer.
"""

import logging
from pathlib import Path
from typing import Dict, Optional

import yaml

DEFAULT_CONFIG_PATH = (
    Path(__file__).parent.parent / "config" / "default_categories.yaml"
)


def load_config(config_path: Optional[str] = None) -> Dict:
    """
    Load configuration from YAML file.

    Args:
        config_path: Optional path to custom config file

    Returns:
        Dict: Configuration dictionary
    """
    path = Path(config_path) if config_path else DEFAULT_CONFIG_PATH

    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise Exception(f"Error loading config from {path}: {str(e)}")


def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
