import Augmentor
import sys
import os
import glob
import pandas as pd
import shutil

def main():
    if len(sys.argv) != 3:
        print("Usage: python data_augmentation.py training_directory n_samples\n\n")
        return
    if os.path.exists(sys.argv[1]):
    	print('Directory checked\n\n')
    else:
    	print('Check the directory')
    	return


    working_directory=sys.argv[1]
    working_directory_abs=os.path.abspath(working_directory)
    n_samples=int(sys.argv[2])

	#Removing any existing directory
    if os.path.exists(working_directory_abs+"/output"):
        shutil.rmtree(working_directory_abs+"/output")

    p = Augmentor.Pipeline(working_directory)

    p.rotate(probability=0.7, max_left_rotation=5, max_right_rotation=5)
    p.rotate90(probability=0.7)
    p.rotate270(probability=0.7)
    p.flip_left_right(probability=0.6)
    p.flip_top_bottom(probability=0.5)
    p.crop_random(probability=0.8, percentage_area=0.6)
    p.skew(probability=0.7,magnitude=1)
    p.random_erasing(probability=0.5, rectangle_area=0.4)
    p.random_distortion(probability=0.7, grid_width=5, grid_height=5, magnitude=5)

    p.sample(n_samples)

    print("\n\nGetting file with labels and paths")

    list_files=[]
    list_labels=[]

    for directory in glob.glob(working_directory_abs+"/output/*"):
        for file_ in glob.glob(directory+"/*"):
            list_files.append(str(file_))
            list_labels.append(float(file_.split("/")[-1].split("_")[0]))


    df_paths_temp=pd.DataFrame(list_files)
    df_labels_temp=pd.DataFrame(list_labels)

	#Getting the files
    text_file_name=working_directory_abs+"/data_ag.txt"
    pd.concat([df_paths_temp, df_labels_temp], axis=1).sample(frac=1).to_csv(text_file_name,sep=" ",index=False,header=False)
    print("\n\nDone")
if __name__ == '__main__':
    main()
