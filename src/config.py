from pathlib import Path
from transformers import BartForConditionalGeneration, AutoTokenizer
import torch
import os

os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["TF_ENABLE_ONEDNN_OPTS"]="0"

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Model paths
MODEL_PATH = BASE_DIR / "src" / "assets" / "model"
TOKENIZER_PATH = BASE_DIR / "src" / "assets" / "tokenizer"

# Device configuration
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load model and tokenizer
def load_model():
    model = BartForConditionalGeneration.from_pretrained(MODEL_PATH)
    model.to(DEVICE)
    return model

def load_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
    return tokenizer

# Model parameters
MAX_INPUT_LENGTH = 1024
MAX_TARGET_LENGTH = 130
MIN_TARGET_LENGTH = 30