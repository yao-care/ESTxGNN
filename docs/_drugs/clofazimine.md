---
layout: default
title: Clofazimine
parent: Solo predicción del modelo (L5)
nav_order: 195
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Clofazimine: nueva indicación predicha, Pneumocystosis (neumocistosis) (nivel de evidencia L5). Indicación original: Lepra (según las indicaciones del grafo de conocimiento"
monitor_inn: "Clofazimine"
predicted_indications: ["pneumocystosis", "malaria", "gastrin secretion abnormality"]
---

# Clofazimine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Clofazimina: De Lepra a Pneumocystosis
{: .text-alpha }

## Resumen en Una Frase

Clofazimina es un fármaco antimicobacteriano utilizado originalmente en el tratamiento de la lepra (incluida la lepra multibacilar) y del pioderma gangrenoso.
El modelo TxGNN predice que podría ser efectivo para **pneumocystosis (neumocistosis)**, pero actualmente **no hay ensayos clínicos** y solo **3 publicaciones** de relevancia indirecta, ninguna de las cuales demuestra actividad frente a *Pneumocystis*.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lepra (según las indicaciones del grafo de conocimiento; el texto de indicación de la autorización de AEMPS está vacío) |
| Nueva Indicación Predicha | Pneumocystosis (neumocistosis) |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, clofazimina es un colorante de tipo riminofenazina cuya eficacia en lepra, como parte de la terapia multifármaco junto con dapsona y rifampicina, ha sido comprobada. Su actividad antimicobacteriana se atribuye probablemente a alteración de membrana y ciclo redox, aunque esto no está confirmado en los datos compilados.

La neumocistosis es una infección oportunista pulmonar causada por un hongo. La relación con la indicación original es débil: la literatura recuperada trata sobre pacientes con sida en los que la clofazimina se usó contra *Mycobacterium avium* o en coinfecciones, sin mostrar actividad contra *Pneumocystis*.

Por tanto, **no se ha establecido un vínculo mecanístico creíble**. El puntaje de 99.90% es una predicción basada únicamente en el grafo de conocimiento y no debe interpretarse como evidencia de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | Ensayo clínico aleatorizado abierto (profilaxis de MAC; no específico de *Pneumocystis*) | J Infect Dis | 110 pacientes con VIH (primer episodio de neumonía por *P. carinii* o CD4 ≤100/mm³) recibieron clofazimina como profilaxis de infección diseminada por *M. avium*; no evalúa neumocistosis |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Reporte de caso | Infection | Paciente con sida con enfermedad pulmonar por *M. kansasii* complicada con neumonía por *P. carinii*; la recuperación se atribuye al tratamiento combinado, incluido trimetoprima-sulfametoxazol; coinfección, no evidencia de tratamiento |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Revisión | PI Perspective | Actualización general sobre infecciones oportunistas; sin resumen disponible ni evidencia específica de clofazimina en neumocistosis |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 48886 | LAMPREN CÁPSULAS (Novartis Farmacéutica S.A.) | Cápsula blanda | No disponible en los datos compilados |

---

## Citotoxicidad

No aplica: clofazimina es un antimicobacteriano, no un fármaco antineoplásico.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, enfermedad diarreica, enfermedad ulcerosa péptica activa, enfermedades del sistema digestivo e intestinales, infarto esplénico, enfermedad esplénica e hiperesplenismo.
- **Interacciones farmacológicas**: la consulta se completó con 1 registro, de tipo farmacológico (no una interacción fármaco-fármaco clínica): el fármaco se une a la proteína ZC3H14 (dedo de zinc CCCH 14). No se dispone de nivel de gravedad.
- Los datos compilados señalan que las advertencias y contraindicaciones del prospecto de AEMPS no se han podido obtener. Consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (L5): no hay ensayos clínicos y la literatura disponible no muestra actividad de clofazimina contra *Pneumocystis*. Además, existen alertas de seguridad gastrointestinal y hepática en el grafo de conocimiento.

**Para avanzar se necesita:**
- Estudios in vitro e in vivo de clofazimina frente a *Pneumocystis*
- Datos del mecanismo de acción original
- Obtención y revisión del prospecto de AEMPS (advertencias y contraindicaciones)
- Evaluación del beneficio-riesgo frente a las alternativas establecidas (p. ej., trimetoprima-sulfametoxazol)

---

### Nota sobre otras predicciones evaluadas

- **Malaria** (TxGNN 99.60%, nivel L4, categoría "pregunta de investigación"): solo hay evidencia preclínica indirecta, un estudio in vitro de análogos de clofazimina con actividad antiplasmodial (PMID 29026393). No hay ensayos clínicos. Justifica seguimiento preclínico, no recomendación clínica.
- **Anomalía de la secreción de gastrina** (TxGNN 99.57%, nivel L5, Hold): sin ensayos ni literatura y sin fundamento mecanístico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

