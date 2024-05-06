import cv2

img = cv2.imread("download.jpg")

cv2.imshow("İlk Resim",img)
k =cv2.waitkey(0) & 0xFF

if k == 27: 
# esc ye basmak demektir.
    cv2.destroyAllWindows()
elif k == ord("q"):
    cv2.imwrite("download.jpg")
    cv2.destroyAllWindows()