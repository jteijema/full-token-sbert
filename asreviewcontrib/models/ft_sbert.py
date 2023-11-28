from sentence_transformers import models
from sentence_transformers.SentenceTransformer import SentenceTransformer

from asreview.models.feature_extraction.base import BaseFeatureExtraction


class FullTextSBERTModel(BaseFeatureExtraction):
    """Full Text Sentence BERT model.
    """

    name = "ft_sbert"
    label = "Full Text Sentence BERT"

    def __init__(
        self,
        *args,
        transformer_model="all-mpnet-base-v2",
        is_pretrained_sbert=True,
        pooling_mode="mean",
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.transformer_model = transformer_model
        self.is_pretrained_sbert = is_pretrained_sbert
        self.pooling_mode = pooling_mode

    def transform(self, texts):
        model = SentenceTransformer(self.transformer_model)
        print("Encoding texts using sbert, this may take a while...")
        X = model.encode(texts, show_progress_bar=True)

        return X