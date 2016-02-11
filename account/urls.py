from django.conf.urls import include, url
# from account.views import SkillSetList
urlpatterns = [
    url(r'^logout/$', 'account.views.logout', name = 'logout'),
    url(r'^home/$', 'account.views.home',name='home'),
    # url(r'^login/$', 'account.views.login', name = 'login'),
    url(r'^signup/$', 'account.views.signup',name='signup'),
    url(r'^activate/(?P<uid>\d+)/(?P<token>[0-9A-Za-z_\-]+)/$', 'account.views.activate', name='activate'),
    url(r'^reset_password/(?P<uid>\d+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'account.views.reset_password', name='reset_password'),
    url(r'^forgot_password/$', 'account.views.forgot_password',name='forgot_password'),
    url(r'^edit_profile/$', 'account.views.edit_profile',name='edit_profile'),
    url(r'^search/$', 'account.views.search', name = 'searchSkills'),
    url(r'^add_skills/$', 'account.views.add_skills', name = 'add_skills'),
    # url(r"^$", SkillSetList.as_view(), name="skillset_list"),
    url(r'^add_project/$', 'account.views.add_project', name = 'add_project'),
    url(r'^save/$', "account.views.save", name="save"),
    url(r'^my_profile/$', "account.views.my_profile", name="my_profile"),
    url(r'^user/(?P<id>\d+)$', 'account.views.open_profile', name = 'open_profile'),
    url(r'^otherhome/$', 'account.views.otherhome', name = 'otherhome'),
    url(r'^otherhome/user/(?P<id>\d+)/follow/$', 'account.views.follow', name = 'follow'),
    url(r'^otherhome/user/(?P<id>\d+)/unfollow/$', 'account.views.unfollow', name = 'unfollow'),
]

# (?P<skill_id>\d+)/$