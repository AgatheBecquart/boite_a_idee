from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Idea, Like, Dislike
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'main/home.html')

class IdeaListView(ListView):
    model = Idea
    template_name = 'main/idea_list.html'
    context_object_name = 'idea_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        for idea in context['idea_list']:
            idea.user_liked = idea.like_set.filter(user=user).exists()
            idea.user_disliked = idea.dislike_set.filter(user=user).exists()
        return context

class MyIdeaListView(ListView):
    model = Idea
    template_name = 'main/my_idea_list.html'
    context_object_name = 'my_idea_list'

    
class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'main/idea_detail.html'
    
class IdeaCreateView(CreateView, LoginRequiredMixin):
    model = Idea
    template_name = 'main/idea_create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('idea_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class IdeaUpdateView(LoginRequiredMixin, UpdateView):
    model = Idea
    template_name = 'main/idea_update.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('my_idea_list')
    
class IdeaDeleteView(LoginRequiredMixin, DeleteView):
    model = Idea
    template_name = 'main/idea_delete.html'
    success_url = reverse_lazy('my_idea_list')
    

def like_or_dislike(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            like_or_dislike = request.POST.get('like_or_dislike')
            if like_or_dislike == 'like':
                dislike = idea.dislike_set.filter(user=request.user)
                if dislike.exists():
                    dislike.delete()
                like, created = idea.like_set.get_or_create(user=request.user)
                if not created:
                    like.delete()
            elif like_or_dislike == 'dislike':
                like = idea.like_set.filter(user=request.user)
                if like.exists():
                    like.delete()
                dislike, created = idea.dislike_set.get_or_create(user=request.user)
                if not created:
                    dislike.delete()
        return redirect('idea_list')
    else:
        return redirect('idea_list')

import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

def idea_chart(request):
    ideas = Idea.objects.all()
    votes = [(idea.title, idea.like_set.count() - idea.dislike_set.count()) for idea in ideas]    
    votes_sorted = sorted(votes, key=lambda x: x[1], reverse=True)
    ideas_id = [vote[0] for vote in votes_sorted]
    votes_count = [vote[1] for vote in votes_sorted]

    # Créer le graphique avec Seaborn
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax = sns.barplot(x=votes_count, y=ideas_id, palette="rocket")
    ax.set_xticks(range(min(votes_count), max(votes_count)+1, 1))
    plt.tight_layout()

    # Convertir le graphique en image PNG
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Convertir l'image en base64 pour l'afficher dans le template
    image_base64 = base64.b64encode(image_png).decode('utf-8')
    image_src = 'data:image/png;base64,{}'.format(image_base64)

    context = {
        'image_src': image_src
    }
    return render(request, 'main/idea_chart.html', context)
