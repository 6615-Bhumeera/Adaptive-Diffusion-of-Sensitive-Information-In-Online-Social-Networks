"""adaptive_diffusion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Remote_User import views as remoteuser
from adaptive_diffusion import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', remoteuser.login, name="login"),
    url(r'^Register1/$', remoteuser.Register1, name="Register1"),
    url(r'^Search_Tweet_Details/$', remoteuser.Search_Tweet_Details, name="Search_Tweet_Details"),
    url(r'^ratings/(?P<pk>\d+)/$', remoteuser.ratings, name="ratings"),
    url(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    url(r'^Add_DataSet_Details/$', remoteuser.Add_DataSet_Details, name="Add_DataSet_Details"),
    url(r'^serviceproviderlogin/$',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    url(r'View_Remote_Users/$',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
    url(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
    url(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
    url(r'^Search_Tweet/$', serviceprovider.Search_Tweet, name="Search_Tweet"),
    url(r'^View_Positive_Info/$', serviceprovider.View_Positive_Info, name="View_Positive_Info"),
    url(r'^View_Sensitive_Info/$', serviceprovider.View_Sensitive_Info, name="View_Sensitive_Info"),
    url(r'^View_TweetDataSets_Details/$', serviceprovider.View_TweetDataSets_Details, name="View_TweetDataSets_Details"),
    url(r'^View_Negative_Info/$', serviceprovider.View_Negative_Info, name="View_Negative_Info"),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
