import cv2
import numpy as np

img = np.zeros((512,513,3),np.uint8)

# cv2.line(img,(0,0),(511,511),(255, 0,0),5)
# cv2.line(img,(50,400),(511,100),(0, 255,0),5)

# cv2.rectangle(img,(50,50),(300,300),(0,0,255),5)
# cv2.rectangle(img,(300,300),(511,511),(0,0,255),-1)

# cv2.circle(img,(255,255),60,(120,120,120),5)
# cv2.circle(img,(100,100),90,(255,50,500),-1)

# cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,100,0),3)

# pts = np.array([[20,30],[100,120],[255,255],[10,400]],np.int32)


font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,'Eren',(10,300),font,4,(0,155,255),2,cv2.LINE_AA)


cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()