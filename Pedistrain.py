import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

img_size = [200, 360]

scr = np.float32([[20, 200],
                  [350, 200],
                  [275, 120],
                  [85, 120]])

dst = np.float32([[0, img_size[0]],
                [img_size[1], img_size[0]],
                [img_size[1], 0],
                [0, 0]])

scr_draw = np.array(scr, dtype = np.int32)

while (cv.waitKey(1) != 27):
    ret, frame = cam.read()

    resized = cv.resize(frame, (img_size[1], img_size[0]))
    cv.imshow("frame", resized)

    red = resized[:, :, 2]
    binary = np.zeros_like(red)
    binary[(red > 200)] = 1
    #cv.imshow("RED", binary)

    hls = cv.cvtColor(resized, cv.COLOR_BGR2HLS)
    light = resized[:, :, 2]
    binary2 = np.zeros_like(light)
    binary2[(red > 160)] = 1

    all_binary = np.zeros_like(binary)
    all_binary[((binary == 1) | (binary2 == 1))] = 255
    #cv.imshow("Binary", all_binary)

    all_binary_visual = all_binary.copy()
    cv.polylines(all_binary_visual, [scr_draw], True, 255)
    cv.imshow("Poligon", all_binary_visual)

    matrix = cv.getPerspectiveTransform(scr, dst)
    warped = cv.warpPerspective(all_binary, matrix, (img_size[1], img_size[0]), flags = cv.INTER_LINEAR)
    cv.imshow("Warped", warped)


    histogram = np.sum(warped[warped.shape[0] // 2 :, :], axis = 0)

    midpoint = histogram.shape[0] // 2
    IndWhitestColumn_L = np.argmax(histogram[: midpoint])
    IndWhitestColumn_R = np.argmax(histogram[midpoint :]) + midpoint
    warped_visual = warped.copy()
    cv.line(warped_visual, (IndWhitestColumn_L, 0), (IndWhitestColumn_L, warped_visual.shape[0]), 110, 2)
    cv.line(warped_visual, (IndWhitestColumn_R, 0), (IndWhitestColumn_R, warped_visual.shape[0]), 110, 2)
    cv.imshow("WhitestColumn", warped_visual)


    nWindows = 9
    window_height = np.int(warped.shape[0] / nWindows)
    window_half_width = 25

    XCenterWind_L = IndWhitestColumn_L
    XCenterWind_R = IndWhitestColumn_R

    left_lane_inds = np.array([], dtype = np.int16)
    right_lane_inds = np.array([], dtype=np.int16)

    out_img = np.dstack((warped, warped, warped))

    nonzero = warped.nonzero()
    WhitePixelIndY = np.array(nonzero[0])
    WhitePixelIndX = np.array(nonzero[1])

    for window in range(nWindows):

        win_y1 = warped.shape[0] - (window + 1) * window_height
        win_y2 = warped.shape[0] - (window) * window_height

        left_win_x1 = XCenterWind_L - window_half_width
        left_win_x2 = XCenterWind_L + window_half_width
        right_win_x1 = XCenterWind_R - window_half_width
        right_win_x2 = XCenterWind_R + window_half_width

        cv.rectangle(out_img, (left_win_x1, win_y1), (left_win_x2, win_y2), (50 + window * 21, 0, 0), 2)
        cv.rectangle(out_img, (right_win_x1, win_y1), (right_win_x2, win_y2), (0, 0, 50 + window * 21), 2)
        cv.imshow("windows", out_img)

        good_left_inds = ((WhitePixelIndY >= win_y1) & (WhitePixelIndY <= win_y2) &
                          (WhitePixelIndX >= left_win_x1) & (WhitePixelIndX <= left_win_x2)).nonzero()[0]

        good_right_inds = ((WhitePixelIndY >= win_y1) & (WhitePixelIndY <= win_y2) &
                          (WhitePixelIndX >= right_win_x1) & (WhitePixelIndX <= right_win_x2)).nonzero()[0]

        left_lane_inds = np.concatenate((left_lane_inds, good_left_inds))
        right_lane_inds = np.concatenate((right_lane_inds, good_right_inds))

        if len(good_left_inds) > 50:
            XCenterWind_L = np.int(np.mean(WhitePixelIndX[good_left_inds]))

        if len(good_right_inds) > 50:
            XCenterWind_R = np.int(np.mean(WhitePixelIndX[good_right_inds]))

    out_img[WhitePixelIndY[left_lane_inds], [WhitePixelIndX[left_lane_inds]]]= [255, 0, 0]
    out_img[WhitePixelIndY[right_lane_inds], [WhitePixelIndX[right_lane_inds]]] = [0, 0, 255]
    cv.imshow("Lane", out_img)

    leftX = WhitePixelIndX[left_lane_inds]
    leftY = WhitePixelIndY[left_lane_inds]
    rightX = WhitePixelIndX[right_lane_inds]
    rightY = WhitePixelIndY[right_lane_inds]

    left_fit = np.polyfit(leftY, leftX, 2)
    right_fit = np.polyfit(rightY, rightX, 2)

    center_fit = ((left_fit + right_fit / 2))

    for ver_ind in range(out_img.shape[0]):
        gor_ind = ((center_fit[0]) * (ver_ind ** 2) +
                   center_fit[1] * ver_ind + center_fit[2])
        cv.circle(out_img, (int(gor_ind), int(ver_ind)), 2, (255, 0, 255), 1)

    cv.imshow("Center", out_img)