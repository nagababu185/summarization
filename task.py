from transformers import pipeline

# Load a summarization pipeline using a pre-trained model
summarizer = pipeline("summarization")

# Get user input
text = input("Paste a large paragraph to summarize:\n")

# Check if text is long enough
if len(text.split()) < 50:
    print("\nText is too short to summarize. Add more content.")
else:
    # Run summarization
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)

    print("\n--- Summary ---\n")
    print(summary[0]['summary_text'])