from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.pipeline import make_pipeline

class Model:
    def __init__(_self,model,normalization):
        _self.model=model
        if normalization == "MinMaxScaler":
            _self.normalization = MinMaxScaler()
        elif normalization == "StandardScaler":
            _self.normalization = StandardScaler()
        elif normalization == "RobustScaler":
            _self.normalization = RobustScaler()
        else:
            raise Exception("Invalid Normalization Must Be Applied")
        _self.model=make_pipeline(_self.normalization,_self.model)
        
    def get_model(_self):
        return _self.model