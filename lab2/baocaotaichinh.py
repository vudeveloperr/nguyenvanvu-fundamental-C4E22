from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/1/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)

raw_data = conn.read()

webpage_text = raw_data.decode("utf-8")
# f = open("baocaotaichinh.html", "wb")
# f.write(raw_data)
# f.close()


soup = BeautifulSoup(webpage_text, "html.parser")
tbody = soup.find("table",id = "tblGridData") # id = "tblGridData"
td_list = tbody.find_all("td")
for td in td_list:
    print(td.prettify())
    print("*******************************")

sbody = soup.find("table",id="tableContent")
sd_list = sbody.find_all("tr")
# for tr in sd_list:
#     print(tr.prettify)
#     print("**********************************")    

for tr in sd_list:
    td = tr.td
    print(td)

    
    

pyexcel.save_as(records=news_list, dest_file_name="bao_cao_tai_chinh.xlsx")