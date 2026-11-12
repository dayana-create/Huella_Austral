from django.urls import path
from . import views

app_name ='rescates'

urlpatterns = [
    path('',views.ejemplarListView.as_view(),name='lista'),
    path('ejemplar/<int:pk>/',views.ejemplarDetailView.as_view(),name='detalle'),
    path('ejemplar/nuevo/',views.ejemplarCreateView.as_view(),name='crear'),
    path('ejemplar/<int:pk>/editar/',views.ejemplarUpdateView.as_view(),name='editar'),
    path('ejemplar/<int:pk>/eliminar/',views.ejemplarDeleteView.as_view(),name='eliminar'),
]
