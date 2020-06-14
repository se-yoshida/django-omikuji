from django.shortcuts import render
import random   # randomをインポート


# Create your views here.
def index(request):
    return render(request, 'omikuji/index.html')


def result(request):
    l = ('大吉', '中吉', '小吉', '凶', '大凶')
    fortun = random.choice(l)
    # 運勢の情報を格納
    context = {
        'omikuji': fortun
    }
    return render(request, 'omikuji/result.html', context)  # contextの情報をテンプレートに送る
