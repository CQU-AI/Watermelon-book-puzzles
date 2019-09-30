#### 2-2
> 数据集包含100个样本，其中正反例各一半，假定学习算法所产生的模型是将新样本预测为训练样本数较多的类别（训练样本数相同时进行随机猜测），试给出用10折交叉验证法和留一法分别对错误率进行评估所得的结果。

 - Loo:
    ```py
    from scipy.special import comb
    import numpy as np

    possibility = np.array(
        [np.arange(10), [comb(50, i) * comb(50, 10 - i) / comb(100, 10) for i in range(10)]]
    )
    exceptation_E = possibility * np.array(
        [np.ones(10), [i / 10 if i >= 5 else (10 - i) / 10 for i in range(10)]]
    )
    print("Exceptation of Error Rate: ", np.sum(exceptation_E[1]))
    ```
