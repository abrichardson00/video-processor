import numpy as np
import sys
from numpy import linalg as LA
from scipy import linalg as LA
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage
from scipy import signal
import random
import math

from image_manipulator import Image

class ArtGenerator(Image):



	"""

	Higher level subclass of Image - uses lower level methods in sequence to produce
	unusual or abstract versions of images
	"""

	




	def abstract1(self,f):

	    #Abstract nonsense
	    #f between 1 and 10 works best

	    #self.rgb_partition("rgb",[random.randint(0,1),random.randint(0,1),random.randint(0,1)],random.randint(0,20))
	    #self.fft_filter(f,"h")
	    #self.perm_chunk()
	    #self.fft_filter(f*2,"l")
	    self.edge()
	    self.smooth(2)

	    #self.norm()
	    #self.show()


	def mangle(self,am):

	    #Shuffles image beyond recognition
	    for x in range(am):
	        self.rgb_partition("rgb",[random.randint(0,1),random.randint(0,1),random.randint(0,1)],random.randint(0,x))
	        #if x%2==0:
	    for x in range(am):
	        self.perm_chunk("b")

	    #self.show()

	def glitch(self,am):
		axes = np.array([random.randint(0,1),random.randint(0,1),random.randint(0,1)])
		self.interleave([random.randint(0,am),random.randint(0,am),random.randint(0,am)],"v")
		for x in range(am):
			self.roll_chunk(x)
		self.rgb_offset([random.randint(0,am),random.randint(0,am),random.randint(0,am)],1-axes)
		self.rgb_partition("rgb",axes,[random.randint(0,am),random.randint(0,am),random.randint(0,am)])
		self.interleave([random.randint(0,am),random.randint(0,am),random.randint(0,am)],"h")
		self.fft_filter(100,"l")
		#self.show()

	def glitch2(self,am):

	    #tamer glitching

	    l_im = Image()
	    u_im = Image()
	    self.thresh_split(u_im,l_im,128)
	    #for x in range(am//10):

	    #    u_im.perm_chunk("b")
	    #    l_im.perm_chunk("b")
	    u_im.interleave([random.randint(0,am),random.randint(0,am),random.randint(0,am)],"h")
	    l_im.interleave([random.randint(0,am),random.randint(0,am),random.randint(0,am)],"v")
	    u_im.fft_filter(100,"l")
	    l_im.fft_filter(10,"h")
	    self.add(u_im,l_im)
	    self.smooth(3)
	    #self.show()

	def glitch3(self,f):

		sub_im1 = ArtGenerator()
		sub_im2 = ArtGenerator()
		self.thresh_split(sub_im1,sub_im2,f)

		#sub_im1.show()
		#sub_im2.show()





	def twist(self,am):
	    #Rotates image and slices it in horrible ways
	    for x in range(am):
	        self.rotate(360//am)
	        self.perm_chunk("h")
	        self.rgb_offset([random.randint(0,am),random.randint(0,am),random.randint(0,am)],[0,0,0])
	    #self.show()


	def impressionist(self,am):
	    #imitates impressionism

	    self.noise(am*10)


	    for x in range(am):
	        self.smooth(3)
	    self.fold(am/10.0 +1)
	    self.smooth(5)
	    #self.show()

	def abstract2(self,am):
	    self.fold(3)
	    self.smooth(5)
	    self.thresh(100)
	    self.fft_perm_chunk("b",n=am)
	    self.fft_offset([random.randint(0,am),random.randint(0,am),random.randint(0,am)],[random.randint(0,1),random.randint(0,1),random.randint(0,1)])
	    self.bright(4)
	    #self.show()


	def abstract3(self,am,th):
		#axes = np.array([random.randint(0,1),random.randint(0,1),random.randint(0,1)])
		sub_im1 = ArtGenerator()
		sub_im2 = ArtGenerator()
		#self.copy_to(sub_im1)
		#self.copy_to(sub_im2)
		self.thresh_split(sub_im1,sub_im2,th)
		res = gcd(self.image.shape[1],self.image.shape[0])
		#print(res)
		sub_im2.pixelate(res/float(am))
		sub_im2.pixelate(float(am)/res)
		#self.add(sub_im1,sub_im2)
		#sub_im1.rgb_partition("rgb",axes,[random.randint(0,am),random.randint(0,am),random.randint(0,am)])
		#sub_im1.fft_filter(am,"l")
		sub_im1.key(sub_im2,th)
		#sub_im1.show()
		#sub_im2.show()
		#self.show()






def gcd(x,y):
	if x==y:
		return x
	while(y):
		x,y = y,x%y
	return x

'''
def main():
	im1 = ArtGenerator()

	#--- im1.load("path_to_image_file",x_center,y_center,size)

	im1.load()#"TestPictures/bhouse.jpeg",500,700,700)

	#im1.show()

	#--- im1.image_editing_method(parameters)
	im1.twist(3)
	#im1.svd("u")
	#im1.impressionist(5)
	#im1.show();
	#im1.abstract2(60)
	#im1.mangle(50)
	#im1.glitch(19)
	#im1.pixelate(64)
	#for i in range(10):
	 #im1.pixelate(64)
	  #im1.pixelate(1.0/64.0)
	  #im1.abstract3(5,100)

	#im1.svd("c")

	#im1.show()


	#im1.show()
	#im1.save()


main()
'''
