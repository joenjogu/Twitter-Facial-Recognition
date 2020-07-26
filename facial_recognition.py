import cv2  as cv
import os

def tagFaces(directory):
    save_path = os.path.join(f"{os.getcwd()}", "Detected_Faces")
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    
    haar_cascade_path = \
        "C:\\Users\\JOE\\JOB\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt.xml"

    for filename in os.listdir(directory):
        original_image = cv.imread(os.path.join(directory, filename))
        grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
        face_cascade = cv.CascadeClassifier(haar_cascade_path)
        detected_faces = face_cascade.detectMultiScale(grayscale_image)

        for (column, row, width, height) in detected_faces:
            cv.rectangle(
                original_image,
                (column, row),
                (column + width, row + height),
                (0, 255, 0),
                2
            )
        print(f"processed.....{filename} of {len(os.listdir(directory))}")
        image_save_path = os.path.join(save_path, filename)
        cv.imwrite(image_save_path, original_image)
    
