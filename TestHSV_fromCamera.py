import cv2 as cv
import numpy as np

def nothing(x):
    pass

def getPixelInWin(event, x, y, flags, param):
    global frame
    if event == cv.EVENT_LBUTTONDOWN:
        img = cv.cvtColor(frame, cv.COLOR_BGR2HLS)
        print("BGR =", frame[y][x], "  HSV =", img[y][x])
        img = np.zeros((200, 200, 3), np.uint8)
        img[...] = frame[y][x]
        cv.imshow("Color", img)

cap = cv.VideoCapture(0)

cv.namedWindow('result')

cv.createTrackbar('Blur', 'result', 0, 29, nothing)

cv.createTrackbar('minH', 'result', 0, 255, nothing)
cv.createTrackbar('minS', 'result', 0, 255, nothing)
cv.createTrackbar('minV', 'result', 0, 255, nothing)

cv.createTrackbar('maxH', 'result', 128, 255, nothing)
cv.createTrackbar('maxS', 'result', 128, 255, nothing)
cv.createTrackbar('maxV', 'result', 128, 255, nothing)

ret, frame = cap.read()

cv.imshow("RGB", frame)
cv.setMouseCallback("RGB", getPixelInWin)

while(True):

    ret, frame = cap.read()

    blur = cv.getTrackbarPos('Blur', 'result') + 1

    frame = cv.blur(frame, (blur, blur))
    cv.imshow("RGB", frame)

    minH = cv.getTrackbarPos('minH', 'result')
    minS = cv.getTrackbarPos('minS', 'result')
    minV = cv.getTrackbarPos('minV', 'result')

    maxH = cv.getTrackbarPos('maxH', 'result')
    maxS = cv.getTrackbarPos('maxS', 'result')
    maxV = cv.getTrackbarPos('maxV', 'result')

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv = cv.blur(hsv, (5, 5))
    #cv.imshow("HSV", hsv)
    mask = cv.inRange(hsv, (minH, minS, minV), (maxH, maxS, maxV))
    cv.imshow("Mask", mask)
    result = cv.bitwise_and(frame, frame, mask = mask)
    cv.imshow("Result", result)

    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()
