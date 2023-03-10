from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import Post, User

# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
   author = ModelMultipleChoiceFilter(
      field_name = 'author__user',
      queryset = User.objects.all(),
      label = 'Author',
   )

   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'title': ['icontains'],
           # 'author__user': ['exact'],
           # время должно быть больше или равно
           # 'quantity': ['gt'],
       }