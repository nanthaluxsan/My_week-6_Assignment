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
    # for i in range(2, len(folders)):
    base_dir = folders[3]
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
