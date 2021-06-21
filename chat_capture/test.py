from urllib.request import urlopen
from lxml.html import parse

youtube_url = 'https://www.youtube.com/watch?v='
url = youtube_url + 'J6XqykqWzbE'
page = urlopen(url)
p = parse(page)
print("".join(list(filter(lambda ch: ord(ch) > 0 and ord(ch) < 127, p.find(".//title").text.replace(" - YouTube", "")))))