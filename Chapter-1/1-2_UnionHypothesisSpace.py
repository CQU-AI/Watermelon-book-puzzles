from 1-1_DatasetSpace import DatasetSpace
import json

class UnionHypothesisSpace:
    def init(self,dataset=None):
        if dataset is None:
            return
        self.__data = dataset
        self.__space = DatasetSpace(dataset)
 
        self.his_hypothsis_code = {}
        self.his_hypothsis_code["k=1"] = self.get_conj_hypothesis
        for i,h in enumerate(self.his_hypothsis_code["k=1"]):
            self.his_hypothsis_code["k=1"][i] = self.encoder(h)
        self.hypothsis_code_pool = self.his_hypothsis_code["k=1"]

        self.sample_space = self.get_sample_space()

        self.__features = list(self.__data.columns)
        self.__features.remove("target")

    def get_conj_hypothesis(self):
        return self.__space.get_hypothesis_space()

    def get_sample_space(self):
        return self.__space.get_sample_space()

    def encode(self,hypothesis):
        code = ""
        for s in self.sample_space:
            for i in range(len(self.__features)):
                if s[i] == hypothesis[i] or hypothesis[i]=="*":
                    code+="1"
                else:
                    code+="0"
        return code
    
    def union(self,k):
        self.his_hypothsis_code["k="+str(k+1)]=[]
        for h_l in self.his_hypothsis_code["k="+str(k)]:
            for h_r in self.his_hypothsis_code["k=1"]:
                if (h_l or h_l) not in self.hypothsis_code_pool:
                    self.hypothsis_code_pool.append(h_l or h_l)
                    self.his_hypothsis_code["k="+str(k+1)].append(h_l or h_l)

    def run(self,k=1):
        max_hypothsis_number = 2**(len(self.sample_space))
        while len(self.hypothsis_code_pool) < max_hypothsis_number:
            self.union(k)
            self.save_report(k)
            k+=1

    def load(self):
        with open("./res.json",'r') as f:
            res = json.loads(f.read())

        self.__data = res["dataset"]
        self.__space = DatasetSpace(res["dataset"])
        self.his_hypothsis_code = res["his_hypothsis_code"]
        self.hypothsis_code_pool = res["hypothsis_code_pool"]

        self.sample_space = self.get_sample_space()

        self.__features = list(self.__data.columns)
        self.__features.remove("target")

    def save_report(self,k):
        with open("./res.json",'w') as f:
            res = {"dataset":self.__data,
            "his_hypothsis_code":self.his_hypothsis_code,
            "hypothsis_code_pool":self.hypothsis_code_pool}

        f.write(res)
        print("Working on {}-term-disjunction:\n Currently number of hypothsis:{}\nNumber of hypothsis:{}".format(k,len(self.his_hypothsis_code["k="+str(k)]),len(self.hypothsis_code_pool)))

if __name__ =="__main__":
    melon_data = pd.DataFrame(
        [
            ["青绿", "蜷缩", "浊响", True],
            ["乌黑", "蜷缩", "浊响", True],
            ["青绿", "硬挺", "清脆", False],
            ["乌黑", "稍蜷", "沉闷", False],
        ],
        columns=["色泽", "根蒂", "敲声", "target"],
    )

    space = UnionHypothesisSpace(melon_data)
    space.run()

    # space = UnionHypothesisSpace()
    # space.load()
    # space.run(10)