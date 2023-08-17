from articles.models import Article


def get_all_articles():
    return Article.objects.all()


def get_rated_articles():
    return Article.objects.order_by(['-views.count()'])
