#import os
#
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Goto.settings")

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.append('/home/Danil118312/Goto/Goto')

from rost.models import Time, Online
from django.shortcuts import render
import time
import vk
#import requests
import json
#from datetime import datetime
#from pyrogram import Client as tg
try:
    api = vk.API(session = vk.Session(access_token = 'a0fda04c8caf87e28f5f2d16bd917f5b9d3e788383d080af6b2d004ca521a1cd9cf9881b1dcafccc17d5e'))
    data = {'list': {'vk': ['agim3', 520379262, 3], 'tg': ['fathutnik', 'danil118312']}}
    l = data['list']
    while True:
        print('sleep')
        time.sleep(600 - (time.time() % 600))
        print('wake_up')
        time = Time()
        t = time.time() - 600
        ids = ''
        for i in l['vk']:
            ids += str(i) + ', '
        a = api.users.get(user_ids = ids[:-2], fields = 'online, last_seen', v = '5.92')
        ans = []
        for i in range(len(a)):
            if a[i]['online'] == 1 or a[i].get('last_seen', {'time': 0})['time'] > t:
                user = Online(time = time, vk = True,
                    user = 0) #id)
                user.save()
                ans.append(data['list']['vk'][i])
#--
        #teg = tg(
        #'roctbb228_420',
        #api_id='864763',# your api_id
        #api_hash='68f9b8c6306c86b0f1359b75f56e88ea'
        #)

        #members = [m for m in teg.iter_chat_members(
        #'fathutnik123')]
        #for member in members:
        #    user = member.user
        #    if user.is_bot:
        #        continue
        #    last_active = (user.status.date - 3 * 3600) % 86400
        #    if last_active > t:
        #        #data_l[...]['t'].append(data['id'])
        #        teg.send_message('danil118312', '@' + user.username + ' не спит в Телеграмме')
#--
        print(*ans)
        for i in ans:
            if str(i).isdigit():
                api.messages.send(domain='agim3', message = '*id' + str(i) + ' не спит в ВК', random_id = 0, v='5.92')
    #            teg.send_message('danil118312', 'vk.com/id' + i + ' не спит в ВК')
            else:
                api.messages.send(domain='agim3', message = '@' + i + ' не спит в ВК', random_id = 0, v='5.92')
    #            teg.send_message('danil118312', 'vk.com/' + i + ' не спит в ВК')
        0/0
except:
    pass