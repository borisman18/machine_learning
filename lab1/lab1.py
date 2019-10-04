from skimage.io import imread, imshow, show, imsave
from skimage.transform import rotate, AffineTransform, warp, resize, downscale_local_mean
import numpy as np
from sys import argv



def rotate(img, angle):
    rotated_img = tr.rotate(img, angle)
    imsave('rotated_img.png', rotated_img)

def shift(img, vector):
    transform = AffineTransform(translation=vector)
    shifted = warp(img, transform, mode='wrap', preserve_range=True)
    shifted = shifted.astype(img.dtype)
    imsave('shifted_img.png', shifted)

def resize_(img, dim):
    imsave('resized_img.png', resize(img, (img.shape[0] // dim[0], img.shape[1] // dim[1]), anti_aliasing=True))

def symmetry(img, axis):
    if axis == 1:
        imsave('symmetry_img.jpg', np.hstack((img, np.flip(img, axis))))
    elif axis == 0:
        imsave('symmetry_img.jpg', np.vstack((img, np.flip(img, axis))))
    else:
        ValueError

def process(img, actions):
    for action in actions:
        if action[0] == 'rotate':
            rotate(img, action[1])
        elif action[0] == 'shift':
            shift(img, action[1])
        elif action[0] == 'resize':
            resize_(img, action[1])
        elif action[0] == 'symmetry':
            symmetry(img, action[1])
        else:
            raise ValueError

if __name__ == "__main__":
	img = imread(argv[1])
	
	print(type(argv[2]))
	#process(argv[1])
	'''
	process(img, [
		('rotate', 30), 
		('shift', (100, 100)),
		('resize', (3, 0.5)),
		('symmetry', 1)
	])
	'''