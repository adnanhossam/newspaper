from django.urls import path 
from .models import Articles
from .views import( 
                   ArticlesListView,
                   ArticlesUpdateView,
                   ArticlesDetailView,
                   ArticlesDeleteView,
                   ArticlesCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/',
        ArticlesUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/',
        ArticlesDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete',
        ArticlesDeleteView.as_view(), name= 'article_delete'),
    path('new/',ArticlesCreateView.as_view(),name='article_new'),
    path('', ArticlesListView.as_view(), name='articles_list'),
    
]
