import numpy as np 
import cv2 
webcam = cv2.VideoCapture("open_cv/task2/task 1/lemon.mp4") 
arr=eval(input("Enter BGR value")) 
ar=cv2.cvtColor(np.uint8([[arr]]),cv2.COLOR_BGR2HSV)
arr1=ar[0][0][0] - 10,100,100
arr2=ar[0][0][0] + 10,255,255
fps = webcam.get(cv2.CAP_PROP_FPS)
width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # You can choose other codecs like MJPG, DIVX, etc.
output_video_path = "color_detection.avi"
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

while webcam.isOpened(): 
    _, imageFrame = webcam.read()
    if not _ or imageFrame is None:
        break
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    lower_mask=np.array(arr1,np.uint8)
    upper_mask=np.array(arr2,np.uint8)
    mask = cv2.inRange(hsvFrame, lower_mask,upper_mask) 

    contours, hierarchy = cv2.findContours(mask, 
                                           cv2.RETR_TREE, 
                                              cv2.CHAIN_APPROX_SIMPLE) 
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour)
        if(area > 300):
            # cv2.drawContours(imageFrame,contour,-1,(0,0,0),2) 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 0), 2) 
              
            cv2.putText(imageFrame, "Your Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (arr[0],arr[1],arr[2]) )
              
    out.write(imageFrame) 

webcam.release()
out.release()
cv2.destroyAllWindows()   
    
    
    
    # if cv2.waitKey(10) & 0xFF == ord('q'): 
    #     webcam.release() 
    #     cv2.destroyAllWindows() 
    #     break