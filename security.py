import os
from dropbox import files
import cv2
import dropbox
import random
startTime=time.time()
def TakeSnapshot():
    number=random.randint(0, 100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret, frame=videoCaptureObject.read()
        imgName="img"+str(number)+".png"
        cv2.imWrite(imgName, frame)
        startTime=time.time
        result=False
    return imgName
    print("snapshot taken dude")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadFile(imgName):
    access_Token="sl.AzM35fYPju2_qSEA0X6ekPeVylf6H0wsPYTaQlUZEGa94Y9TLkpOnGdB-gvHGu2cQqnPHTdAxhjo-cOfXk_fl8E9kyLL3cdRAL6xuuSmbHh0j_ciyqEDEU8G8Y7cpUvhqYhliAA"
    file=imgCounter
    fileFrom=file
    file2="/newFolder/"+(imgName)
    dbx=dropbox.Dropbox(access_Token)
    with open(fileFrom, 'rb')as f:
        dbx.files_upload(f.read(),file2, mode=dropbox.files.WriteMode.overWrite)
        print("fileUploaded")
def main():
    while(True):
        if((time.time()-startTime)>=100):
            name=TakeSnapshot()
            uploadFile(name)
main()