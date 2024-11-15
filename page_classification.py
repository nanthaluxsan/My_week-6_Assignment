import os
import json
from paddleocr import PaddleOCR
from fuzzywuzzy import fuzz
import cv2

# Define the keywords for each category along with the threshold for classification
categories = {
    "Medical Documents": {
        "keywords": [
            "Patient ID",
            "Medical Record",
            "Diagnosis",
            "Prescription",
            "Healthcare",
            "Insurance ID",
            "Doctor",
            "Medical Center",
            "Hospital",
            "Lab Results",
            "Procedure",
            "Treatment Plan",
            "Symptoms",
            "Allergies",
            "Dosage",
            "Referral",
        ],
        "threshold": 70,  # Minimum matches required to classify as Medical Documents
    },
    "Bank Statements": {
        "keywords": [
            "Account Number",
            "Statement Date",
            "Balance",
            "Credit",
            "Debit",
            "Transaction",
            "Bank",
            "Account Summary",
            "Available Balance",
            "ATM",
            "Interest",
            "Fee",
            "Banking Institution",
            "Account Holder",
            "Deposit",
            "Withdrawal",
            "Monthly Statement",
        ],
        "threshold": 70,  # Minimum matches required to classify as Bank Statements
    },
    "Invoices": {
        "keywords": [
            "Invoice Number",
            "Invoice Date",
            "Total Amount",
            "Due Date",
            "Customer ID",
            "Billing Address",
            "Itemized Charges",
            "Unit Price",
            "Quantity",
            "Subtotal",
            "Tax",
            "Discount",
            "Total Due",
            "Remittance",
            "Payment Terms",
            "Supplier",
            "Purchase Order (PO)",
        ],
        "threshold": 70,  # Minimum matches required to classify as Invoices
    },
    "Utility Bills": {
        "keywords": [
            "Account Number",
            "Billing Date",
            "Service Provider",
            "Utility",
            "Electricity",
            "Water",
            "Gas",
            "Due Date",
            "Consumption",
            "Meter Reading",
            "Total Charges",
            "Billing Period",
            "Payment Details",
        ],
        "threshold": 70,  # Minimum matches required to classify as Utility Bills
    },
    "Salary Slips": {
        "keywords": [
            "Employee ID",
            "Employee Name",
            "Designation",
            "Department",
            "Basic Pay",
            "Allowances",
            "Deductions",
            "Gross Pay",
            "Net Pay",
            "Salary Month",
            "Payment Date",
            "Tax Deduction",
            "Provident Fund",
            "Employer",
            "Payroll",
        ],
        "threshold": 70,  # Minimum matches required to classify as Salary Slips
    },
    "ITR Forms": {
        "keywords": [
            "Income Tax",
            "Assessment Year",
            "PAN",
            "Taxpayer",
            "Taxable Income",
            "Refund",
            "Deductions",
            "Exemptions",
            "Gross Total Income",
            "Advance Tax",
            "Self Assessment Tax",
            "Verification",
            "ITR Form",
            "Filing Date",
            "Tax Payment",
        ],
        "threshold": 70,  # Minimum matches required to classify as ITR Forms
    },
    "Checks": {
        "keywords": [
            "Payee",
            "Drawer",
            "Amount",
            "Check Number",
            "Bank Name",
            "Date",
            "Signature",
            "Account Holder",
            "Pay to the Order",
            "MICR Code",
            "IFSC Code",
            "Routing Number",
            "Clearing",
            "Crossed Check",
            "Bearer Check",
            "Postdated Check",
        ],
        "threshold": 70,  # Minimum matches required to classify as Checks
    },
}


def classify_text(text):
    """Classifies the text based on predefined categories using fuzzy matching and returns a score."""
    classified_results = {}

    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()

    # Check each category for keywords
    for category, details in categories.items():
        matched_keywords = []
        total_score = 0

        for keyword in details["keywords"]:
            # Calculate the fuzzy match score
            score = fuzz.partial_ratio(keyword.lower(), text_lower)

            # Check if the score meets the threshold
            if score >= details["threshold"]:
                matched_keywords.append(keyword)
                total_score += score  # Accumulate scores for matched keywords

        # Store results if any keywords are matched
        if matched_keywords:
            average_score = total_score / len(
                matched_keywords
            )  # Calculate average score
            classified_results[category] = {
                "matched_keywords": matched_keywords,
                "average_score": average_score,
            }

    return classified_results


def classify_images(pdf_dir_path):
    """Extracts text from images in the given directory and classifies them based on thresholds."""
    ocr = PaddleOCR(use_angle_cls=True, lang="en")

    # Dictionary to hold classification results for each image
    classification_results = {}

    # Loop through all images in the directory
    for filename in sorted(os.listdir(pdf_dir_path)):
        image_path = os.path.join(pdf_dir_path, filename)
        img = cv2.imread(image_path)
        if img is not None:
            # Extract OCR result from the image
            ocr_result = ocr.ocr(image_path, cls=True)
            if ocr_result[0] is not None:
                # Concatenate extracted text from all detected words
                extracted_text = " ".join(
                    [line[1][0] for result in ocr_result for line in result]
                )

                # Classify the extracted text
                classification = classify_text(extracted_text)

                # Store the classification results
                page_num = os.path.splitext(filename)[0].split("_")[
                    -1
                ]  # Get page number from filename
                classification_results[f"{page_num}"] = classification

    print(f"classification results is {classification_results}")
    # Save the classification results to a JSON file
    json_path = os.path.join(pdf_dir_path, "classification_results.json")
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(classification_results, json_file, ensure_ascii=False, indent=4)

    return classification_results
