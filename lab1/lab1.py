from skimage.io import imread, imshow, show, imsave
from skimage.transform import rotate, AffineTransform, warp, resize, downscale_local_mean
import numpy as np
from sys import argv



def rotate_(img, angle):
    rotated_img = rotate(img, angle)
    imsave('rotated_img.png', rotated_img)

def shift(img, vector):
    transform = AffineTransform(translation=vector)
    shifted = warp(img, transform, mode='wrap', preserve_range=True)
    shifted = shifted.astype(img.dtype)
    imsave('shifted_img.png', shifted)

def resize_(img, dim):
    imsave('resized_img.png', resize(img, (img.shape[0] // dim[0], img.shape[1] // dim[1])))

def symmetry(img, axis):
    if axis == 1:
        imsave('symmetry_img.jpg', np.hstack((img, np.flip(img, axis))))
    elif axis == 0:
        imsave('symmetry_img.jpg', np.vstack((img, np.flip(img, axis))))
    else:
        ValueError


if __name__ == "__main__":
	# EXAMPLE:
	# python lab1.py pic.jpg rotate 90 shift 50 50 resize 0.5 0.5 symmetry 1
	
	img = imread(argv[1])
	actions = argv[2:]
	for i,arg in enumerate(actions):
		if arg == 'rotate':
			rotate_(img, float(actions[i+1]))
		elif arg == 'shift':
			shift(img, [float(actions[i+1]), float(actions[i+2])])
		elif arg == 'resize':
			resize_(img, [float(actions[i+1]), float(actions[i+2])])
		elif arg == 'symmetry':
			symmetry(img, int(actions[i+1]))
		else:
			continue
