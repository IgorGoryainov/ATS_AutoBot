img_size = [200, 360]

resized = cv2.resize(frame, (img_size[1], img_size[0]))

r_channel = resized[:, :, 2]
binary=np.zeros_like(r_channel)
binnary[(r_channel>200)]=1

hls = cv2.cvtColor(resized, cv2.COLOR_BGR2HLS)
s_channel = resized[:, :, 2]
binary2=np.zeros_like(s_channel)
binnary2[(s_channel>160)]=1
Отвечает за яркость

allBinary = np.zeros_like(binary)
allBinary[(binary==1)|(binary2==1)]=255

src = np.float32([20, 200], [350,200], [275, 120], [85, 120]) координаты для трапеции (вид сверху делает) перенести в начало программы

src_draw = np.array(src, dtype=np.int32)
Массив для рисования

allBinary_visual = allBinary.copy()
cv2.polylines(allBinary_visual, [src_draw], True, 255)

dst = np.floar32([[0, img_size[0]], [img_size[1], img_size[0]], [img_size[1], 0], [0,0]])

M = cv2.getPerspectiveTransform(src, dst)
warped = cv2.warpPerspective(allBinary, M, (img_size[1], img_size[0]), flags = cv2.INTER_LINEAR) Это преобразование используя матрицу, изображение из трапеции в вид сверху

histogram = np.sum(warped[warped.shape[0]//2:, ☺, axis = 0)

midpoint = histogram.shape[0]//2
L = np.argmax(histogram[:midpoint])
R = np.argmax(histogram[midpoint:])+midpoint
warped_visual = warped.copy()
Находим линии максимума

cv2.line(warped_visual, (L, 0), (L, warped_visual.shape[0]), 110, 2)
cv2.line(warped_visual, (R, 0), (R, warped_visual.shape[0]), 110, 2)
Рисуем линии

nwindows = 9
window_height = np.int(warped.shape[0]/nwindows)
window_half_width = 25

XcL = L
XcR = R

left_lane = np.array([], dtype = np.int16)
right_lane = np.array([], dtype = np.int16)
out_img = np.dstack((warped, warped, warped))

nonzero = warped.nonzero()
WPY = np.array(nonzero[0])
WPX= np.array(nonzero[1])

for window in range(nwindows):
win_y1 = warped.shape[0] - (window+1)*window_height
win_y2 = warped.shape[0] - (window)*window_height

lwx1 = XcL - window_half_width
lwx2 = XcL + window_half_width
rwx1 = XcR - window_half_width
rwx2 = XcR + window_half_width

cv2.rectangle(out_img, (lwx1, win_y1), (lwx2, win_y2), (50 + window*21, 0, 0), 2)
cv2.rectangle(out_img, (rwx1, win_y1), (rwx2, win_y2), (0, 0, 50 + window*21), 2)
goodleft = ((WPY>=win_y1) and (WPY < = win_y2) and (WPX >= lwx1) and (WPX <= lwx2)).nonzero()[0]
goodright = ((WPY>=win_y1) and (WPY < = win_y2) and (WPX >= rwx1) and (WPX <= rwx2)).nonzero()[0]
leftlaneinds = np.concantenate((leflaneinds, goodleft))
rightlaneinds = np.concantenate((rightlaneinds, goodright))

out_img(
