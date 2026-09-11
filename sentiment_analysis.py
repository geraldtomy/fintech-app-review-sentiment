import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv("fintech_reviews.csv")

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    scores = analyzer.polarity_scores(str(text))
    return scores['compound']

df["sentiment"] = df["content"].apply(get_sentiment)

print(df[["app", "score", "content", "sentiment"]].head(10))

print("\nAverage sentiment by app:")
print(df.groupby("app")["sentiment"].mean())

df.to_csv("fintech_reviews_scored.csv", index=False)
print("\nSaved scored data to fintech_reviews_scored.csv")