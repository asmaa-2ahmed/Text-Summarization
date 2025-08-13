from pydantic import BaseModel

class SummarizationRequest(BaseModel):
    text: str
    max_length: int = 130
    min_length: int = 30
    do_sample: bool = False

class SummarizationResponse(BaseModel):
    summary: str
    status: str = "success"