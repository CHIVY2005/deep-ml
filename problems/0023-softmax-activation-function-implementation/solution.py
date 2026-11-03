import math

def softmax(scores: list[float]) -> list[float]:
    max_s = max(scores)
    expz = [math.exp(s-max_s) for s in scores]
    sum_exp = sum(expz)
    softmax = [v / sum_exp for v in expz]
    return softmax
    pass