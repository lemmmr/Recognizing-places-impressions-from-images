folder: notebooks

Description: Contains the different (jupyter) notebooks used to do pre-processing and feature analysis:
	-CECYTE_annotations.ipynb: Contains the pre-processing of the CECYTE annotations, as well as the analysis (e.g. correlation analysis, co-occurrence matrices, etc.) of them and generates files to process in R.
	-MTurk_annotations.ipynb: Contains the pre-processing of the MTUrk annotations and generates files to process in R.
	-classification_places365.ipynb: Contains an example of classification based on the GoogLeNet CNN pre-trained on the places365 database.
	
	-feature_analysis folder: Contains two other jupyter notebooks:
		-feature_analysis.ipynb: Contains the feature analysis based mostly on the places205 and semantic segmentation datasets.
		-feature_analysis_2.ipynb: Contains the complementary feature analysis based on the places365 dataset.

	-manual_annotation: contains a jupyter notebook with the manual annotation task. There is a readme.txt file with the explanation of the folder.

	-TSNE_analysis: contains a jupyter notebook with the t-SNE analysis based on the semantic segmentation and places205 datasets, as well as a folder with the generated plots. Please note that the t-SNE analysis of the places365 dataset is made in the feature_analysis_2.ipynb.