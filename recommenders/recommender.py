from abc import ABC, abstractmethod

class MovieRecommenderBase(ABC):
    """Abstract Base Class for Movie Recommenders."""
    
    def __init__(self, data_path):
        self.data_path = data_path
    
    @abstractmethod
    def preprocess_data(self):
        pass
    
    @abstractmethod
    def train_model(self):
        pass
    
    @abstractmethod
    def load_model(self):
        pass
    
    @abstractmethod
    def get_recommendations(self, title, top_n=5):
        pass
