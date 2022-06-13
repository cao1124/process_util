import logging
import os
import numpy as np
import torch
from PIL import Image
from torch import nn
from torchvision import models, transforms
from numpy import linalg as LA
skin_mean, skin_std = [0.321, 0.321, 0.327], [0.222, 0.222, 0.226]  # 1342张 us_label_mask1
# skin_mean, skin_std = [0.526, 0.439, 0.393], [0.189, 0.183, 0.177]  # 839张 photo_img_merge


def get_logger(name) -> logging.Logger:
    if name:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        return logger
    else:
        return logging.root


class ResnetFeature:
    def __init__(self):
        self.model = models.resnet50(pretrained=True)
        self.model.fc = nn.Linear(2048, 2048)

    def execute(self, img_path, ignore_error_img=False):
        try:
            img = Image.open(img_path).convert('RGB')
            image_transforms = transforms.Compose([transforms.Resize([224, 224]), transforms.ToTensor(),
                                                   transforms.Normalize(skin_mean, skin_std)])
            if transforms is not None:
                img = image_transforms(img)
            # expand batch dimension
            img = torch.unsqueeze(img, dim=0)
            self.model.eval()
            with torch.no_grad():
                features = torch.squeeze(self.model(img))
                # features = self.model(img)
                norm_feature = features / LA.norm(features)
                norm_feature = [i.item() for i in norm_feature]
            return norm_feature

        except Exception as e:
            logging.error(f"ResNet50, {str(img_path)} execute error: {e}")
            if ignore_error_img:
                return None
            else:
                raise RuntimeError(str(img_path)) from e