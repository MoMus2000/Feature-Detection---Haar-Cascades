import cv2, time
face_casecade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)
a=1
d=True
while d == True:
    a= a+1
    check , frame = video.read()
    face_found = False
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_casecade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    for x,y,w,h in faces:
        if w>0:
            face_found =True

        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Capturing",frame)
    if face_found ==True:
        print("Face Detected")
    else:
        print("Face Not Detected")
    key = cv2.waitKey(1)
    if key == ord('x'):
        d= False

print(a)
video.release()
cv2.destroyAllWindows()
