import cv2
import numpy as np
import math

def slope (p1,p2):
    try:
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    except ZeroDivisionError:
        return float('inf') 

def findangle(a,b,c,img):
    m1 = slope(b,a)
    m2 = slope(b,c)
    if not math.isinf(m1) and not math.isinf(m2):
        Calc_angle = (m2-m1)/(1+m1*m2)
        rad_angle = math.atan(Calc_angle)
        degree_angle = round(math.degrees(rad_angle))
        print("degree angle is ", degree_angle )
        if degree_angle <0:
            degree_angle=180+degree_angle
        cv2.putText(img,str(degree_angle),(b[0]+20,b[1]+20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3,cv2.LINE_AA)


# webcam=cv2.VideoCapture(0)
# while(1):
    # _,image=webcam.read()
image=cv2.imread("open_cv/task2/task 6/angle.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    area = cv2.contourArea(contour)
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    num_vertices = len(approx)
    if (area > 600 and 2<num_vertices<7):
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
        for i in range(num_vertices):
            a=approx[i-1][0]
            b=approx[i][0]
            if(i>=num_vertices-1):
                c=approx[0][0]
            else:
                c=approx[i+1][0]
            findangle(a,b,c,image)
cv2.imwrite("output_image.jpg", image)
# cv2.imshow("Angle-Detection",image)
# if cv2.waitKey(10) & 0xFF == ord('q'): 
#         webcam.release() 
#         cv2.destroyAllWindows() 
#         break