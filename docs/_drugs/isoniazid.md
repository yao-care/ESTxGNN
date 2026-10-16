---
layout: default
title: Isoniazid
parent: Evidencia moderada (L3-L4)
nav_order: 432
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Isoniazid: nueva indicación predicha, Conjuntivitis (nivel de evidencia L4). Indicación original: Tuberculosis pulmonar (según el grafo de conocimiento"
monitor_inn: "isoniazid"
predicted_indications: ["conjunctivitis"]
---

# Isoniazid
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Isoniazida: De Tuberculosis Pulmonar a Conjuntivitis

## Resumen en Una Frase

Isoniazida es un fármaco antituberculoso, utilizado originalmente para el tratamiento de la tuberculosis pulmonar.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis**, pero actualmente no hay ensayos clínicos registrados y las **12 publicaciones** recuperadas son en su mayoría informes de casos o revisiones que no demuestran eficacia.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tuberculosis pulmonar (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Conjuntivitis |
| Puntaje de Predicción TxGNN | 99.36% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la isoniazida es un agente antituberculoso con acción bactericida frente a *Mycobacterium tuberculosis*, mediante la inhibición de la síntesis de ácidos micólicos. Su eficacia en tuberculosis está comprobada.

El único vínculo plausible con la conjuntivitis es indirecto: la enfermedad ocular asociada a la tuberculosis, en concreto la queratoconjuntivitis flictenular (una reacción de hipersensibilidad a antígenos micobacterianos) y la tuberculosis conjuntival primaria. En esos casos la isoniazida trata o previene la infección micobacteriana subyacente, no la conjuntivitis en general.

No hay evidencia de actividad frente a conjuntivitis bacteriana, vírica o alérgica común. El puntaje elevado de TxGNN (99.36%) es una predicción computacional y probablemente refleja la cercanía en el grafo con cuadros oculares relacionados con la tuberculosis. Varias de las publicaciones recuperadas tratan de efectos adversos oculares o sistémicos, o de artritis reactiva por BCG, y no respaldan la eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Cohorte / profilaxis | Am Rev Respir Dis | Estudio de campo de profilaxis con isoniazida para queratoconjuntivitis flictenular en población esquimal de Alaska; es el estudio más cercano a una señal de eficacia, pero es antiguo y sin resumen disponible |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Reporte de caso y revisión | Medicine | Queratoconjuntivitis flictenular pediátrica asociada a tuberculosis sinonasal primaria |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Serie de casos | Oftalmologia | 28 casos de queratoconjuntivitis tuberculosa, muchos en niños con tuberculosis primaria |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Reporte de caso | Arch Ophthalmol | Tuberculosis primaria de la conjuntiva |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Sin clasificar | Annales d'oculistique | Uso local de isoniazida en tuberculosis ocular (sin resumen disponible) |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | Reporte/serie de casos | Rev Rhum (Engl Ed) | Artropatía refractaria tras BCG intravesical; se discute la utilidad de isoniazida (no es conjuntivitis) |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Revisión | Optom Clin | Efectos adversos oculares de fármacos sistémicos; relevante para seguridad, no para eficacia |
| [10084173](https://pubmed.ncbi.nlm.nih.gov/10084173/) | 1999 | Reporte de caso y revisión | Rev Rhum (Engl Ed) | Poliartritis tras BCG intravesical; la conjuntivitis aparece como parte de un síndrome reactivo |
| [12226788](https://pubmed.ncbi.nlm.nih.gov/12226788/) | 2002 | Reporte de caso | Dtsch Med Wochenschr | Artritis reactiva crónica con conjuntivitis tras BCG |
| [8136810](https://pubmed.ncbi.nlm.nih.gov/8136810/) | 1993 | Serie de casos | Rev Rhum (Ed Fr) | Poliartritis en 4 pacientes tratados con BCG intravesical |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 18697 | CEMIDON 60 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible |
| 63335 | CEMIDON B6 300 MG/50 MG COMPRIMIDOS | Comprimido | No disponible |
| 54213 | RIFINAH 300 MG/150 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto | No disponible |
| 40689 | CEMIDON B6 150 MG/25 MG COMPRIMIDOS | Comprimido | No disponible |
| 38394 | CEMIDON B6 50 MG/15 MG COMPRIMIDOS | Comprimido | No disponible |

Hay 7 autorizaciones vigentes en total; se muestran las 5 principales.

## Consideraciones de Seguridad

- **Contraindicaciones o precauciones según el grafo de conocimiento** (no proceden del prospecto): insuficiencia hepática y hepatopatías (incluida hepatitis e insuficiencia hepática aguda), porfiria, enfermedad de la vesícula biliar, diabetes mellitus y cetoacidosis diabética, gota, enfermedad del sistema nervioso periférico y neuropatía periférica, abuso/dependencia de sustancias y acetilación lenta.
- **Interacciones farmacológicas**: se identificaron 242 interacciones en total. Entre las mostradas predominan las de nivel moderado, por ejemplo con antidiabéticos (acarbosa, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina), metronidazol, budesonida, vitamina D y derivados (colecalciferol, calcifediol, calcitriol), alosetrón y ácido picosulfúrico. Las interacciones con corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona) son de nivel menor.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L4, sin ensayos clínicos) y la literatura es mayoritariamente de casos o de seguridad. El único hallazgo cercano es un estudio de profilaxis de 1965 en queratoconjuntivitis flictenular, que es de origen tuberculoso y no equivale a conjuntivitis en general.

**Para avanzar se necesita:**
- Acotar la indicación a conjuntivitis de origen tuberculoso o queratoconjuntivitis flictenular, en lugar de conjuntivitis general.
- Datos del mecanismo de acción y del texto de indicaciones aprobadas.
- Advertencias y contraindicaciones del prospecto de la AEMPS (dato bloqueante para el cribado de seguridad).
- Revisión crítica del estudio de 1965 y búsqueda de estudios más recientes.
- Evaluación de la compatibilidad de vías de administración (la vía oftálmica no está respaldada por las formas autorizadas).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

