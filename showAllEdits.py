import cv2
import pickle
import cvzone
import numpy as np

cap = cv2.VideoCapture('video/vid1.mp4')
width, height = 1192, 668
with open('TerminalPos', 'rb') as f:
    posList = pickle.load(f)

print(posList)
def empty(a):
    pass


cv2.namedWindow("Vals")
cv2.resizeWindow("Vals", 1192, 668)
cv2.createTrackbar("Val1", "Vals", 25, 50, empty)
cv2.createTrackbar("Val2", "Vals", 16, 50, empty)
cv2.createTrackbar("Val3", "Vals", 5, 50, empty)


def checkSpaces():
    spaces = 0
    for pos in posList:
        x1, y1, x2, y2 = pos

        imgCrop = imgThres[y1:y2, x1:x2]
        count = cv2.countNonZero(imgCrop)

        if count < 100:
            color = (0, 200, 0)
            thic = 5
            spaces += 1

        else:
            color = (0, 0, 200)
            thic = 2

        cv2.rectangle(img, (x1, y1), (x2, y2), color, thic)

        cv2.putText(img, str(cv2.countNonZero(imgCrop)), (x1, y2 - 6), cv2.FONT_HERSHEY_PLAIN, 1,
                    color, 2)

    cvzone.putTextRect(img, f'Free: {spaces}/{len(posList)}', (50, 60), thickness=3, offset=20,
                       colorR=(0, 200, 0))


while True:

    # Get image frame
    success, img = cap.read()
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    # img = cv2.imread('img.png')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    # ret, imgThres = cv2.threshold(imgBlur, 150, 255, cv2.THRESH_BINARY)

    val1 = cv2.getTrackbarPos("Val1", "Vals")
    val2 = cv2.getTrackbarPos("Val2", "Vals")
    val3 = cv2.getTrackbarPos("Val3", "Vals")
    if val1 % 2 == 0: val1 += 1
    if val3 % 2 == 0: val3 += 1
    imgThres = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY_INV, val1, val2)
    imgThres = cv2.medianBlur(imgThres, val3)
    kernel = np.ones((3, 3), np.uint8)
    imgThres = cv2.dilate(imgThres, kernel, iterations=1)

    checkSpaces()
    # Display Output

    cv2.imshow("Image", img)
    cv2.imshow("ImageGray", imgGray)
    cv2.imshow("ImageBlur", imgBlur)
    cv2.imshow("ImageThres", imgThres)
    key = cv2.waitKey(1)
    if key == ord('r'):
        pass
