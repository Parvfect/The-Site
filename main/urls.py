from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.views.generic import TemplateView
from .models import Story

app_name = 'main' #namespacing urls


urlpatterns = [
    path('', views.start, name = "start"),
    path('imp/', views.imp, name = "imp"),
    path('homepage/', views.home, name = "home"),
    path('books/', views.books, name = "start"),
    path('writings/', views.writings, name = "start"),
    path('rl/', views.rl, name = "start"),
    path('studio/', views.studio, name = 'studio'),
    path('writings/stories/', views.stories, name = "stories"),
    path('writings/essays/', views.essays, name = "bio"),
    path('writings/funliners/', views.funl, name = "bio"),
    path('writings/stories/<str:story_name>',views.StoryContent, name = 'content'),
    path('writings/essays/<str:story_name>',views.StoryContent, name = 'content'),
    path('rl/<str:book_name>', views.BookSummary, name = "Summary"),
]

urlpatterns += staticfiles_urlpatterns()
