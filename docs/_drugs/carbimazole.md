---
layout: default
title: Carbimazole
parent: Solo predicción del modelo (L5)
nav_order: 103
evidence_level: L5
indication_count: 3
---

# Carbimazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Carbimazol: De Hipertiroidismo a Resistencia a la Hormona Tiroidea por Mutación del Receptor Beta (THRB)

## Resumen en Una Frase

Carbimazol es un fármaco antitiroideo (profármaco del metimazol) comercializado en España, cuyo texto de indicación aprobada no figura en los datos recibidos.
El modelo TxGNN predice que podría ser efectivo para la **resistencia a la hormona tiroidea por mutación de THRB**, pero hay **0 ensayos clínicos** y solo **1 publicación** (un caso diagnóstico, no un estudio de tratamiento).
La predicción tiene una puntuación alta, pero no se sostiene con una justificación terapéutica plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en la ficha de autorización (texto vacío). Uso antitiroideo conocido: hipertiroidismo |
| Nueva Indicación Predicha | Resistencia a la hormona tiroidea por mutación en el receptor beta de la hormona tiroidea |
| Puntaje de Predicción TxGNN | 99,71 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, carbimazol es un profármaco del metimazol e inhibe la peroxidasa tiroidea, lo que reduce la síntesis de T4 y T3.

En este caso la predicción **no resulta razonable mecanísticamente**. En la resistencia a la hormona tiroidea por mutación de THRB, el defecto está en el receptor y la TSH ya está no suprimida. Reducir la producción hormonal elevaría aún más la TSH y podría provocar bocio y síntomas de hipotiroidismo. El único documento de apoyo es un artículo de tipo diagnóstico sobre tiroxina libre elevada con TSH no suprimida, que trata del diagnóstico diferencial y no de un tratamiento. La puntuación alta de TxGNN no tiene respaldo terapéutico.

**Otras predicciones del modelo para este fármaco** (para contexto):

| Rango | Indicación predicha | Puntaje TxGNN | Nivel | Publicaciones | Recomendación |
|------|------|------|------|------|------|
| 2 | Tirotoxicosis neonatal | 99,41 % | L3 | 18 | Pregunta de investigación |
| 3 | Hipertiroxinemia | 99,21 % | L4 | 7 | Hold |

La tirotoxicosis neonatal es la más coherente mecanísticamente. Suele deberse a anticuerpos maternos que estimulan el receptor de TSH, y el bloqueo de la síntesis hormonal tiene sentido. Además, hay casos publicados de respuesta al tratamiento con carbimazol. La hipertiroxinemia solo sería aplicable cuando refleja tirotoxicosis verdadera.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Discusión diagnóstica (clasificado solo por el título) | BMJ Case Reports | Varón joven con tiroxina libre elevada (25–36,9 pmol/L) y TSH no suprimida durante 10 años. Fue tratado de forma intermitente con carbimazol como hipertiroidismo, sin normalización. Es un caso de diagnóstico diferencial, no un estudio de eficacia. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 28996 | NEO-TOMIZOL 5 mg COMPRIMIDOS (Ferrer Internacional S.A.) | Comprimido | No disponible en los datos recibidos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No hay datos de interacciones farmacológicas (consulta sin resultados).

Como aviso derivado de la evidencia asociada a otras predicciones, la exposición a carbimazol/metimazol en el primer trimestre del embarazo conlleva riesgo teratogénico. Se ha descrito un caso de atresia de coanas tras tratamiento materno (PMID 12124735).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación de rango 1 (resistencia a la hormona tiroidea por THRB) tiene nivel L5, sin ensayos y con una única publicación diagnóstica. Además, su mecanismo predice un posible efecto perjudicial (aumento de TSH y bocio).

**Para avanzar se necesita:**
- Obtener la ficha técnica de la AEMPS (indicación aprobada, advertencias y contraindicaciones), ya que la ausencia de estos datos bloquea el cribado de seguridad.
- Obtener los datos de mecanismo de acción desde DrugBank.
- Reorientar la evaluación hacia la **tirotoxicosis neonatal** (L3, coherente mecanísticamente), revisando los textos completos de los estudios de cohortes. Requeriría protocolos especializados de dosificación y monitorización neonatal.
- Confirmar los diseños de los estudios, ya que la clasificación actual se infirió solo de los títulos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

