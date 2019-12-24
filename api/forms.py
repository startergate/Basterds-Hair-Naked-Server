from django import forms

from api.models import Match


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ('matchid', 'pid', 'status', 'score', 'playtime', 'turn_count',
                  'spawned_alias', 'killed_alias', 'killed_hostiles', 'damage', 'heal')
        app_label = 'api'
