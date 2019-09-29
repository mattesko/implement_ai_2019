import urllib.request
import cv2
import os
import torch
from torchvision import transforms, models
import numpy as np
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

model = torch.load('data/models/resnet.pt', map_location=torch.device('cpu'))
input_size = 224
NUM_CLASSES = 2

data_transforms = {
    'test': transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((input_size, input_size)),
        transforms.CenterCrop(input_size),
        transforms.ToTensor()
    ])
}


def set_parameter_requires_grad(model, feature_extracting):
    if feature_extracting:
        for param in model.parameters():
            param.requires_grad = False

class LewdDataset(Dataset):
    def __init__(self, X, transform):
        self.X = X
        # self.y = y
        self.transform = transform

    def __getitem__(self, index):
        image = self.X[index]
        # label = self.y[index]

        return self.transform(image)

    def __len__(self):
        return len(self.X)


def make_prediction(sentences):
    global model, NUM_CLASSES
    X = []
    y = []

    maps = {0: True,
            1: False}

    for i, s in enumerate(sentences):
        try:
            path_img = "data/current_site/%s.jpg" % i
            urllib.request.urlretrieve(s, path_img)
            image = cv2.imread(path_img)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image,(input_size,input_size)).reshape(3, input_size, input_size)
            image = torch.tensor(np.array(image))
            X.append(image)
            os.remove(path_img)

            set_parameter_requires_grad(model, True)
            num_ftrs = model.fc.in_features
            model.fc = nn.Linear(num_ftrs, NUM_CLASSES)
            results = model(torch.unsqueeze(data_transforms['test'](image), 0))
            results = results[0].detach().cpu().numpy()
            y.append(maps[np.argmax(results)])
        except:
            print(s, "IT failed!!")
            y.append(False)

    return y