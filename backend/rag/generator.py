import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class LLMGenerator:
    """Lightweight LLM for answer generation."""

    def __init__(self, model_name: str = "google/flan-t5-xl"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def generate_answer(self, query: str, context: str) -> str:
        prompt = f"""
You are a helpful campus assistant.
Using ONLY the information provided in the context,
write a complete, well-formed answer in natural language.
If the answer is not present, say:
"The information is not available in the provided college data."

Context:
{context}

Question:
{query}

Answer:
"""

        inputs = self.tokenizer(
            prompt,
            max_length=512,
            truncation=True,
            return_tensors="pt"
        ).to(self.device)

        outputs = self.model.generate(
            **inputs,
            max_length=200,
            min_length=40,
            num_beams=4,
            repetition_penalty=1.2,
            no_repeat_ngram_size=3,
            early_stopping=True
        )

        return self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        ).strip()