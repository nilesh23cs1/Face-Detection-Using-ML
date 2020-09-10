# Write a Python Script that captures images from your webcam video stream
# Extracts all Faces from the image frame (using haarcascades)
# Stores the Face information into numpy arrays

# 1. Read and show video stream, capture images
# 2. Detect Faces and show bounding box (haarcascade)
# 3. Flatten the largest face image(gray scale) and save in a numpy array
# 4. Repeat the above for multiple people to generate training data


import cv2
import numpy as np

#Init Camera
cap = cv2.VideoCapture(0)


count=0

# Face Detection
face_cascade = cv2.CascadeClassifier("../OpenCV Basics/haarcascade_frontalface_alt.xml")#create a classifier object

#for store every 10th face
skip = 0
face_data = [] #for store the face information
dataset_path = '../data/'  #path where information about image is stored
file_name = input("Enter the name of the person : ")
while True:
   
        
    ret,frame = cap.read() #capture the frame
    if ret==False:  #if fail to capture frame go to next iteration of loop
        continue
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert colored grame into gray frame
    faces = face_cascade.detectMultiScale(frame,1.3,5) #scaling factor=1.3 and number of neighbours=5
        #it returns x,y,w,h for all faces.it return list of tuples i.e[(x0,y0,w0,h0),(x1,y1w1h1)] 
    if len(faces)==0:
        continue

  
    faces = sorted(faces,key=lambda f:f[2]*f[3])
	# Pick the last face (because it is the largest face acc to area(f[2]*f[3]))
        #for drawing a bunding boxes[rectangle over face]
    for face in faces[-1:]:  #iterate over all faces
        x,y,w,h = face  #face have x,y,w,h of faces object
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)#draw a rectangle around faces.(0,255,255) is color.
        offset = 10 #used for padding.#Extract (Crop out the required face) : Region of Interest
        face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset] #cut the required region of faces in[y,x] format .use little padding
        face_section = cv2.resize(face_section,(100,100)) #resize the image
        skip += 1
		#store every 10th face
        if skip%10==0:
            face_data.append(face_section)
            print(len(face_data)) #it shows how many faces i have captured

        cv2.imshow("Frame",frame) #display a frame
        cv2.imshow("Face Section",face_section)

    #key_pressed = cv2.waitKey(1) & 0xFF
    #if key_pressed == ord('q'):
        #break    

    count+=1
    if count%100==0:
        break

       

# Convert our face list array into a numpy array
face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)

# Save this data into file system
np.save(dataset_path+file_name+'.npy',face_data)
print("Data Successfully save at "+dataset_path+file_name+'.npy')

cap.release()
cv2.destroyAllWindows()





"""
scaleFactor – Parameter specifying how much the image size is reduced at each image scale.
Basically the scale factor is used to create your scale pyramid. More explanation can be found here. In short, as described here, your model has a fixed size defined during training, which is visible in the xml. This means that this size of face is detected in the image if present. However, by rescaling the input image, you can resize a larger face to a smaller one, making it detectable by the algorithm.
1.05 is a good possible value for this, which means you use a small step for resizing, i.e. reduce size by 5%, you increase the chance of a matching size with the model for detection is found. This also means that the algorithm works slower since it is more thorough. You may increase it to as much as 1.4 for faster detection, with the risk of missing some faces altogether.
minNeighbors – Parameter specifying how many neighbors each candidate rectangle should have to retain it.
This parameter will affect the quality of the detected faces. Higher value results in less detections but with higher quality. 3~6 is a good value for it.
"""



