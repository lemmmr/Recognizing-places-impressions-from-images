folder: scripts

Description of the folder: contains the different scripts used for the experiments and data processing. Please check that the directories match before running them. The distribution is the following:
	-bash_scripts: contains bash scripts that call the python scripts to make the execution easier:
		-data_augmentation.sh: calls the data_augmentation.py python script to generate data augmentation of the images.
		-run_caffe.sh: run the caffe command to do fine-tuning.
		-run_convert_images_lmdb.sh: convert a set of images to a lmdb database as well as resize them to 256x256 pixels.
		-run_split_image_data.sh: split the images into training and validation data as well as between different folders that are going to be used to generate data augmentation.
	
	-python_scripts: contains the python scripts to process the data.
		-classification_googlenet_places365.py: makes classification based on the GoogLeNet places365 CNN.
		-convert_proto_mean.py: converts a binaryproto mean file to an equivalent python npy mean file.
		-data_augmentation.py: generates data augmentation based.
		-splitting_data_to_hdf5.py: split the image corpus into train and validation datasets and stores them into a hdf5 file.
		-splitting_data_v2.py: splits the image corpus into validation and training datasets and prepare both to data augmentation.
		-spliitng_data.py: makes a simple split of the data into validation and training datasets.

	-R_scripts: contains the R scripts to do statistical analysis as well as machine learning:
		-RF_classification.R: performs classification based on Random Forests.
		-RF_regression.R: performs regression based on Random Forests.
		-RF_regression_cecyte.R: performs regression based on Random Forest and it is used only with the CECYTE datasets.
		-ggbiplot2.R: a modified version to plot the loadings of the 2 Principal components of a PCA analysis.
		-icc_kappa_analysis.R: gets the ICC(1,k), Fleiss' kappa values and the Krippendorf's Alpha to see agreement between annotators.
		-pairwise_scatter_plot.R: gets the pairwise_scatter_plot between MTurkers and CECYTE students.
		-pca_analysis_labels.R: gets the plots of the loadings of the PCA analysis.
		-readRDS_results_files.R: reads the RDS files from the "/r_results" folder
tukey_hsd.R
