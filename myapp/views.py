from django.shortcuts import render
import random
data = [('автомобиль', 'https://media.tenor.com/images/2ba0b58392a86f3e3ecf9ad9fb9f4bca/tenor.gif'), ('ничего', 'https://s.androidinsider.ru/2017/10/Nothing.@750.jpg'), ('0 рублей', 'https://www.mtv.ru/upload/medialibrary/f30/f30331b9cc9f9e5e08b4b315fa2492ce.jpg'), ('квартиру', 'https://schasliviy.dp.ua/wp-content/uploads/2016/03/%D0%BA%D0%BB%D1%8E%D1%87%D0%B8-%D0%BE%D1%82-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%8B.png'), ('INF денег', 'https://avatars.mds.yandex.net/get-zen_doc/1368767/pub_5cd3190fc9c89500afe8fabe_5cd31a85ac5cc400b322f2f4/scale_2400')]

def alisa(request):
    return render(request, 'alisa.html')

def win(request):
    if request.method == 'GET':
        r = random.choice(data)
        return render(request, 'index.html', {'prize': r[0], 'image': r[1]})
    else:
        name = request.POST['name']
        prize = request.POST['prize']
        image = request.POST['image']
        out = open('rw', 'out.txt')
        out.write(name+' '+prize)
        out.close()
        if name == '':
            return render(request, 'index.html', {'prize': prize, 'image': image})
        else:
            return render(request, 'index2.html', {'prize': prize, 'name': name})