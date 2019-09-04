# User Define parameters

# Make it True if you want to use the provided coco weights
is_coco = False

# keras model directory path
MODEL_DIR = '/data/bengang/keras_model/'

# keras model file path
H5_WEIGHT_PATH = '/data/keras_model/mask_rcnn_asdc_gpu_0004.h5'

# Path where the Frozen PB will be save
PATH_TO_SAVE_FROZEN_PB = '/data/frozen_model/'

# Name for the Frozen PB name
FROZEN_NAME = 'mask_rcnn_frozen_graph.pb'

# PATH where to save serving model
PATH_TO_SAVE_TENSORFLOW_SERVING_MODEL = '/data/serving_model'

# Version of the serving model
VERSION_NUMBER = 1

# Number of classes that you have trained your model
NUMBER_OF_CLASSES = 5
