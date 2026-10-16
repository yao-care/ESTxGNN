---
layout: default
title: Tinidazole
parent: Solo predicción del modelo (L5)
nav_order: 795
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tinidazole: nueva indicación predicha, Vaginitis atrófica posmenopáusica (nivel de evidencia L5). Indicación original: Giardiasis, vaginosis bacteriana, vaginitis, vulvitis, vulvovaginitis…"
monitor_inn: "Tinidazole"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vulvar neoplasm", "breast fibrocystic disease", "AIDS", "apocrine adenosis of breast", "blunt duct adenosis of breast", "congenital human immunodeficiency virus", "AIDS related complex", "benign mammary dysplasia"]
---

# Tinidazole
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

# Tinidazol: De Giardiasis y Vaginosis Bacteriana a Vaginitis Atrófica Posmenopáusica

## Resumen en Una Frase

Tinidazol es un antimicrobiano de la familia de los 5-nitroimidazoles, utilizado originalmente para tratar infecciones por protozoos y bacterias anaerobias (giardiasis, amebiasis, tricomoniasis, vaginosis bacteriana).
El modelo TxGNN predice que podría ser efectivo para **vaginitis atrófica posmenopáusica**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección concreta; la predicción se basa solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Giardiasis, vaginosis bacteriana, vaginitis, vulvitis, vulvovaginitis, amebiasis por *Entamoeba histolytica* y tricomoniasis (según el grafo de conocimiento; el texto de indicación de la autorización española no está disponible) |
| Nueva Indicación Predicha | Vaginitis atrófica posmenopáusica |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, tinidazol pertenece a la clase de los 5-nitroimidazoles, su eficacia en infecciones vaginales por *Trichomonas* y vaginosis bacteriana está establecida, y mecanísticamente su utilidad se limitaría a escenarios con componente infeccioso.

La vaginitis atrófica posmenopáusica se debe principalmente a la deficiencia de estrógenos y no a una infección. Por ello, el mecanismo antimicrobiano difícilmente abordaría la patología central; en el mejor de los casos, el beneficio se limitaría a infecciones secundarias.

El alto puntaje de TxGNN probablemente refleja la cercanía en la red del conocimiento con las indicaciones vaginales ya existentes (vaginitis, vulvovaginitis), más que un vínculo biológico demostrado. Esta predicción debe interpretarse con cautela.

### Otras predicciones del modelo (contexto)

| Rank | Indicación predicha | Puntaje TxGNN | Nivel de evidencia |
|------|------|------|------|
| 2 | Ulceración de la vulva | 99.87% | L5 |
| 3 | Neoplasia vulvar | 99.86% | L5 |
| 4 | Enfermedad fibroquística de la mama | 99.75% | L5 |
| 5 | SIDA | 99.69% | L4 |

Ninguna cuenta con evidencia clínica directa. En el caso del SIDA, la literatura solo respalda un beneficio indirecto (tratar coinfecciones como amebiasis, tricomoniasis o giardiasis), no una actividad antirretroviral.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para vaginitis atrófica posmenopáusica.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para vaginitis atrófica posmenopáusica.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52568 | TRICOLAM COMPRIMIDOS (Farmasierra Laboratorios S.L.) | Comprimido recubierto | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (grafo de conocimiento, no texto del prospecto)**: epilepsia, neutropenia, agranulocitosis, enfermedad del sistema nervioso periférico y neuropatía periférica.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones; las 20 mostradas son todas de nivel moderado, entre ellas paclitaxel, adalimumab, trastuzumab emtansina, etinilestradiol, etanol, estradiol, amiodarona, amobarbital, apalutamida, atorvastatina, auranofina, bexaroteno, bortezomib, brentuximab vedotina, brigatinib, butalbital, cabazitaxel, capecitabina, levodopa y abametapir (tópico). Destaca la interacción con etanol y con estrógenos, relevante para la población posmenopáusica.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y literatura, y su racionalidad biológica es débil: la vaginitis atrófica es de origen hormonal, no infeccioso. El puntaje alto parece un artefacto de proximidad en el grafo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y análisis del vínculo mecanístico
- Advertencias y contraindicaciones del prospecto de la AEMPS (texto de indicación incluido), pendientes de obtener
- Evidencia clínica o preclínica de que un componente infeccioso anaerobio/protozoario contribuya a la vaginitis atrófica
- Evaluación de compatibilidad de vía de administración
- Revisión de seguridad dados los riesgos señalados (neutropenia, neuropatía, epilepsia) y las interacciones
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

