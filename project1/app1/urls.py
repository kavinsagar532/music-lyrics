from django.urls import path
from . import views
urlpatterns=[
    path('homepage/',views.homepage,name='homepage'),
    path('homepage/first.html/',views.first,name='first'),
    path('homepage/login.html/',views.login,name='login'),
    path('homepage/login.html/homepage.html',views.homepage,name='homepage'),
    path('homepage/login.html/signup.html/',views.signup,name='signup'),
    path('homepage/signup.html/',views.signup,name='signup'),
    path('homepage/signup.html/login.html/',views.login,name='login'),
    path('homepage/first.html/english_songs.html/',views.english_songs,name='english_songs'),
    path('homepage/first.html/english_songs.html/shape_of_you.html',views.shape_of_you,name='shape_of_you'),
    path('homepage/first.html/english_songs.html/dandelions.html',views.dandelions,name='dandelions'),
    path('homepage/first.html/english_songs.html/believer.html',views.believer,name='believer'),
    path('homepage/first.html/english_songs.html/perfect.html',views.perfect,name='pefect'),
    path('homepage/first.html/english_songs.html/love_me_like_you_do.html',views.love_me_like_you_do,name='love_me_like_you_do'),
    path('homepage/first.html/tamil_songs.html/',views.tamil_songs,name='tamil_songs'),
    path('homepage/first.html/tamil_songs.html/hukum.html',views.hukum,name='hukum'),
    path('homepage/first.html/tamil_songs.html/nira.html',views.nira,name='nira'),
    path('homepage/first.html/tamil_songs.html/naa_ready.html',views.naa_ready,name='naa_ready'),
    path('homepage/first.html/tamil_songs.html/naan_gaali.html',views.naan_gaali,name='naan_gaali'),
    path('homepage/first.html/tamil_songs.html/aval.html',views.aval,name='aval'),
    path('homepage/first.html/lyrics.html',views.lyrics,name='lyrics'),

]