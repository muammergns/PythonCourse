import cv2
camera = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    _,img = camera.read()
    grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImage,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow("Press q for quit",img)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()

#NOTE - hazır yüz tanıma fonksiyonu kullanıldı.
# diğer özelliklere de bakılacak