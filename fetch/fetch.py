import requests as req
import json as json

endPointsAvailable = 7
domain = "http://localhost:8083/administrador"

test = {
    "test_data_1": '''[
        {
            "hora_inicio": "10:00",
            "hora_fin": "12:00",
            "n_grupos": 15
        },
        {
            "hora_inicio": "12:00",
            "hora_fin": "14:00",
            "n_grupos": 30
        },
        {
            "hora_inicio": "14:00",
            "hora_fin": "16:00",
            "n_grupos": 20
        }
    ]''',
    
    "test_data_2": '''[
        {
            "tipo_pregunta": "multiple",
            "n_preguntas": "40"
        },
        {
            "tipo_pregunta": "verdadero_falso",
            "n_preguntas": "65"
        }    
    ]''',

    "test_data_3": '''{
        "profesores": [
            "ramiro", "romulo"
        ],
        "materias": [
            "ciencia", "fisica", "filosofia"
        ],
        "heatmap_n_quices": [
            [30, 40, 50],
            [60, 30, 20]
        ]
    }''',

    "test_data_4": '''{
        "grupos": [
            "01-D", "02-D", "01-N"
        ],
        "temas": [
            "calculo", "biologia"
        ],
        "heatmap_calificacion_promedio": [
            [4.5, 4.0],
            [3.0, 2.5],
            [5.0, 4.2]
        ]
    }''',

    "test_data_5": '''{
        "meses": ["2022-09", "2022-10", "2022-11"],
        "calificacion_promedio": [4.3, 4.0, 2.0]
    }''',

    "test_data_6": '''{
        "meses": ["2022-09", "2022-10", "2022-11"],
        "cantidad_quices": [45, 50, 40]
    }''',

    "test_data_7": '''{
        "profesores": [
            "romulo", "ramiro", "andres"
        ],
        "n_bancos": [
            25, 15, 40
        ],
        "n_preguntas_promedio": [
            8.6, 9, 17
        ]
    }'''
}

def load_report_data(number: int):
    
    if number > endPointsAvailable: return

    res = req.get(f"{domain}/reporte{number}")
    return json.loads(res.text)

def load_test_data(number: int):
    return json.loads(test[f"test_data_{number}"])