import cv2
import numpy as np

def canny(img):
    if img is None:
        return None
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    if lines is None:
        return None
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit = np.polyfit((x1, x2), (y1, y2), 1)
            if fit is None:
                print("Fit is None")
                continue
            slope = fit[0]
            intercept = fit[1]
            if slope < 0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
    if not left_fit or not right_fit:
        return None
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line = m_points(image, left_fit_average)
    right_line = m_points(image, right_fit_average)
    averaged_lines = [left_line, right_line]
    return averaged_lines

def m_points(image, line):
    slope, intercept = line
    y1 = int(image.shape[0])
    y2 = int(y1 * 3.0 / 5)
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return [[x1, y1, x2, y2]]

def region(img):
    height, width = img.shape
    mask = np.zeros_like(img)
    triangle = np.array([[(100, height), (width, height), (int((100 + width) / 2), 0)]], np.int32)
    cv2.fillPoly(mask, triangle, 255)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img

def d_lines(img, lines):
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            if isinstance(line, (int, np.int32)):
                # Handle case where 'lines' is a single line
                x1, y1, x2, y2 = lines
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 10)
            else:
                for x1, y1, x2, y2 in line:
                    cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 10)
    return line_image


cap = cv2.VideoCapture("open_cv/task2/task 8/Video_nameHD.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # You can choose other codecs like MJPG, DIVX, etc.
output_video_path = "output.avi"
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
while cap.isOpened():
    _, image = cap.read()
    if not _ or image is None:
        break
    canny_image = canny(image)
    region_img = region(canny_image)
    lines = cv2.HoughLinesP(region_img, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    avgl = average_slope_intercept(image, lines)
    line_img = d_lines(image, avgl)
    result_img = cv2.addWeighted(image, 0.8, line_img, 1, 1)
    # cv2.imshow("Result", result_img)
    out.write(result_img) 
cap.release()
out.release()
cv2.destroyAllWindows()  
