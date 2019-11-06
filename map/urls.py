from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

from . import views

app_name = 'map'
urlpatterns = [
    # path('article/<int:pk>', views.ArticleViewDetail.as_view(), name='article'),
    # path('articles/', views.ArticleView.as_view(), name='articles'),
    # path('', views.IndexView.as_view(), name='index'),
    path('', staff_member_required(views.MainVew.as_view()), name='main'),
    # path('console/order/<int:pk>', staff_member_required(views.ConsoleEditProjectView.as_view()), name='console_order'),
    # path('/user/', staff_member_required(views.MainVew.as_view()), name='response'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
