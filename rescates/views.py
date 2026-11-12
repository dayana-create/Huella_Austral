from django.urls import reverse_lazy
from django.views.generic import ( ListView,DetailView,CreateView,UpdateView,DeleteView)
from .forms import ejemplarForm
from .models import ejemplar

class ejemplarListView(ListView):
    model = ejemplar 
    template_name = 'rescates/ejemplar_list.html'
    context_object_name = 'ejemplares'
    
    def get_queryset(self):
        return ejemplar.objects.select_related('especie')
    
class ejemplarDetailView(DetailView):
    model = ejemplar
    template_name = 'rescates/ejemplar_detail.html'
    context_object_name = 'ejemplar'
    
    def get_queryset(self):
        return ejemplar.objects.select_related('especie')
    
class ejemplarCreateView (CreateView):
    model = ejemplar
    form_class = ejemplarForm
    template_name = 'rescates/ejemplar_form.html'
    success_url = reverse_lazy ('rescates:lista')
    
class ejemplarUpdateView (UpdateView):
    model = ejemplar
    form_class = ejemplarForm
    template_name = 'rescates/ejemplar_form.html'
    success_url = reverse_lazy ('rescates:lista')
    
class ejemplarDeleteView (DeleteView):
    model = ejemplar
    template_name = 'rescates/ejemplar_form.html'
    context_object_name = 'ejemplar'
    success_url = reverse_lazy ('rescates:lista')

