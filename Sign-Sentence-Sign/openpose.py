import os
import argparse
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("-csv_files_path","--csv_files_path",required=True,
    help="path of input iamge directories")
ap.add_argument("-openpose_path","--openpose_path",required=True,
    help="path of openpose")
ap.add_argument("-output_dir","--output_dir",required=True,
    help="directory of output")

args = vars(ap.parse_args())
train = pd.read_csv(args['csv_files_path'], error_bad_lines=False)
openpose =args['openpose_path']
output_dir = args['output_dir']
files = list(train['path for sentence'])
words = list(train['word'])

if os.path.isdir(output_dir) == False:
    os.mkdir(output_dir)

os.chdir(openpose)

for no,file in enumerate(files):
  #f = format(file, "03")
  #path = '/content/data/png-segments/'+'{}'.format(f)
  path = file 
  print(path)
  jsn = os.path.join(output_dir,str(words[no]))
  openposepath = os.path.join(openpose,'build/examples/openpose/openpose.bin')
  print(openposepath)
  #!cd openpose && ./build/examples/openpose/openpose.bin --image_dir $path  --display 0 --face --hand --write_images $jsn  --disable_blending --alpha_pose 1 --write_json $jsn --part_candidates --model_pose BODY_25
  cmd = '{} --image_dir {}  --display 0 --face --hand --write_images {}  --disable_blending --alpha_pose 1 --write_json {} --part_candidates --model_pose BODY_25'.format(openposepath,path,jsn,jsn) 
  os.system(cmd)
  print('----------------------------------------')
