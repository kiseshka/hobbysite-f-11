from django.shortcuts import render, get_object_or_404
from .models import Article, ArticleCategory, Comment

def article_list_view(request):
    articles = Article.objects.all()
    categories = ArticleCategory.objects.all()
    context = {'articles': articles, 'categories': categories}
    return render(request, 'article_list.html', context)

def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    related_articles = Article.objects.filter(category=article.category).exclude(id=pk)[:2]
    comments = Comment.objects.filter(article=article)
    context = {'article': article, 'related_article': related_article, 'context': context}
    return render(request, 'article_detail.html', context)

def article_update_view(request, pk):
    article = Article.objects.get(pk=pk)
    categories = Articlecategory.objects.all()

    context = {
        'article': article, 
        'categories': categories,
    }

    return render(request, 'article_update.html', context)
