from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed


# Create your views here.

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') #쿼리셋 : select * from content_feed

        for feed in feed_list:
            print(feed.content)

        return render(request, "instagram/main.html", context=dict(feeds = feed_list)) 
        #CONTEXT DATA로 넣어줄때는 사전 형식으로 전달해줘야함.원래는 JSON이지만 호환가능

        


