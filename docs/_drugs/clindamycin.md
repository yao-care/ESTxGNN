---
layout: default
title: Clindamycin
parent: Solo predicción del modelo (L5)
nav_order: 132
evidence_level: L5
indication_count: 6
---

# Clindamycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Clindamicina: De Antibiótico (indicación original no registrada) a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Clindamicina es un antibiótico comercializado en España en múltiples formas farmacéuticas (cápsulas, solución inyectable, crema vaginal, óvulos y formas cutáneas). Los datos de AEMPS suministrados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS suministrados |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99,97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 16 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según el conocimiento general, clindamicina es un antibacteriano que inhibe la subunidad ribosomal 50S. Esta acción es antibacteriana y no tiene una relación establecida con la queratoconjuntivitis epitelial punteada.

La queratoconjuntivitis epitelial punteada suele ser de origen viral o inflamatorio. Un antibacteriano no actúa sobre esas causas, por lo que el vínculo mecanístico es débil. El puntaje de 99,97% proviene únicamente de un modelo de grafos (TxGNN), sin respaldo clínico ni bibliográfico.

Por ahora esta predicción debe considerarse una hipótesis sin fundamento demostrado. Solo tendría sentido si se identificara un componente bacteriano (por ejemplo, sobreinfección) en la enfermedad.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 62911 | DALACIN 100 mg ÓVULOS | Óvulo |
| 81565 | CLINDAMICINA QUALIGEN 300 MG CÁPSULAS DURAS EFG | Cápsula dura |
| 60034 | DALACIN 20 mg/g CREMA VAGINAL | Crema vaginal |
| 81568 | CLINDAMICINA QUALIGEN 150 MG CÁPSULAS DURAS EFG | Cápsula dura |
| 63669 | CLINDAMICINA NORMON 600 mg/4 ml SOLUCIÓN INYECTABLE EFG | Solución inyectable |

Se muestran 5 de las 16 autorizaciones. El texto de la indicación aprobada no figura en los datos suministrados.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura. Además, la acción antibacteriana de clindamicina no explica un beneficio en una enfermedad habitualmente viral o inflamatoria.

**Para avanzar se necesita:**
- Prospecto de AEMPS (advertencias y contraindicaciones), que actualmente bloquea el cribado de seguridad
- Datos del mecanismo de acción desde DrugBank
- Indicación aprobada de cada autorización, para definir la indicación original
- Estudios clínicos o preclínicos que evalúen clindamicina en esta enfermedad
- Definir la vía de administración (tópica oftálmica o sistémica). Actualmente ninguna de las formas autorizadas en España es oftálmica

**Nota sobre otras predicciones:** entre las demás predicciones del modelo, "queratitis por exposición" (nivel L4, Research Question) es la que tiene mayor respaldo indirecto. Es una hipótesis limitada a la infección bacteriana secundaria, sin ningún estudio que pruebe clindamicina en esa enfermedad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

