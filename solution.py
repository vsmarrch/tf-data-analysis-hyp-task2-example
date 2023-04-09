import pandas as pd
import numpy as np


chat_id = 260376781 # Ваш chat ID, не меняйте название переменной

from scipy.stats import ks_2samp

def solution(x: np.array, y: np.array) -> bool:
    p_val = ks_2samp(x, y).pvalue
    answer = False if p_val > 0.01 else True
    return answer # Ваш ответ, True или False
