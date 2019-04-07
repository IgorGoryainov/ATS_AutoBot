rgb = cv2.imread()
rgb = cv2.resize(rgb, (700,350))

Хранение пикселей в массиве 
[x, y, [b, g, r]]

b = rgb[:, :, 0]
g = rgb[:, :, 1]
r = rgb[:, :, 2]

cv2.imshow("b", b)

hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)

h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

h - определяет сам цвет (столбики равны)
s - определяет насыщенность цвета (чем более контрастен и насыщен, тем больше составляющая)
v - яркость

frame = cv2.resize(frame, (60,120)) для светофора лучше всего оьрезать в такие размеры
cutedFrame = frame[20:101, 8:52]
hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
v = hsv[:, :, 2] для распознания нужна только яркость

red_sum = numpy.sum(v[0:27, 0:44])
yellow_sum = numpy.sum(v[28:54, 0:44])
green_sum = numpy.sum(v[55:81, 0:44])

cv2.rectangle(cutedFrame, (0,0), (44,27), (0,0,255), 2)
Так начертить три прямоугольника используя предыдущие координаты, указывая левый верхний и правый нижний угол
