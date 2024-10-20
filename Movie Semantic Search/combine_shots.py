import os
import cv2
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips
from skimage.metrics import structural_similarity


directory = r'C:\Users\tirun\OneDrive\Desktop'
os.chdir(directory)

i=827
shots=829
while i<shots :
    print(i)
    prev= VideoFileClip("shot"+str(i-1)+".mp4")
    clip = VideoFileClip("shot"+str(i)+".mp4")
    j=i+1
    if clip.duration < 1 :
        print(clip.duration)
        frame1 = prev.save_frame("frame1.png", t =prev.duration-0.1 ) #last frame of prev
        frame2=clip.save_frame("frame2.png", t =0 ) # first frame of clip
        next = VideoFileClip("shot"+str(j)+".mp4")
        while(next.duration<1) :
            print(j)
            clip = concatenate_videoclips([clip,next])
            j+=1
            next = VideoFileClip("shot"+str(j)+".mp4")   
        frame3 = clip.save_frame("frame3.png", t =clip.duration-0.1 ) # last frame of clip
        frame4=next.save_frame("frame4.png", t =0 ) # first frame of next

        imageA = cv2.imread(r"C:\Users\tirun\OneDrive\Desktop\frame1.png")
        imageB = cv2.imread(r"C:\Users\tirun\OneDrive\Desktop\frame2.png")
        imageC = cv2.imread(r"C:\Users\tirun\OneDrive\Desktop\frame3.png")
        imageD = cv2.imread(r"C:\Users\tirun\OneDrive\Desktop\frame4.png")
    

        hsvA = cv2.cvtColor(imageA,cv2.COLOR_BGR2HSV)
        hsvB = cv2.cvtColor(imageB,cv2.COLOR_BGR2HSV)
        hsvC = cv2.cvtColor(imageC,cv2.COLOR_BGR2HSV)
        hsvD = cv2.cvtColor(imageD,cv2.COLOR_BGR2HSV)

        hist1 = cv2.calcHist([hsvA], [0, 1, 2], None, [70, 70, 70],[0, 180, 0, 265, 0, 256])
        hist1 = cv2.normalize(hist1, hist1,0, 1, cv2.NORM_MINMAX)
        h1 = hist1

        hist = cv2.calcHist([hsvB], [0, 1, 2], None, [70, 70, 70],[0, 180, 0, 265, 0, 256])
        hist = cv2.normalize(hist, hist,0, 1, cv2.NORM_MINMAX)
        h2 = hist

        hist2 = cv2.calcHist([hsvC], [0, 1, 2], None, [70, 70, 70],[0, 180, 0, 265, 0, 256])
        hist2 = cv2.normalize(hist2, hist2,0, 1, cv2.NORM_MINMAX)
        h3 = hist1

        hist3 = cv2.calcHist([hsvD], [0, 1, 2], None, [70, 70, 70],[0, 180, 0, 265, 0, 256])
        hist3 = cv2.normalize(hist3, hist3,0, 1, cv2.NORM_MINMAX)
        h4 = hist

        d1 = cv2.compareHist(h1, h2, cv2.HISTCMP_BHATTACHARYYA)    #
        d2 = cv2.compareHist(h3, h4, cv2.HISTCMP_BHATTACHARYYA)

        print(d1)
        print(d2)
        if(d1<d2) :
            final_clip = concatenate_videoclips([prev,clip])
            #"shot" +str(i) +".mp4".release()
            #os.remove("shot" +str(i) +".mp4")
            final_clip.write_videofile("shot" +str(i) +"_1.mp4")   
        else :
            final_clip = concatenate_videoclips([clip,next])
            #"shot" +str(i+1) +".mp4".release()
            #os.remove("shot" +str(i+1) +".mp4")
            final_clip.write_videofile("shot" +str(j-1) +"_1.mp4")
    i=j
