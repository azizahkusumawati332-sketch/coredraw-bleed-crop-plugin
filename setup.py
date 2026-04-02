"""
Setup script for Bleed & Crop Plugin
Handles installation and configuration
"""

from setuptools import setup, find_packages
from pathlib import Path

readme_file = Path(__file__).parent.parent / "README.md"
readme_content = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="coredraw-bleed-crop-plugin",
    version="1.0.0",
    author="CorelDraw Plugin Developer",
    author_email="developer@example.com",
    description="Professional Bleed, Crop & Safe Area Plugin for CorelDraw 2024",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    url="https://github.com/azizahkusumawati332-sketch/coredraw-bleed-crop-plugin",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "presets": ["presets.json"],
        "ui": ["*.py"],
        "features": ["*.py"],
        "utils": ["*.py"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Utilities"
    ],
    python_requires=">=3.8",
    install_requires=[
        "reportlab>=3.6.0",
        "Pillow>=9.0.0",
        "PyPDF2>=3.0.0"
    ],
    entry_points={
        "console_scripts": [
            "coredraw-bleed-crop=src.main:load_plugin",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/azizahkusumawati332-sketch/coredraw-bleed-crop-plugin/issues",
        "Source": "https://github.com/azizahkusumawati332-sketch/coredraw-bleed-crop-plugin",
    }
)