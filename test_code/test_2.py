import cv2
print "OpenCV version :  {0}".format(cv2.__version__)
major_ver, minor_ver, subminor_ver = (cv2.__version__).split('.')
print "Major version :  {0}".format(major_ver)
print "Minor version :  {0}".format(minor_ver)
print "Subminor version :  {0}".format(subminor_ver)
