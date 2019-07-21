from django.shortcuts import render, redirect
data = [('автомобиль', 'https://media.tenor.com/images/2ba0b58392a86f3e3ecf9ad9fb9f4bca/tenor.gif'), ('ничего', 'https://s.androidinsider.ru/2017/10/Nothing.@750.jpg'), ('0 рублей', 'https://www.mtv.ru/upload/medialibrary/f30/f30331b9cc9f9e5e08b4b315fa2492ce.jpg'), ('квартиру', 'https://schasliviy.dp.ua/wp-content/uploads/2016/03/%D0%BA%D0%BB%D1%8E%D1%87%D0%B8-%D0%BE%D1%82-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%8B.png'), ('INF денег', 'https://avatars.mds.yandex.net/get-zen_doc/1368767/pub_5cd3190fc9c89500afe8fabe_5cd31a85ac5cc400b322f2f4/scale_2400')]

from myapp.models import Poem, Abzac

import random

def alisa0(request):
    if request.method == 'GET':
        return render(request, 'alisa0.html')
    else:
        poem = Poem()
        poem.name = request.POST['name']
        poem.text = request.POST['text']
        abzac = Abzac()
        abzac.text = poem.text
        abzac.people = request.POST['people']
        poem.save()
        abzac.poem_id = poem.id
        abzac.save()
        return redirect('/alisa/write')

def alisa(request):
    if request.method == 'GET':
        poems = list(Poem.objects.filter(ended = False))
        if len(poems) == 0:
            return redirect('/alisa/new')
        return render(request, 'alisa4.html', {'list': poems})
    elif request.POST['button'] == 'get':
        poem = Poem.objects.get(id = request.POST['id'])
        return render(request, 'alisa.html', {'poem': poem.text, 'id': poem.id, 'name': poem.name})
    else:
        abzac = Abzac()
        abzac.text = request.POST['text']
        abzac.people = request.POST['name']
        abzac.poem_id = request.POST['id']
        abzac.save()
        poem = Poem.objects.get(pk=request.POST['id'])
        poem.text = abzac.text
        if request.POST['button'] == 'end':
            poem.ended = True
            poem.save()
            return redirect('/alisa/read')
        else:
            poem.save()
            return render(request, 'alisa.html', {'poem': poem.text, 'id': poem.id, 'name': poem.name})

def alisa2(request):
    if request.method == 'GET' or not request.POST['button'] == 'go':
        poems = list(Poem.objects.filter(ended = True))
        return render(request, 'alisa3.html', {'list': poems})
    else:
        poem = Poem.objects.get(id = request.POST['id'])
        abzacs = list(Abzac.objects.filter(poem=poem.id))
        return render(request, 'alisa2.html', {'list': abzacs, 'name': poem.name})

def win(request):
    if request.method == 'GET':
        r = random.choice(data)
        return render(request, 'index.html', {'prize': r[0], 'image': r[1]})
    else:
        name = request.POST['name']
        prize = request.POST['prize']
        image = request.POST['image']
        out = open('out.txt', 'a')
        out.write(name+' '+prize+'\n')
        out.close()
        if name == '':
            return render(request, 'index.html', {'prize': prize, 'image': image})
        else:
            return render(request, 'index2.html', {'prize': prize, 'name': name})