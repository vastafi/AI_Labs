import cv2
import matplotlib.pyplot as plt

#Blur function
image_path = '/Users/astafivalentina/PycharmProjects/AILabs/5.OpenCV/test_images/33C8EE.jpg'

def blur_image(input_path, output_path=None, kernel_size=(3, 3), sigmaX=20):
    image = cv2.imread(input_path)

    blurred_image = cv2.GaussianBlur(image, kernel_size, sigmaX)
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original image')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
    plt.title('Blurred image')

    plt.show()

    if output_path:
        cv2.imwrite(output_path, blurred_image)

blur_image(image_path, output_path='/Users/astafivalentina/PycharmProjects/AILabs/5.OpenCV/image_tasks/image_task_1_blurred.jpg', kernel_size=(15, 15), sigmaX=0)

#Sharpening function

image_path = '/Users/astafivalentina/PycharmProjects/AILabs/5.OpenCV/test_images/4CA327.jpg'
def sharpen_image(input_path, output_path=None, strength=2.5):

    image = cv2.imread(input_path)
    blurred_image = cv2.GaussianBlur(image, (0, 0), 10)

    sharpened_image = cv2.addWeighted(image, 1.0 + strength, blurred_image, -strength, 0)
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original image')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
    plt.title('Sharpened image')

    plt.show()

    if output_path:
        cv2.imwrite(output_path, sharpened_image)

sharpen_image(image_path, output_path='/Users/astafivalentina/PycharmProjects/AILabs/5.OpenCV/image_tasks/image_task_1_sharpened.jpg', strength=2.0)
