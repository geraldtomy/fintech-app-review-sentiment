from google_play_scraper import reviews, Sort
import pandas as pd

def fetch_app_reviews(app_id, app_name, target_count=500):
    all_reviews = []
    continuation_token = None

    while len(all_reviews) < target_count:
        result, continuation_token = reviews(
            app_id,
            lang='en',
            country='de',
            sort=Sort.NEWEST,
            count=100,
            continuation_token=continuation_token
        )
        all_reviews.extend(result)
        print(f"{app_name}: collected {len(all_reviews)} so far...")
        if continuation_token is None:
            break

    df = pd.DataFrame(all_reviews)
    df = df[["reviewId", "userName", "score", "at", "content"]]
    df["app"] = app_name
    return df

n26_df = fetch_app_reviews('de.number26.android', 'N26')
revolut_df = fetch_app_reviews('com.revolut.revolut', 'Revolut')

combined = pd.concat([n26_df, revolut_df], ignore_index=True)
combined.to_csv("fintech_reviews.csv", index=False)
print(f"Saved {len(combined)} total reviews to fintech_reviews.csv")