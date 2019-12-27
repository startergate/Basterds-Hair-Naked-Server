from django import forms

from api.models import Match, Object, Action


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ('matchid', 'player1', 'played_as2', 'status', 'played_as1', 'played_as2', 'score1', 'score2', 'playtime', 'turn_count',
                  'spawned1', 'killed1', 'spawned2', 'killed2', 'damage1', 'heal1', 'damage2', 'heal2', 'created_at', 'terminated_at')
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
