from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello, name="show"),
    url(r'^result',views.result),
    url(r'^edit/(?P<id>[0-9]+)/$',views.edit, name = "edit"),
    url(r'^pxe/(?P<id>[0-9]+)/$',views.pxe, name="pxe"),
    url(r'^changeuser/(?P<id>[0-9]+)/',views.changeuser, name="changeuser"),
    url(r'^changePWD/$', views.mychangePWD, name = "mychangePWD"),
    url(r'^Oberon/$', views.myOberon, name = "myOberon"),
    url(r'^editBeachcomber/(?P<id>[0-9]+)/$',views.editBeachcomber, name = "editBeachcomber"),
    url(r'^editPDU/(?P<id>[0-9]+)/$',views.editPDU, name = "editPDU"),
    # url(r'^editIOHOST/(?P<id>[0-9]+)/$',views.editIOHOST, name = "editIOHOST"),
    url(r'^editBearcat/(?P<id>[0-9]+)/$',views.editBearcat, name = "editBearcat"),

    # url(r'^password/reset/$', views.reset, name="reset"),
    url(r'^mainLog/(?P<id>[0-9]+)/$', views.mainLog, name="mainLog"),
    url(r'^pxeResult/(?P<id>[0-9]+)/$',views.pxeResult, name = "pxeResult"),
    url(r'^statusResult/(?P<id>[0-9]+)/$',views.statusResult, name = "statusResult"),
    # url(r'^statusResult/(?P<id>[0-9]+)/$',views.statusResult, name = "statusResult"),
	url(r'^statusResult/$',views.statusResult, name = "statusResult"),
    url(r'^mainLog/delete/$', views.delete, name="delete"),
]
