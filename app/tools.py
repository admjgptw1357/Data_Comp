#-*-coding:utf-8 -*-

from sklearn import metrics
import math
import numpy as np

# スコアリングメソッドの集合
def scoring(result,competition):
    res = np.array(map(float,result))
    ans  = np.array(map(float,competition.answer.rstrip().split("\n")))

    ms =competition.mid_test_s
    me = competition.mid_test_e
    fs = competition.f_test_s
    fe = competition.f_test_e
    if me == 0:
        me = len(res)
    if fe == 0:
        fe = len(res)

    mid_res = res[ms:me]
    mid_ans = ans[ms:me]
    f_res = res[fs:fe]
    f_ans =ans[fs:fe]

    if competition.scoring == "MSE":
        mid = metrics.mean_squared_error(mid_res,mid_ans)
        f = metrics.mean_squared_error(f_res,f_ans)
    elif competition.scoring == "RMSE":
        print metrics.mean_squared_error(mid_res,mid_ans)
        mid = math.sqrt(metrics.mean_squared_error(mid_res,mid_ans))
        f = math.sqrt(metrics.mean_squared_error(f_res,f_ans))
    elif competition.scoring == "CORRELATION":
        mid = metrics.r2_score(mid_res,mid_ans)
        f = metrics.r2_score(f_res,f_ans)
    elif competition.scoring == "ACCURACY":
        mid = metrics.accuracy_score(mid_res,mid_ans)
        f = metrics.accuracy_score(f_res,f_ans)
    elif competition.scoring == "F1":
        mid = metrics.f1_score(mid_res, mid_ans,average="macro")
        f = metrics.f1_score(f_res, f_ans,average="macro")
    else:
        mid = metrics.adjusted_rand_score(mid_res, mid_ans)
        f = metrics.adjusted_rand_score(f_res, f_ans)

    return mid,f