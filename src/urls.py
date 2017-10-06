from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^accounts/', include("accounts.urls", namespace = "accounts")),
    url(r'^$', login_required(TemplateView.as_view(template_name="home.html"))),
]

