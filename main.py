import cv2 as cv
import numpy as np
import os

mainFoler = "Images"
myFolder = os.listdir(mainFoler)
print(myFolder)

for folder in myFolder:
    path = mainFoler + "/" + folder
    print(path)
    images = []
    myList = os.listdir(path)
    print(f"Total no of images detected {len(myList)}")
    for imgN in myList:
        curImg = cv.imread(f'{path}/{imgN}')
        curImg = cv.resize(curImg, (0,0), None, 0.2, 0.2)
        images.append(curImg)
        
    stitcher = cv.Stitcher.create()
    (statues, result) = stitcher.stitch(images)
    if statues == cv.STITCHER_OK:
        print("Panorama Generated")
        cv.imshow(folder, result)
        if cv.waitKey(1) & 0xFF == ord('s'):
            cv.imwrite(f'Result/{folder}.jpg', result)
    else:
        print("Panorama Generation Unsuccessful")

cv.waitKey(0)
cv.destroyAllWindows()

