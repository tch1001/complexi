# Complexi
A simple tool for modelling the complex plane and visualisation of complex functions

Hi guys, I wrote this tool in python that helps you model the complex plane by simple creating an instance of the class `complexPlane`. This tool was created in order to make life easier for mathematicians (or math enthusiasts) who do not have the programs required to model the complex plane or want to code specific functions by themselves (e.g. Mandelbrot set, Visualisation of Complex Functions). 

I hope you find this tool useful and feel free to report any bugs or suggest any improvements! :D Happy mathing! 

Usage
-----
Demo is available (Demo IPython Notebook included)
 1. `import complexi`
 2. Create an instance of the class `complexPlane` by calling: `plane = complexi.complexPlane(name)`.
 3. The object `plane` now has the following functions (in the next section)
 4. If you want to display the graph, call `plane.show()`.
	 

Functions
-------

 - `plane.drawLine(startZ, endZ, step)`
 
  Draws a line from the point `startZ` to the point `endZ` with `step` 'pieces' in the line (for convenience and speed just put 1 for steps). Steps will come into play in a future update! 
  Draws in cyan color (0,1,1).
  
 - `plane.drawLineColor(startZ, endZ, step, r, g, b)`

 Same thing as `drawLine()` but you can choose what color to draw in (can be used to draw multi-colored lines with smart use of loops).

 - `plane.show()`

 Displays the complex plane you have drawn!

 - `plane.clear()`

 Clears the plane and all points on it.

 - `plane.points()`

 Prints out all the points on the plane. 


**Note: Blog on this tool coming up soon! :D Stay tuned!**
Have fun!
