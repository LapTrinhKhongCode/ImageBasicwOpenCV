import cv2

img = cv2.imread('DATA/00-puppy.jpg')
while True: 
    
    cv2.imshow('Puppy',img)
    #if we're waited at least 1 ms AND we've pressed the Esc(code 27)
    if cv2.waitKey(1) & 0xFF==27:
        break
    
cv2.destroyAllWindows()


