## Visual Description Description

We take the VLT5 model as the bassline.

** Note **
Please go into [VLT5](https://github.com/j-min/VL-T5) and follow the README there for Pretrained Models and Feature Extraction.


## Setup
```bash
# Create python environment (optional)
conda create -n vsd python=3.7
source activate vsd

# Install python dependencies
pip install -r requirements.txt

# For captioning evaluation
python -c "import language_evaluation; language_evaluation.download('coco')"

# To run the SPICE evaluation, you need switch the JDK to 1.8
```

## Code structure
```bash
# Store images, features, and annotations
./datasets

# Image feature extraction
./feature_extraction

# Train VL-T5
./VLModel/
    src/
        modeling_t5.py modeling_bart.py                       <= VL-T5/VL-BART model classes
        caption_sp.py, vrd_caption.py                         <= fine-tuning
        param.py                                              <= (argparse) configuration
        tokenization.py                                       <= custom tokenizer
        utils.py, dist_utils.py                               <= utility functions
    snap/                                                     <= store weight checkpoints
```


## Pretrained Models
- pretrained VL-BART and VL-T5 are provided by [VLT5](https://github.com/j-min/VL-T5).
- Download `snap/` from [Google Drive](https://drive.google.com/drive/folders/1_SBj4sZ0gUqfBon1gFBiNRAmfHv5w_ph?usp=sharing)
```bash
gdrive download 1_SBj4sZ0gUqfBon1gFBiNRAmfHv5w_ph --recursive
```

## Run
```bash
bash ./baseline.sh gpu_num
```

## Acknowledgement

This repo is adapted from [VLT5](https://github.com/j-min/VL-T5).


## Reference
Please cite our paper if you use our models or data in your project.

This repository cotains code and data for our paper [Visual Spatial Description: Controlled Spatial-Oriented Image-to-Text Generation](https://arxiv.org/abs/2210.11109)


```bibtex
@inproceedings{zhao2022vsd,
  title     = {Visual Spatial Description: Controlled Spatial-Oriented Image-to-Text
               Generation},
  author    = {Yu Zhao and
               Jianguo Wei and
               Zhichao Lin and
               Yueheng Sun and
               Meishan Zhang and
               Min Zhang},
  booktitle = {EMNLP},
  year      = {2022}
}
```