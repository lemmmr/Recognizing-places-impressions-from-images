echo "Splitting image data"

SPLITTED_DATA_PATH="fine-tuning/data"
IMAGES_PATH="city-image-corpus/"
DATASET_LABELS_PATH="datasets/all-places-all-labels-median-medina.csv"

source activate python27
python scripts/splitting_data_v2.py $SPLITTED_DATA_PATH $DATASET_LABELS_PATH $IMAGES_PATH
source deactivate
