
# anh Quân ơi bài này em làm nó toàn fail đoạn tự động gửi 



import psutil
import os
import subprocess
from gmail import GMail,Message
import datetime
from random import choice

now = datetime.datetime.now()
print("year now:",now.year,"\nmonth now:", now.month,"\nday now:", now.day,"\nhour now:", now.hour,"\nminute now:", now.minute,"\nsecond now:" ,now.second)




gmail = GMail('nguyenvanvu240499@gmail.com','ngvavu17150217')
#msg = Message(' Message',to='c4e.techkidsvn@gmail.com',text='hello')
html_template= '''
<p style="text-align: left;"><em>em ch&agrave;o sếp&nbsp;</em></p>
<p style="text-align: left;"><span style="text-decoration: underline;">sếp ơi</span> ! h&ocirc;m nay sếp cho em xin nghỉ v&igrave; em bị</p>{{ symptom }}
<p style="text-align: left;"><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-sealed.gif" alt="sealed" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-sealed.gif" alt="sealed" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-sealed.gif" alt="sealed" /></p>
<p style="text-align: left;"><strong>cảm ơn sếp&nbsp;</strong></p>
<p style="text-align: left;"><span style="color: #ff0000;">nh&acirc;n vi&ecirc;n&nbsp; bla bla</span></p>
'''




symptom_list = ['đau chân', 'đau tay', 'đau bụng', 'đau đầu', 'đau tim', 'ê mông', 'buồn ngủ']
html_content = html_template.replace("{{ symptom }}",choice(symptom_list))
msg = Message(' Message',to='vubaojr99@gmail.com',html=html_content)
gmail.send(msg)

import win32com.client as win32
def send_notification():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'nguyenvanvu240499@gmail.com; vubaojr99@gmail.com', 
    mail.Subject = 'Sent through Python'
    mail.body = 'This email alert is auto generated. Please do not respond.'
    mail.send

def open_outlook():
    try:
        subprocess.call(['C:\Program Files\Microsoft Office\Office15\Outlook.exe'])
        os.system("C:\Program Files\Microsoft Office\Office15\Outlook.exe")
    except:
        print("Outlook didn't open successfully")


for item in psutil.pids():
    p = psutil.Process(item)
    if p.name() == "OUTLOOK.EXE":
        flag = 1
        break
    else:
        flag = 0
 
if (flag == 1):
    send_notification()
else:
    open_outlook()
    send_notification()

   