import numpy as np
import sys
import cv2_test
import dlib
import scipy
import sklearn

if cv2_test.__version__[0]!= '2':
    assert("cv2 version should be 2.4")
if sys.version_info[0]!='2':
    assert("we need python2")

