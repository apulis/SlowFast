import os, glob, json, pwd
import os.path as osp

def line2rec(line):
    items = line.strip().split(' ')
    path = items[0] + '.avi'
    label = items[1]
    return path, label

def main():
    '''
    Assume the dataset's root is '${slowfast}/data/ucf101'
    '''
    hmdb51_root = 'data/ucf101'
    train_lst_path = osp.join(os.getcwd(), '{}/ucf101_train_split_1_videos.txt'.format(hmdb51_root))
    val_lst_path = osp.join(os.getcwd(), '{}/ucf101_val_split_1_videos.txt'.format(hmdb51_root))

    with open(train_lst_path) as train_f:
        # generate train.csv
        with open(osp.join(hmdb51_root, "train.csv"), "w") as f:
            for line in train_f.readlines():
                path, label = line2rec(line)
                f.write((osp.join(os.getcwd(), hmdb51_root + '/videos/' + path) + "," + label) + "\n")

    with open(val_lst_path) as val_f:
        # generate val.csv
        with open(osp.join(hmdb51_root, "val.csv"), "w") as f:
            for line in val_f.readlines():
                path, label = line2rec(line)
                f.write((osp.join(os.getcwd(), hmdb51_root + '/videos/' + path) + "," + label) + "\n")


if __name__ == "__main__":
    main()
