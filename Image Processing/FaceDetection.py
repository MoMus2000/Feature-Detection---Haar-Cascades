import cv2
face_cascade = cv2.CascadeClassifier("/Users/a./Desktop/Image Processing/haarcascade_frontalface_default.xml")
img = cv2.imread("/Users/a./Desktop/Image Processing/UNADJUSTEDNONRAW_thumb_9d8.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=10)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("GRAY",img)
cv2.waitKey(0)
cv.destroyAllWindows()
