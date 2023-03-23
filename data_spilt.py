import pandas as pd
import glob
from sklearn.model_selection import train_test_split

DATA_FOLDER = "../suadd23-semseg-amazon/mmsegmentation/data/suadd23/"
split_ratio = 0.1

image_names = [x.split('/')[-1] for x in glob.glob(DATA_FOLDER + "inputs/*")]
image_ann = [x.split('/')[-1] for x in glob.glob(DATA_FOLDER + "semantic_annotations/*")]

scene = [x.split('-')[0] for x in image_names]
df = pd.DataFrame(list(zip(image_names, image_ann,  scene)),
               columns =['image', 'annotations', 'scene'])

gb = df.groupby("scene")
gb_list = [gb.get_group(x) for x in gb.groups]

train,  test = train_test_split(gb_list, test_size = split_ratio)

train_df = pd.concat(train)
test_df = pd.concat(test)

train_df["type"] = "train"
test_df["type"] = "test"

train_df.to_csv(DATA_FOLDER + "train.csv", index=0)
test_df.to_csv(DATA_FOLDER + "test.csv", index=0)


