import numpy as np

def Matcher(keypoints1, keypoints2):
    tolerance = 10
    new_keypoints_1 =[]
    new_keypoints_2 =[]
    err1 = 0
    err2 = 0
    err3 = 0
    err4 = 0
    err = 0
    for i in keypoints1:
        for j in keypoints2:
            err1 = i[0]-j[0]
            err2 = i[1]-j[1]
            err3 = i[2]-j[2]
            err4 = i[3]-j[3]
            err = abs(err1) + abs(err2) + abs(err3) + abs(err4)
            if err < tolerance:
                new_keypoints_1.append(i[4])
                new_keypoints_2.append(j[4])

    return new_keypoints_1, new_keypoints_2
