# import the opencv library
import cv2

a = int(input("Choose which camera to use (Number) > "))
# define a video capture object
vid = cv2.VideoCapture(a)

width, height = int(input("Choose width (Max 1500) > ")), int(input("Choose height (Max 900) > "))

F1 = False
F2 = False
F3 = False

while True:
    # Capture the video frame
    liste = []
    liste2 = {"[0, 0, 0]": 0}
    maximum = []
    maxxx = ""
    ret, frame = vid.read()
    frame = cv2.resize(frame, (width, height))

    if F1:
        h, w, c = frame.shape
        for t in range(h):
            for y in range(w):
                frame[t][y][1] = 255 - frame[t][y][1]

    if F2:
        frame = frame[::-1]
        #

    if F3:
        h, w, c = frame.shape
        for i in range(480):
            for j in range(w):
                frame[i][j] = (frame[i][j][0], frame[i][j][0], frame[i][j][0])

    # Display the resulting frame
    cv2.imshow('Video', frame)
    maxx = 0
    # Get the color that is the most on the screen
    if cv2.waitKey(1) & 0xFF == ord('r'):
        for a in range(width):
            for b in range(height):
                liste.append(str(frame[a, b]))
        for i in liste:
            if i in liste2:
                liste2[i] += 1
            elif not i in liste2:
                liste2.update({i: 1})
        for i in liste:
            if maxx < liste2[i]:
                maxx = liste2[i]
        for i in liste:
            if maxx == liste2[i] and not maxx in maximum:
                maxxx = i
        print(maxxx)

    # All Functions
    if True:
        # Invert Image Colors
        if (cv2.waitKey(1) & 0xFF == ord('i')) and not F1:
            F1 = True
        if (cv2.waitKey(1) & 0xFF == ord('i')) and F1:
            F1 = False

        # Invert y pixels
        if (cv2.waitKey(1) & 0xFF == ord('o')) and not F2:
            F2 = True
        if (cv2.waitKey(1) & 0xFF == ord('o')) and F2:
            F2 = False

        # Idk
        if (cv2.waitKey(1) & 0xFF == ord('g')) and not F3:
            F3 = True
        if (cv2.waitKey(1) & 0xFF == ord('g')) and F3:
            F3 = False

    # Quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
