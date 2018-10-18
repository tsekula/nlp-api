from textblob import TextBlob

wiki = TextBlob("Jeff Bezos ignites interest in London apartments.")

print(wiki.tags)