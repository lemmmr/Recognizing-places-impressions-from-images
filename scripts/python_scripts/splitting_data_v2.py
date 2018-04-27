import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import shutil


def main():
	#Validating
	if len(sys.argv) != 4:
		print('\n\nUsage: python scripts/splitting_data.py splitted_data_path dataset_labels_path images_path\n\n')
		return
	if os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]) and os.path.exists(sys.argv[3]):
		print('Directories checked')
	else:
		print('Check the directories')
		return

    #Getting directories
	images_dir=os.path.abspath(sys.argv[3])
	labels_dir=os.path.abspath(sys.argv[2])
	splitted_data_path_dir=os.path.abspath(sys.argv[1])

	#Reading the labels file into a pandas dataframe
	df_labels = pd.read_csv(labels_dir)
	labels = df_labels.drop(["annotation","city"],axis=1).columns.tolist()
	length_total=len(df_labels)
	print("Number of samples for training: "+str(length_total*0.80))
	print("Number of samples for validation: "+str(length_total*0.10))
	print("Number of samples for testing: "+str(length_total*0.10))

	with open(splitted_data_path_dir+"/labels.txt", "w") as output:
		for label in labels:
			output.write(str(label)+'\n')

	labels = df_labels.drop(["annotation","city"],axis=1).columns.tolist()

	for label in labels:
		print("Splitting data for: "+label)
		X_train, X_test, y_train, y_test = train_test_split(df_labels["annotation"],df_labels[label],test_size=0.20)
		X_test, X_val, y_test, y_val = train_test_split(X_test,y_test,test_size=0.5)

		X_train.reset_index(drop=True,inplace=True)
		y_train.reset_index(drop=True,inplace=True)

		X_val.reset_index(drop=True,inplace=True)
		y_val.reset_index(drop=True,inplace=True)

		X_test.reset_index(drop=True,inplace=True)
		y_test.reset_index(drop=True,inplace=True)

		#Creating folders for each label
		if os.path.exists(splitted_data_path_dir+"/"+label):
			shutil.rmtree(splitted_data_path_dir+"/"+label)
			os.makedirs(splitted_data_path_dir+"/"+label)
		else:
			os.makedirs(splitted_data_path_dir+"/"+label)

		#Creating subfolders for training, validation and test data
		os.makedirs(splitted_data_path_dir+"/"+label+"/training")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation")
		os.makedirs(splitted_data_path_dir+"/"+label+"/test")

		#Creating subfolders in training folder for the values:
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/1")
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/1.5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/2")
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/2.5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/3")
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/3.5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/4")
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/4.5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/5.5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/6")
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/6.5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/training/7")

		#Creating subfolders in validation folder for the values:
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/1")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/1.5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/2")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/2.5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/3")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/3.5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/4")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/4.5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/5.5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/6")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/6.5")
		os.makedirs(splitted_data_path_dir+"/"+label+"/validation/7")

		paths=[]
		label_val=[]
		#########
		#Training data
		#########

		#Distributing the images through the folders
		for i in range(len(X_train)):
			if y_train[i]==1:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/1/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/1/"+X_train[i]))
				label_val.append(y_train[i])
			if y_train[i]==1.5:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/1.5/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/1.5/"+X_train[i]))
				label_val.append(y_train[i])
			if y_train[i]==2:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/2/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/2/"+X_train[i]))
				label_val.append(y_train[i])
			if y_train[i]==2.5:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/2.5/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/2.5/"+X_train[i]))
				label_val.append(y_train[i])
			if y_train[i]==3:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/3/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/3/"+X_train[i]))
				label_val.append(y_train[i])
			if y_train[i]==3.5:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/3.5/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/3.5/"+X_train[i]))
				label_val.append(y_train[i])
			if y_train[i]==4:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/4/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/4/"+X_train[i]))
				label_val.append(y_train[i])
			if y_train[i]==4.5:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/4.5/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/4.5/"+X_train[i]))
				label_val.append(y_train[i])
			if y_train[i]==5:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/5/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/5/"+X_train[i]))
				label_val.append(y_train[i])
			if y_train[i]==5.5:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/5.5/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/5.5/"+X_train[i]))
				label_val.append(y_train[i])
			if y_train[i]==6:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/6/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/6/"+X_train[i]))
				label_val.append(y_train[i])
			if y_train[i]==6.5:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/6.5/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/6.5/"+X_train[i]))
				label_val.append(y_train[i])
			if y_train[i]==7:
				shutil.copyfile(images_dir+"/"+X_train[i],splitted_data_path_dir+"/"+label+"/training/7/"+X_train[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/training/7/"+X_train[i]))
				label_val.append(y_train[i])

		df_paths_temp=pd.DataFrame(paths)
		df_labels_temp=pd.DataFrame(label_val)

		#Getting the files
		text_file_name=splitted_data_path_dir+"/"+label+"/train.txt"
		pd.concat([df_paths_temp, df_labels_temp], axis=1).to_csv(text_file_name,sep=" ",index=False,header=False)

		##########
		#Validation data
		##########
		paths=[]
		label_val=[]
		#Distributing the images through the folders
		for i in range(len(X_val)):
			if y_val[i]==1:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/1/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/1/"+X_val[i]))
				label_val.append(y_val[i])
			if y_val[i]==1.5:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/1.5/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/1.5/"+X_val[i]))
				label_val.append(y_val[i])
			if y_val[i]==2:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/2/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/2/"+X_val[i]))
				label_val.append(y_val[i])
			if y_val[i]==2.5:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/2.5/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/2.5/"+X_val[i]))
				label_val.append(y_val[i])
			if y_val[i]==3:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/3/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/3/"+X_val[i]))
				label_val.append(y_val[i])
			if y_val[i]==3.5:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/3.5/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/3.5/"+X_val[i]))
				label_val.append(y_val[i])
			if y_val[i]==4:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/4/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/4/"+X_val[i]))
				label_val.append(y_val[i])
			if y_val[i]==4.5:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/4.5/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/4.5/"+X_val[i]))
				label_val.append(y_val[i])
			if y_val[i]==5:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/5/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/5/"+X_val[i]))
				label_val.append(y_val[i])
			if y_val[i]==5.5:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/5.5/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/5.5/"+X_val[i]))
				label_val.append(y_val[i])
			if y_val[i]==6:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/6/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/6/"+X_val[i]))
				label_val.append(y_val[i])
			if y_val[i]==6.5:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/6.5/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/6.5/"+X_val[i]))
				label_val.append(y_val[i])
			if y_val[i]==7:
				shutil.copyfile(images_dir+"/"+X_val[i],splitted_data_path_dir+"/"+label+"/validation/7/"+X_val[i])
				paths.append(str(splitted_data_path_dir+"/"+label+"/validation/7/"+X_val[i]))
				label_val.append(y_val[i])

		df_paths_temp=pd.DataFrame(paths)
		df_labels_temp=pd.DataFrame(label_val)

		#Getting the files
		text_file_name=splitted_data_path_dir+"/"+label+"/validation.txt"
		pd.concat([df_paths_temp, df_labels_temp], axis=1).to_csv(text_file_name,sep=" ",index=False,header=False)

		############
		#Test data
		############
		paths=[]
		label_val=[]
		for i in range(len(X_test)):
			shutil.copyfile(images_dir+"/"+X_test[i],splitted_data_path_dir+"/"+label+"/test/"+X_test[i])
			paths.append(str(splitted_data_path_dir+"/"+label+"/test/"+X_test[i]))
			label_val.append(y_test[i])

		df_paths_temp=pd.DataFrame(paths)
		df_labels_temp=pd.DataFrame(label_val)

		#Getting the files
		text_file_name=splitted_data_path_dir+"/"+label+"/test.txt"
		pd.concat([df_paths_temp, df_labels_temp], axis=1).to_csv(text_file_name,sep=" ",index=False,header=False)
	print("\ndone")

if __name__ == '__main__':
	main()
