# video-processor
Python script for processing videos and making them look funky. 
Makes use of art_gen.py and image_manipulator.py from https://github.com/AlexDR1998/Art-Generator. Only change made was removing the main method from art_gen.py.
The class ArtGenerator from art_gen.py is used in video_processor to process each frame.

To use the video processor, edit the file to include the appropriate file name of the input video. Add functions from the ArtGenerator class which are applied to each frame in the 'while true' that iterates over all frames of the video.

There's some experimental WIP functions that can be toggled by setting 'timestretch' to true. The idea is that they process each frame by setting columns of the current frame to columns from future frames. Looks pretty cool, but has proven to be very computationally intensive. I plan to sort this out properly later.

Requirements:
Python 2.7, Numpy, OpenCV
(if it doesn't run, Scipy and Matplotlib might also be needed, as specified for https://github.com/AlexDR1998/Art-Generator - although their functionality isn't needed for video_processor.py)
