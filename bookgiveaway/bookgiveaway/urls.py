from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/swagger/', SpectacularAPIView.as_view(), name='swagger'),
    path('api/swagger/docs/', SpectacularSwaggerView.as_view(url_name='swagger'), name='swagger_docs'),

    path('api/user/', include('user.urls')),
    path('api/book/', include('book.urls')),
    path('api/giveaway/', include('giveaway.urls'))
]

