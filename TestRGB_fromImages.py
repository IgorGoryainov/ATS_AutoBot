import cv2 as cv

def nothing(x):
    pass

#cap = cv.VideoCapture(0)

cv.namedWindow('result')

cv.createTrackbar('Blur', 'result', 1, 29, nothing)

cv.createTrackbar('minH', 'result', 0, 179, nothing)
cv.createTrackbar('minS', 'result', 7, 255, nothing)
cv.createTrackbar('minV', 'result', 171, 255, nothing)

cv.createTrackbar('maxH', 'result', 3, 255, nothing)
cv.createTrackbar('maxS', 'result', 255, 255, nothing)
cv.createTrackbar('maxV', 'result', 227, 255, nothing)

color = cv.imread('vosem-chervey.jpg.png', -1)
color = cv.cvtColor(color, cv.COLOR_BGRA2BGR)
#cv.imshow("Source", color)

while(True):

    #ret, frame = cap.read()
    hsv = cv.cvtColor(color, cv.COLOR_BGR2HSV)
    srcCopy = color.copy()
    ##cv.imshow("HSV", hsv)

    Blur = cv.getTrackbarPos('Blur', 'result') + 1

    minH = cv.getTrackbarPos('minH', 'result')
    minS = cv.getTrackbarPos('minS', 'result')
    minV = cv.getTrackbarPos('minV', 'result')

    maxH = cv.getTrackbarPos('maxH', 'result')
    maxS = cv.getTrackbarPos('maxS', 'result')
    maxV = cv.getTrackbarPos('maxV', 'result')

    hsv = cv.blur(hsv, (Blur, Blur))
    #cv.imshow("Blur", hsv)

    #mask = cv.inRange(hsv, (minR, minG, minB), (maxR, maxG, maxB))
    #cv.imshow("Mask", mask)

    mask2 = cv.inRange(hsv, (minH, minS, minV), (maxH, maxS, maxV))
    cv.imshow("Mask2", mask2)

    contours = cv.findContours(mask2, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    contours = contours[0]
    if contours:
        contours = sorted(contours, key=cv.contourArea, reverse=True)
        #help(cv.drawContours)
        cv.drawContours(srcCopy, contours[0:10], -1, (255, 150, 0), 2)
        cv.imshow("Contours", srcCopy)

    #maskEr = cv.erode(mask, None, iterations = 2)
    ##cv.imshow("Erode", maskEr)

    #maskDi = cv.dilate(maskEr, None, iterations = 4)
    #cv.imshow("Dilate", maskDi)

    #result = cv.bitwise_and(frame, frame, mask = mask)
    #cv.imshow("Result", result)

    #result = cv.bitwise_and(color, color, mask = mask2)
    #cv.imshow("Result2", result)

    if cv.waitKey(1) == 27:
        break

#cap.release()
cv.destroyAllWindows()
