import cv2

# # Tasvirni o‘qish
img = cv2.imread('Odilbek.png')

# # Tasvirni ko‘rsatish
cv2.imshow('Rasm', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite('Odilbek.png', cv2.imread('Odilbek.png'))

# cap = cv2.VideoCapture('videoplayback.mp4')
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     cv2.imshow('Video', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture(0)  # 0 - default kamera
# while True:
#     ret, frame = cap.read()
#     cv2.imshow('Kamera', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# img2 = cv2.resize(img, (100, 100))

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('Yuzlar', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

