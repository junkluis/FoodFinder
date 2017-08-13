from rest_framework import serializers
from .models import Denuncia

class DenunciaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Denuncia
		fields = ('comedor', 'fecha_den', 'denuncia')