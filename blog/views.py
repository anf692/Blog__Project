from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from .forms import formulaire

#fonction pour afficher les differentes postes
def post_list(request):
    # posts = Post.objects.all().order_by('-created_at')
    # return render(request, 'blog\post_list.html', {'posts': posts})
    return render(request, 'blog\post_list.html')


#fonction pour afficher les details de chaque poste
def post_detail(request, id):
    post=Post.objects.get(id=id)
    #post=get_object_or_404(Post,id=id)
    return render (request, 'blog\post_detail.html',{'post':post})

#fonction pour ajouter des  postes
def ajout_post(request):
    # Vérification si la méthode de requête est POST (soumission d'un formulaire)
    if request.method == "POST":
        # Instanciation du formulaire Ajout_post avec les données soumises
        form = formulaire(request.POST)
        # Vérification si la formulaire est valide et on le sauvegarde
        if form.is_valid():
            form.save()
            # Rediriger vers la page des postes
            return redirect('blog')
    else:
        # Si la méthode de requête est GET, afficher un formulaire vide
        form =  formulaire()
    return render(request,'blog\Forms.html', {'form':form})

#fonction pour modifier une articles
def modifier(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = formulaire (request.POST, instance= post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = formulaire (instance= post)
    return render(request, 'blog/modifier.html', {'form': form, 'post': post})

#fonction pour supprimer un poste
def supprimer(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('blog')
    return render(request, 'blog/supprimer.html', {'post': post})


#fonction pour la page index.html
def index(request):
    return render(request, 'blog\index.html')

#fonction pour la page Blog.html
def blog(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog\Blog.html', {'posts': posts})
    

# Create your views here.
