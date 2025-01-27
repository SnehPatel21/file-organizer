"""
File Handler module
Handles file operations and type detection.
"""

import logging
import shutil
from pathlib import Path
from typing import Dict, List

# Different import strategy based on platform
try:
    import magic

    USING_MAGIC = True
except ImportError:
    import filetype

    USING_MAGIC = False


class FileHandler:
    """Handles file operations and type detection."""

    def __init__(self, config: Dict):
        """Initialize FileHandler with configuration."""
        self.config = config
        self.logger = logging.getLogger(__name__)

    def get_category(self, file_path: Path) -> str:
        """
        Determine the category of a file based on its extension.

        Args:
            file_path: Path to the file
        Returns:
            str: Category name or 'others' if no match
        """
        extension = file_path.suffix.lower()

        # Check each category's extensions
        for category, info in self.config["categories"].items():
            if extension in info["extensions"]:
                return category

        return "others"

    def get_mime_type(self, file_path: Path) -> str:
        """
        Get MIME type of file using appropriate library based on platform.
        """
        try:
            if USING_MAGIC:
                return magic.from_file(str(file_path), mime=True)
            else:
                kind = filetype.guess(str(file_path))
                return kind.mime if kind else "application/octet-stream"
        except Exception as e:
            self.logger.warning(f"Could not determine MIME type for {file_path}: {e}")
            return "application/octet-stream"

    def process_directory(self, source_dir: Path) -> Dict[str, List[str]]:
        """
        Process all files in the source directory.

        Args:
            source_dir: Directory to process

        Returns:
            Dict[str, List[str]]: Summary of moved files by category
        """
        summary = {}

        # Create category directories
        for category in self.config["categories"].keys():
            category_dir = source_dir / category
            category_dir.mkdir(exist_ok=True)
            summary[category] = []

        # Create others directory
        others_dir = source_dir / "others"
        others_dir.mkdir(exist_ok=True)
        summary["others"] = []

        # Process each file
        for file_path in source_dir.iterdir():
            if file_path.is_file():
                self._process_file(file_path, source_dir, summary)

        return summary

    def _process_file(
        self, file_path: Path, source_dir: Path, summary: Dict[str, List[str]]
    ) -> None:
        """Process a single file."""
        category = self.get_category(file_path)
        dest_dir = source_dir / category

        try:
            # Generate unique filename if needed
            dest_path = self._get_unique_path(dest_dir / file_path.name)

            # Move the file
            shutil.move(str(file_path), str(dest_path))
            summary[category].append(file_path.name)
            self.logger.info(f"Moved {file_path.name} to {category}")

        except Exception as e:
            self.logger.error(f"Error processing {file_path}: {str(e)}")

    def _get_unique_path(self, path: Path) -> Path:
        """Generate a unique path if file already exists."""
        if not path.exists():
            return path

        base = path.stem
        extension = path.suffix
        counter = 1

        while True:
            new_path = path.parent / f"{base}_{counter}{extension}"
            if not new_path.exists():
                return new_path
            counter += 1
