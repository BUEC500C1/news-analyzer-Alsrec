import feedparser
import logging

def news():
	logging.info('Accessing News') #news feed ingester, through rss
	feed = feedparser.parse("http://rss.cnn.com/rss/cnn_topstories.rss")
	feed1 = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/World.xml")

	nlist = [feed, feed1]

	return nlist
