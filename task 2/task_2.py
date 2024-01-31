import cv2,numpy as np
webcam = cv2.VideoCapture("open_cv/task2/task 2/color_video.mp4") 
fps = webcam.get(cv2.CAP_PROP_FPS)
width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # You can choose other codecs like MJPG, DIVX, etc.
output_video_path = "output.avi"
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height),isColor=False)
while webcam.isOpened():
    _, imageFrame = webcam.read()
    if not _ or imageFrame is None:
        break
    imageFrame=cv2.cvtColor(imageFrame,cv2.COLOR_BGR2GRAY)     
    out.write(imageFrame) 

webcam.release()
out.release()
cv2.destroyAllWindows()   
    # if cv2.waitKey(10) & 0xFF == ord('q'): 
    #     cv2.release() 
    #     cv2.destroyAllWindows() 
    #     break