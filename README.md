python
======

Python code for tweet classifications

This program helps to determine whether a tweet has video, image or other content link in it.
This program comes handy for clustering disaster related tweets according to the content type of the link communicated
with the tweet content. This progam may work with a standalone tweet crawler or on already collected tweets.

Input: this program takes a tab separated vector file; tweets.tsv as input. tweets.tsv file contains all crawled tweets

Output: this produces output.tsv file as output which contains only tweets from the input that contains link in it and
further the relevant categories (Video, Image  or Others) for those tweets. These categories are derived based on the
domains of the shared link in a tweet. 
