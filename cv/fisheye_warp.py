# Referenced https://stackoverflow.com/questions/47081309/fisheye-calibration-opencv-python for guidance

import numpy as np
import cv2
import matplotlib.pyplot as plt

# This function calibrates the camera using a fisheye image of a chessboard 
# (will need to take new pics using the actual camera soon)
# Returns the matrix and distortion coefficient after calibrating, which
# can be used to adjust warp in a real image so long as the two are the same in 
# the camera that took said image

def calibrate_fisheye():
    # nx and ny for a 9 (acorss) x 6 (up) chessboard
    # nx = num of inner corners across
    # ny = num of inner corners up-down
    nx = 8
    ny = 6

    # object_p is a 3D array of object points
    # each row is a 3D coordinate of a corner of the chessboard
    object_p = np.zeros((ny * nx, 3), np.float32)

    # creates  a 2D array of the corner coordinates
    # select all rows in cols 0 and 1 (x and y cols)
    # this will look like:
        # [[0. 0. 0.]  --> top left corner
        #  [1. 0. 0.], --> next corner to the right
        #     ...
        #  [7. 5. 0.]] --> bottom right corner
    # each row represents a corner
    object_p[:,:2] = np.mgrid[0:nx,0:ny].T.reshape(-1,2)

    object_points = [] # 3D points in real world space
    image_points = [] # 2D points on the image

    img = cv2.imread("fisheye_chess.jpg")

    # Convert the image to RGB (Matplotlib uses RBG)
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # RGB is standard in matplotlib

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Define the checkerboard pattern
    CHECKERBOARD = (8, 6)

    # Search for the chessboard corners in the gray_image
    # ret is a boolean value that indicates whether the corners were found or not
    # corners is an array of the corners found
    ret, corners = cv2.findChessboardCorners(gray_img, (nx, ny), None)

    if ret == True:
        object_points.append(object_p) # how it should look like
        image_points.append(corners) # how it looks like
        cv2.drawChessboardCorners(img, (nx, ny), corners, ret) # Draw the corners on the image

    # Display the corners
    plt.figure()
    plt.imshow(RGB_img) # preserve the color format
    plt.title("Warped Image")
    plt.show()

    # Get the shape of the image for calibration --> (height, width)
    shape = gray_img.shape[::-1] # ::-1 to reverse from height, width --> width, height

    # Camera Matrix: The focal length and optical centre matrix as shown in intrinsic parameters
    # Distortion Coefficients: The coefficients that define how distorted the image is
    # Rotation Vector: The image pixel rotation angles in radians converted to vector by Rodrigues method
    # Translation Vector: The vector depicting shift in pixel values along x and y axis
    ret, matrix, distortion_coeff, rot_vecs, trans_vecs = cv2.calibrateCamera(object_points, image_points, shape, None, None)

    calibrated_img = cv2.undistort(img, matrix, distortion_coeff, None, matrix)

    plt.figure()
    plt.imshow(cv2.cvtColor(calibrated_img, cv2.COLOR_BGR2RGB))
    plt.title("Calibrated Image")
    plt.show()

    return matrix, distortion_coeff

calibrate_fisheye()

# def correct_real_fisheye(martix, distortion_coeff):
#     # load the image from the actual camera, and reset this image with each frame I assume
#     actual_camera_img = cv2.imread("[INSERT REAL CAMERA IMAGE]")

#     cv2.undistort(actual_camera_img, martix, distortion_coeff)

# correct_real_fisheye(matrix, distortion_coeff)
