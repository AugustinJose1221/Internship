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
    error = tolerance
    pos1 = 0
    pos2 = 0
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
                if err < error:
                    error = err
                    pos1 = i[4]
                    pos2 = j[4]
    return new_keypoints_1, new_keypoints_2, pos1, pos2

def Stitcher(img1, keypoints1, img2, keypoints2):
    width = img2.shape[1]
    height = img2.shape[0]
    final = []
    row = []
    for k in range(height):
        row = []
        for i in range(keypoints1[1]):
            row.append(img1[k,i,:])
        for j in range(keypoints2[1],width):
            row.append(img2[k,j,:])
        final.append(row)
    #print(keypoints1," ", keypoints2)
    '''
    final_image1 = img1[:,0:keypoints1[1],:]
    final_image2 = img2[:,keypoints2[1]:width,:]
    '''
    Final = np.array(final)
    #print(row[0])
    return Final
