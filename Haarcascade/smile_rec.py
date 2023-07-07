import cv2
faceCascade = cv2.CascadeClassifier('D:/Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('D:/Downloads/opencv/sources/data/haarcascades/haarcascade_smile.xml')
cap = cv2.VideoCapture(0)

while True:
    true, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,204),2)
        gray_temp = gray[y:y+h, x:x+w]
        smile = smileCascade.detectMultiScale(gray_temp, scaleFactor= 1.3, minNeighbors=5)
        for i in smile:
            if len(smile)>1:
                cv2.putText(frame,"Smiling",(x,y-50),cv2.FONT_HERSHEY_PLAIN, 2,(255,0,0),3,cv2.LINE_AA)
    cv2.imshow('RESULT', frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()