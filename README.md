# Information

Feel free to create pull requests to add words clouds.

To create a visualization :

1.  Get the words
2.  Preprocess the image using [a graphical tool](https://www.gimp.org/) to create a mask.
    -   Black: Word cloud space
    -   White: Kept as is from the image
    -   Grey value: Discarded from the visualization
3.  From this mask and the words, the script uses [nltk](https://www.nltk.org/) to remove stop words, [wordcloud](https://pypi.org/project/wordcloud/) to create a visualization and a bit of [numpy](https://numpy.org/) image math's.

# List

1.  [Apple App Store](#apple-app-store)

## Apple App Store

![](wordclouds/appstore.png)

Data used:

-   https://www.kaggle.com/sophiahill/all-apps-from-itunes-wesbite/version/1
-   https://en.wikipedia.org/wiki/App_Store_(iOS/iPadOS)#/media/File:App_Store_(iOS).svg

Reddit posts: [r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/comments/pfve1w/oc_apple_app_store_most_common_app_words/)
