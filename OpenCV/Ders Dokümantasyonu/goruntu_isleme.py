import cv2
from matplotlib import pyplot as plt

# Görüntüyü gri tonlama olarak oku
resim = cv2.imread("download.jpg")

cv2.namedWindow("Arhavi",cv2.WINDOW_NORMAL)
cv2.imshow("Arhavi ", resim)

# Matplotlib ile görüntülemek için
plt.imshow(resim)  # cmap argümanını kullanarak renk haritasını belirt
plt.title("Arhavi")
plt.show()

# Kullanıcıdan bir tuş girişi bekler
e = cv2.waitKey(0)

# Tuşa basılma durumlarını kontrol et
if e == 27:
    print("ESC tuşuna basıldı")
elif e == ord("q"):
    print("q tuşuna basıldı, resim kaydedildi")
    cv2.imwrite("download_saved.jpg", resim)  # Üzerine yazmamak için yeni bir dosya adı

# Tüm pencereleri kapat
cv2.destroyAllWindows()
