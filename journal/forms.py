from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from .models import Trade


class ProfileForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = '__all__'

        widgets = {

            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'initial_balance': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'target_balance': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }

class TradeForm(forms.ModelForm):

    class Meta:

        model = Trade

        exclude = [

            'trade_type',

            'user',

            'created_at',

        ]

        widgets = {

            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'symbol': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'lot_size': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),

            'entry_price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.00001'
                }
            ),

            'exit_price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.00001'
                }
            ),

            'take_profit': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.00001'
                }
            ),

            'stop_loss': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.00001'
                }
            ),

            'trade_result': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'profit': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),

            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 6,
                    'placeholder': 'Что произошло в этой сделке?'
                }
            ),

            'screenshot': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }



class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }
        )
    )