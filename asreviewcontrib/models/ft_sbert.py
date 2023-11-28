from sentence_transformers import SentenceTransformer
from asreview.models.feature_extraction.base import BaseFeatureExtraction
import numpy as np
from tqdm import tqdm

class FullTextSBERTModel(BaseFeatureExtraction):
    """Full Text Sentence BERT model."""

    name = "ft_sbert"
    label = "Full Text Sentence BERT"

    def __init__(
        self,
        *args,
        transformer_model="all-mpnet-base-v2",
        combination_mode="mean",
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.transformer_model = transformer_model
        self.combination_mode = combination_mode
        self.max_token_length = 384
        self.model = SentenceTransformer(transformer_model)
        self.tokenizer = self.model.tokenizer

    def split_text(self, text, token_limit):
        words = text.split()
        for i in range(0, len(words), token_limit):
            yield ' '.join(words[i:i + token_limit])

    def transform(self, texts):
        print("Encoding texts with sbert, this may take a while...")

        encoded_texts = []

        for text in tqdm(texts):
            segments = list(self.split_text(text, self.max_token_length))

            segment_embeddings = self.model.encode(segments, show_progress_bar=False)

            if len(segments) > 1:
                if self.combination_mode == "mean":
                    combined_embedding = np.mean(segment_embeddings, axis=0)
                elif self.combination_mode == "max":
                    combined_embedding = np.max(segment_embeddings, axis=0)
                elif self.combination_mode == "first":
                    combined_embedding = segment_embeddings[0]
                elif self.combination_mode == "last":
                    combined_embedding = segment_embeddings[-1]
                else:
                    raise ValueError("Invalid combination mode. Choose 'mean', 'max', 'first', or 'last'.")
            else:
                combined_embedding = segment_embeddings[0]
            encoded_texts.append(combined_embedding)

        return encoded_texts
