from setuptools import find_packages, setup

setup(
    name="file-organizer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-magic>=0.4.27",
        "PyYAML>=6.0.1",
    ],
    entry_points={
        "console_scripts": [
            "organize-cli=src.organizer:main",
        ],
        "gui_scripts": [
            "organize-gui=src.gui:main",
        ],
    },
    author="Sneh Patel",
    author_email="supatel5678.90@gmail.com",
    description="A tool to organize files by their types",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SnehPatel21/file-organizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
