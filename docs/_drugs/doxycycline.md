---
layout: default
title: Doxycycline
parent: Evidencia moderada (L3-L4)
nav_order: 265
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Doxycycline: nueva indicación predicha, Queratoconjuntivitis epitelial punctata (nivel de evidencia L4). Indicación original: Bronquitis, acné, neumonía bacteriana, ántrax…"
monitor_inn: "doxycycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "exposure keratitis", "chronic gingivitis"]
---

# Doxycycline
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

# Doxiciclina: De Bronquitis, Acné y Neumonía Bacteriana a Queratoconjuntivitis Epitelial Punctata

## Resumen en Una Frase

La doxiciclina es un antibiótico de la familia de las tetraciclinas, utilizado originalmente para infecciones bacterianas como bronquitis, neumonía bacteriana y acné.
El modelo TxGNN predice que podría ser efectiva para la **queratoconjuntivitis epitelial punctata**, pero actualmente solo hay **0 ensayos clínicos** y **1 publicación** (un reporte de casos de 1992) que mencionan esta dirección, de modo que la evidencia es muy débil.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Bronquitis, acné, neumonía bacteriana, ántrax, gonorrea y otras infecciones (según el grafo de conocimiento del modelo; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punctata |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 14 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según lo conocido, la doxiciclina es una tetraciclina de amplio espectro con eficacia comprobada en infecciones bacterianas. Es activa frente a *Chlamydia trachomatis*, y mecanísticamente podría ser aplicable a la inflamación de la superficie ocular.

La relación con la indicación original es indirecta. La queratoconjuntivitis epitelial punctata suele asociarse a infecciones oculares, entre ellas las causadas por clamidia, un patógeno que la doxiciclina trata. Además, la doxiciclina tiene propiedades antiinflamatorias y de inhibición de metaloproteinasas de matriz (MMP), que podrían ayudar a controlar la inflamación corneal.

El puntaje de 99.94% (posición 509 en el ranking del modelo) no cuenta con respaldo clínico. El único registro de apoyo es un reporte anecdótico que no demuestra beneficio del fármaco. Por ello, la predicción debe considerarse una hipótesis a investigar y no una indicación respaldada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Reporte de casos | Cornea | Dos casos de conjuntivitis folicular por *C. trachomatis* tratados con tetraciclina oral o doxiciclina. Los folículos se resolvieron, pero después aparecieron lesiones epiteliales corneales punteadas recurrentes y bilaterales. Describe la queratitis persistente tras el tratamiento, no un beneficio de la doxiciclina. |

## Información de Mercado en España

El estado de mercado es "Comercializado", con 14 autorizaciones vigentes (14 de producto único, 0 combinaciones, 0 canceladas). A continuación se listan 5 de ellas. Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 61227 | PRODERMA 200 mg cápsulas duras | Cápsula dura | Industrial Farmacéutica Cantabria S.A. |
| 50521 | VIBRAVENOSA 100 mg solución inyectable y para perfusión | Solución inyectable | Hospira Invicta S.A. |
| 47831 | DOXITÉN BIO 100 mg cápsulas | Cápsula dura | Teofarma S.R.L. |
| 46554 | VIBRACINA 10 mg/ml suspensión oral | Suspensión oral | Hospira Invicta S.A. |
| 73622 | ORACEA 40 mg cápsulas duras de liberación modificada | Cápsula dura de liberación modificada | Laboratorios Galderma S.A. |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): colitis por *Clostridium difficile*, enterocolitis necrosante perinatal y discinesia esofágica.
- **Interacciones farmacológicas**: se identificaron 471 interacciones en total. Entre las 20 revisadas:
  - **Mayores**: isotretinoína, acitretina y ácido aminolevulínico.
  - **Moderadas**: hidróxido de aluminio, amoxicilina, ampicilina, aminofilina y asparaginasa, entre otras.
  - **Menores**: acetazolamida, amilorida y bendroflumetiazida, entre otras.
- Hay una señal de seguridad en estudios *in vitro*: las tetraciclinas mostraron citotoxicidad en fibroblastos de membrana timpánica humana, aunque menor que la de las quinolonas. Es relevante solo si se considerara una vía tópica en el oído.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la única publicación es un reporte de dos casos de 1992, que no demuestra beneficio de la doxiciclina. El puntaje alto del modelo no está respaldado por evidencia clínica, por lo que no se justifica avanzar por ahora.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre doxiciclina en queratitis y queratoconjuntivitis, incluida la clamidial.
- Estudios preclínicos o clínicos pequeños que evalúen el efecto antiinflamatorio y de inhibición de MMP en la superficie ocular.
- Definir la vía de administración (sistémica u ocular tópica) y su compatibilidad con las formas farmacéuticas disponibles en España.
- Datos del mecanismo de acción y las advertencias y contraindicaciones oficiales del prospecto de la AEMPS.
- Evaluar la relevancia de la resistencia a tetraciclinas y las interacciones farmacológicas en la población objetivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

