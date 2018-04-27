#Visual extraction of images by using googlenet_places365 CNN
import numpy as np
import caffe
import glob

#Setting up the caffe mode
caffe.set_mode_cpu()

#Loading the pre-trained model
model_def='../googlenet_places365/deploy_googlenet_places365.prototxt'
model_weights="../googlenet_places365/googlenet_places365.caffemodel"
net=caffe.Net(model_def,model_weights,caffe.TEST)

#Loading the categories
features=np.loadtxt('../googlenet_places365/categories_places365.txt',str)

#Loading the mean file of the pictures
mu=np.load("../googlenet_places365/places365CNN_mean.npy")
mu=mu.mean(1).mean(1)

#Creating the transformer for the input data
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
transformer.set_mean('data', mu)            # subtract the dataset-mean value in each channel
transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]
transformer.set_channel_swap('data', (2,1,0))  # swap channels from RGB to BGR
transformer

net.blobs['data'].reshape(1,3,224, 224) #1 image per batch, 3 chanels, cropping size 224 x 224

#Classification: Visual extraction
class_prob=[]
i=0
for image in glob.glob("../city-image-corpus/*.jpg"):
	print "classifying picture: ",i
	image_caffe = caffe.io.load_image(image)
	#Resizing the image
	image_caffe = caffe.io.resize_image(image_caffe,(256,256))
	#Transforming the image
	transformed_image = transformer.preprocess('data', image_caffe)
	net.blobs['data'].data[...] = transformed_image
	output = net.forward()
	output_prob=output['prob'][0]
	class_prob.append(np.append([str(image.split("../city-image-corpus/")[1]),str(features[output_prob.argmax()][0]),str(output_prob[output_prob.argmax()])],output_prob))
	i+=1
np.savetxt("../datasets/googlenet_places365-class-prob-summary.csv",class_prob,delimiter=",",fmt="%s")
print "done"
