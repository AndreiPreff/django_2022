from django import forms
from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
#         'max_length': 'Слишком длинное имя',
#         'min_length': 'Слишком короткое имя',
#         'required': 'Укажите хотя бы 2 символа',})
#     surname = forms.CharField(label='Фамилия', max_length=30, min_length=2)
#     feedback = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'rows': 4, 'cols': 60}))
#     rating = forms.IntegerField(label='Рейтинг', min_value=1, max_value=5)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }
        error_messages = {
            'name': {'max_length': 'ой как много символов',
                     'min_length': 'ой как мало символов',
                     'required': 'Не должно быть пустым'
                     },
            'surname': {'max_length': 'ой как много символов',
                        'min_length': 'ой как мало символов',
                        'required': 'Не должно быть пустым'
                        }
        }

