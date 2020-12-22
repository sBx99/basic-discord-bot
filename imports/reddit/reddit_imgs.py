# function to create dataframe of posts and to scrape image urls from reddit
import urllib.parse
import pandas as pd
from praw import Reddit

def img_urls(sub_name, CLIENT_ID, CLIENT_SECRET, USER_AGENT):
    reddit = Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT)

    collected_posts = []
    sub = reddit.subreddit(str(sub_name))

    for post in sub.hot(limit=100):
        collected_posts.append([post.url])

    posts = pd.DataFrame(
        collected_posts, columns=['url'])

    image_urls = [x for x in posts.url if x.endswith(('jpg', 'jpeg', 'png'))]

    return image_urls

'''
# to test
sub_name = 'meirl'
REDDIT_CLIENT_ID = '_23RxiP8dTlZTA'
REDDIT_CLIENT_SECRET = 'jUEAw7Nz4Wl-PZDF9nswTKGyaa9ZTg'
REDDIT_USER_AGENT = 'MemeTextScraper'
imgs = img_urls(sub_name, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT)
print(imgs[:5])
'''