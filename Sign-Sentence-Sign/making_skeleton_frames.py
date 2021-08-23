import natsort
import cv2
import os
import argparse
import pandas as pd
from glob import glob
import numpy as np
ap = argparse.ArgumentParser()


ap.add_argument("-output_dir","--output_dir",required=True,
    help="path of output_dir")
ap.add_argument("-csvfile","--csvfile",required=True,
    help="path of csv file")

args = vars(ap.parse_args())

output_dir = args['output_dir']

data = pd.read_csv(args['csvfile'])
files = data['skeleton path for word'].tolist()


origin = os.getcwd()
if os.path.isdir(output_dir) == False:
    os.makedirs(os.path.join(output_dir,'test'))


#original_frames = natsort.natsorted(glob(imagespath+'/'+ '*.png'))
#skeleton_frames = natsort.natsorted(glob(ske_output_dir+'/'+ '*.png'))
names = np.arange(len(files))
for ske,n in zip(files,names):
    print(ske,n)
    im_A = np.zeros(shape=[256,256, 3], dtype=np.uint8)
    im_B = cv2.imread(ske, 1)
    im_B_re = cv2.resize(im_B,(256,256))
    im_AB = np.concatenate([im_A, im_B_re], 1)
    cv2.imwrite(output_dir+'/test/'+str(n)+'.jpg', im_AB)
                           
