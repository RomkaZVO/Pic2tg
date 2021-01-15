import os
import requests

token = ""
channel_name = ""

#setpicdir
picdir = os.getcwd()

archive_path = '%s/%s' % (picdir, 'tg.txt')
ismylogthere = os.path.exists(archive_path)
if ismylogthere == False:
	print('Posted-log in %s' % (archive_path))
	f=open(archive_path,"w")
	f.close()

posted = open(archive_path).read()

pictures = os.listdir(picdir)
for pics in pictures:
    if pics.lower().endswith(('.png', '.jpg', '.gif', '.mp4', '.jpe', '.jpeg')):
        if pics in posted:
            print('Picture already posted: %s' % (pics))
        else:
            print('Ready to post new picture: %s' % (pics))
            pic_path = '%s/%s' % (picdir, pics)
            f=open(archive_path,"a")
            f.write(pics)
            f.write('\n')
            f.close()
            break
#post				    
url = "https://api.telegram.org/bot{}/sendPhoto".format(token)
files = {'photo': open(pic_path, 'rb')}
data = {'chat_id' : channel_name}
r= requests.post(url, files=files, data=data)

