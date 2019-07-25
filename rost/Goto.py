import time
import vk
#import requests
#import json
#from datetime import datetime
#from pyrogram import Client

try:
    #fi = open('data.p', 'rb')
    #fo = open('data.p', 'wb')
    #data_l = pickle.load(fi)
    api = vk.API(session = vk.Session(access_token = 'a0fda04c8caf87e28f5f2d16bd917f5b9d3e788383d080af6b2d004ca521a1cd9cf9881b1dcafccc17d5e'))
    #result = requests.get('http://92.222.159.126:9191/api/get/achievements')
    #data = json.loads(result.text)
    #print(data)
    data = {'list': {'vk': ['agim3', 520379262, 3], 'tg': ['fathutnik', 'Pastryobsessed']}}
    l = data['list']
    #time.sleep(600 - (time.time() % 600))
    #while True:
    t = time.time() - 600
    ids = ''
    for i in l['vk']:
        ids += str(i) + ', '
    a = api.users.get(user_ids = ids[:-2], fields = 'online, last_seen', v = '5.92')
    ans = {'sleep': [], 'not_sleep': []}
    for i in range(len(a)):
        if a[i]['online'] == 1 or a[i].get('last_seen', {'time': 0})['time'] > t:
            ans['not_sleep'].append(data['list']['vk'][i])
            #data_l[...]['v'].append(data['id'])
        else:
            ans['sleep'].append(data['list']['vk'][i])
#--
    #app = Client(
    #    'my_account',
    #    api_id=123456,  # your api_id
    #    api_hash='your_hasn'
    #)
    #for _ in range(3):
    #    with app:
    #        members = [m for m in l['tg']]
    #        for member in members:
    #            user = member.user
    #            if user.is_bot:
    #                continue
    #            last_active = (user.status.date - 3 * 3600) % 86400
    #            if last_active > t:
    #                #data_l[...]['t'].append(data['id'])
    #                app.send_message('danil118312', '@' + user.username + ' не спит в Телеграмме')
#--
    for i in ans['not_sleep']:
        if str(i).isdigit():
            api.messages.send(domain='agim3', message = '*id' + str(i) + ' не спит в ВК', random_id = 0, v='5.92')
    #        app.send_message('danil118312', 'vk.com/id' + i + ' не спит в ВК')
        else:
            api.messages.send(domain='agim3', message = '@' + i + ' не спит в ВК', random_id = 0, v='5.92')
    #        app.send_message('danil118312', 'vk.com/' + i + ' не спит в ВК')
    #time.sleep(600 - (time.time() % 600))  # пока что ждем обновлений три минуты
#t = time.time() - 600
#a = api.users.get(user_ids = ids[:-2], fields = 'online, last_seen', v = '5.92')
#for i in range(len(a)):
#    if a[i]['online'] == 1 or a[i].get('last_seen', {'time': 0})['time'] > t:
#        requests.get('http://92.222.159.126:9191/api/add?access_key=2749f9f89wf9wyf9sufw9uf&user_id=007&ach_id=3')
except:
    0/0
    #return PermissionDenied