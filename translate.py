from transformers import MarianMTModel, MarianTokenizer

# Pretrained multilingual to English model
model_name = "Helsinki-NLP/opus-mt-mul-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_text(text):
    inputs = tokenizer([text], return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

def translate_kv_pairs(kv_pairs):
    return {translate_text(k): translate_text(v) for k, v in kv_pairs.items()}
