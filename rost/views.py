from django.http import HttpResponse
from rost.models import Time, Online
from django.shortcuts import render
import time
import vk
import json
from pyrogram import Client

def api(request):
    result = json.loads(request.GET['data'])
    ids = ''
    has_vk = list(filter(lambda x:x['vk_id']!='', result))
    has_tg = list(filter(lambda x:x['tg_id']!='', result))
    tg_ids = []
    for i in has_tg:
        tg_ids.append(i['tg_id'])
    for i in has_vk:
        ids += str(i['vk_id']) + ', '
    api = vk.API(session = vk.Session(access_token = 'a0fda04c8caf87e28f5f2d16bd917f5b9d3e788383d080af6b2d004ca521a1cd9cf9881b1dcafccc17d5e'))

    app = Client(
        'roctbb228bot',
        api_id=864763,  # your api_id
        api_hash='68f9b8c6306c86b0f1359b75f56e88ea',
        proxy=dict(
            hostname="t.geekclass.ru",
            port=7777,
            username="geek",
            password="socks"
        )
    )
    return HttpResponse(ids)
    m = Time()
    m.save()
    t = time.time() - 600
    a = api.users.get(user_ids = ids[:-2], fields = 'online, last_seen', v = '5.92')
    ans = []
    for i in range(len(a)):
        if a[i]['online'] == 1 or a[i].get('last_seen', {'time': 0})['time'] > t:
            ans.append(has_vk[i]['id'])
            u = Online(time = m, vk = True, id = has_vk[i]['id'])
            u.save()
            api.messages.send(domain='agim3', message = '{}{}, {} домик, не спит в ВК'.format('*id' if str(has_vk[i]['vk_id']).isdigit() else '@', has_vk[i]['vk_id'], has_vk[i]['home_number'] if has_vk[i]['home_number'] != '' else 'n'), random_id = 0, v='5.92')
            #app.send_message('fatnikita', 'vk.com/{}{}, {} домик, не спит в ВК'.format('id' if str(has_vk[i]['vk_id']).isdigit() else '', has_vk[i]['vk_id'], has_vk[i]['home_number'] if has_vk[i]['home_number'] != '' else 'n'))

    #with app:
    #    members = [m for m in app.iter_chat_members(
    #        '-207970256')]
    #    for member in members:
    #        user = member.user
    #        if not user.is_bot and user.status.date > t:
    #            #if user.username in tg_ids:
    #            #    if u.id = has_tg:
    #            #        u.tg = True
    #            #    else:
    #            #        u2 = Online(time = m, vk = True, id = has_tg)
    #            #api.messages.send(domain='agim3', message = '@{} не спит в TG'.format(user.username), random_id = 0, v='5.92')
    #            #app.send_message('fatnikita', '@' + user.username + ' не спит в TG')

    return HttpResponse(json.dumps(ans))

def api1(request):
    a = api.users.get(user_ids = request.GET['id'], fields = 'online, last_seen', v = '5.92')
    for i in range(len(a)):
        if a[i]['online'] == 1:
            return HttpResponse('{"online":true}')
        else:
            return HttpResponse('{"online":false,"last_seen":'+a[i]['last_seen']+'}')