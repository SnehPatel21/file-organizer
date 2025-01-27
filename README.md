# File Organizer

A robust Python-based file organization tool that automatically categorizes and organizes files based on their types.

## Features

- 🚀 Automatic file categorization based on file types
- 📁 Custom category support
- 🔄 Intelligent duplicate file handling
- 📊 Detailed operation logging
- ⚙️ Configurable through YAML

## Installation

Clone the repository:
```bash
git clone https://github.com/SnehPatel21/file-organizer.git
```

Navigate to the directory:
```bash
cd file-organizer
```

Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python -m src.organizer /path/to/directory
```

With custom configuration:
```bash
python -m src.organizer /path/to/directory --config path/to/config.yaml
```

## Configuration

Customize categories in `config/default_categories.yaml`:

```yaml
categories:
  images:
    extensions: [".jpg", ".jpeg", ".png", ".gif"]
    description: "Image files"
  documents:
    extensions: [".pdf", ".doc", ".docx", ".txt"]
    description: "Document files"
```

## Project Structure

```
file-organizer/
├── src/
│   ├── __init__.py
│   ├── organizer.py       # Core organization logic
│   ├── file_handler.py    # File operations
│   └── utils.py          # Helper functions
├── tests/
│   ├── __init__.py
│   └── test_organizer.py
├── config/
│   └── default_categories.yaml
└── ...
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development

Set up development environment:
```bash
pip install -r requirements.txt
pre-commit install
```

Run tests:
```bash
pytest tests/
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [@SnehPatel21](https://github.com/SnehPatel21)

Project Link: [https://github.com/SnehPatel21/file-organizer](https://github.com/SnehPatel21/file-organizer)