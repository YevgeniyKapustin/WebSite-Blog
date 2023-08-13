from .models import ViewCount
from .utils import get_client_ip


class ArticleViewCountMixin(object):
    def get_object(self):
        article = super().get_object()
        ip_address = get_client_ip(self.request)
        ViewCount.objects.get_or_create(article=article, ip_address=ip_address)
        return article
