from transformers import pipeline

# Initialize the summarizer (only once)
summarizer_pipeline = pipeline("summarization", model="t5-small")

def summarize_text(text, max_length=150, min_length=50):
    summary_outputs = summarizer_pipeline(
        text, 
        max_length=max_length, 
        min_length=min_length, 
        do_sample=False
    )
    summary = summary_outputs[0]['summary_text']
    return summary
