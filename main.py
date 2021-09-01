import nltk
from visualization import wordcloud_visualization

import appstore

if __name__ == '__main__':
    nltk.download("stopwords")
    nltk.download("punkt")

    wordcloud_visualization(appstore)
