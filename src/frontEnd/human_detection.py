import cv2
import time

# from medium article

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('video1.h264')
# cap = cv2.VideoCapture('TownCentreXVID.avi')  # another example video

# Check if camera opened successfully
if cap.isOpened() is False:
    print("Error opening video stream or file")

start_time = time.time() #get start time of code execution

#counter variable
counter = -1
#variable which says how many frames to skip
frame_skip = 5

# Read until video is completed
while cap.isOpened():

    counter += 1 #increment the counter for each loop
    ret, frame = cap.read() #read the frame
    if counter % frame_skip == 0: #if it is every nth frame, then detect humans in it, or just continue to next iteration

        if ret is True: # if we are able to open the video

            frame = cv2.resize(frame, (960, 540))  # Downscale to improve frame rate. Can adjust this value as needed
            #Interestingly, it gives an error if I downscale it by half i.e 480x270 Try it out
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)  # HOG needs a grayscale image. Convert frame from rgb to grayscale
            rects, confidence = hog.detectMultiScale(gray_frame, ) # actual detection of humans using HOG

            # draw rectangles
            for i, (x, y, w, h) in enumerate(rects):
                if confidence[i] < 0.8: #if the system is really confident, then draw the rectangle or just go to next iteration
                    continue
                else:
                    print(("Confidence value is {}".format(confidence)))
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # draw rectangle

                    # cropping box from frame
                    cropImg = frame[y: y + h, x: x + w]
                    cv2.imshow('cropImg', cropImg) #show cropped image in window
                    cv2.imwrite("cropped" +str(i) + ".jpg", cropped)

            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break
    # Break the loop
    else:
        continue

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

print("Execution time ---> %s seconds " % ((time.time() - start_time))) #print code execution time
