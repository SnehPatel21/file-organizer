"""
File Organizer - Main module
Handles the core logic for organizing files based on their types.
"""

import logging
import sys
from pathlib import Path
from typing import Dict, List, Optional

from .file_handler import FileHandler
from .utils import load_config, setup_logging


class FileOrganizer:
    """Main class for organizing files into categories."""

    def __init__(self, source_dir: str, config_path: Optional[str] = None):
        self.source_dir = Path(source_dir)
        self.config = load_config(config_path)
        self.file_handler = FileHandler(self.config)
        setup_logging()
        self.logger = logging.getLogger(__name__)

    def organize(self) -> Dict[str, List[str]]:
        """
        Organize files in the source directory according to their types.

        Returns:
            Dict[str, List[str]]: Summary of moved files by category
        """
        if not self.source_dir.exists():
            self.logger.error(f"Source directory {self.source_dir} does not exist")
            sys.exit(1)

        self.logger.info(f"Starting organization of {self.source_dir}")
        return self.file_handler.process_directory(self.source_dir)


def main():
    """Main entry point for the file organizer."""
    import argparse

    parser = argparse.ArgumentParser(description="Organize files by type")
    parser.add_argument("source_dir", help="Directory to organize")
    parser.add_argument("--config", help="Path to custom config file")

    args = parser.parse_args()

    organizer = FileOrganizer(args.source_dir, args.config)
    summary = organizer.organize()

    # Print summary (only non-empty categories)
    print("\nOrganization Summary:")
    for category, files in summary.items():
        if files:  # Only show categories with files
            print(f"\n{category}:")
            for file in files:
                print(f"  - {file}")


if __name__ == "__main__":
    main()
