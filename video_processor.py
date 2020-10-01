import numpy as np
import cv2
import colorsys

from art_gen import ArtGenerator

### enter video file name here:
cap = cv2.VideoCapture('sesh.mp4')

fourcc = cv2.cv.CV_FOURCC(*'XVID')
crop = False
timestretch = False
step = 4 # used with WIP 'timestretch' functions

### get width/height
width = int(cap.get(3))
height = int(cap.get(4))
print("width: " + str(width))
print("height: " + str(height))

### initialise square output if needed
if (crop):
    if (height > width):
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width,  width))
        midpoint = height/2
    elif (height <= width): #also handle square video here
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (height,  height))
        midpoint = width/2
else:
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width,  height))

### crop image/array f
def crop_frame(f):
    if (height > width):
        return f[(midpoint - width/2):(midpoint + width/2), 0:width]
    elif (height < width):
        return f[0:height,(midpoint - height/2):(midpoint + height/2)]
    else:
        return f # cropping already square image

### returns the next frame (cropped if necessary)
def read_frame():
    # get frame
    ret, frame = cap.read()
    if not ret:
        print("Frame not read (end of stream?). Exiting.")
        return ret, None

    ### crop image if specified
    if (crop):
        cropped_frame = crop_frame(frame)
    else:
        cropped_frame = frame
    return ret, cropped_frame

def get_frames():
    frames = np.zeros((width/step,height,width,3),np.uint8)
    for i in range(width/step):
        ret, f = cap.read()
        if not ret:
            print("Frame not read")
            break
        frames[i] = f
    return frames



### experimental WIP -------------------------
def update_frames(f,frames):
    f = np.reshape(f,(1,height,width,3))
    return np.concatenate((frames[1:width], f), axis=0)

def time_strectch_frame(frames):
    f = np.zeros((height,width,3),np.uint8)
    for w in range(width/step):
        print(w)
        print(width)
        pix = np.reshape(np.vstack([frames[w,:,w]]*step),(height,step,3))

        for i in range(step):
            f[:,(w*step)+i] = frames[w,:,w*step]

    return f
### -----------------------------------------
length = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
print("Number of frames: " + str(length))


if timestretch:
    frames = get_frames()
else:
    frames = None

### loop through video frames
while True:
    ### get the current frame
    ret, frame = read_frame()
    if not ret:
        break

    if timestretch:
        frames = update_frames(frame,frames)
        frame = time_strectch_frame(frames)

    ### process frame using the ArtGenerator class
    ### from https://github.com/AlexDR1998/Art-Generator
    img = ArtGenerator()
    img.load_direct(frame)
    #img.twist(3)
    #img.impressionist(5)
    #img.mangle(1)
    img.glitch2(20)
    #img.glitch(10)
    #img.abstract3(20,100)
    #img.svd("c")
    frame = img.image.astype(np.uint8)
    ### -------------------------------------

    ### show and write image
    cv2.imshow('frame', frame)
    out.write(frame)

    ### press 'q' to quit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


### finish/clean up
cap.release()
out.release()
cv2.destroyAllWindows()
