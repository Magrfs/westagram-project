from django.urls import path, include

urlpatterns = [
    path('account', include('account.urls')),
    path('comment', include('comment.urls')),
]
