import pandas as pd
import numpy as np
from scipy.stats import gamma

chat_id = 215606022


def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    
    TIME = 41
    
    left_edge_gamma = gamma.ppf(q = alpha / 2, a = n, scale = 1 / n)
    right_edge_gamma = gamma.ppf(q = 1 - alpha / 2, a = n, scale = 1 / n)
    
    left_edge_acceleration = 2*(left_edge_gamma + x.mean() - 1/2) / (TIME ** 2)
    right_edge_acceleration = 2*(right_edge_gamma + x.mean() - 1/2) / (TIME ** 2)
    
    return (left_edge_acceleration, right_edge_acceleration)
