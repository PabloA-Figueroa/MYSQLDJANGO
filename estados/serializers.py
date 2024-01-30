from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from estados.models import Estado, Ingreso, Gasto

 # Asegúrate de que estos campos existan en tu modelo Emprendimiento

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = ['tipo', 'valor']

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = ['tipo', 'valor']

class EstadoSerializer(serializers.ModelSerializer):
    ingresos = IngresoSerializer(many=True)
    gastos = GastoSerializer(many=True)

    class Meta:
        model = Estado
        fields = ['id','fecha', 'ingresos', 'gastos', 'beneficios', 'usuario', 'emprendimiento', 'comentarios', 'ingresoTotal', 'gastoTotal', 'beneficiosTotal']

    def create(self, validated_data):
        # Pop removes the field and returns the value
        ingresos_data = validated_data.pop('ingresos', [])
        gastos_data = validated_data.pop('gastos', [])

        # Create the Estado instance
        estado = Estado.objects.create(**{k: v for k, v in validated_data.items() if k not in ['ingresos', 'gastos', 'usuario','emprendimiento']})
        # Create and associate Ingresos and Gastos
        for ingreso_data in ingresos_data:
            ingreso_data = dict(ingreso_data)
            Ingreso.objects.create(estado=estado, **ingreso_data)
        for gasto_data in gastos_data:
            gasto_data = dict(gasto_data)
            Gasto.objects.create(estado=estado, **gasto_data)

        # Check if 'usuario' and 'emprendimiento' are provided and are lists
        usuarios = validated_data.get('usuario', None)
        emprendimientos = validated_data.get('emprendimiento', None)

        if usuarios is not None:
            estado.usuario.set(usuarios)
        if emprendimientos is not None:
            estado.emprendimiento.set(emprendimientos)

        return estado