#https://stackoverflow.com/questions/31774953/test-labels-for-regression-caffe-float-not-allowed/31808324#31808324
#https://groups.google.com/forum/#!topic/caffe-users/mPDvq_9kY9A/discussion

import h5py, os
import caffe
import numpy as np

SIZE = 224 # fixed size to all images
N=12
with open( 'fine-tuning/data/train.txt', 'r' ) as T :
    lines = T.readlines()
mu=np.load("fine-tuning/model/places365CNN_mean.npy") #mean file
mu=mu.mean(1).mean(1)
# If you do not have enough memory split data into
# multiple batches and generate multiple separate h5 files
X = np.zeros( (len(lines), 3, SIZE, SIZE), dtype='f4' )
y = np.zeros( (len(lines), N), dtype='f4' )
for i,l in enumerate(lines):
    sp = l.split(' ')
    img = caffe.io.load_image( sp[0] )
    img = caffe.io.resize( img, (SIZE, SIZE, 3) ) # resize to fixed size
    transposed_img = img.transpose((2,0,1))[::-1,:,:] # RGB->BGR
    X[i] = transposed_img
    labelvec = np.array(sp[1:], dtype='f4')
    y[i] = labelvec
with h5py.File('train.h5','w') as H:
    H.create_dataset( 'X', data=X ) # note the name X given to the dataset!
    H.create_dataset( 'y', data=y ) # note the name y given to the dataset!
with open('train_h5_list.txt','w') as L:
    L.write( 'train.h5' ) # list all h5 files you are going to use

with open( 'fine-tuning/data/test.txt', 'r' ) as T :
    lines = T.readlines()
mu=np.load("fine-tuning/model/places365CNN_mean.npy") #mean file
mu=mu.mean(1).mean(1)
# If you do not have enough memory split data into
# multiple batches and generate multiple separate h5 files
X = np.zeros( (len(lines), 3, SIZE, SIZE), dtype='f4' )
y = np.zeros( (len(lines), N), dtype='f4' )
for i,l in enumerate(lines):
    sp = l.split(' ')
    img = caffe.io.load_image( sp[0] )
    img = caffe.io.resize( img, (SIZE, SIZE, 3) ) # resize to fixed size
    transposed_img = img.transpose((2,0,1))[::-1,:,:] # RGB->BGR
    X[i] = transposed_img
    labelvec = np.array(sp[1:], dtype='f4')
    y[i] = labelvec
with h5py.File('test.h5','w') as H:
    H.create_dataset( 'X', data=X ) # note the name X given to the dataset!
    H.create_dataset( 'y', data=y ) # note the name y given to the dataset!
with open('test_h5_list.txt','w') as L:
    L.write( 'train.h5' ) # list all h5 files you are going to use
