#!/usr/bin/env python
#
"""
Created on Mon Nov 13 12:48:43 2017
@author: mmusy
"""
from __future__ import print_function
import numpy as np
import plotter

# Declare an instance of the class
vp = plotter.vtkPlotter()
#vp.help() # shows a help message

# Load a vtk file as a vtkActor and visualize it.
#The tridimensional shape corresponds to the outer shape of the embryonic mouse limb
#at about 11 days of gestation.
#Choose a tomato color for the internal surface, and no transparency.
#Press Esc to close the window and exit python session, or q to continue:
vp.load('data/250.vtk', c='b', bc='tomato', alpha=1) # c=(R,G,B), #hex, letter or name
vp.show()             # picks what is automatically stored in vp.actors list


# Load a vtk file as a vtkActor and visualize it in wireframe style.
a = vp.load('data/290.vtk', wire=1) # same as a.GetProperty().SetRepresentationToWireframe()
vp.axes = False
vp.show(legend=None) # picks what is automatically stored in vp.actors
#vp.show(a)           # ignores the content of vp.actors and draws a
#vp.show(actors=[a])  # same as above


# Load 3 actors assigning each a different color, use their file names as legend entries.
# No need to use any variables, as actors are stored internally in vp.actors:
vp = plotter.vtkPlotter()
vp.load('data/250.vtk', c=(1,0.4,0))
vp.load('data/270.vtk', c=(1,0.6,0))
vp.load('data/290.vtk', c=(1,0.8,0))
print ('Loaded vtkActors: ', len(vp.actors))
vp.show()


# Draw a spline that goes through a set of points, don't show the points (nodes=False):
from random import uniform as u
pts = [(u(0,10), u(0,10), u(0,10)) for i in range(20)]
vp = plotter.vtkPlotter()
vp.spline(pts, s=.1, nodes=False)
vp.show(legend='a random spline')


# Draw a PCA ellipsoid that contains 67% of a cloud of points:
vp = plotter.vtkPlotter()
pts = [(u(0,200), u(0,200), u(0,200)) for i in range(50)]
vp.points(pts)
vp.ellipsoid(pts, pvalue=0.67, pcaAxes=True)
vp.show(legend=['points', 'PCA ellipsoid'])


# Show 3 planes as a grid, add a dummy sine plot on top left:
xycoords = [(np.exp(i/10.), np.sin(i/5.)) for i in range(40)]
vp = plotter.vtkPlotter()
vp.xyplot( xycoords )
vp.grid(center=(0,0.5,0.5), normal=(1,0,0), c=(1,0,0))
vp.grid(center=(0.5,0,0.5), normal=(0,1,0), c=(0,1,0))
vp.grid(center=(0.5,0.5,0), normal=(0,0,1), c=(0,0,1))
vp.show(axes=0)


# Show the vtk boundaries of a vtk surface and its normals
# (ratio reduces the total nr of arrows by the indicated factor):
vp = plotter.vtkPlotter()
va = vp.load('data/290.vtk', c='maroon', legend=0)
vp.normals(va, ratio=5, legend=False)
vp.boundaries(va)
vp.show(legend='shape w/ boundaries')


# Split window in a 36 subwindows and draw something in windows nr 12 and nr 33.
# Then open an independent window and draw on two shapes:
vp1 = plotter.vtkPlotter(shape=(6,6))
vp1.renderers[35].SetBackground(.8,.9,.9)
a = vp1.load('data/250.vtk')     
b = vp1.load('data/270.vtk')     
c = vp1.load('data/290.vtk') 
vp1.interactive = False
vp1.axes = False
vp1.show(at=12, actors=[a,b]) 
vp1.show(at=33, actors=[b,c]) 
vp2 = plotter.vtkPlotter(bg=(0.9,0.9,1))
vp2.load('data/250.vtk')
vp2.load('data/270.vtk')
vp2.show(legend='an other window')


# Load a surface and show its curvature based on 4 different schemes.
# All four shapes share a common vtkCamera:
# 0-gaussian, 1-mean, 2-max, 3-min
vp = plotter.vtkPlotter(shape=(1,4))
v = vp.load('data/290.vtk')
vp.interactive = False
vp.axes = False
for i in [0,1,2,3]:
    c = vp.curvature(v, method=i, r=1, alpha=0.8)
    vp.show(at=i, actors=[c], legend='method #'+str(i+1))
vp.interact()


# Draw a simple objects on separate parts of the rendering window:
vp = plotter.vtkPlotter(shape=(2,3))
vp.axes    = True
vp.commoncam   = False
vp.interactive = False
vp.show(at=0, actors=vp.arrow( [0,0,0], [1,1,1] ) )
vp.show(at=1, actors=vp.line(  [0,0,0], [1,2,3] ) )
vp.show(at=2, actors=vp.points( [ [0,0,0], [1,1,1], [3,1,2] ] ) )
vp.show(at=3, actors=vp.text('hello', cam=False, bc=(0,1,0) ) )
vp.show(at=4, actors=vp.sphere([.5,.5,.5], r=0.3), axes=0 )
vp.show(at=5, actors=vp.cube(  [.5,.5,.5], r=0.3), axes=0, legend='a dummy cube' )
vp.interact()


# Draw a bunch of objects
vp = plotter.vtkPlotter(shape=(3,3))
vp.commoncam   = False
vp.interactive = False
vp.show(at=0, c=0, actors='data/beethoven.ply', ruler=1, axes=0)
vp.show(at=1, c=1, actors='data/big_atc.ply', wire=1)
vp.show(at=2, c=2, actors='data/big_porsche.ply', edges=1)
vp.show(at=3, c=3, actors='data/big_spider.ply')
vp.show(at=4, c=4, actors='data/egret.ply')
vp.show(at=5, c=5, actors='data/mug.ply')
vp.show(at=6, c=6, actors='data/scissors.ply')
a = vp.getActors('sciss') # retrieve actors by matching legend string 
a[0].RotateX(90)          # and rotate it by 90 degrees around x
vp.show(at=7, c=7, actors='data/shuttle.obj')
vp.show(at=8, c=8, actors='data/skyscraper.obj')
vp.interact()


# Draw a line in 3D that fits a cloud of points,
# also show the first set of 20 points and fit a plane to them:
vp = plotter.vtkPlotter(verbose=False)
for i in range(500): # draw 500 fit lines superimposed
    x = np.linspace(-2, 5, 20) # generate 20 points
    y = np.linspace( 1, 9, 20)
    z = np.linspace(-5, 3, 20)
    data = np.array(zip(x,y,z))
    data+= np.random.normal(size=data.shape)*0.8 # add gauss noise
    if i==0:
        vp.points(data, c='red')
        vp.fitPlane(data)
    vp.fitLine(data, lw=10, alpha=0.01) # fit
print ('Fit slope=', vp.result['slope']) # the last fitted slope direction
vp.show(legend=['points','fitting plane','fitting line'])


# Cut a set of shapes with a plane that goes through the 
# point at x=500 and has normal (0, 0.3, -1). 
# Wildcards are ok to load multiple files or directories:
vp = plotter.vtkPlotter()
vp.load('data/*.vtk', c='orange', bc='aqua', alpha=1) 
for a in vp.actors:
    vp.cutActor(a, origin=(500,0,0), normal=(0,0.3,-1))
vp.show()


# As a short-cut, the filename can be given in the show command directly:
plotter.vtkPlotter().show('data/limb.pcd') # Point cloud (PCL file format)


# Display a tetrahedral mesh (Fenics/Dolfin format).
# The internal vertices are displayed too:
vp = plotter.vtkPlotter()
vp.load('data/290.xml.gz')
vp.show(legend='tetrahedral mesh')


# Align 2 shapes and for each vertex of the first draw 
# and arrow to the closest point of the second:
vp = plotter.vtkPlotter()
a1, a2 = vp.load('data/2[79]0.vtk') 
a1.GetProperty().SetColor(0,1,0)
a1b = vp.align(a1, a2, rigid=1)
ps1 = vp.getCoordinates(a1b) # coordinates of actor
for p in ps1: vp.arrow(p, vp.closestPoint(a2, p))
vp.show(legend=['Source','Target','Aligned','Links'])            


# Find closest point in set pts1 to pts2 within a specified radius
from random import uniform as u
pts1 = [(u(0,5), u(0,5), u(0,5)) for i in range(40)]
pts2 = [(u(0,5), u(0,5), u(0,5)) for i in range(20)]
vp = plotter.vtkPlotter()
vp.points(pts1, r=4,  alpha=1, legend='point set 1')
vp.points(pts1, r=25, alpha=0.1) # make a halo 
a = vp.points(pts2, r=4, c='r', alpha=1, legend='point set 2')
for p in pts1:
    cp = vp.closestPoint(a, p, radius=2)
    vp.line(p, cp)
    #print (vp.result['closest_exists'], 'dist2=', vp.result['distance2'])
vp.show()


# Draw a cloud of points each one with a different color 
# which depends on its position
vp = plotter.vtkPlotter()
rgb = [(u(0,255), u(0,255), u(0,255)) for i in range(1000)]
vp.points(rgb, c=rgb, alpha=0.8, legend='RGB points')
vp.show()


# Make a video  (needs cv2 package)
vp = plotter.vtkPlotter(interactive=0, verbose=0)
vp.load('data/290.vtk', c='b', bc='tomato', alpha=1)
vp.show()                 # inits camera etc.
vp.openVideo(duration=5) # will make it last 5 seconds
for i in range(100):
    vp.camera.SetPosition(700.-i*20., -10, 4344.-i*80.)
    vp.show()
    vp.addFrameVideo()
vp.releaseVideo()
print ('Video saved as movie.avi')
vp.interact()




