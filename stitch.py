# USAGE
# python stitch.py --first images/bryce_left_01.png --second images/bryce_right_01.png 

# import the necessary packages
from pyimagesearch.panorama import Stitcher
import argparse
import imutils
import cv2
'''
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="path to the first image")
ap.add_argument("-s", "--second", required=True,
	help="path to the second image")
args = vars(ap.parse_args())
'''
# load the two images and resize them to have a width of 400 pixels
# (for faster processing)

capleft = cv2.VideoCapture('Video/left.mp4')
capright = cv2.VideoCapture('Video/right.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Video/out.avi',fourcc, 20, (640,480))
out1 = cv2.VideoWriter('Video/vis.avi',fourcc, 20, (640,480))
k = 0
while(capleft.isOpened() and capright.isOpened()):
    k = k+1
    print(k)
    if k==130:
        break
    retleft, frameleft = capleft.read()
    retright, frameright = capright.read()
    if retleft==False:
        break
    if retright==False:
        break
    frameleft = cv2.rotate(frameleft, cv2.ROTATE_90_CLOCKWISE)
    frameright = cv2.rotate(frameright, cv2.ROTATE_90_CLOCKWISE)
    imageA = imutils.resize(frameleft, width=400)
    imageB = imutils.resize(frameright, width=400)
    stitcher = Stitcher()
    try :
        (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
    except TypeError:
        break
    cv2.imshow('LEFT',imageA)
    cv2.imshow('RIGHT',imageB)
    cv2.imshow('RESULT',result)
    cv2.imshow('VIS',vis)
    out.write(result)
    out1.write(vis)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#imageA = cv2.imread(args["first"])
#imageB = cv2.imread(args["second"])


# stitch the images together to create a panorama


# show the images
capleft.release()
out.release()
capright.release()
out1.release()
cv2.destroyAllWindows()