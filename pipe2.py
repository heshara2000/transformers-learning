from transformers import pipeline
generator = pipeline("text-generation", model="distilgpt2")

res = generator(
    "in this course, we will teach you how to",
    max_length=50,
    num_return_sequences=2,
)

print(res)