import pandas as pd


class DatasetSpace:
    """
    Automatically generate the sample_space, hypothesis_space and version_space for a data set
    """

    def __init__(self, dataset):
        """
        :param dataset: pd.DataFrame
        """
        self.__data = dataset
        self.__features = self.__data.columns

    def get_hypothesis_space(self):
        """
        :return: list (list hypothesis (unknown sample_value))
        """
        sample_space = self.get_sample_space()
        enum = Enumerator([len(sample_space[f]) for f in self.__features])
        hypothesis_space = []

        while True:
            res = [0] * len(self.__features)
            code = enum.next()
            if code == -1:
                break
            for i, e in enumerate(code):
                res[i] = sample_space[self.__features[i]][e]
            hypothesis_space.append(res)
        hypothesis_space.append(["-"] * len(self.__features))
        return hypothesis_space

    def get_version_space(self):
        """
        Check the hypothesis_space with the samples, which will get version_space
        :return:
        """
        # TODO: implement of get_version_space
        for sap in self.__data:
            for hps in self.get_hypothesis_space():
                return hps

    def get_sample_space(self):
        """
        Get the sample space
        :return: dic (key:(str feature)
                      value:(list possible_feature_values))
        """
        sample_space = {}
        for f in self.__features:
            sample_space[f] = list(self.__data[f].unique()) + ["*"]
        return sample_space

    # TODO: format and print space


class Enumerator:
    """
    enumerator for hypothesis_space
    """

    def __init__(self, max):
        self.code = [0] * len(max)
        self.base = max
        self.overflow = False

    def next(self):
        if self.overflow:
            return -1

        self.code[0] += 1
        if not self.carry():
            self.overflow = True
            return self.code
        else:
            return self.code

    def carry(self):
        for i, b in enumerate(self.base):
            if self.code[i] == b:
                self.code[i] = 0
                if i + 1 >= len(self.code):
                    return False
                self.code[i + 1] += 1

                self.carry()
            else:
                return True


if __name__ == "__main__":
    melon_data = pd.DataFrame(
        [
            ["青绿", "蜷缩", "浊响"],
            ["乌黑", "蜷缩", "浊响"],
            ["青绿", "硬挺", "清脆"],
            ["乌黑", "稍蜷", "沉闷"],
        ],
        columns=["色泽", "根蒂", "敲声"],
    )
    space = DatasetSpace(melon_data)
    print(space.get_hypothesis_space())
