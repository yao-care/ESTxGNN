---
layout: default
title: Ciprofloxacin
parent: Evidencia moderada (L3-L4)
nav_order: 128
evidence_level: L4
indication_count: 10
---

# Ciprofloxacin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Ciprofloxacino: De Antibacteriano Fluoroquinolónico a Esclerodermia Difusa

## Resumen en Una Frase

Ciprofloxacino es un antibiótico fluoroquinolónico comercializado en España en varias formas farmacéuticas. El texto de indicación aprobada no figura en los datos de AEMPS recibidos.
El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa**, aunque actualmente hay **0 ensayos clínicos** registrados y **2 publicaciones** de respaldo débil.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS recibidos (los textos de indicación vienen vacíos) |
| Nueva Indicación Predicha | Esclerodermia difusa |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, ciprofloxacino pertenece a la clase de las fluoroquinolonas, que inhiben la ADN girasa y la topoisomerasa IV bacterianas. Su eficacia antibacteriana está bien establecida, pero ese mecanismo no explica por sí solo un efecto en una enfermedad autoinmune como la esclerodermia.

La literatura recuperada sugiere dos vías plausibles, ambas con respaldo débil:

1. **Efecto antifibrótico en la piel.** Un estudio publicado en 2010 evaluó ciprofloxacino oral como antifibrótico en la piel de pacientes con esclerodermia (PMID 20507401). El fragmento del resumen disponible menciona un ensayo controlado, doble ciego y aleatorizado. Sin embargo, la clasificación automática lo marca como preclínico/ex vivo con diseño sin verificar, y los resultados no están en el extracto.
2. **Tratamiento del sobrecrecimiento bacteriano del intestino delgado (SIBO).** Es una complicación frecuente en la esclerosis sistémica. El estudio de 1995 (PMID 7728404) es sobre todo de detección de SIBO, no un ensayo de tratamiento. En ese caso, el beneficio sería sobre una complicación y no sobre la enfermedad de fondo.

Ninguna de las dos vías constituye evidencia clínica directa de beneficio en esclerodermia difusa. El puntaje TxGNN es muy alto, pero por sí solo no eleva el nivel de evidencia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Preclínico/ex vivo según la clasificación (diseño sin verificar; el resumen menciona un ensayo aleatorizado doble ciego) | The Journal of Dermatology | Evalúa si ciprofloxacino oral reduce la gravedad de la esclerodermia como antifibrótico cutáneo. Los resultados no figuran en el extracto disponible. |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Cohorte diagnóstica | British Journal of Rheumatology | 24 pacientes con esclerosis sistémica y síntomas de malabsorción, estudiados con aspiración yeyunal para detectar sobrecrecimiento bacteriano del intestino delgado. El estudio se centra en la detección; los resultados del tratamiento no figuran en el extracto. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 58407 | Ciprofloxacino Tarbis 250 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 62709 | Ciprofloxacino Pensa 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 65447 | Ciprofloxacino Vir Pharma 750 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 61521 | Septocipro Ótico 1 mg gotas óticas en solución en envase unidosis | Gotas óticas en solución |
| 80160 | Ciprofloxacino Aurovitas 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

De las 20 autorizaciones, se muestran las 5 principales. Los registros no incluyen el texto de la indicación aprobada. Además de los comprimidos y las gotas óticas, existen formas de solución para perfusión, colirio en solución y suspensión oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya en solo dos publicaciones de valor limitado, sin ensayos clínicos registrados y con diseño sin verificar en la más relevante. El nivel de evidencia es L4 y no hay datos de seguridad locales para evaluar el balance beneficio-riesgo.

**Para avanzar se necesita:**
- Verificar el diseño, la población y los resultados del estudio PMID 20507401, ya que su resumen menciona un ensayo aleatorizado doble ciego. Si se confirma y es positivo, el nivel de evidencia podría revisarse.
- Descargar y revisar el prospecto de AEMPS (advertencias y contraindicaciones), pendiente y bloqueante para el cribado de seguridad.
- Obtener los datos de mecanismo de acción desde DrugBank y analizar el vínculo mecanístico con la fibrosis cutánea.
- Confirmar la indicación original aprobada, que el Evidence Pack no incluye.

*Nota:* entre las otras predicciones del paquete, la peste septicémica tiene evidencia L1 (ensayo aleatorizado en peste bubónica). Es probable que ya sea una indicación establecida y no un reposicionamiento real.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

