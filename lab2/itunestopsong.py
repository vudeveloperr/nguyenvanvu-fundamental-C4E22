# 1.download webpage
from youtube_dl import YoutubeDL
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://www.apple.com/itunes/charts/songs/"

#1.1 CONNECT to website  / open a connection
conn = urlopen(url)

# 1.2 download raw data
raw_data = conn.read()

#1.3 decode data
webpage_text = raw_data.decode("utf-8")

#print(len(webpage_text))

# 1.4 save text

# f = open("itunestopsong.html", "wb")
# f.write(raw_data)
# f.close()

#2. EXTRACT ROI
# 2.1 convert text to soup
soup = BeautifulSoup(webpage_text, "html.parser")
ul = soup.find("section","section chart-grid")

li_list = ul.find_all("li")
news_list = []
for li in li_list:
    a = li.h3.a
    namesong = a.string
    a = li.h4.a
    artists = a.string
    #link = url + a["href"]
    # print(artists)
    # print(namesong)
    news = {
        "name s'song" : namesong,
        "artists" : artists,
    }
    news_list.append(news)
print(*news_list, sep="\n *******\n")

options = {
    'default_search': 'ytsearch', 
    #'max_downloads': 1
}
dl = YoutubeDL(options)
dl.download(["name s'song"])



# 3 EXTRACT DATA




# 4 . SAVE DATA
#".xlsx"