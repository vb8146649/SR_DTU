import cv2
import numpy as np
from imutils.perspective import four_point_transform

cap = cv2.VideoCapture(0)
count = 0

font = cv2.FONT_HERSHEY_SIMPLEX

WIDTH, HEIGHT = 1920, 1080
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

def image_processing(image):
    image_blurr = cv2.medianBlur(image,5)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    return threshold


def scan_detection(image):
    global document_contour

    document_contour = np.array([[0, 0], [WIDTH, 0], [WIDTH, HEIGHT], [0, HEIGHT]])

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, threshold = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.015 * peri, True)
            if area > max_area and len(approx) == 4:
                document_contour = approx
                max_area = area

    cv2.drawContours(frame, [document_contour], -1, (0, 255, 0), 3)


while True:

    _, frame = cap.read()
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    frame_copy = frame.copy()

    scan_detection(frame_copy)
    # cv2.imshow("input",frame)

    warped = four_point_transform(frame_copy, document_contour.reshape(4, 2))
    warped_resize=cv2.resize(warped,(400,230))
    cv2.imshow("Warped",warped_resize)


    processed = image_processing(warped)
    processed_resize=cv2.resize(processed,(400,230))
    cv2.imshow("Processed",processed_resize)
    if cv2.waitKey(10) & 0xFF == ord('q'): 
        cap.release() 
        cv2.destroyAllWindows() 
        break
    elif cv2.waitKey(10) & 0xFF == ord('s'):
        cv2.imwrite("scanned_" + str(count) + ".jpg", processed)
        count += 1

