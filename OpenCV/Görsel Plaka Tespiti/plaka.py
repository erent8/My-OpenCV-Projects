import cv2
import pytesseract

# Görüntüyü yükleyin
image = cv2.imread('download.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gürültü azaltma ve kenar algılama
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

# Konturları bulma
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    # Konturun alanını hesaplayın ve uygun alan aralığına sahip konturları filtreleyin
    if 1000 < cv2.contourArea(contour) < 10000:
        x, y, w, h = cv2.boundingRect(contour)
        # Konturun oranını kontrol edin (plaka genellikle geniş bir dikdörtgendir)
        aspect_ratio = w / float(h)
        if 2 < aspect_ratio < 6:
            # Plaka adayını görselleştirin
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # Plaka adayının görüntüsünü alın
            plate_image = gray[y:y+h, x:x+w]
            # Tesseract ile metni okuyun
            text = pytesseract.image_to_string(plate_image, config='--psm 8')
            print("Plaka Metni: ", text)

# Sonuçları göster
cv2.imshow('Plaka Algılama', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
