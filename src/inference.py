from transformers import pipeline
from .config import load_model, load_tokenizer, DEVICE
from .schemas import SummarizationRequest, SummarizationResponse

class TextSummarizer:
    def __init__(self):
        self.model = load_model()
        self.tokenizer = load_tokenizer()
        self.summarizer = pipeline(
            "summarization",
            model=self.model,
            tokenizer=self.tokenizer,
            device=0 if DEVICE == "cuda" else -1
        )

    def summarize(self, request: SummarizationRequest) -> SummarizationResponse:
        try:
            result = self.summarizer(
                request.text,
                max_length=request.max_length,
                min_length=request.min_length,
                do_sample=request.do_sample
            )
            return SummarizationResponse(summary=result[0]["summary_text"])
        except Exception as e:
            return SummarizationResponse(
                summary=str(e),
                status="error"
            )

# Singleton instance
text_summarizer = TextSummarizer()