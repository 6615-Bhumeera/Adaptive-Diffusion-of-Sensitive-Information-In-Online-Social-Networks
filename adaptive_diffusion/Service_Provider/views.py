
from django.db.models import  Count, Avg
from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Count,Subquery
from django.db.models import Q
import datetime


# Create your views here.
from Remote_User.models import adaptive_diffusion_model,ClientRegister_Model,review_Model,recommend_Model,tweet_accuracy_model


def serviceproviderlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "SProvider" and password =="SProvider":
            tweet_accuracy_model.objects.all().delete()
            return redirect('View_Remote_Users')

    return render(request,'SProvider/serviceproviderlogin.html')


def viewtreandingquestions(request,chart_type):
    dd = {}
    pos,neu,neg =0,0,0
    poss=None
    topic = adaptive_diffusion_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics=t['ratings']
        pos_count=adaptive_diffusion_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss=pos_count
        for pp in pos_count:
            senti= pp['names']
            if senti == 'positive':
                pos= pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics]=[pos,neg,neu]
    return render(request,'SProvider/viewtreandingquestions.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def Search_Tweet(request): # Search
    if request.method == "POST":
        kword = request.POST.get('keyword')
        obj = adaptive_diffusion_model.objects.all().filter(Q(uname__contains=kword) | Q(names__contains=kword))
        return render(request, 'SProvider/Search_Tweet.html',{'objs': obj})
    return render(request, 'SProvider/Search_Tweet.html')

def View_Sensitive_Info(request): # Using SVM

    if request.method == "POST":
        atype = 'Sensitive'
        f1 = 'slum'
        f2 = 'low'
        f3 = 'poor'
        f4 = 'kill'
        f5 = 'caste'
        f6 = 'fuck'
        f7 = 'booms'
        obj = adaptive_diffusion_model.objects.all().filter(
            Q(retweet__contains=f1) | Q(retweet__contains=f2) | Q(retweet__contains=f3) | Q(retweet__contains=f4) | Q(
                retweet__contains=f5) | Q(retweet__contains=f6) | Q(retweet__contains=f7)).delete()

        return render(request, 'SProvider/Search_Tweet.html', {'objs': obj})

    atype='Sensitive'

    f1 = 'slum'
    f2 = 'low'
    f3 = 'poor'
    f4 = 'kill'
    f5 = 'caste'
    f6 = 'fuck'
    f7 = 'booms'
    obj = adaptive_diffusion_model.objects.all().filter(
        Q(retweet__contains=f1) | Q(retweet__contains=f2) | Q(retweet__contains=f3) | Q(retweet__contains=f4) | Q(
            retweet__contains=f5) | Q(retweet__contains=f6) | Q(retweet__contains=f7))
    obj1 = adaptive_diffusion_model.objects.all()
    count = obj.count()
    count1 = obj1.count()
    accuracy = count / count1
    if accuracy != 0:
        tweet_accuracy_model.objects.create(names=atype, accuracy=accuracy)
    return render(request, 'SProvider/View_Sensitive_Info.html', {'objs': obj,'count':accuracy})


def View_Positive_Info(request): # Positive # Using SVM
    atype = 'Positve'
    f1 = 'good'
    f2 = 'beautiful'
    f3 = 'fantastic'
    f4 = 'extraordinary'
    f5 = 'best'
    f6 = 'healthy'
    f7 = 'happy'
    f8 = 'marvel'
    f9 = 'worth'
    f10 = 'value'
    f11 = 'amazing'
    obj = adaptive_diffusion_model.objects.all().filter(Q(retweet__contains=f1) | Q(retweet__contains=f2) | Q(retweet__contains=f3) | Q(retweet__contains=f4) | Q(retweet__contains=f5) | Q(retweet__contains=f6) | Q(retweet__contains=f7)| Q(retweet__contains=f8)| Q(retweet__contains=f9)| Q(retweet__contains=f10)| Q(retweet__contains=f11))
    obj1 = adaptive_diffusion_model.objects.all()
    count = obj.count()
    count1 = obj1.count()
    accuracy = count / count1
    if accuracy != 0:
        tweet_accuracy_model.objects.create(names=atype,accuracy=accuracy)
    return render(request, 'SProvider/View_Positive_Info.html', {'objs': obj,'count':accuracy})


def View_Remote_Users(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'SProvider/View_Remote_Users.html',{'objects':obj})

def ViewTrendings(request):
    topic = adaptive_diffusion_model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return  render(request,'SProvider/ViewTrendings.html',{'objects':topic})

def negativechart(request,chart_type):
    dd = {}
    pos, neu, neg = 0, 0, 0
    poss = None
    topic = adaptive_diffusion_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics = t['ratings']
        pos_count = adaptive_diffusion_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss = pos_count
        for pp in pos_count:
            senti = pp['names']
            if senti == 'positive':
                pos = pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics] = [pos, neg, neu]
    return render(request,'SProvider/negativechart.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def charts(request,chart_type):
    chart1 = tweet_accuracy_model.objects.values('names').annotate(dcount=Avg('accuracy'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def View_TweetDataSets_Details(request):
    obj = adaptive_diffusion_model.objects.all()
    return render(request, 'SProvider/View_TweetDataSets_Details.html', {'list_objects': obj})

def View_Negative_Info(request):
    atype = 'Negative'
    f1 = 'bad'
    f2 = 'worst'
    f3 = 'heavy'
    f4 = 'ridicules'
    f5 = 'sad'
    f6 = 'damn'
    f7 = 'shameful'
    f8 = 'failed'
    f9 = 'dangerous'
    f10 = 'waste'
    f11 = 'diseased'
    obj = adaptive_diffusion_model.objects.all().filter(
        Q(retweet__contains=f1) | Q(retweet__contains=f2) | Q(retweet__contains=f3) | Q(retweet__contains=f4) | Q(
            retweet__contains=f5) | Q(retweet__contains=f6) | Q(retweet__contains=f7) | Q(retweet__contains=f8) | Q(
            retweet__contains=f9) | Q(retweet__contains=f10) | Q(retweet__contains=f11))
    obj1 = adaptive_diffusion_model.objects.all()
    count = obj.count()
    count1 = obj1.count()
    accuracy = count / count1
    if accuracy != 0:
        tweet_accuracy_model.objects.create(names=atype, accuracy=accuracy)
    return render(request, 'SProvider/View_Negative_Info.html', {'objs': obj,'count':accuracy})

def likeschart(request,like_chart):
    charts = adaptive_diffusion_model.objects.values('names').annotate(dcount=Avg('score'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})
