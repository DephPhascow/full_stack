
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from main import views
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from strawberry.django.views import GraphQLView
from main.graphql.scheme import schema
from main.graphql.view import GraphQLView as GQV


handler404 = views.error404


urlpatterns = [
    path("admin/", admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    # path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema, subscriptions_enabled=True)), name='graphql'),
    path('graphql/', csrf_exempt(GQV.as_view(graphiql=True, schema=schema, subscriptions_enabled=True)), name='graphql'),
    path('adminactions/', include('adminactions.urls')),
    path("", include("main.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns