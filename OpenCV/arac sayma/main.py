# import cv2
# import numpy as np

# def main(video_path):
#     cap = cv2.VideoCapture(video_path)
#     background_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=100, detectShadows=True)
#     car_count = 0

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Arka plan çıkarma
#         fg_mask = background_subtractor.apply(frame)
#         _, fg_mask = cv2.threshold(fg_mask, 250, 255, cv2.THRESH_BINARY)

#         # Gürültüyü azaltmak ve küçük konturları temizlemek için morfolojik işlemler
#         kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
#         fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)
#         fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

#         # Konturları bul
#         contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         for contour in contours:
#             if cv2.contourArea(contour) > 500:  # Min alanı ayarla
#                 x, y, w, h = cv2.boundingRect(contour)
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                 car_count += 1  # Her kontur için araç sayısını artır

#         # Araç sayısını göster
#         cv2.putText(frame, 'Araclar: {}'.format(car_count), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#         cv2.imshow('Araclar', frame)

#         if cv2.waitKey(30) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     video_path = 'kaza.mp4'  # Video dosyanızın yolu
#     main(video_path)



import cv2
import numpy as np

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    background_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=100, detectShadows=True)
    car_count = 0
    detection_line_position = 300  # Geçiş çizgisi pozisyonu
    detect_dict = {}  # Tespit edilen araçları saklamak için

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Arka plan çıkarma ve gürültü azaltma
        fg_mask = background_subtractor.apply(frame)
        _, fg_mask = cv2.threshold(fg_mask, 250, 255, cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

        # Kontur tespiti
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        frame_with_contours = frame.copy()
        cv2.line(frame_with_contours, (0, detection_line_position), (frame.shape[1], detection_line_position), (255, 0, 0), 2)  # Tespit çizgisi

        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                car_center = y + h // 2
                if car_center > detection_line_position - 10 and car_center < detection_line_position + 10:
                    id = f"{x}_{y}"
                    if id not in detect_dict:
                        car_count += 1
                        detect_dict[id] = True
                cv2.rectangle(frame_with_contours, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(frame_with_contours, 'Araclar: {}'.format(car_count), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Araclar', frame_with_contours)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = 'yeni.mp4'  # Video dosyanızın yolu
    main(video_path)
