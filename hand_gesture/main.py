import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips =[8, 12, 16, 20]
thumb_tip= 4

def counting_fingers(image, hand_landmarks, handNo = 0):
    fingers = []
    if hand_landmarks:
        landmarks = hand_landmarks[handNo].landmark
        print(landmarks)

def draw_hand_landmarks(image, hand_landmarks):
    if hand_landmarks:
        for landmarks in hand_landmarks:
            mp_drawing.draw_landmarks(
                image, landmarks, mp_hands.HAND_CONNECTIONS
            )


while True:
    ret,image = cap.read()
    image = cv2.flip(image, 1)
    
    results = hands.process(image)
    
    hand_landmarks = results.multi_hand_landmarks
    if results.multi_hand_landmarks:
        image_width, image_height, c = image.shape
        for hand_landmark in results.multi_hand_landmarks:
            # accessing the landmarks by their position
            lm_list = []
            for id, lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)
            for tip in finger_tips:
                x, y = int(
                    lm_list[tip].x * image_width), int(lm_list[tip].y * image_height)

                cv2.circle(image, (x, y), 10, (255, 10, 0), cv2.FILLED)
                finger_fold_status = []
                # Changing the color to green when fist is closed
                if lm_list[tip].x < lm_list[tip - 3].x:
                    cv2.circle(image, (x, y), 15, (0, 255, 0), cv2.FILLED)
                    finger_fold_status.append(True)
                else:
                    finger_fold_status.append(False)

                if all(finger_fold_status):
                    if lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y:
                        print("LIKE")
                    if lm_list[thumb_tip].y > lm_list[thumb_tip - 1].y > lm_list[thumb_tip - 2].y:
                        print("DISLIKE")
                


    draw_hand_landmarks(image, hand_landmarks)
    #counting_fingers(image, hand_landmarks)
    

    cv2.imshow("hand tracking", image)
    cv2.waitKey(1)