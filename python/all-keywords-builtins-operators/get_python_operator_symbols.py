#!/usr/bin/env python3
import urllib3
import re
from html.parser import HTMLParser

DOCS_URL="https://docs.python.org/3.4/library/operator.html"
TABLE_ID="mapping-operators-to-functions"
TABLE_REGEX=re.compile(r"<tbody[^>]*>(.+)</tbody>")

class MyHTMLParser(HTMLParser):
		def handle_data(self, data):
				try:
					self.data += data
				except:
					self.data = data
		def handle_endtag(self, tag):
				self.data += "\n"

def main():
	parser = MyHTMLParser()

	html_body = urllib3.PoolManager().request('GET', DOCS_URL).data.decode().partition(TABLE_ID)[2].replace("\n","")

	html_body = re.findall(TABLE_REGEX, html_body)[0]

	parser.feed(html_body)

	html_body = parser.data.split("\n\n")
	operator_symbols = set()
	for i in range(0, len(html_body), 3):
		operator_string = html_body[i].partition("\n")[2].replace("\n","").split(" ")
		if len(operator_string) == 3:
			operator_symbols.add(operator_string[1])

	operator_symbols.remove("is")
	operator_symbols.remove("in")
	return operator_symbols

if __name__ == "__main__":
	print(" ".join(main()))