---
layout: default
title: Fluorometholone
parent: Solo predicción del modelo (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluorometholone: nueva indicación predicha, Vasculitis postinfecciosa (nivel de evidencia L5). Indicación original: Uveítis, enfermedad del iris, enfermedad del cuerpo ciliar…"
monitor_inn: "fluorometholone"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "punctate epithelial keratoconjunctivitis", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Fluorometholone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Fluorometolona: De Uveítis y Patología Inflamatoria Ocular a Vasculitis Postinfecciosa

## Resumen en Una Frase

La fluorometolona es un corticosteroide tópico oftálmico, utilizado originalmente para tratar procesos inflamatorios oculares como la uveítis, la conjuntivitis alérgica y la úlcera corneal.
El modelo TxGNN predice que podría ser efectiva para **vasculitis postinfecciosa**, pero **sin ensayos clínicos ni publicaciones** que respalden esta predicción; se basa únicamente en el puntaje del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Uveítis, enfermedad del iris, enfermedad del cuerpo ciliar, conjuntivitis atópica/vernal/papilar, iritis, iridociclitis, úlcera corneal (según el grafo de conocimiento; los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Vasculitis postinfecciosa |
| Puntaje de Predicción TxGNN | 99,91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la fluorometolona es un corticosteroide sintético que actúa sobre el receptor de glucocorticoides (NR3C1), con efecto antiinflamatorio e inmunosupresor. Su eficacia en inflamación de la superficie ocular y del segmento anterior es la base de su uso actual.

Mecanísticamente, la vasculitis postinfecciosa es un proceso inmunomediado, por lo que una acción antiinflamatoria podría ser teóricamente aplicable. Sin embargo, la formulación es tópica oftálmica con exposición sistémica mínima, lo que hace poco verosímil que alcance una enfermedad vascular sistémica. La predicción se apoya solo en el puntaje del modelo, sin estudios que la sustenten.

**Otras predicciones del modelo (todas con puntajes similares, ~99,8–99,9%):**
- **Queratoconjuntivitis epitelial punteada** (nivel L4, "Pregunta de investigación"): el candidato biológicamente más coherente, ya que afecta a los mismos tejidos donde el fármaco ya se usa. Las dos publicaciones halladas aportan solo contexto indirecto.
- **Iridociclitis inducida por cristalino** y **crisis glaucomatociclítica** (ambas L4, "Pregunta de investigación"): son subtipos de uveítis anterior, cercanos a las indicaciones actuales. No hay estudios específicos.
- Otitis externa, síndrome postinfeccioso, trastorno postbacteriano, estenosis uretral infecciosa, síndrome hemolítico urémico asociado a infección y miocardiopatía de Chagas: sin evidencia (L5, Hold). En los dos últimos casos no existe una justificación mecanística creíble.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la vasculitis postinfecciosa.

Como referencia indirecta, para la predicción de mayor coherencia biológica (queratoconjuntivitis epitelial punteada) se recuperaron:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34011737](https://pubmed.ncbi.nlm.nih.gov/34011737/) | 2021 | Revisión | Indian Journal of Ophthalmology | Caracteriza las secuelas de la queratoconjuntivitis microsporidial y su manejo; no evalúa la fluorometolona |
| [35128186](https://pubmed.ncbi.nlm.nih.gov/35128186/) | 2021 | Cohorte | Journal of Current Ophthalmology | Uso de OCT de segmento anterior para monitorizar la queratoconjuntivitis epidémica y el efecto del esteroide tópico; no es específico de la fluorometolona |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 57606 | FML 1 mg/ml colirio en suspensión | Colirio en suspensión | No disponible en los datos compilados |
| 56132 | Isopto Flucon 1 mg/ml colirio en suspensión | Colirio en suspensión | No disponible en los datos compilados |
| 53774 | Solubalm 0,5 mg/g + 100 mg/g crema | Crema | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): queratitis por virus del herpes simple, glaucoma de ángulo abierto, hipertensión ocular, infecciones oculares (incluidas fúngicas, virales y tuberculosis ocular), conjuntivitis infecciosa, diabetes mellitus, cetoacidosis diabética, porfiria y trastornos del metabolismo de porfirinas, deficiencia de G6PD, enfermedad de depósito de glucógeno, cistinuria, galactosemia y pigmentación corneal.
- **Interacciones farmacológicas:** se identificaron 11 posibles interacciones (doxiciclina, salbutamol, ciclosporina, paracetamol, digoxina, brimonidina, cefalexina, ácido alendrónico, aciclovir, diazepam y fenofibrato), todas con nivel de gravedad desconocido. Además, la fluorometolona actúa sobre el receptor de glucocorticoides.
- Consultar el prospecto para las advertencias y contraindicaciones oficiales, ya que no se dispone de ellas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para vasculitis postinfecciosa tiene un puntaje alto en el modelo, pero carece de ensayos clínicos y literatura (nivel L5), y la formulación oftálmica con mínima exposición sistémica limita su plausibilidad. Entre las predicciones, las de segmento anterior ocular (queratoconjuntivitis epitelial punteada, iridociclitis inducida por cristalino y crisis glaucomatociclítica) merecen priorizarse como preguntas de investigación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura específica sobre fluorometolona en las indicaciones predichas.
- Evaluar la compatibilidad de la vía de administración (tópica ocular frente a la necesaria para enfermedad sistémica).
- Considerar reorientar el análisis hacia las predicciones oculares de nivel L4.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

