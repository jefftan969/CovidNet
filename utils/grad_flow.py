import torch
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plot_grad_flow(named_parameters):
    """
    Usage: plot_grad_flow(model.named_parameters())
    """ 
    ave_grads = []    
    max_grads= []    
    layers = []    
    for n, p in named_parameters:        
        if(p.requires_grad) and ("bias" not in n):            
            if(p is not None):                
                layers.append(n)                
                ave_grads.append(p.grad.abs().mean())                
                max_grads.append(p.grad.abs().max())
    plt.clf()
    plt.bar(np.arange(len(max_grads)), max_grads, alpha=0.1, lw=1, color="y")    
    plt.bar(np.arange(len(max_grads)), ave_grads, alpha=0.1, lw=1, color="b")    
    plt.hlines(0, 0, len(ave_grads)+1, lw=2, color="k" )    
    plt.xticks(range(0,len(ave_grads), 1), layers, rotation="vertical")    
    plt.xlim(left=0, right=len(ave_grads))    
    plt.ylim(bottom = -0.001, top=0.02)  
    plt.xlabel("Layers")
    plt.ylabel("Avg gradient")    
    plt.title("Gradient flow")  
    plt.grid(True)    
    plt.legend([Line2D([0], [0], color="y", lw=4),
                Line2D([0], [0], color="b", lw=4),
                Line2D([0], [0], color="k", lw=4)], ['max', 'mean', 'zero-grad'])    
    return plt