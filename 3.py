# Read a Video Stream from Camera(Frame by Frame)
import cv2

cap = cv2.VideoCapture(0) # 0 is id of default webcam


while True:
        ret,frame = cap.read() #ret is boolean value that can be true or false.
                               #frame means cap.read() return  capture frame
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY )
        if ret == False:   #if ret is false frame is not capture properly
                            #so we continue the loop to try again
                continue
        cv2.imshow("Video Frame",frame) #display the captured frame
        cv2.imshow("gray Frame",gray_frame)
	#Wait for user input - q, then you will stop the loop
        key_pressed = cv2.waitKey(1) & 0xFF #see video to understand
        if key_pressed == ord('q'):
        	break

cap.release()
cv2.destroyALlWindows()

