import cv2
import pickle

try:
    with open('TerminalPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

width, height = 107, 48
drawing = False
start_x, start_y = -1, -1
current_x, current_y = -1, -1

def mouseClick(events, x, y, flags, params):
    global drawing, start_x, start_y, current_x, current_y

    if events == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y
    elif events == cv2.EVENT_LBUTTONUP:
        drawing = False
        posList.append((start_x, start_y, x, y))
        with open('TerminalPos', 'wb') as f:
            pickle.dump(posList, f)
    elif events == cv2.EVENT_MOUSEMOVE:
        if drawing:
            current_x, current_y = x, y

while True:
    img = cv2.imread('PPS-3-CAM-SCREEN-SAVE.png')
    for pos in posList:
        x1, y1, x2, y2 = pos
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

    if drawing:
        cv2.rectangle(img, (start_x, start_y), (current_x, current_y), (0, 255, 0), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
