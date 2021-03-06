# Realtime Video Stitching using Scale Invariant Feature Transform(SIFT)

<h2>Description</h2>
<p align="justify">This project aims to stitch the video outputs from two camera sensor into one complete video. The process involves, extracting features points from each frame of the video, generating descriptors for each keypoint, matching keypoints with the images, generate a homography matrix using RANSAC algorithm and stitching and warping the images. </p>
<h2>Installation</h2>

```
git clone https://github.com/AugustinJose1221/Internship.git
pip install -r requirements.txt
```
Note: The program won't work for opencv-contrib-python for version above 3.4

To run the program,

```
python main.py
```

Change the video files in the Video directory to test it on custom video files

<h2>Working</h2>
<br>
<h3>Input Image</h3>
<img src="Test/img/test.jpg">

```
The input image is loaded using OpenCV functions. All operations on the image is done as numpy
arrays.
```

<br>
<h3>Grayscale image</h3>
<img src="Test/img/gray1.jpg">

```
The image is converted to grayscale. By doing so, the details get more prominent and the number of 
channels of the image gets reduced from 3 to 1. This also increases the processing time of the 
program
```

<br>
<h3>Gaussian Blur</h3>
<table>
  <tr>
    <td>sigma=11</td>
    <td>sigma=12</td>
  </tr>
  <tr>
    <td><img src="Test/img/GrayBlur2.jpg" width="500"></td>
    <td><img src="Test/img/GrayBlur2.jpg" width="500"></td>
  </tr>
 </table>
 
```
The grayscale image is applied with a Gaussian filter. Two filters of different sigma values are 
applied to it and the two outputs are kept seperately. The Gaussian filter smoothens the image, 
reducing noise and clearing minor details and imperfections in the image.
```

 <br>
<h3>Difference of Gaussian</h3>
<img src="Difference/Output/GrayDiff1.jpg"></img>

```
By taking the difference of the output of Gaussian filter of two different sigma values on the same 
image, the edges and corners gets sharpened while the open space gets nullified. This enchances the 
image for making feature point detection.
```
