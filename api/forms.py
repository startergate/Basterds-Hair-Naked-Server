from django import forms

from api.models import Match, Object, Action


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ('matchid', 'pid', 'status', 'played_as', 'score', 'playtime', 'turn_count',
                  'spawned_alias', 'killed_alias', 'killed_hostiles', 'damage', 'heal')
        app_label = 'api'


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ('objectid', 'matchid', 'belong_to', 'status', 'job', 'hp', 'damage')
        app_label = 'api'


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ('actionid', 'pid', 'matchid', 'type', 'origin', 'to', 'destination_x', 'destination_y', 'amount')
        app_label = 'api'
