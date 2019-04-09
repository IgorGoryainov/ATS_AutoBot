import cv2 as cv

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

cam = cv.VideoCapture(0)

while (cv.waitKey(1) != 27):
    ret, frame = cam.read()
    frame = cv.resize(frame, (400, 300))

    (rects, weights) = hog.detectMultiScale(frame, scale = 1.1, winStride = (2, 2))     #изменяя эти параметры можно играть со скоростью/качеством

    for (x, y, sx, sy), wei in zip(rects, weights):
        cv.rectangle(frame, (x, y), (x + sx, y + sy), (0, 0, 255), 2)

    cv.imshow("Frame", frame)

cv.destroyAllWindows()
cam.release()
