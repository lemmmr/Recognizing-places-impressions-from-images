LABELS="Dangerous Dirty Pretty Preserved Accessible Interesting Picturesque Wealthy Quiet Polluted Pleasant Happy"

while getopts "t:" opt; do
  case $opt in
    t)
			NUM_SAMPLES_TRAINING=$OPTARG
      ;;
    \?)
      echo "Invalid option: $OPTARG"
			echo "Usage:"
			echo "./data_augmentation.sh -t -Number of samples for training-"
			exit
      ;;
  esac
done

for label in $LABELS; do
  echo "Processing label: ${label}"
  LABEL_DIR="/idiap/temp/lmedina/fine-tuning/data/${label}"
  IMAGES_TRAIN_DIR="/idiap/temp/lmedina/fine-tuning/data/${label}/training"
  python scripts/data_augmentation.py $IMAGES_TRAIN_DIR $NUM_SAMPLES_TRAINING
  cat ${LABEL_DIR}/train.txt ${IMAGES_TRAIN_DIR}/data_ag.txt > ${LABEL_DIR}/train_images.txt

 # IMAGES_VALIDATION_DIR="/idiap/temp/lmedina/fine-tuning/data/${label}/validation"
 # python scripts/data_augmentation.py $IMAGES_VALIDATION_DIR $NUM_SAMPLES_VALIDATION
 # cat ${LABEL_DIR}/validation.txt ${IMAGES_VALIDATION_DIR}/data_ag.txt > ${LABEL_DIR}/validation_images.txt
done

echo "done"
