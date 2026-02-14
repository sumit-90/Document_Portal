from setuptools import setup, find_packages
from pathlib import Path


def parse_requirements(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#") and not line.startswith("-e")]

setup(
    name="document_portal",
    version="0.1.0",
    author="Sumit Umbardand",
    description="An intelligent document analysis and comparison system powered by LLMs and vector databases.",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests*","examples*"]),
    include_package_data=True,
    install_requires=parse_requirements("requirements.txt"),
    extras_require={
        "dev":["pytest","pylint","ipykernel"]
    },
    classifiers=[
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.13",
)