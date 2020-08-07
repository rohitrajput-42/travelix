from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', include('home.urls')),

    path('cont/', include('cont.urls')),
    path('cont/home/', include('cont.urls')),
    path('cont/gal/', include('gal.urls')),
    path('cont/desties/', include('desties.urls')),
    path('cont/accounts/', include('accounts.urls')),

    path('gal/', include('gal.urls')),
    path('gal/home/', include('gal.urls')),
    path('gal/cont/', include('cont.urls')),
    path('gal/desties/', include('desties.urls')),
    path('gal/accounts/', include('accounts.urls')),

    path('desties/', include('desties.urls')),
    path('desties/home/', include('desties.urls')),
    path('desties/cont/', include('cont.urls')),
    path('desties/gal/', include('gal.urls')),
    path('desties/accounts/', include('accounts.urls')),

    path('desties/agr/', include('agr.urls')),
    path('desties/agr/home/', include('agr.urls')),
    path('desties/agr/gal/', include('gal.urls')),
    path('desties/agr/cont/', include('cont.urls')),
    path('desties/agr/accounts/', include('accounts.urls')),
    path('desties/agr/bookieagr/', include('bookieagr.urls')),
    path('desties/agr/bookieagr/confirm/', include('confirm.urls')),
    path('desties/agr/bookieagr/confirm/cont', include('cont.urls')),

    path('desties/go/', include('go.urls')),
    path('desties/go/home/', include('agr.urls')),
    path('desties/go/gal/', include('gal.urls')),
    path('desties/go/cont/', include('cont.urls')),
    path('desties/go/accounts/', include('accounts.urls')),
    path('desties/go/bookiego/', include('bookiego.urls')),

    path('desties/aul/', include('aul.urls')),
    path('desties/aul/home/', include('agr.urls')),
    path('desties/aul/gal/', include('gal.urls')),
    path('desties/aul/cont/', include('cont.urls')),
    path('desties/aul/accounts/', include('accounts.urls')),
    path('desties/aul/bookieaul/', include('bookieaul.urls')),


    path('accounts/', include('accounts.urls')),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
