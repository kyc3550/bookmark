from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1/bookmark/
    # 클래스형 뷰에는 as_view가 붙는다.
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(),name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'), #<int:pk> 글번호를 넣기 위함
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]
