import cv2 as cv

def nothing(x):
    pass

cap = cv.VideoCapture(0)

cv.namedWindow('result')

cv.createTrackbar('minR', 'result', 0, 255, nothing)
cv.createTrackbar('minG', 'result', 0, 255, nothing)
cv.createTrackbar('minB', 'result', 0, 255, nothing)

cv.createTrackbar('maxR', 'result', 0, 255, nothing)
cv.createTrackbar('maxG', 'result', 0, 255, nothing)
cv.createTrackbar('maxB', 'result', 0, 255, nothing)



while(True):

    ret, frame = cap.read()

    minR = cv.getTrackbarPos('minR', 'result')
    minG = cv.getTrackbarPos('minG', 'result')
    minB = cv.getTrackbarPos('minB', 'result')

    maxR = cv.getTrackbarPos('maxR', 'result')
    maxG = cv.getTrackbarPos('maxG', 'result')
    maxB = cv.getTrackbarPos('maxB', 'result')

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv = cv.blur(hsv, (5, 5))
    cv.imshow("HSV", hsv)
    mask = cv.inRange(hsv, (minR, minG, minB), (maxR, maxG, maxB))
    cv.imshow("Mask", mask)
    result = cv.bitwise_and(frame, frame, mask = mask)
    cv.imshow("Result", result)

    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()
