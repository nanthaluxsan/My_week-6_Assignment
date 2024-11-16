# Automated Financial Document Processing Script Overview

Handling financial documents often involves extracting structured information from unstructured sources like PDFs. This script streamlines the process by integrating multiple automated steps, including OCR, page classification, key-value extraction, and table recognition. By leveraging modular components, it processes financial data efficiently and outputs actionable insights. The customizable design allows users to adapt the workflow to various directory structures and requirements, making it a powerful tool for financial data analysis and management..

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Outputs](#Output)
- [Conclusion](#Conclusion)

## Overview

This script is designed to process and extract structured information from financial documents. It integrates several modules and methods to automate the conversion of PDFs into actionable data. Here's how the script operates:

1. Directory Handling:

Scans a specified directory for folders containing financial data files.
Processes each folder individually to ensure scalability and organization.

2. Key Functional Modules:

PDF Conversion: Converts PDF files into images for further processing.
OCR Extraction: Uses OCR to extract text from the generated images.
Page Classification: Classifies pages based on their content to streamline further extraction.
Key-Value Extraction: Extracts specific key-value pairs from OCR results based on classified pages.
Table Extraction: Identifies and extracts tables present in the documents.
Post-Processing: Combines and processes extracted data to provide a consolidated output.

3. Customizable Workflow:
   The script allows for path adjustments, ensuring it can be tailored to varying directory structures or requirements.

This modular approach ensures flexibility and scalability for processing financial data efficiently.

## Installation

### Prerequisites

- Python 3.x>=3.10
- pip
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/nanthaluxsan/My_week-6_Assignment

   ```

2. Navigate to the project directory:

```bash
   cd WEEK6_ASSIGNMENT
```

3. Set up a virtual environment:

```bash
python3 -m venv venv
venv\Scripts\activate  # On Windows, use
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Install pyTorch version:

```bash
#uninstall torch current version
pip uninstall torch torchvision torchaudio

#install correct version
pip install torch==2.2.2 torchvision torchaudio
```

# Usage

changed the path of financial_data based on requirment

```python
import pdf_to_images
import os
import argparse
import page_classification
import ocr_extraction
import key_value_extraction
import table_extraction
import post_processing
import image_check


def check_pages(data):
    result = {}
    for page_key, page_value in data.items():
        if isinstance(page_value, dict) and page_value:
            result[page_key] = list(page_value.keys())
        else:
            result[page_key] = []  # pass an empty list

    return result


if __name__ == "__main__":
    # Set arguments
    # phot, classes = image_check.image_checker(
    #     "d:\study_further\Senzemate\week_6\Week6_assignment\Financial_data"
    # )
    # base_dir = os.path.dirname(phot[0])
    # Specify the directory you want to scan
    directory = "D:\study_further\Senzemate\week_6\Week6_assignment\Financial_data"

    # Get a list of all folders in the directory
    folders = [
        os.path.join(directory, name)
        for name in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, name))
    ]
    for i in range(len(folders)):
        base_dir = folders[i]
        print(base_dir)
        # Convert PDF to images
        # pdf_to_images.convert_to_images(pdf_path)
        ocr_path = os.path.join(base_dir, "ocr_results.json")
        ocr_extraction.extract_text_from_images(base_dir)
        classfication_results = page_classification.classify_images(base_dir)
        classfication_keys = check_pages(classfication_results)

        key_value_results = key_value_extraction.extract_key_info_from_ocr_results(
            ocr_path, classfication_keys
        )
        table_results = table_extraction.extract_tables_from_images(base_dir)

        post_processing.extract_combined_information(
            classfication_results, key_value_results, table_results, base_dir
        )
        print(classfication_results.keys())

```

## Outputs

ouputs which are in json format, are saved in the same files. (bank statement folder)

## Conclusion

The script automates the process of extracting and classifying financial data from PDF files by performing a sequence of operations, including OCR text extraction, page classification, key-value data extraction, table recognition, and post-processing. By iterating through folders in the specified directory, it ensures modular and reusable workflows tailored to different data sets. The modular design and integration of various components make it adaptable for diverse financial document processing tasks, enabling efficient handling and extraction of structured information.

Changes made, such as modifying the financial_data path, ensure alignment with specific requirements and enhance usability in varied contexts.
