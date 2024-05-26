# coding=utf-8

import os
from detectron2_proposal_maxnms import collate_fn, extract, NUM_OBJECTS, DIM
from torch.utils.data import Dataset, DataLoader
import cv2
from tqdm import tqdm
from pathlib import Path
import argparse



class VSDataset(Dataset):
    def __init__(self, image_dir):
        self.image_dir = image_dir
        self.image_path_list = list(tqdm(image_dir.iterdir()))
        self.n_images = len(self.image_path_list)

        # self.transform = image_transform

    def __len__(self):
        return self.n_images

    def __getitem__(self, idx):
        image_path = self.image_path_list[idx]
        image_id = image_path.stem

        img = cv2.imread(str(image_path))

        return {
            'img_id': image_id,
            'img': img
        }

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--batchsize', default=1, type=int, help='batch_size')
    parser.add_argument('--vrdroot', type=str, default='../dataset/')

    args = parser.parse_args()

    vrd_dir = Path(args.vrdroot).resolve()
    vsd_img_dir = vrd_dir.joinpath('images')


    out_dir = vrd_dir.joinpath('features')
    if not out_dir.exists():
        out_dir.mkdir()

    print('Load images from', vsd_img_dir)
    print('# Images:', len(list(vsd_img_dir.iterdir())))

    dataset = VSDataset(vsd_img_dir)

    dataloader = DataLoader(dataset, batch_size=args.batchsize,
                            shuffle=False, collate_fn=collate_fn, num_workers=4)

    output_fname = out_dir.joinpath(f'vrd_boxes{NUM_OBJECTS}.h5')
    print('features will be saved at', output_fname)

    desc = f'VRD_{(NUM_OBJECTS, DIM)}'

    extract(output_fname, dataloader, desc)
