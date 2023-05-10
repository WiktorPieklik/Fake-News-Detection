from typing import List
from pathlib import Path
from os import walk
import json

import pandas as pd
from alive_progress import alive_bar


RAW_DIR = Path(__file__).parent.parent / "raw"
DS_DIR = RAW_DIR / "dataset"
DATASET_CSV = RAW_DIR / "dataset.csv"


def get_tweet_credentials(tweet: dict, id: int, is_fake: bool, replies_count: int = 0) -> dict:
    text = tweet["text"]
    verified = tweet["user"]["verified"]
    followers_count = tweet["user"]["followers_count"]
    reactions_count = tweet["favorite_count"]
    retweet_count = tweet["retweet_count"]
    source = tweet["source"]
    description = tweet["user"]["description"]

    return {
        "id": id,
        "followers_count": followers_count,
        "verified": verified,
        "reactions_count": reactions_count,
        "retweet_count": retweet_count,
        "text": text,
        "source": source,
        "description": description,
        "replies_count": replies_count,
        "fake": is_fake
    }


def gather_tweets(root: Path, files: List[str], is_fake: bool, dataset: dict, replies_count: int = 0) -> None:
    for file in files:
        if file.startswith('.'):
            continue
        tweet_path = root / file
        tweet_id = int(tweet_path.stem)
        with open(tweet_path, 'r') as raw_json:
            tweet = json.load(raw_json)
            credentials = get_tweet_credentials(
                tweet=tweet,
                id=tweet_id,
                is_fake=is_fake,
                replies_count=replies_count
            )
        dataset["id"].append(credentials["id"])
        dataset["followers_count"].append(credentials["followers_count"])
        dataset["verified"].append(credentials["verified"])
        dataset["reactions_count"].append(credentials["reactions_count"])
        dataset["retweet_count"].append(credentials["retweet_count"])
        dataset["text"].append(credentials["text"])
        dataset["source"].append(credentials["source"])
        dataset["description"].append(credentials["description"])
        dataset["replies_count"].append(credentials["replies_count"])
        dataset["fake"].append(credentials["fake"])


if __name__ == "__main__":
    dataset = {
        "id": [],
        "followers_count": [],
        "verified": [],
        "reactions_count": [],
        "retweet_count": [],
        "text": [],
        "source": [],
        "description": [],
        "replies_count": [],
        "fake": []
    }
    replies_count = 0
    with alive_bar(spinner='pulse') as bar:
        for root, dirs, files in walk(DS_DIR):
            if not files or dirs:
                continue
            is_fake = 'fake' in root
            root = Path(root)
            if root.stem == 'reactions':
                replies_count = len(files)
                gather_tweets(root=root, files=files, is_fake=is_fake, dataset=dataset)
            else:
                gather_tweets(root=root, files=files, replies_count=replies_count, is_fake=is_fake, dataset=dataset)
                replies_count = 0
            bar()
    df = pd.DataFrame.from_dict(dataset)
    df.to_csv(DATASET_CSV, index=False)
    print("Created dataset.csv")
