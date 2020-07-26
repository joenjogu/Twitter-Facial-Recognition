import cv2  as cv

def showFaces(imagepath):
    haar_cascade_path = \
        "C:\\Users\\JOE\\JOB\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt.xml"
    original_image = cv.imread(imagepath)
    grayscale_image = cv.cvtColor(original_image,cv.COLOR_BGR2GRAY)

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
    cv.imwrite("faces.png", original_image)

showFaces("C:\\Users\\JOE\JOB\\test\\facial_test.jpg")
    
