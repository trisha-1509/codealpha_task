from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# FAQ Data
faqs = {
    "What is AI?": "AI stands for Artificial Intelligence.",
    "What is machine learning?": "Machine learning is a subset of AI.",
    "What is Python?": "Python is a programming language.",
    "What is data science?": "Data science involves analyzing data."
}

questions = list(faqs.keys())
answers = list(faqs.values())

# Convert text to vectors
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(questions)

print("FAQ Chatbot is ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chatbot: Bye 👋")
        break

    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, faq_vectors)
    
    best_match = similarity.argmax()
    print("Chatbot:", answers[best_match])
