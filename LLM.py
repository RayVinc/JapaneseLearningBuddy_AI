from transformers import BertModel, BertTokenizer

model_name = "cl-tohoku/bert-base-japanese-char-v3"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)
