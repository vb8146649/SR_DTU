import cv2
import numpy as np
webcam=cv2.VideoCapture("open_cv/task2/task 9/ball.mp4")
fps = webcam.get(cv2.CAP_PROP_FPS)
width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # You can choose other codecs like MJPG, DIVX, etc.
output_video_path = "output.avi"
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
while webcam.isOpened():
    _, image = webcam.read()
    if not _ or image is None:
        break
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    count=0
    for contour in contours:
        area = cv2.contourArea(contour)
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        num_vertices = len(approx)
        if(area > 100 and num_vertices > 5):
            count+=1
            cv2.drawContours(image, contour, -1, (0, 255, 0), 2)
    cv2.putText(image,"No . of Spheres " + str(count), (90,90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    out.write(image) 

webcam.release()
out.release()
cv2.destroyAllWindows()

    # cv2.imshow("Shape-Detection",image)
    # if cv2.waitKey(10) & 0xFF == ord('q'): 
    #         webcam.release() 
    #         cv2.destroyAllWindows()
    #         break
    # circles= cv2.HoughCircles(blurred,cv2.HOUGH_GRADIENT,1.2,50,param1=100,param2=30,minRadius=75,maxRadius=400)
    # count=0
    # if circles is not None:
    #     circles=np.uint16(np.around(circles))
    #     chosen=None
    #     for i in circles[0,:]:
    #         if chosen is None : chosen = i 
    #         if prevCircle is not None :
    #              if dist(chosen[0],chosen[1],prevCircle[0],prevCircle[1]) <= dist(i[0],i[1],prevCircle[0],prevCircle[1]):
    #                 chosen=i
    #                 count+=1
    #     cv2.circle(image,(chosen[0],chosen[1]),1,(0,100,100),3)
    #     cv2.circle(image,(chosen[0],chosen[1]),chosen[2],(255,0,255),3)
    #     prevCircle=chosen
    # cv2.putText(image,"No . of Spheres " + str(count), (90,90),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    