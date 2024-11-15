import pkg_resources
import sys
import torch

# File to save output
output_file = "package_versions.txt"

# Open the file in write mode
with open(output_file, "w") as f:
    # Write Python and PyTorch versions
    f.write(f"Python version: {sys.version}\n")
    f.write(f"PyTorch version: {torch.__version__}\n\n")

    # List of packages to check
    packages = [
        "PyMuPDF",
        "paddlepaddle",
        "paddleocr",
        "premailer",
        "transformers",
        "pillow",
        "huggingface_hub",
        "timm",
        "matplotlib",
        "opencv-python",
        "pandas",
        "fuzzywuzzy",
        "spacy",
        "pytest",
    ]

    # Check and write package versions
    for package in packages:
        try:
            version = pkg_resources.get_distribution(package).version
            f.write(f"{package}: {version}\n")
        except pkg_resources.DistributionNotFound:
            f.write(f"{package} is not installed.\n")
f.close()
