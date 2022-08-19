from abc import ABC, abstractmethod


class AbstractOption: 
    def __init__(self):
        pass

    @abstactmethod
    def initiate(self):
        pass

    @abstactmethod
    def get_action(self):
        pass
    
    @abstactmethod
    def terminate(self):
        pass


class BottleneckOption(AbstractOption):
    def __init__(self):
        pass

    def initiate(self):
        pass

    def get_action(self):
        pass
    
    def terminate(self):
        pass