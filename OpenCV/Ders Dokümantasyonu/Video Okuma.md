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





