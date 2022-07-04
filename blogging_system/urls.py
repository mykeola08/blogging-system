from django.urls import path
from . views import HomeView, PostListView, PostDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', PostListView.as_view(), name='post_list'),
    path('blog/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
]
