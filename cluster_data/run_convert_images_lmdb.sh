CAFFE_DIR="/idiap/home/lmedina/caffe"
LABELS="Dangerous Dirty Pretty Preserved Accessible Interesting Picturesque Wealthy Quiet Polluted Pleasant Happy"

for label in $LABELS; do
  echo "Processing label: $label"
  TEXT_IMAGES_TRAIN_DIR="/idiap/temp/lmedina/fine-tuning/data/${label}/train_images.txt"
  LMDB_TRAIN_DIR="/idiap/temp/lmedina/fine-tuning/data/${label}/train_lmdb"
  TEXT_IMAGES_VALIDATION_DIR="/idiap/temp/lmedina/fine-tuning/data/${label}/validation_images.txt"
  LMDB_VALIDATION_DIR="/idiap/temp/lmedina/fine-tuning/data/${label}/validation_lmdb"

  echo "Processing train images"
  echo ""
  $CAFFE_DIR/build/tools/convert_imageset -resize_height=256 -resize_width=256 -shuffle=true / $TEXT_IMAGES_TRAIN_DIR $LMDB_TRAIN_DIR
  echo "done"
  echo ""
  echo "Processing validation images"
  echo ""
  $CAFFE_DIR/build/tools/convert_imageset -resize_height=256 -resize_width=256 -shuffle=true / $TEXT_IMAGES_VALIDATION_DIR $LMDB_VALIDATION_DIR
  echo "done"
  echo ""
  echo ""
done
