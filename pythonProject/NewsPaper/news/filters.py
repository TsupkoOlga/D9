import django_filters
from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import Post, User, Category


class PostFilter(FilterSet):
    author = ModelMultipleChoiceFilter(
        field_name = 'author__user',
        queryset = User.objects.all(),
        label = 'Author',
    )
    time_in = django_filters.DateFilter(
        lookup_expr='gt',
        label = 'Start date',
    )


    # category = ModelMultipleChoiceFilter(
    #    field_name = 'postcategory__category',
    #    queryset = Category.objects.all(),
    #    label = 'Category',
    #)

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
             # 'time_in': ['gt'],
        }