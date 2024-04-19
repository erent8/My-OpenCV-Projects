import cv2
 #---------------- Video Oynatma -----------------#

# cam = cv2.VideoCapture("kontravolta.mp4")

# while cam.isOpened():
#     ret,frame = cam.read()

#     if not ret:
#         print("Kameradan Goruntu Okunamiyor")
#         break

#     cv2.imshow("Görüntü",frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         print("video kapatıldı")
#         break

# cam.release()
# cv2.destroyAllWindows()

# ------------------ VİDEO KAYIT ETME --------------------- #

import cv2

cam = cv2.VideoCapture(0)

# Doğru fonksiyon adı 'fourcc'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("kontravolta.", fourcc, 30.0, (640, 480))

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        print("Kameradan goruntu alinamadi.")
        break
    out.write(frame)
    cv2.imshow("Kamera", frame)

    if cv2.waitKey(1) == ord("q"):
        print("videodan ayrıldınız.")
        break

cam.release()
out.release()
cv2.destroyAllWindows()










# ------------------- Boyutlandırma --------------------- #


# cam = cv2.VideoCapture(0)

# print(cam.get(3))
# print(cam.get(4))

# cam.set(3,400) 
# cam.set(4,350)

# if not cam.isOpened():
#     print("Kamera tanınmadı...")
#     exit()

# while True:
#     ret, frame = cam.read()

#     if not ret:
#         print("Kameradan Goruntu Okunamiyor.")
#         break

#     cv2.imshow("Kamera",frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         print("Goruntu Sonlandirildi.")
#         break

# cam.release()
# cv2.destroyAllWindows()



