
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import handler404

from main import views
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from strawberry.django.views import GraphQLView
from main.graphql.scheme import schema


handler404 = views.error404

urlpatterns = [
    path("admin/", admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)), name='graphql'),
    path('adminactions/', include('adminactions.urls')),
    path("", include("main.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns