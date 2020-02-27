import os, glob, json, pwd
import os.path as osp

def line2rec(line):
    items = line.strip().split(' ')
    path = items[0] + '.avi'
    label = items[1]
    return path, label

def main():
    '''
    Assume the dataset's root is '${slowfast}/data/hmdb51'
    '''
    data_root = 'data/hmdb51'
    train_lst_path = osp.join(os.getcwd(), '{}/hmdb51_train_split_1_videos.txt'.format(data_root))
    val_lst_path = osp.join(os.getcwd(), '{}/hmdb51_val_split_1_videos.txt'.format(data_root))

    with open(train_lst_path) as train_f:
        # generate train.csv
        with open(osp.join(data_root, "train.csv"), "w") as f:
            for line in train_f.readlines():
                path, label = line2rec(line)
                f.write((osp.join(os.getcwd(), data_root + '/videos/' + path) + "," + label) + "\n")

    with open(val_lst_path) as val_f:
        # generate val.csv
        with open(osp.join(data_root, "val.csv"), "w") as f:
            for line in val_f.readlines():
                path, label = line2rec(line)
                f.write((osp.join(os.getcwd(), data_root + '/videos/' + path) + "," + label) + "\n")


if __name__ == "__main__":
    main()
