"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView #Login view
from django.contrib import admin
from blog.views import(

    home,
    BlogList,
    BlogDetail,
    BlogCreate,
    MyBlogList,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^login/',LoginView.as_view(),name='login'),
    url(r'^blogs/$',BlogList.as_view()),
    url(r'^myblogs/$',MyBlogList),
    url(r'^blogs/create/$',BlogCreate.as_view()),
    url(r'^blogs/(?P<slug>[\w-]+)/$',BlogDetail.as_view()),
]
