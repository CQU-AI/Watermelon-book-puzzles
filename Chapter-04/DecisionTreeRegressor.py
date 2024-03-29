# description: 使用MSE最小化作为划分准则的CART回归树
import numpy as np

class TreeNode:
    def __init__(
        self, feature=None, threshold=None, n_node=None, value=None
    ):
        self.left_child = self.right_child = -1
        self.feature = feature
        self.threshold = threshold
        self.n_node = n_node
        self.value = value

class DecisionTreeRegressor:
    def __init__(self, max_depth=2):
        self.max_depth = max_depth
        self._nodes = []
        
    @staticmethod
    def mse_regressor(train_y):
#         return np.var(train_y)
        return np.sum(np.square(train_y - np.mean(train_y)))/train_y.size
#         return np.sum((train_y - np.mean(train_y)) ** 2)/train_y.size
    
    def _build_leaf(self, X, y, cur_depth, parent, is_left):
        self._nodes.append(
            TreeNode(
                n_node=X.shape[0],
                value=np.mean(y),
            )
        )
        self._set_parent(parent, is_left, len(self._nodes) - 1)
        return

    def _set_parent(self, parent, is_left, child_ind):
        if parent is not None:
            if is_left:
                self._nodes[parent].left_child = len(self._nodes) - 1
            else:
                self._nodes[parent].right_child = len(self._nodes) - 1
        return

    def _build_tree(self, X, y, cur_depth, parent, is_left):
        if cur_depth == self.max_depth:
            self._build_leaf(X, y, cur_depth, parent, is_left)

        best_mse = np.inf
        best_feature = None
        best_threshold = None
        best_left_ind = best_right_ind = None
        
        step = lambda x, y, a: (x + a, y - a)

        for i in range(X.shape[1]):  # for features
            y_left = np.array([])
            y_right = y.copy()
            ind = np.argsort(X[:, i])

            for j in range(ind.shape[0] - 1):  # for all sample
                # step by step

                y_left = np.append(y_left, y[ind[j]])
                y_right[ind[j]] = 0
                
                cur_mse = self.mse_regressor(y_left) + self.mse_regressor(y_right[y_right > 0])

                if cur_mse < best_mse:  # found better choice
                    best_mse = cur_mse
                    best_feature = i
                    best_threshold = X[ind[j], i]
                    best_left_ind, best_right_ind = ind[: j + 1], ind[j + 1 :]

        self._nodes.append(
            TreeNode(
                feature=best_feature,
                threshold=best_threshold,
                n_node=X.shape[0],
                value=np.mean(y),
            )
        )
        cur_id = len(self._nodes) - 1
        self._set_parent(parent, is_left, cur_id)

        if cur_depth < self.max_depth:
            self._build_tree(
                X[best_left_ind], y[best_left_ind], cur_depth + 1, cur_id, True
            )
            self._build_tree(
                X[best_right_ind], y[best_right_ind], cur_depth + 1, cur_id, False
            )

    def fit(self, X, y):
        self.n_features = X.shape[1]
        self._nodes = []
        self._build_tree(X, y, 0, None, None)
        return self

    def predict(self, X):
        pred = np.zeros(X.shape[0])
        for i in range(X.shape[0]):
            cur_node = 0
            while self._nodes[cur_node].left_child != -1:  # search in tree
                if (
                    X[i][self._nodes[cur_node].feature]
                    <= self._nodes[cur_node].threshold
                ):
                    cur_node = self._nodes[cur_node].left_child
                else:
                    cur_node = self._nodes[cur_node].right_child
            pred[i] = self._nodes[cur_node].value
        return pred
