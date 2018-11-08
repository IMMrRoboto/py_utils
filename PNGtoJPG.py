import os
import glob
from PIL import Image

Dir = '/home/connor/Downloads/flower_images'
picDir = Dir+'/*.png'
picDir = glob.glob(picDir)
print(picDir)
for i, f in enumerate(picDir):
		#print(i)
		im = Image.open(f)
		name = os.path.basename(f)
		#print(name)
		rgb_im = im.convert('RGB')
		name = name.replace('.png','.jpg' )
		name = '/home/connor/Downloads/flower_images_jpg/'+name
		print(name)
		rgb_im.save(name)

