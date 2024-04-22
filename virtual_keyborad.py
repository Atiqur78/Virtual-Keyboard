import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

initHand = mp.solutions.hands
mainHand = initHand.Hands()
draw = mp.solutions.drawing_utils

keys = [["A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P", "^", "$"],
        ["Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "%", "*"],
        ["W", "X", "C", "V", "B", "N", ",", ";", ":", "!", ".", "?"]]

finalText = ""
clicked = False

def handLandmarks(colorImg):
    landmarkList = []
    landmarkPositions = mainHand.process(colorImg)
    if landmarkPositions.multi_hand_landmarks:
        for hand_landmarks in landmarkPositions.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                landmarkList.append([landmark.x * colorImg.shape[1], landmark.y * colorImg.shape[0]])
    return landmarkList

def drawAll(img, buttonList):
    for button in buttonList:
        x, y, w, h = button.pos
        cv2.rectangle(img, (x, y), (x + w, y + h), (64, 64, 64), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 55), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img

class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.text = text
        self.size = size

buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50, 85, 85], key))

buttonList.append(Button([50, 350, 885, 85], "Space"))
buttonList.append(Button([950, 350, 285, 85], "Delete"))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    landmark_list = handLandmarks(img)
    img = drawAll(img, buttonList)

    if landmark_list:
        for button in buttonList:
            x, y, w, h = button.pos
            if x < landmark_list[8][0] < x + w and y < landmark_list[8][1] < y + h:
                if button.text == "Space" or button.text == "Delete":
                    if not clicked:
                        finalText += " " if button.text == "Space" else finalText[:-1]
                        clicked = True
                else:
                    finalText += button.text
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 55), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (64, 64, 64), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 55), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

    cv2.rectangle(img, (50, 580), (1235, 680), (64, 64, 64), cv2.FILLED)
    cv2.putText(img, finalText, (60, 645), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

    cv2.imshow('Virtual Keyboard', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
