import cv2
import numpy as np

def process_image(img):
    # Görüntüyü gri tonlamaya çevir
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Görüntüyü bulanıklaştır
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Kenar tespiti
    edges = cv2.Canny(blur, 50, 150)
    
    # Hough dönüşümü ile çizgileri tespit et
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
    return img

def main(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Video okuma işlemi bitti veya hata oluştu.")
            break

        processed_frame = process_image(frame)
        cv2.imshow('Şerit Takibi', processed_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' tuşuna basıldığında çık
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = 'yol.mp4'  # Video dosyası
    main(video_path)


