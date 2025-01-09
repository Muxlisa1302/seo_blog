from django.shortcuts import render, redirect, get_object_or_404
from .models import Author
from .models import Article


def home(request):
    return render(request, 'index.html')


def author_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        email = request.POST.get('email')
        if name and bio and email:
            Author.objects.create(
                name=name,
                bio=bio,
                email=email
            )
            return redirect('authors:list')
    return render(request,'articles/create-author.html')


def article_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        image = request.POST.get('image')
        if title and content and author and image:
            Article.objects.create(
                title=title,
                content=content,
                author=author,
                image=image
            )
            return redirect('articles:list')
    return render(request,'articles/create-article.html')


def article_detail(request, year, month, day, slug):
    article = get_object_or_404(
        Article,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    ctx = {'article':article}
    return render(request, 'articles/create-author.html', ctx)