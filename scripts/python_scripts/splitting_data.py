import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split


def main():
	#Validating
	if len(sys.argv) != 5:
		print('\n\nUsage: python scripts/splitting_data.py splitted_data_path dataset_labels_path images_path splitting_option\n\n')
		return
	if os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]) and os.path.exists(sys.argv[3]):
		print('Directories checked')
	else:
		print('Check the directories')
		return
	if sys.argv[4] != str(1) and sys.argv[4] !=str(2):
		print('Select a valid option')
		print(sys.argv[4])
		return
    #Getting directories
	images_dir=os.path.abspath(sys.argv[3])
	labels_dir=os.path.abspath(sys.argv[2])
	splitted_data_path_dir=os.path.abspath(sys.argv[1])

	#Reading the labels file into a pandas dataframe
	df_labels = pd.read_csv(labels_dir)
	labels = df_labels.drop(["annotation","city"],axis=1).columns.tolist()
	with open(splitted_data_path_dir+"/labels.txt", "w") as output:
		for label in labels:
			output.write(str(label)+'\n')

	if sys.argv[4]==str(1):
		labels = df_labels.drop(["annotation","city"],axis=1).columns.tolist()

		for label in labels:
			print("Splitting data for: "+label)
			X_train, X_test, y_train, y_test = train_test_split(df_labels["annotation"],df_labels[label],test_size=0.20)

			#Adding absolute paths
			X_train=images_dir+"/"+X_train
			X_test=images_dir+"/"+X_test

			#Getting the files
			text_file_name_train=splitted_data_path_dir+"/"+label+"_train.txt"
			text_file_name_test=splitted_data_path_dir+"/"+label+"_test.txt"

			#Train data
			pd.concat([X_train, y_train], axis=1).to_csv(text_file_name_train,sep=" ",index=False,header=False)

			#Test data
			pd.concat([X_test, y_test], axis=1).to_csv(text_file_name_test,sep=" ",index=False,header=False)

	if sys.argv[4]==str(2):
		print("Splitting data for all labels")
		X_train, X_test, y_train, y_test = train_test_split(df_labels["annotation"],df_labels.drop(["annotation","city"],axis=1),test_size=0.20)

		#Adding absolute paths
		X_train=images_dir+"/"+X_train
		X_test=images_dir+"/"+X_test

		#Getting the files
		text_file_name_train=splitted_data_path_dir+"/train.txt"
		text_file_name_test=splitted_data_path_dir+"/test.txt"

		#Train data
		pd.concat([X_train, y_train], axis=1).to_csv(text_file_name_train,sep=" ",index=False,header=False)

		#Test data
		pd.concat([X_test, y_test], axis=1).to_csv(text_file_name_test,sep=" ",index=False,header=False)

	print("\ndone")

if __name__ == '__main__':
	main()
