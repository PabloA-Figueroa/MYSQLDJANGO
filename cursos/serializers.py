from rest_framework.serializers import ModelSerializer, SerializerMethodField
from Cursos.models import Cursos, Tema, ContenidoCurso, Recurso, RecursoTexto, RecursoImagen, RecursoVideo


class CursoSerializer(ModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'


class ContenidoCursoSerializer(ModelSerializer):
    class Meta:
        model = ContenidoCurso
        fields = '__all__'


class RecursoSerializer(ModelSerializer):
    detalle_recurso = SerializerMethodField()

    class Meta:
        model = Recurso
        fields = ['id', 'nombre', 'detalle_recurso']  # Incluimos el campo personalizado detalle_recurso
    def get_detalle_recurso(self, obj):
    # Verificamos el tipo de instancia y serializamos los datos respectivos
        if isinstance(obj, RecursoTexto):
            return RecursoTextoSerializer(obj).data
        elif isinstance(obj, RecursoImagen):
            return RecursoImagenSerializer(obj).data
        elif isinstance(obj, RecursoVideo):
            return RecursoVideoSerializer(obj).data
        return None  #

class RecursoTextoSerializer(ModelSerializer):
    class Meta:
        model = RecursoTexto
        fields = ['texto']

class RecursoImagenSerializer(ModelSerializer):
    class Meta:
        model = RecursoImagen
        fields = ['imagen']

class RecursoVideoSerializer(ModelSerializer):
    class Meta:
        model = RecursoVideo
        fields = ['video', 'url_video']

class ContenidoCursoSerializer(ModelSerializer):
    recursos = SerializerMethodField()  # Utilizamos este campo para obtener los recursos

    class Meta:
        model = ContenidoCurso
        fields = '__all__'  # Asegúrate de incluir 'recursos'

    def get_recursos(self, obj):
        # Obtenemos los recursos relacionados con este contenido del curso
        recursos = obj.recurso_set.all()  # Asegúrate de que estás llamando al related_name correcto
        # Serializamos los recursos y los devolvemos
        return RecursoSerializer(recursos, many=True, context=self.context).data