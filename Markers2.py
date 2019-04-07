Image = cv2.imread('/frame.png')

Image = cv2.resize(image, (64,64)) обрезка картинки. 

noDrive = cv2.inRange(noDrive, (89, 91, 149), (255, 255, 255)) перевод картинки в черно белую по конкертным диапозонам.

Меняем изображение с камеры:
roImg=cv2.resize(roImg, (64,64))
+ бинаризация inRange (89, 124, 73), (255, 255, 255)

Проверяем (сверяем) каждый пиксель в изображении с камеры и эталоном. 

noDrive_val = 0
pedistrain_val = 0
for i in range(64):
for j in range(64):
if roImg[i][j] == noDrive[i][j]:
noDrive_val += 1
if roimg[i][j] == .....

Далее просто сравниваем валовые значения
