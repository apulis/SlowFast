import os, glob, json, pwd
import os.path as osp

def main():

    train_path = osp.join(os.getcwd(), '../../data/kinetics400/videos_train/')
    val_path = osp.join(os.getcwd(), '../../data/kinetics400/videos_val/')
    anno_path = osp.join(os.getcwd(), '../../data/kinetics400/annotations/')

    with open(osp.join(anno_path, "classids.json")) as f:
        video_label2id=json.load(f)
    video_label2id = {"_".join(x.strip('"').split(" ")):y for x,y in video_label2id.items()}

    # generate train.csv
    video_list = glob.glob(train_path+"*/*.mp4")
    f = open(osp.join(anno_path, "../train.csv"), "w")
    for video in video_list:
        f.write(video + "," + str(video_label2id[video.split('/')[-2]]) + "\n")
    f.close()

    # generate val.csv
    video_list = glob.glob(val_path+"*/*.mp4")
    f = open(osp.join(anno_path, "../val.csv"), "w")
    for video in video_list:
        f.write(video + "," + str(video_label2id[video.split('/')[-2]]) + "\n")
    f.close()

if __name__ == "__main__":
    main()
