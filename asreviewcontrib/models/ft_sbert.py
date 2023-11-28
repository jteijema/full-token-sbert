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
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.transformer_model = transformer_model
        self.model = SentenceTransformer(transformer_model)
        self.tokenizer = self.model.tokenizer

    def split_text(self, text, token_limit):
        tokens = self.tokenizer.tokenize(text)
        token_ids = self.tokenizer.convert_tokens_to_ids(tokens)

        for i in range(0, len(token_ids), token_limit):
            segment_ids = token_ids[i:i + token_limit]
            segment = self.tokenizer.convert_ids_to_tokens(segment_ids)
            yield self.tokenizer.convert_tokens_to_string(segment)

    def transform(self, texts):
        print("Encoding texts with sbert, this may take a while...")

        encoded_texts = []

        for text in tqdm(texts):
            segments = list(self.split_text(text, self.model.max_seq_length))

            segment_embeddings = self.model.encode(segments, show_progress_bar=False)

            if len(segments) == 1:
                    encoded_texts.append(segment_embeddings[0])
                    continue

            encoded_texts.append(np.mean(segment_embeddings, axis=0))

        return np.array(encoded_texts)
