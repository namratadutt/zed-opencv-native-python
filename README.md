# Stereolabs ZED -  OpenCV Native Capture in Python

This sample shows how to capture rectified images with the ZED (or ZED-M) Stereo Camera and OpenCV, **without the ZED SDK**, using only Python. It is inspired by the C++version of the same available from [stereolabs](https://github.com/stereolabs/zed-opencv-native).

Alternatively, if you want to use OpenCV with the ZED SDK features, check our sample [here](https://github.com/stereolabs/zed-opencv).

Developed to support teaching within the undergraduate Computer Science programme at [Durham University](http://www.durham.ac.uk) (UK) by [Prof. Toby Breckon](http://community.dur.ac.uk/toby.breckon/).

All tested with [OpenCV](http://www.opencv.org) 3.x and Python 3.x.

---

### How to download and run:

**First** - you need to know the serial number of the ZED stereo camera you are trying to use. To do so, you can use ZED Explorer tools (ZED SDK tools) and check the serial number on the top right of ZED Explorer window or alternatively each camera has a small label on the end of the USB lead with the serial number on it.


Clone the repository and run as follows, with your camera serial number as ```SERIAL```:

```
git clone https://github.com/tobybreckon/zed-opencv-native-python.git
cd zed-opencv-native-python
python3 ./zed-stereo.py --serial SERIAL --camera_to_use 1
```

Example will retrieve camera calibration from manufacturer's on-line calibration site and write to file as ``` zed-cam-sn-SERIA.conf```

In general example can be used as follows:

```
usage: zed-stereo.py [-h] [-c CAMERA_TO_USE] [-s SERIAL] [-cf CONFIG_FILE]

Native live stereo from a StereoLabs ZED camera using factory calibration.

optional arguments:
  -h, --help            show this help message and exit
  -c CAMERA_TO_USE, --camera_to_use CAMERA_TO_USE
                        specify camera to use
  -s SERIAL, --serial SERIAL
                        camera serial number
  -cf CONFIG_FILE, --config_file CONFIG_FILE
                        camera calibration configuration file
```

Press the _"f"_ key to run disparity fullscreen, press  _"f"_ key to add colour map and _space_ to change camera resolution mode (press _"x"_ to exit).

---

### References:

If using this example in your own work (e.g _"... based on the implementation of REF..."_), please reference the related research work from which this set of SGBM parameters where defined:

- [A Foreground Object based Quantitative Assessment of Dense Stereo Approaches for use in Automotive Environments](http://community.dur.ac.uk/toby.breckon/publications/papers/hamilton13stereo.pdf) (O.K. Hamilton, T.P. Breckon, X. Bai, S. Kamata), In Proc. International Conference on Image Processing, IEEE, pp. 418-422, 2013. [[pdf]](http://community.dur.ac.uk/toby.breckon/publications/papers/hamilton13stereo.pdf)

---

If you find any bugs raise an issue (or much better still submit a git pull request with a fix) - toby.breckon@durham.ac.uk

_"may the source be with you"_ - anon.
