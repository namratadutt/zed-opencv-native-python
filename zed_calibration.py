################################################################################

# native stereo camera calibration using the StereoLabs ZED camera in Python

# Copyright (c) 2018 Toby Breckon, Durham University, UK

# License: MIT License (MIT)

################################################################################

import cv2
import numpy as np

################################################################################

# read zed stereo camera calibration based on camera calibration data read
# from manufacturer provided calibration file

# return set of values
# as (fx, fy, B, Kl,Kr) which are:
# fx - lens focal length in x-axis
# fy - lens focal length in x-axis
# B - Baseline
# Kl - camera matrix K for left camera
# Kr - camera matrix R for right camera

# parts based on:
# https://github.com/stereolabs/zed-opencv-native/blob/master/include/calibration.hpp
# https://github.com/LarkinLabs/SRAAS/blob/master/ZED_CV2.py

def zed_camera_calibration(camera_calibration, camera_mode, full_width, height):

    left = camera_calibration['LEFT_CAM_'+camera_mode];
    right = camera_calibration['RIGHT_CAM_'+camera_mode];
    common = camera_calibration['STEREO'];

    #[LEFT_CAM_xxx] - intrinsics

    Lfx = float(left['fx']);
    Lfy = float(left['fy']);
    Lcx = float(left['cx']);
    Lcy = float(left['cy']);
    Lk1 = float(left['k1']);
    Lk2 = float(left['k2']);
    Lk3 = 0;
    Lp1 = float(left['p1']);
    Lp2 = float(left['p2']);

    #[RIGHT_CAM_xxx]  - intrinsics

    Rfx = float(right['fx']);
    Rfy = float(right['fy']);
    Rcx = float(right['cx']);
    Rcy = float(right['cy']);
    Rk1 = float(right['k1']);
    Rk2 = float(right['k2']);
    Rk3 = 0;
    Rp1 = float(right['p1']);
    Rp2 = float(right['p2']);

    # define intrinsic camera matrices, K for {left, right} caneras

    K_CameraMatrix_left = np.array([[Lfx, 0, Lcx],[ 0, Lfy, Lcy],[0, 0, 1]]);
    K_CameraMatrix_right = np.array([[Rfx, 0, Rcx],[ 0, Rfy, Rcy],[0, 0, 1]]);

    # define intrinsic camera distortion coefficients, for {left, right} caneras
    # N.B. in ZED code last three values are zero by default

    distCoeffsR = np.array([[Rk1], [Rk2], [Rk3], [Rp1], [Rp2]]);
    distCoeffsL = np.array([[Lk1], [Lk2], [Lk3], [Lp1], [Lp2]]);

    # camera - extrinsics

    Baseline = float(common['Baseline']);
    CV = float(common['CV_'+camera_mode]);
    RX = float(common['RX_'+camera_mode]);
    RZ = float(common['RZ_'+camera_mode]);

    # define rotation matrix, R

    R_xyz_vector = np.array([[RX], [CV], [RZ]]);
    R,_ = cv2.Rodrigues(R_xyz_vector);

    # define translation vector, T (baseline is x-axis)

    T = np.array([[Baseline],[0],[0]]);

    # depth image is registered against left image so return set of values
    # as (fx, fy, B, Kl,Kr) which are:
    # fx - lens focal length in x-axis
    # fy - lens focal length in x-axis
    # B - Baseline
    # Kl - camera matrix K for left camera
    # Kr - camera matrix R for right camera

    # N.B.  ZED camera are pre-rectified

    return Lfx, Lfy, Baseline, K_CameraMatrix_left, K_CameraMatrix_right, R, T;


################################################################################
