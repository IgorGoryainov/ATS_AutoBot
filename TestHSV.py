import cv2 as cv
import numpy as np


def getMousePosInWin_SV(event, x, y, flags, param):
    global SV_BGR_image
    if event == cv.EVENT_LBUTTONDOWN:
        print('SV vs S: HSV =', img[y][x], '  BGR =', SV_BGR_image[y][x])

def getMousePosInWin_HV(event, x, y, flags, param):
    global HV_BGR_image
    if event == cv.EVENT_LBUTTONDOWN:
        img = cv.cvtColor(HV_BGR_image, cv.COLOR_BGR2HLS)
        print('HV vs S: HSV =', img[y][x], '  BGR =', HV_BGR_image[y][x])

def getMousePosInWin_HS(event, x, y, flags, param):
    global HS_BGR_image
    if event == cv.EVENT_LBUTTONDOWN:
        img = cv.cvtColor(HS_BGR_image, cv.COLOR_BGR2HLS)
        print('HS vs V: HSV =', img[y][x], '  BGR =', HS_BGR_image[y][x])

im_width = 255
im_height = 255

SV_image = np.zeros((im_height, im_width, 3), np.uint8)
HV_image = np.zeros((im_height, im_width, 3), np.uint8)
HS_image = np.zeros((im_height, im_width, 3), np.uint8)

cv.namedWindow('result')
cv.createTrackbar('H', 'result', 128, 255, nothing)
cv.createTrackbar('S', 'result', 128, 255, nothing)
cv.createTrackbar('V', 'result', 128, 255, nothing)

cv.imshow("SV vs H", SV_image)
cv.imshow("HV vs S", HV_image)
cv.imshow("HS vs V", HS_image)
cv.setMouseCallback("SV vs H", getMousePosInWin_SV)
cv.setMouseCallback("HV vs S", getMousePosInWin_HV)
cv.setMouseCallback("HS vs V", getMousePosInWin_HS)

while(True):

    Hue = cv.getTrackbarPos('H', 'result')
    Sat = cv.getTrackbarPos('S', 'result')
    Val = cv.getTrackbarPos('V', 'result')

    for i in range(im_height):
        for j in range(im_width):
            SV_image[j][i] = (Hue, i, j)
            HV_image[j][i] = (i, Sat, j)
            HS_image[j][i] = (i, j, Val)

    SV_BGR_image = cv.cvtColor(SV_image, cv.COLOR_HLS2BGR)
    cv.imshow("SV vs H", SV_BGR_image)

    HV_BGR_image = cv.cvtColor(HV_image, cv.COLOR_HLS2BGR)
    cv.imshow("HV vs S", HV_BGR_image)

    HS_BGR_image = cv.cvtColor(HS_image, cv.COLOR_HLS2BGR)
    cv.imshow("HS vs V", HS_BGR_image)

    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows()
