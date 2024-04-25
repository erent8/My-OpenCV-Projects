import cv2
import pytesseract

# Tesseract OCR'nin çalışabilmesi için tesseract yolunu belirtin
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path)

    # Görüntü boş mu diye kontrol et
    if image is None:
        print("Görüntü okunamadı. Lütfen dosya yolunu kontrol edin.")
        return ""

    # Görüntüyü gri tonlamaya dönüştür
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Görüntüyü bulanıklaştır
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Görüntüdeki metinleri tanı
    extracted_text = pytesseract.image_to_string(blurred_image)

    return extracted_text

# OCR yapılacak görüntünün dosya yolunu belirtin
image_path = 'download.jpg'

# OCR işlemini gerçekleştir
extracted_text = ocr_image(image_path)

# Tanınan metni yazdır
print("OCR ile Tanınan Metin:")
print(extracted_text)
