import os, sys
import Image
import glob
from PIL import Image

basewidth = 128

Dir = '/home/connor/Downloads/flower-thumbs'
picDir = Dir+'/*.jpg'
picDir = glob.glob(picDir)
for infile in picDir:
    	outfile = os.path.splitext(infile)[0] + ".thumbnail"
	print(outfile)
    #if infile != outfile:
        try:
      		
		img = Image.open(infile)
		wpercent = (basewidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img = img.resize((basewidth,hsize), Image.ANTIALIAS)
		img.save(outfile+'.jpg') 
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
