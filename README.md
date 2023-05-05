# suadd
## Segmentation
* [https://github.com/baaivision/EVA/tree/master/EVA-01/seg](https://github.com/baaivision/EVA/tree/master/EVA-01/seg)
* [https://github.com/OpenGVLab/InternImage/blob/master/README_EN.md](https://github.com/OpenGVLab/InternImage/blob/master/README_EN.md)
* [https://github.com/czczup/ViT-Adapter/tree/main/segmentation](https://github.com/czczup/ViT-Adapter/tree/main/segmentation)

### Additional Datasets
* [https://www.tugraz.at/index.php?id=22387](https://www.tugraz.at/index.php?id=22387)
* [https://uavid.nl/](https://uavid.nl/)
* [https://midair.ulg.ac.be/download.html](https://midair.ulg.ac.be/download.html)
* [https://github.com/montefiore-ai/midair-dataset/](https://github.com/montefiore-ai/midair-dataset/)

### Usage instructions
* git clone https://github.com/czczup/ViT-Adapter/tree/main
* cd ViT-Adapter/segmentation
* pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
* pip install mmcv-full==1.4.2 -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.9.0/index.html
* pip install timm==0.4.12
* pip install mmdet==2.22.0 # for Mask2Former
* pip install mmsegmentation==0.20.2
* ln -s ../detection/ops ./
* cd ops & sh make.sh # compile deformable attention

Then use the config provided here to train the model. Our final submission was a soup of the 18kth and the 20kth iter models.
