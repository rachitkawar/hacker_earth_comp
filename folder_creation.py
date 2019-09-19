import pandas as pd
import os
import numpy as np
import shutil
# Open dataset file
dataset = pd.read_csv('train.csv')
file_names = list(dataset['image_id'].values)
img_labels = list(dataset['category'].values)
folders_to_be_created = np.unique(list(dataset['category']))

source = os.getcwd()

for new_path in folders_to_be_created:
    if not os.path.exists(".//train//" + str(new_path)):
        os.makedirs(".//train//" + str(new_path))
        os.makedirs(".//validation//" + str(new_path))

# Be sure that there is nothing else in your directory except the data, csv and the code file, IT's Better to only have your data in that directory and reference the CSV file from a different Directory...

folders = folders_to_be_created.copy()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(file_names, img_labels, test_size=0.15, random_state=42)
for f in range(1,len(X_train)):

  current_img = X_train[f]
  current_label = y_train[f]

   ## **Check this Line Accordingly** 

  shutil.move("I://Data Science//Hackerearth//Garden nerd//data//train//"+str(current_img)+'.jpg', "I://Data Science//Hackerearth//Garden nerd//data//train//"+str(current_label)+'//'+str(current_img)+'.jpg')

for f in range(1,len(X_test)):

  current_img = X_test[f]
  current_label = y_test[f]

   ## **Check this Line Accordingly** 

  shutil.move("I://Data Science//Hackerearth//Garden nerd//data//train//"+str(current_img)+'.jpg', "I://Data Science//Hackerearth//Garden nerd//data//validation//"+str(current_label)+'//'+str(current_img)+'.jpg')