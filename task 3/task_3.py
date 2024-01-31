import cv2,numpy as np
webcam = cv2.VideoCapture("open_cv/task2/task 3/ball.mp4") 
str1=input("Enter your string")
x=int(input("Enter x "))
y=int(input("Enter y "))
fps = webcam.get(cv2.CAP_PROP_FPS)
width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # You can choose other codecs like MJPG, DIVX, etc.
output_video_path = "output.avi"
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
while webcam.isOpened():
    _, imageFrame = webcam.read()
    if not _ or imageFrame is None:
        break
    cv2.putText(imageFrame, str1 , (x, y),cv2.FONT_HERSHEY_SIMPLEX,1.0, (0,0,0))
    out.write(imageFrame) 

webcam.release()
out.release()
cv2.destroyAllWindows()  
    # if cv2.waitKey(10) & 0xFF == ord('q'): 
    #     webcam.release() 
    #     cv2.destroyAllWindows() 
    #     break