from django import template


register = template.Library()

censored_words = ['блин', 'хрен']

# Регистрируем наш фильтр под именем censor, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.

@register.filter()
def censor(value):
   """
   value: значение, к которому нужно применить фильтр
   """

   for w in censored_words:
      asterisk = '*' * len(w)
      value = value.replace(w, asterisk)
      value = value.replace(w.title(), asterisk)

    # Возвращаемое функцией значение подставится в шаблон.
   return value