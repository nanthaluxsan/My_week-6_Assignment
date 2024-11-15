import os
from PIL import Image
import cv2
import argparse


def image_checker(path):
    # load the data
    # "d:\study_further\Senzemate\week_6\Week6_assignment\Financial_data"
    images = path
    PATH = "./"

    classes = os.listdir(images)

    paths = [
        os.path.join(images, o)
        for o in os.listdir(images)
        if os.path.isdir(os.path.join(images, o))
    ]

    nbEntries = []

    for i in range(len(classes)):
        nbEntries.append(len(os.listdir(paths[i])))

    total_set = []
    # Loop through each folder
    for folder in paths:
        # Walk through the directory and its subdirectories
        for root, dirs, files in os.walk(folder):
            for file in files:
                # Check if the file is an image (you can adjust this based on your image types)
                if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                    # Add the full path of the image to the total_set list
                    total_set.append(os.path.join(root, file))
    #     check = image_checker(
    #     "d:\study_further\Senzemate\week_6\Week6_assignment\Financial_data"
    # )
    # Open and display the image
    correct_images = []
    for i in total_set:
        if os.path.exists(i):
            img = cv2.imread(i)
            if img is not None:
                correct_images.append(i)

    return correct_images, classes
