# File Organizer

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A powerful and user-friendly desktop application to automatically organize files by their types.

## Features

- 🖥️ Modern graphical user interface
- 🚀 Fast and efficient file processing
- 📁 Intelligent file type detection
- 🎯 Custom category support
- 💫 Real-time progress tracking
- 🛡️ Error handling and recovery

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/file-organizer.git

# Navigate to directory
cd file-organizer

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m src.gui
```

## Usage

1. Launch the application
2. Click "Browse" to select a directory
3. Click "Organize Files" to start
4. Monitor progress in real-time
5. Review organization summary

## Development

```bash
# Setup development environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run tests
pytest tests/

# Build executable
pyinstaller --name FileOrganizer --windowed --onefile src/gui.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built with Python and Tkinter
- File type detection using python-magic
- Configuration using PyYAML

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [@SnehPatel21](https://github.com/SnehPatel21)

Project Link: [https://github.com/SnehPatel21/file-organizer](https://github.com/SnehPatel21/file-organizer)
