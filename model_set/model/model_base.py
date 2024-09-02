from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self):
        self.params_flops = self.get_params_flops()  

    @abstractmethod
    def get_input(self):

        pass

    @abstractmethod
    def load_model(self):

        pass

    @abstractmethod
    def get_params_flops(self) -> list:
        '返回值是[params, flops]'

        pass

    @abstractmethod
    def inferrence(self):

        pass
