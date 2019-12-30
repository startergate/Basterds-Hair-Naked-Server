from django import forms

from api.models import Match, Object, Action


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ('matchid', 'player', 'status', 'played_as', 'score', 'playtime', 'turn_count',
                  'spawned', 'killed', 'damage', 'heal', 'created_at', 'terminated_at')
        app_label = 'api'


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ('objectid', 'matchid', 'belong_to', 'status', 'faction', 'job', 'hp', 'damage')
        app_label = 'api'


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ('actionid', 'pid', 'matchid', 'type', 'origin', 'to', 'destination_x', 'destination_y', 'amount')
        app_label = 'api'
