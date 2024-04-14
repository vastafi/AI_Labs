import cv2
from matplotlib import pyplot as plt

image_path = '/Users/astafivalentina/PycharmProjects/AILabs/5.OpenCV/test_images/7E0875.jpg'
def check_passport_photo(image_path):

    image = cv2.imread(image_path)

    is_color = (image[:,:,0] != image[:,:,1]).any() or (image[:,:,1] != image[:,:,2]).any()

    if not is_color:
        return False, "Image is not in color"

    height, width, _ = image.shape
    aspect_ratio = width / height
    if not (0.9 <= aspect_ratio <= 1.1):
        return False, "Image is not in portrait orientation or square"

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) != 1:
        return False, "No or multiple faces detected"

    x, y, w, h = faces[0]
    roi_gray = gray[y:y+h, x:x+w] # regiunea de interes

    eyes = eye_cascade.detectMultiScale(roi_gray)

    if len(eyes) != 2:
        return False, "No or multiple eyes detected"

    (eye1_x, eye1_y, eye1_w, eye1_h), (eye2_x, eye2_y, eye2_w, eye2_h) = eyes

    max_error = 5
    if abs(eye1_y + eye1_h // 2 - eye2_y - eye2_h // 2) > max_error:
        return False, "Eyes are not at the same level"

    head_area = w * h
    image_area = width * height
    if not (0.2 <= head_area / image_area <= 0.5):
        return False, "Head does not represent 20% to 50% of the photo area"

    return True, "Passport photo meets requirements"


is_valid, message = check_passport_photo(image_path)
print(message)

image = cv2.imread(image_path)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Passport photo')
plt.show()
