import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 1112700607  # Ваш chat ID, не меняйте название переменной

def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = x_success / x_cnt - y_success / y_cnt
    numerator = (x_cnt + y_cnt) * x_cnt * y_cnt
    denominator = ((x_success + y_success) * (x_cnt + y_cnt - x_success - y_success))
    return a * np.sqrt(numerator / denominator) <= norm.ppf(0.05)
