from typing import BinaryIO
import numpy as np
import torch
import sklearn
from sklearn.metrics import roc_auc_score

def generalized_AUC(prediction, target, n_classes):
    # prediction is tensor
    prediction = prediction.cpu().detach().numpy()
    if (len(np.unique(target)) != n_classes):
        print("Target does not contain all possible classes, AUC may be inaccurate")
    binarizer = sklearn.preprocessing.LabelBinarizer()
    binarizer.fit(prediction)
    prediction = binarizer.transform(prediction)
    target = binarizer.transform(target)

    return roc_auc_score(prediction, target, average="macro")
    
