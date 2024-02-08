# ASL-Video-Swin-Tiny :-
Implementation of American-Sign-Language recognition using Video-Swin-Transformer which was pretrained on kinetics-400 dataset.   

# Dataset Description :- 
For this project we used the WLASL dataset ([https://github.com/dxli94/WLASL](url)) and it had total of 2000 glosses and short videos of maximum 4-5 second duration.
Here is an example video- 



https://github.com/Sid-tyagi-ar/ASL-Swin-B/assets/115366825/227435f8-de67-4dab-b83a-8aa5ab3d5151

# Pre-Processing the data :- 

The initial dataset had provided with the json file with gloss with their respective video_ids and other details. From this we used the json file in order to make a dictionary containing only glosses with their video_ids then removing the missing video_ids. 

Since we were using Video Swin Transformer for the recognition purpose we first changed the fps of every video to 25 fps and then resized every video into 224x224.
Now the problem which arised was that irregularity of samples for every gloss. After analysis there were only 662 classes with samples equal to or more than 7. Now to prevent overfitting we only finetuned with glosses with 7 sample, using 115 glosses only.

Before feeding videos into the model for training and validation we performed the following data augmentations-
1. Centre-crop
2. Random-resized-crop
3. Flip

# Model-Setting :-

1. Video-swin-transformer tiny pretrained on kinetics-400 dataset and fine-tuned on 30 epochs.
2. AdamW optimiser and cosineannealinglr, linearlr for regularizer

# Notes :-
1. Used MMAction2([https://github.com/open-mmlab/mmaction2](url)) for getting pretrained video-swin-transformer and finetuning purpose.
2. ([[(https://drive.google.com/file/d/1M2x5fQvMvmI3pia2ArxfPrTMaGdEykAR/view?usp=sharing)](url)) - Checkpoint file for using the trained weights for further uses.
# Accuracy -
top1/acc - 53.91%
top5/acc - 91.30%





