import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("fintech_reviews_scored.csv")

extra_stopwords = ['app', 'account', 'bank', 'money', 'n26', 'revolut', 'just', 'use', 'don', 'die']

for app_name in ["N26", "Revolut"]:
    negative = df[(df["app"] == app_name) & (df["sentiment"] < -0.3)]["content"].astype(str)
    
    vectorizer = CountVectorizer(stop_words=list(CountVectorizer(stop_words='english').get_stop_words()) + extra_stopwords, ngram_range=(2, 2), max_features=10)
    X = vectorizer.fit_transform(negative)
    freqs = X.sum(axis=0).A1
    words = vectorizer.get_feature_names_out()
    
    top_words = sorted(zip(words, freqs), key=lambda x: -x[1])
    
    print(f"\n--- Top complaint phrases: {app_name} ({len(negative)} negative reviews) ---")
    for word, freq in top_words:
        print(f"{word}: {freq}")