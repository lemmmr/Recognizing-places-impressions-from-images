CAFFE_DIR="/Users/lemr/Documents/librerias_python/caffe-master"
while getopts "n:l:" opt; do
  case $opt in
    n)
			CNN_architecture=$OPTARG
      ;;
		l)
			label=$OPTARG
			;;
    \?)
      echo "Invalid option: $OPTARG"
			echo "Usage:"
			echo "./run_caffe.sh -n -CNN_architecture- -l -label-"
			exit
      ;;
  esac
done
SOLVER_DIR="fine-tuning/${CNN_architecture}_places365/${label}/solver.prototxt"
WEIGHTS_DIR="fine-tuning/${CNN_architecture}_places365/${CNN_architecture}_places365.caffemodel"
LOG_DIR="fine-tuning/${CNN_architecture}_places365/${label}/model.log"

$CAFFE_DIR/build/tools/caffe train --solver $SOLVER_DIR -weights $WEIGHTS_DIR 2>&1 | tee $LOG_DIR
