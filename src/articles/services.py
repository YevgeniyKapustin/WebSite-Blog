from articles.models import Article


def get_all_articles():
    return Article.objects.all()
