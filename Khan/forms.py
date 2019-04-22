from django import forms
from .models import MapleDB

class MapleNameForm(forms.Form):
    MapleName = forms.CharField(label='', widget=forms.TextInput)

    # pylint Maybe no member 오류 처리
    # pylint: disable=maybe-no-member
    MapleName.widget.attrs.update({
        'class': 'form-control setting-border',
        'placeholder': '메이플 닉네임을 입력해주세요...',
        'aria-label': "메이플 닉네임을 입력해주세요...",
        'aria-describedby': "button-addon2",
    })

    