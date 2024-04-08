import cv2

image_path = '/Users/astafivalentina/PycharmProjects/AILabs/5.OpenCV/test_images/14A19C.jpg'
def detect_face(image_path, output_path=None):
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    if len(faces) == 0:
        print("No face detected!")
        return None
    else:
        print(f"Face detected at coordinates: ({x}, {y}, {w}, {h})")

    if output_path:
        cv2.imwrite(output_path, image)
        print(f"Image saved to {output_path}")

    return image
output_path = '/Users/astafivalentina/PycharmProjects/AILabs/5.OpenCV/image_tasks/image_task_2_detect_face.jpg'

detect_face(image_path, output_path=output_path)
