import pandas as pd
import numpy as np


chat_id = 260376781 # Ваш chat ID, не меняйте название переменной

from hyppo.ksample import MMD

def solution(x: np.array, y: np.array) -> bool:
    stat, p_val = MMD(compute_kernel="laplacian").test(x, y)
    answer = False if p_val > 0.01 else True
    return answer # Ваш ответ, True или False
