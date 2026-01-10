from django.db import migrations


def seed_questions(apps, schema_editor):
    QuizQuestion = apps.get_model('quizzes', 'QuizQuestion')
    questions = [
        {"id": 1, "pregunta": "¿Cuál es la arquitectura principal en la que se basa Django?", "opciones": ["MVC", "MVT (Model-View-Template)", "MVVM", "Microservicios"], "respuesta_correcta": "MVT (Model-View-Template)"},
        {"id": 2, "pregunta": "¿Qué método del ORM se usa para realizar un JOIN y optimizar relaciones ForeignKey?", "opciones": ["prefetch_related", "select_related", "filter_join", "get_related"], "respuesta_correcta": "select_related"},
        {"id": 3, "pregunta": "¿Qué comando genera los archivos de migración tras cambiar los modelos?", "opciones": ["migrate", "sync_db", "makemigrations", "check"], "respuesta_correcta": "makemigrations"},
        {"id": 4, "pregunta": "¿Cuál es la función principal de los Middlewares?", "opciones": ["Definir tablas", "Procesar peticiones/respuestas globalmente", "Renderizar HTML", "Enviar correos"], "respuesta_correcta": "Procesar peticiones/respuestas globalmente"},
        {"id": 5, "pregunta": "¿Qué decorador restringe el acceso a usuarios no autenticados?", "opciones": ["@auth_required", "@login_required", "@check_user", "@is_authenticated"], "respuesta_correcta": "@login_required"},
        {"id": 6, "pregunta": "¿Qué objeto permite usar lógica 'OR' en consultas del ORM?", "opciones": ["F objects", "Q objects", "Filter objects", "Logic objects"], "respuesta_correcta": "Q objects"},
        {"id": 7, "pregunta": "¿Para qué sirve el atributo 'related_name' en un ForeignKey?", "opciones": ["Nombre de columna", "Acceso inverso desde el modelo relacionado", "Clave primaria", "Traducción"], "respuesta_correcta": "Acceso inverso desde el modelo relacionado"},
        {"id": 8, "pregunta": "¿En qué archivo se mapean las URLs a las vistas?", "opciones": ["settings.py", "views.py", "urls.py", "routes.py"], "respuesta_correcta": "urls.py"},
        {"id": 9, "pregunta": "¿Qué significa que los QuerySets sean 'lazy'?", "opciones": ["Son lentos", "No se ejecutan hasta ser evaluados", "Se borran solos", "Tienen límite de 10"], "respuesta_correcta": "No se ejecutan hasta ser evaluados"},
        {"id": 10, "pregunta": "¿Qué etiqueta de template se usa para la herencia?", "opciones": ["{% include %}", "{% extends %}", "{% block %}", "{% load %}"], "respuesta_correcta": "{% extends %}"},
        {"id": 11, "pregunta": "¿Qué componente hace disponibles variables en todos los templates?", "opciones": ["Middlewares", "Context Processors", "Signals", "Tags"], "respuesta_correcta": "Context Processors"},
        {"id": 12, "pregunta": "¿Qué sistema permite ejecutar código tras guardar un modelo?", "opciones": ["Triggers", "Signals", "Hooks", "Listeners"], "respuesta_correcta": "Signals"},
        {"id": 13, "pregunta": "¿Cuál es la ventaja de ModelForm?", "opciones": ["Soporte NoSQL", "Genera campos automáticamente desde el modelo", "Es más rápido", "No requiere validación"], "respuesta_correcta": "Genera campos automáticamente desde el modelo"},
        {"id": 14, "pregunta": "¿Para qué sirve la SECRET_KEY?", "opciones": ["Contraseña de DB", "Firmar datos criptográficamente", "Ocultar código", "Registrar licencia"], "respuesta_correcta": "Firmar datos criptográficamente"},
        {"id": 15, "pregunta": "¿Contra qué ataque protege CsrfViewMiddleware?", "opciones": ["SQL Injection", "Cross-Site Request Forgery", "XSS", "Brute Force"], "respuesta_correcta": "Cross-Site Request Forgery"},
        {"id": 16, "pregunta": "¿Cómo se define una relación de muchos a muchos?", "opciones": ["ForeignKey", "ManyToManyField", "OneToManyField", "MultiField"], "respuesta_correcta": "ManyToManyField"},
        {"id": 17, "pregunta": "¿Dónde se definen las opciones del modelo como el orden?", "opciones": ["class Config", "class Meta", "class Options", "class Settings"], "respuesta_correcta": "class Meta"},
        {"id": 18, "pregunta": "¿Qué comando reúne los archivos estáticos para producción?", "opciones": ["makestatic", "collectstatic", "minifystatic", "runstatic"], "respuesta_correcta": "collectstatic"},
        {"id": 19, "pregunta": "¿Qué atajo lanza un error 404 si el objeto no existe?", "opciones": ["get_or_error", "get_object_or_404", "find_or_404", "check_404"], "respuesta_correcta": "get_object_or_404"},
        {"id": 20, "pregunta": "¿Qué método actualiza múltiples registros eficientemente?", "opciones": ["save_all()", "update()", "modify()", "bulk_edit()"], "respuesta_correcta": "update()"},
    ]
    for q in questions:
        QuizQuestion.objects.update_or_create(
            id=q["id"],
            defaults={
                "pregunta": q["pregunta"],
                "opciones": q["opciones"],
                "respuesta_correcta": q["respuesta_correcta"],
            },
        )


def unseed_questions(apps, schema_editor):
    QuizQuestion = apps.get_model('quizzes', 'QuizQuestion')
    QuizQuestion.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_questions, unseed_questions),
    ]

