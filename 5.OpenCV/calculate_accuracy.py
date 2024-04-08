import os
import pandas as pd
from passport_photo import check_passport_photo

def calculate_accuracy(test_df, images_folder):
    correct_predictions = 0

    for _, row in test_df.iterrows():
        image_path = os.path.join(images_folder, row['new_path'])
        # print("Verify path:", image_path)
        is_valid, _ = check_passport_photo(image_path)

        if is_valid == row['label']:
            correct_predictions += 1

    accuracy = correct_predictions / len(test_df)
    return accuracy

csv_file_path = '/Users/astafivalentina/PycharmProjects/AILabs/5.OpenCV/test.csv'

# try:
#     test_df = pd.read_csv(csv_file_path)
#     print("CSV file upload")
# except Exception as e:
#     print(f"Error to upload CSV file: {e}")

images_folder = '/Users/astafivalentina/PycharmProjects/AILabs/5.OpenCV/'
test_df = pd.read_csv(csv_file_path)

accuracy = calculate_accuracy(test_df, images_folder)
print(f"System Accuracy: {accuracy:.2f}")