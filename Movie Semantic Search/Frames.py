# import the library
import os
import cv2
import matplotlib.pyplot as plt



source = r"/home/u19581/Movie_Semantic_Search/Movies/Youve.Got.Mail.1998.mp4"

cap = cv2.VideoCapture(source)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

if (cap.isOpened() == False): 
    print("Error opening video stream or file")

directory = r"/home/u19581/Movie_Semantic_Search/Movies/Movie_frames_3"
os.chdir(directory)

frame_count=0



while cap.isOpened():
    os.chdir(directory)
    #print(count)
    ret, frame = cap.read()
    if ret==False:
            break
    cv2.imwrite('Frame'+str(frame_count)+'.png',frame)
            
    frame_count+=1
    
print("done")    
cap.release()
cv2.destroyAllWindows()

