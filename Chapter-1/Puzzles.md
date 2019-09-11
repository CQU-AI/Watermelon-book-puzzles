**1-1** 
> 表1.1中若只包含编号为1，4的两个样例，试给出相应的版本空间。

- [DatasetSpace.py](./DatasetSpace.py) : Automatically generate the sample_space, hypothesis_space and version_space for a data set

---
**1-2** 
> 与使用单个合取式来进行假设表示相比，使用“析合范式”将使得假设空间具有更强的表示能力。若使用最多包含k个合取式的析合范式来表达1.1的西瓜分类问题的假设空间，试估算有多少种可能的假设。

 - [UnionHypothesisSpace.cpp](./UnionHypothesisSpace.cpp) : Figure out how the number of hypothsis change with the disjunction become longer
 - [UnionHypothesisSpace.py](./UnionHypothesisSpace.py) : PY edition
