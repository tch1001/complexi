import math
import cmath
import matplotlib.pyplot as plt
import numpy as np


	
def frange(start, stop, step):
	i = start
	while i <= stop:
		yield i
		i += step
		


class complexPlane:
	def __init__(self, name):
		self.zReal = []
		self.zImag = []
		self.name = name;
	def drawLine(self, startz, endz, step):
		self.drawLineColor(startz, endz, step, 0,1,1);
	def drawLineColor(self, startz, endz, step, xr, xg, xb):
		X = []
		diffz = endz-startz;
		for i in range(0,step+1):
			X.append(startz + diffz*i/step);
		self.plot(X, xr,xg,xb);
#	def drawFunction(self, startz,endz, step, func):
#		self.drawFunctionColor(startz, endz, step, 0,1,1,1,0,1, func)
#	def drawFunctionColor(self, startz, endz, step, xr,xg,xb,yr,yg,yb, func):
#		X = []
#		diffz = endz-startz;
#		for i in range(0,step+1):
#			X.append(startz + diffz*i/step);
#		Y = []
#		for x in X:
#			Y.append(func(x));
#		self.plot(X, xr,xg,xb);
#		self.plot(Y, yr,yg,yb);
    
	def settings(self):
		if(len(self.zReal) == 0):
			return;
		plt.axis([-max(self.zReal)-1, max(self.zReal)+1, -max(self.zImag)-1, max(self.zImag)+1]);
		plt.title(self.name);
		plt.xlabel("Real");
		plt.ylabel("Imaginary");
		plt.grid()
        
	def show(self):
		self.settings()
		plt.show()

	def plot(self, Z, r,g,b):
		real = [];
		imag = [];
		for z in Z:
			real.append(z.real);
			imag.append(z.imag);
		self.settings()
		plt.plot(real, imag, color = (r,g,b));
		
		self.zReal.extend(real);
		self.zImag.extend(imag);

	def points(self):
		for i in range(0,len(self.zReal)):
			print(str(self.zReal[i])+"+"+str(self.zImag[i])+"j");
			
	def clear(self):
		self.zReal = []
		self.zImag = []
		plt.plot();
	
	
    
    

    