from gmail import GMail,Message
gmail = GMail('nguyenvanvu240499@gmail.com','ngvavu17150217')
#msg = Message(' Message',to='c4e.techkidsvn@gmail.com',text='hello')
html_template= '''
<b>hello</b>
<i>asdfgh</i>
<p><span style="text-decoration: underline;">ch&agrave;o sếp</span>&nbsp;</p>
<p>{{ symptom }}<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-sealed.gif" alt="sealed" /><em>ng&agrave;y mai</em> cho em <strong>xin nghỉ</strong></p>
<p>Nh&acirc;n Vi&ecirc;n</p>
'''
from random import choice
symptom_list = ['dau chan', 'dau tay', 'dau bung']
html_content = html_template.replace("{{ symptom }}",choice(symptom_list))
msg = Message(' Message',to='c4e.techkidsvn@gmail.com',html=html_content)
gmail.send(msg)

