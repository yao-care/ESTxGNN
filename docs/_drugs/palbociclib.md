---
layout: default
title: Palbociclib
parent: Solo predicción del modelo (L5)
nav_order: 402
evidence_level: L5
indication_count: 4
---

# Palbociclib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Palbociclib: De Cáncer de Mama a Hipertiroidismo

## Resumen en Una Frase

Palbociclib es un inhibidor de CDK4/6 utilizado en el cáncer de mama avanzado con receptores hormonales positivos y HER2 negativo (HR+/HER2-). El modelo TxGNN predice que podría ser efectivo para **hipertiroidismo**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, por lo que se basa solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama HR+/HER2- (deducido de la literatura recopilada; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Hipertiroidismo |
| Puntaje de Predicción TxGNN | 99.44% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la literatura recopilada, palbociclib es un inhibidor dual de CDK4/6 con eficacia comprobada en cáncer de mama HR+/HER2-. Actúa frenando la proliferación celular en la fase G1 del ciclo celular.

**No hay un vínculo mecanístico respaldado** entre la inhibición de CDK4/6 y el hipertiroidismo. La puntuación de 99.44% proviene únicamente del grafo de conocimiento de TxGNN. No existen ensayos clínicos ni literatura sobre este uso, y la similitud con la indicación original no ha sido evaluada. Esta predicción debe tratarse como una hipótesis sin sustento y no como un candidato con fundamento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se registran 6 autorizaciones en total. Los datos disponibles incluyen 5, todas de Pfizer Europe MA EEIG. El registro no incluye texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1161147005 | IBRANCE 125 mg cápsulas duras | Cápsula dura |
| 1161147003 | IBRANCE 100 mg cápsulas duras | Cápsula dura |
| 1161147001 | IBRANCE 75 mg cápsulas duras | Cápsula dura |
| 1161147012 | IBRANCE 100 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 1161147010 | IBRANCE 75 mg comprimidos recubiertos con película | Comprimido recubierto con película |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de CDK4/6) |
| Riesgo de Mielosupresión | Alto (la neutropenia es un efecto conocido de la clase; un estudio preclínico también describe mielosupresión con palbociclib, PMID 39940918) |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

No hay datos de advertencias, contraindicaciones ni interacciones en el paquete de evidencia. Consultar el prospecto para información de seguridad.

Como referencia, la literatura recopilada para otras predicciones señala estas señales de seguridad de la clase CDK4/6:
- **Eventos tromboembólicos** (PMID 36794339, 35300061), detectados en estudios de farmacovigilancia.
- **Enfermedad pulmonar intersticial** (PMID 37994878).
- **Neutropenia y supresión de médula ósea**, los efectos adversos más habituales de la clase.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de hipertiroidismo tiene nivel L5: solo hay puntuación del modelo, sin ensayos, sin literatura y sin vínculo mecanístico plausible.

**Para avanzar se necesita:**
- Datos de la indicación original y del mecanismo de acción (DrugBank y ficha técnica de la AEMPS).
- Datos de advertencias y contraindicaciones del prospecto.
- Una revisión de literatura específica sobre CDK4/6 y patología tiroidea que justifique un vínculo biológico.

**Nota sobre otras predicciones del mismo análisis:**
- **Artritis reumatoide** (puntaje 99.36%, nivel L4, "Research Question"): es la más prometedora. Hay un caso clínico de mejoría en una paciente con cáncer de mama tratada con palbociclib (PMID 33587021) y estudios en animales sobre hiperplasia sinovial dependiente de CDK6 (PMID 25165034, 39940918). Antes de cualquier estudio clínico habría que evaluar el riesgo de inmunosupresión y neutropenia.
- **Enfermedad trombótica** (puntaje 99.32%, nivel L4, Hold): debe tratarse como una **alerta de seguridad**, no como una oportunidad terapéutica. La farmacovigilancia indica que los inhibidores de CDK4/6 se asocian a un mayor riesgo de eventos tromboembólicos.
- **Resistencia a la hormona tiroidea por mutación en TRβ** (puntaje 99.30%, nivel L5, Hold): sin datos que la respalden.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

