from transformers import pipeline

model = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)

result = model("Explain this code: print('Hello World')", max_length=100)
print(result)
