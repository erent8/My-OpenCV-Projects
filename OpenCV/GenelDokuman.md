

### 1. Giriş
#### OpenCV Nedir?
- OpenCV (Open Source Computer Vision Library), gerçek zamanlı bilgisayarlı görü ve makine öğrenimi projeleri için açık kaynaklı bir kütüphanedir.
- C++, Python, Java ve MATLAB gibi dillerde uygulama desteği sunar ve platform bağımsızdır.

#### OpenCV'nin Kurulumu
- Python ile OpenCV kullanımı için, pip kullanarak kolayca kurulum yapılabilir:
  ```bash
  pip install opencv-python
  ```

### 2. Temel Görüntü İşleme Operasyonları
#### Görüntü Yükleme, Gösterme ve Kaydetme
- `cv2.imread`, `cv2.imshow`, `cv2.imwrite` fonksiyonları sırasıyla görüntü yükleme, gösterme ve kaydetme işlemleri için kullanılır.
  ```python
  import cv2
  img = cv2.imread('image.jpg')  # Görüntüyü yükler
  cv2.imshow('Image', img)       # Görüntüyü ekranda gösterir
  cv2.imwrite('output.jpg', img) # Görüntüyü kaydeder
  ```

#### Renk Uzayları
- RGB, HSV ve L*a*b gibi farklı renk uzaylarına dönüşüm işlemleri için `cv2.cvtColor` fonksiyonu kullanılır.
  ```python
  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Görüntüyü gri tonlamaya çevirir
  ```

### 3. Görüntü Filtreleme
#### Kenar Belirleme
- Sobel ve Canny kenar belirleme yöntemleri sıklıkla kullanılır.
  ```python
  edges = cv2.Canny(gray_img, 100, 200)  # Canny kenar belirleme
  ```

### 4. Özellik Algılama ve Eşleştirme
#### Anahtar Nokta Dedektörleri
- SIFT, SURF, ve ORB OpenCV'de anahtar nokta dedektörü olarak kullanılabilir.
  ```python
  orb = cv2.ORB_create()
  keypoints = orb.detect(img, None)
  ```

### 5. Görüntü Segmentasyonu
#### Eşik Değeri Belirleme
- Basit eşikleme yöntemleri ile görüntü üzerinde belirli bir renk veya yoğunluk aralığını segmente edebilirsiniz.
  ```python
  ret, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
  ```

### 6. Video İşleme
#### Video Okuma ve Yazma
- `cv2.VideoCapture` ve `cv2.VideoWriter` fonksiyonları ile video işleme yapılabilir.
  ```python
  cap = cv2.VideoCapture('video.mp4')
  ```

### 7. Makine Öğrenimi ile Görüntü İşleme
#### Yüz Tanıma
- Haarcascades kullanarak yüz tanıma işlemi yapılabilir.
  ```python
  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)
  ```

### 8. Uygulamalar ve Proje Fikirleri
#### Trafik İşareti Tanıma
- Görüntü işleme teknikleri ve makine öğrenimi modelleri kullanarak trafik işareti tanıma sistemi geliştirilebilir.

Bu ders notları, OpenCV ile görüntü işleme ve makine öğrenimi konularında temel bir rehber olarak kullanılabilir. 
