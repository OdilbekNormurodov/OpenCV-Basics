import cv2  # OpenCV kutubxonasini chaqirish

# --- 1. Rasmni kompyuterdan o'qish ---
img = cv2.imread('Odilbek.png')

# --- 2. O'qilgan rasmni ekranda ko'rsatish ---
cv2.imshow('Rasm', img)
cv2.waitKey(0)  # Tugmachani bosmaguncha rasm oynasi ochiq qoladi
cv2.destroyAllWindows()  # Barcha oynalarni yopadi

# --- 3. Rasmni kompyuterga qayta saqlash (hozircha izohda) ---
cv2.imwrite('Odilbek.png', cv2.imread('Odilbek.png'))

# --- 4. Video faylni o'qib, uni oynada ko'rsatish (hozircha izohda) ---
cap = cv2.VideoCapture('videoplayback.mp4')
while True:
    ret, frame = cap.read()  # Har bir freymni o'qish
    if not ret:
        break  # Agar video tugagan bo‘lsa
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Q tugmasi bosilsa, to‘xtaydi
        break
cap.release()
cv2.destroyAllWindows()

# --- 5. Kompyuter kamerasidan jonli tasvir olish (hozircha izohda) ---
cap = cv2.VideoCapture(0)  # 0 - asosiy (default) kamera
while True:
    ret, frame = cap.read()
    cv2.imshow('Kamera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# --- 6. Rasmni qayta o'lchamini o'zgartirish (masalan, 100x100 px) ---
img2 = cv2.resize(img, (100, 100))

# --- 7. Rasmni kulrang formatga o'tkazish ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# --- 8. Yuzni aniqlash uchun Haar Cascade yuklash ---
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# --- 9. Rasmni kulrangga o'tkazish (yuz tanish uchun kerak) ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# --- 10. Yuzlarni aniqlash ---
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# --- 11. Topilgan yuzlar atrofini kvadrat bilan belgilash ---
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# --- 12. Yuzlar belgilangan rasmni ekranda ko‘rsatish ---
cv2.imshow('Yuzlar', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

