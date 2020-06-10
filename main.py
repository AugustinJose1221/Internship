from src.stitch import Stitcher
import imutils
import cv2

capleft = cv2.VideoCapture('Video/left.mp4')
capright = cv2.VideoCapture('Video/right.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Video/out.avi',fourcc, 20, (640,480))
out1 = cv2.VideoWriter('Video/vis.avi',fourcc, 20, (640,480))
k = 0
while(capleft.isOpened() and capright.isOpened()):
    k = k+1
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
    out.write(result) # Writing to an output file "To be completed"
    out1.write(vis)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
capleft.release()
out.release()
capright.release()
out1.release()
cv2.destroyAllWindows()