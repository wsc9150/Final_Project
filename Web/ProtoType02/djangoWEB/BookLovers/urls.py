from BookLovers import views
from django.urls import path, include

urlpatterns = [
    path('index/', views.index, name="index"),

    path('index/category', views.category, name="category"),
    path('index/category_info', views.category_info, name="category_info"),
    path('index/book_info', views.book_info, name="book_info"),
    path('index/content_info', views.content_info, name="content_info"),
    path('index/popularity_info', views.popularity_info, name="popularity_info"),

    path('index/mbti', views.mbti, name="mbti"),
    path('index/exam2', views.exam2, name='exam2'),
    path('index/exam3', views.exam3, name='exam3'),
    path('index/exam4', views.exam4, name='exam4'),
    path('index/result', views.result, name='result'),
    path('index/otherBook', views.otherBook, name='otherBook'),

    path('index/healing', views.healing, name="healing"),
    path('index/keyword_info', views.keyword_info, name="keyword_info"),
]
