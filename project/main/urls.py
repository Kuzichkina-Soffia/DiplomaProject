from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('articles', views.articles),

    path('reg', views.reg, name='registration'),
    path('log', views.log, name='login'),

    path('<int:id>/', views.userpage, name='userpage'),

    path('<int:id>/mychats', views.mychats, name='mychats'),
    path('<int:id>/myfriends', views.myfriends, name='myfriends'),
    path('<int:id>/mysubscribes', views.mysubscribes, name='mysubscribes'),
    path('<int:id>/myarticles', views.myarticles, name='myarticles'),
    path('<int:id>/mychannels', views.mychannels, name='mychannels'),
    path('delete_channel/<int:channel_id>', views.delete_channel, name='delete_channel'),
    path('<int:id>/news', views.news, name='news'),
    #mychats
    path('delete_article/<int:article_id>/', views.delete_article, name='delete_article'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    #myfriends
    path('<int:id>/add_friend/<int:friend_id>', views.add_friend, name='add_friend'),
    path('<int:id>/remove_friend/<int:friend_id>/', views.remove_friend, name='remove_friend'),
    #mychannels
    path('<int:id>/channel<int:channel_id>', views.mychannelpage, name='mychannelpage'),
    # path('delete_channel/<int:channel_id>', views.delete_channel, name='delete_channel'),
    # path('delete_channel/<int:channel_id>/', views.delete_channel, name='delete_channel'),

    path('<int:id>/chat_<str:people_username>', views.open_personal_chat, name='open_personal_chat'),

    path('<int:id>/<str:people_username>', views.peoplepage, name='people'),
]