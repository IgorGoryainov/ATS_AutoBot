import cv2
import numpy
rgb = cv2.imread('z3.jpg')
while True:
    rgb = cv2.resize(rgb, (60, 120))
    cf = rgb[20:101, 8:52]
    ms = cf.copy()
    hsv = cv2.cvtColor(cf, cv2.COLOR_BGR2HSV)
    v = hsv[:, :, 2]
    red_sum = numpy.sum(v[0:27, 0:44])
    yellow_sum = numpy.sum(v[28:54, 0:44])
    green_sum = numpy.sum(v[55:81, 0:44])
    cv2.rectangle(ms, (0, 0), (44, 27), (0, 0, 255), 2)
    cv2.rectangle(ms, (0, 28), (44, 54), (255, 0, 255), 2)
    cv2.rectangle(ms, (0, 58), (44, 81), (0, 255, 255), 2)
    cv2.imshow('hsv', v)
    cv2.imshow('cf', ms)
    print(red_sum, yellow_sum, green_sum)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.DesrtoyAllWindows()
