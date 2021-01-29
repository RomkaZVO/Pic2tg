import os
import requests
import random
import json
from datetime import datetime

config = {}
with open('config.json', 'r') as f:
	config = json.load(f)

#setpicdir
picdir = config['picdir']

archive_path = '%s/%s' % (picdir, 'tg.txt')
log = os.path.exists(archive_path)
if log == False:
	print('Posted-log in %s' % (archive_path))
	f=open(archive_path,"w")
	f.close()

posted = open(archive_path).read()

pictures = os.listdir(picdir)
for pics in pictures:
    if pics.lower().endswith(('.png', '.jpg', '.jpeg')):
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
#set message 
#cheking only hour without minutes
time = datetime.now()
if time.hour == 24: 
	caption = random.choice(config['caption_night'])
elif time.hour == 10:
    caption = random.choice(config['caption_morning'])
else:
	caption = random.choice(config['caption_default'])
    
#post				    
url = "https://api.telegram.org/bot{}/sendPhoto".format(config['token'])
files = {'photo': open(pic_path, 'rb')}
data = {'chat_id' : config['channel_name'], 'caption': caption}
r = requests.post(url, files=files, data=data)