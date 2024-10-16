from recommenders.faiss_recommender import FaissRecommender
# You can add more models like TfIdfRecommender here

class RecommenderFactory:
    @staticmethod
    def get_recommender(recommender_type, config):
        if recommender_type == 'faiss_recommender':
            return FaissRecommender(config['data_path'], config['model_path'])
        # elif recommender_type == 'tfidf_recommender':
        #     return TfIdfRecommender(config['data_path'])
        else:
            raise ValueError(f"Recommender type {recommender_type} not supported.")
