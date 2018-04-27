echo "Splitting image data"

SPLITTED_DATA_PATH="/idiap/temp/lmedina/fine-tuning/data"
IMAGES_PATH="city-image-corpus/"
DATASET_LABELS_PATH="datasets/all-places-all-labels-median-medina.csv"

python scripts/splitting_data_v2.py $SPLITTED_DATA_PATH $DATASET_LABELS_PATH $IMAGES_PATH

echo "done"
