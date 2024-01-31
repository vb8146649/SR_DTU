import cv2
from pyzbar.pyzbar import decode
import numpy as np

def decode_and_draw(image):
    decoded_objects = decode(image)
    for obj in decoded_objects:
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(points)
            cv2.polylines(image, [hull], True, (0, 255, 0), 2)
        else:
            points = np.array(points, dtype=np.int32)
            points = points.reshape((-1, 1, 2))
            cv2.polylines(image, [points], True, (0, 255, 0), 2)
        data = obj.data.decode("utf-8")
        print("Type:", obj.type)
        print("Data:", data)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, data, (obj.rect.left, obj.rect.top - 10),
                    font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
# cap = cv2.VideoCapture(0)
# while True:
frame = cv2.imread("open_cv/task2/task 5/qrcode.jpg")
# if not ret:
#     break
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
decode_and_draw(frame)
cv2.imwrite("output_image.jpg", frame)

# cv2.imshow('Barcode and QR Code Scanner', frame)
# if cv2.waitKey(1) & 0xFF == ord('q'):
    # break
# cap.release()
# cv2.destroyAllWindows()
