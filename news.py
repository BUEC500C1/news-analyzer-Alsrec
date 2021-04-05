import feedparser
from flask import Flask
app = Flask(__name__)
FEED_URL= "https://news.yahoo.com/rss/mostviewed"
@app.route("/")
def print_news():
	feed = feedparser.parse(FEED_URL)
	article = feed['enteries'][0]

	return """<html>
		<body>
			<h1>Yahoo News</h1>
			<b>{0}</b><br/>
			<p>{1}</p><br/>
		</body>
		</html>""".format(article.get("title"), article.get("description"))

if __name__ == '__main__':
	app.run()