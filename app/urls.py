from .import views
from django.conf.urls import url

from shopping import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns

app_name="app"

urlpatterns=[
    url(r'home',views.home,name="home"),
    url(r'log',views.log,name="log"),
    url(r'modify',views.modify,name="modify"),
    url(r'(?P<product_id>[0-9]+)/yoo$',views.yoo,name="yoo"),
    url(r'(?P<product_id>[0-9]+)/top$',views.top,name="top"),
    url(r'(?P<collection_id>[0-9]+)/prod$',views.prod,name="prod"),
    url(r'(?P<product_id>[0-9]+)/nope$',views.nope,name="nope"),
    url(r'(?P<product_id>[0-9]+)/dele$',views.dele,name="dele"),
    url(r'thanks',views.thanks,name="thanks"),
    url(r'username/',views.usernamevarify,name="usernamevarify"),
    url(r'signup',views.signup,name="signup"),
    url(r'ishank',views.ishank,name="user_logout"),
    url(r'cust/',views.cust,name="cust"),
    url(r'deepak/',views.deepak,name="deepak"),
    url(r'sumi/$',views.sumi,name="sumi"),
    url(r'search$',views.search,name="search"),
    url(r'wifi$',views.wifi,name="wifi"),
    url(r'orders$',views.orders,name='orders'),
    url(r'(?P<order_id>[0-9]+)/soonn$',views.soonn,name="soonn"),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
