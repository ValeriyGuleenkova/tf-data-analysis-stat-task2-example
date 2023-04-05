import pandas as pd
import numpy as np
from scipy.stats import expon

chat_id = 215606022


def solution(p: float, x: np.array) -> tuple:
    TIME = 41
    alpha = 1 - p
    stat = x.sum()
    
    left_edge_expon = expon.ppf(alpha / 2)
    right_edge_expon = expon.ppf(1 - alpha / 2)
    
    left_edge_acceleration = (left_edge_expon + stat - 1/2) / (TIME ** 2)
    right_edge_acceleration = (right_edge_expon + stat - 1/2) / (TIME ** 2)
    
    return (left_edge_acceleration, right_edge_acceleration)
