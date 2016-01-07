from django.conf.urls import include, url

urlpatterns = [
    url(r'^signup/$','account.views.signup',name="signup"),
    url(r'^login/$','account.views.handlelogin',name="login"),
    url(r'^home/$','account.views.home',name="home")

]