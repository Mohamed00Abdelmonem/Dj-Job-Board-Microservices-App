
from rest_framework.pagination import PageNumberPagination

class JobsPagination(PageNumberPagination):
    page_size = 5