if cv.waitKey(1) == ord("q"):
break
cap.release()
cv.destroyAllWindows()

Подбор аргументов
def nothing(x):
pass
cv2.namedWindow("result") создание окна
cv2.createTrackbar('minb', 'result', 0, 255, nothing)
В цкиле:
minb = cv2.getTrackbarPos('minb', 'result')

cap = cv.VideoCapture(0) чтение изображение с камеры, точнее обозначение откуда брать эту переменную

ret, frame = cap.read() в while перевод в массив изображения с камеры

cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

cv2.imshow("название окна", frame)

cv2.bitwise_and(frame, frame, mask = mask) замена белой 1 на исходный цвет

cv2.inRange(hsv, (minb,ming,minr), (maxb,maxg,maxr))

hsv = cv2.blur(hsv, (5,5)) размытие матрица

maskEr=cv2.erode(mask, None, iterations = 2) именно с маской (уменьшает кол-во помех белых (похожих цветов))

maskDi = cv2.dilate(mask, None, iterations = 4) увеличивает помехи (белые точки лишние)

contours = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) поиск конутров который выведет x и y каждой точки

countours = countours[1]

cv.drawContours(frame, contours, -1, (255,0,255), 3) рисование контура на каком либо изображении, -1 это значит все контуры из массива, потом идет цвет линии и толщина

sorted(contours, key = cv.contourArea, reverse=True) сортировка массива контуров по площади по убыванию

contours[0] - первый контур в массиве после сортировки

if contours: contours=sorted(contours,key=cv.contourArea, reverse=True)
cv.drawCountrous(frame, contours, 0, (255,0,255),3)
cv.imshow("c", countours)
Проверка есть ли контуры и вывод их на экран

(x,y, w, h)=cv.boundingRect(contours[0]) выводит координату левого верхнего угла прямоугольника, в который вписан контур, потом длину по x и y этого прямоугольника

cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2) рисование прямоугольника (координаты левого верхнего угла и правого нижнего)

roImg = frame[y:y+h, x:x+w] выделение области из массива изображения первоначально обозначая кол во столбцов, а после строк. Это можно сразу выводить.

framecopy = frame.copy()
