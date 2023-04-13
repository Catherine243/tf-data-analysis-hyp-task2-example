import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 557932710 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    pv = ks_2samp(x, y)[1]
    
    if (p_value < 0.05):
    return True
    else:
    return False 
