from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
	path('finchs/', views.finchs_index, name='index'),
  path('finchs/<int:finch_id>', views.finchs_detail, name='detail'),
  path('finchs/create/', views.FinchCreate.as_view(), name='finchs_create'),
  path('finchs/<int:pk>/update/', views.FinchUpdate.as_view(), name='finchs_update'),
  path('finchs/<int:pk>/delete/', views.FinchDelete.as_view(), name='finchs_delete'),
  path('finchs/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),

 ]