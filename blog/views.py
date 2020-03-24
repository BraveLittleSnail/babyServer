from django.shortcuts import render
import json
import requests
from django.conf import settings

# Create your views here.
from django.http import HttpResponse
from .models import Article

def hello(request):
    a = 1+1
    print(a)
    return HttpResponse('Hello World`')


def articlelist(request):
    #获取文章的id、作者、标题、正文
    # article_title = Article.objects.all().values('article_title')
    # body = Article.objects.all().values('body')

    # titles = []
    # bodys = []
    # for title in article_title:
    #     temp = title['article_title']
    #     titles.append(temp)
    # for one in body:
    #     temp = one['body']
    #     bodys.append(temp)
    #=================================供小程序测试使用，以后再设计服务器======================================
    titles = []
    titles.append("防水能救股市吗")
    titles.append("我有一个乖宝宝")
    images = ["a/img.jpg","b/img.jpg"]
    bodys = ["这标题是想通俗一点，比较专业的说法应该是：流动性泛滥能拯救由流动性泛滥造成的恶果吗？\
我三年前开始谈美国股市，预测2019±1年是美股拐点，跌幅50%以上，现在到了检验的时候。\
我不是巫师，预测的依据几年来一直在讲，最近也连续发文在讲。昨天讲《暴跌的逻辑：恐怕不只是金融危机》，转到推上，导致我推号被封杀。足见美国所谓言论自由有多么虚伪，也足见美国现在有多么恐慌，连我这个小人物的一篇短文都不敢让人看下去。逗逗们别再吹捧“你们的”美国了，我越来越鄙视。\
下面我接着讲美股为什么一定会崩盘，而且跌幅会在50%以上。\
标题就是我要讲的核心观点，还可以换个更通俗的说法，泡沫能拯救泡沫破灭吗？\
抛开美国经济政策失误和经济危机的大背景不讲，最近的美股暴跌也绝不是流动性不足所致。恰恰相反，是多年来流动性泛滥的恶果。以新的流动性泛滥去拯救已经由流动性泛滥造成的恶果，你认为会有效果吗？\
也许有，但一定不是救市的效果，而是把股市进一步推向万丈深渊的效果。","天天是我的乖宝宝"]
    result = {"images":images,"titles":titles, "bodys": bodys}

    list = []
    image = "a/img.jpg"
    title = "我有一个乖宝宝"
    body = "天天是我的乖宝宝"
    article = {"image":image,"title":title, "body": body}
    list.append(article)
    image2 = "b/img.jpg"
    title2 = "防水能救股市吗"
    body2 = "这标题是想通俗一点，比较专业的说法应该是：流动性泛滥能拯救由流动性泛滥造成的恶果吗？\
我三年前开始谈美国股市，预测2019±1年是美股拐点，跌幅50%以上，现在到了检验的时候。\
我不是巫师，预测的依据几年来一直在讲，最近也连续发文在讲。昨天讲《暴跌的逻辑：恐怕不只是金融危机》，转到推上，导致我推号被封杀。足见美国所谓言论自由有多么虚伪，也足见美国现在有多么恐慌，连我这个小人物的一篇短文都不敢让人看下去。逗逗们别再吹捧“你们的”美国了，我越来越鄙视。\
下面我接着讲美股为什么一定会崩盘，而且跌幅会在50%以上。\
标题就是我要讲的核心观点，还可以换个更通俗的说法，泡沫能拯救泡沫破灭吗？\
抛开美国经济政策失误和经济危机的大背景不讲，最近的美股暴跌也绝不是流动性不足所致。恰恰相反，是多年来流动性泛滥的恶果。以新的流动性泛滥去拯救已经由流动性泛滥造成的恶果，你认为会有效果吗？\
也许有，但一定不是救市的效果，而是把股市进一步推向万丈深渊的效果。"
    article = {"image":image2,"title":title2, "body": body2}
    list.append(article)
    return HttpResponse(json.dumps(list,ensure_ascii=False), content_type="application/json")

code2Session="https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code"
def onLogin(request):
    code = request.GET['code']
    id = "wxbde504f716614870"
    AppSecret="7a05e044494bb754264b4a677753f9fa"
    #response = requests.get(settings.code2Session.format(settings.AppId,settings.AppSecret,code))
    response = requests.get(code2Session.format(id,AppSecret,code))
    data = response.json()
    if data.get("openid"):
        return data
    else:
        return False
    return HttpResponse('Hello onLogin`')


def get_user_info(js_code):
    req_params = {
        "appid": 'app_id',  # 小程序的 ID
        "secret": 'secret',  # 小程序的 secret
        "js_code": js_code,
        "grant_type": 'authorization_code'
    }
    req_result = requests.get('https://api.weixin.qq.com/sns/jscode2session', 
                              params=req_params, timeout=3, verify=False)
    return req_result.json()