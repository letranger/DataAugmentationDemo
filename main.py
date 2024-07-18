import cv2
import os
import numpy as np

def augment_image(image):
    """對輸入圖像進行數據增強並返回增強後的圖像列表"""
    augmented_images = []

    # 原圖
    augmented_images.append(image)

    # 翻轉圖像
    flip1 = cv2.flip(image, 0)  # 垂直翻轉
    flip2 = cv2.flip(image, 1)  # 水平翻轉
    flip3 = cv2.flip(image, -1) # 垂直和水平翻轉
    augmented_images.extend([flip1, flip2, flip3])

    # 旋轉圖像
    for angle in [90, 180, 270]:
        M = cv2.getRotationMatrix2D((image.shape[1] // 2, image.shape[0] // 2), angle, 1)
        rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
        augmented_images.append(rotated)

    # 縮放圖像
    for scale in [0.9, 1.1]:
        scaled = cv2.resize(image, None, fx=scale, fy=scale)
        augmented_images.append(scaled)

    return augmented_images

def process_directory(input_dir, output_dir):
    """處理輸入目錄中的所有圖像，並將增強後的圖像保存到輸出目錄"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    categories = ['dogs', 'cats']
    for category in categories:
        category_input_dir = os.path.join(input_dir, category)
        category_output_dir = os.path.join(output_dir, category)

        for filename in os.listdir(category_input_dir):
            image_path = os.path.join(category_input_dir, filename)
            image = cv2.imread(image_path)
            augmented_images = augment_image(image)

            for i, augmented_image in enumerate(augmented_images):
                output_filename = f"{os.path.splitext(filename)[0]}_aug_{i}.jpg"
                output_path = os.path.join(category_output_dir, output_filename)
                cv2.imwrite(output_path, augmented_image)

# 輸入和輸出目錄
input_directory = '/修改成你的目錄/DataAugmentationDemo/images'
output_directory = '/修改成你的目錄/DataAugmentationDemo/augImages'

# 處理圖像
process_directory(input_directory, output_directory)
