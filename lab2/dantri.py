# 1.download webpage
# dung urllib

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://dantri.com.vn/"

#1.1 CONNECT to website  / open a connection
conn = urlopen(url)

# 1.2 download raw data
raw_data = conn.read()

#1.3 decode data
webpage_text = raw_data.decode("utf-8")

#print(len(webpage_text))

# 1.4 save text
# w => write
# b-> binary
# f = open("dantri.html", "wb")
# f.write(raw_data)
# f.close()

#2. EXTRACT ROI
# 2.1 convert text to soup
soup = BeautifulSoup(webpage_text, "html.parser")
ul = soup.find("ul", "ul1 ulnew") # id = "ul1 ulnew"

li_list = ul.find_all("li")
# for li in li_list:
#     print(li.prettify())
#     print("*******")
news_list = []
for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a["href"]
    # print(link)
    # print(title)
    news = {
        "Title" : title,
        "Link" : link,
    }
    news_list.append(news)
    #print("*" * 20)
print(*news_list, sep="\n *******\n")
#print(ul.prettify())
#print(soup.prettify())


# 3 EXTRACT DATA




# 4 . SAVE DATA
#"dantri.xlsx"