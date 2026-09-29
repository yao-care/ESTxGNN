---
layout: default
title: Dexchlorpheniramine
parent: Solo predicción del modelo (L5)
nav_order: 171
evidence_level: L5
indication_count: 2
---

# Dexchlorpheniramine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Dexclorfeniramina: De Antihistamínico H1 sin Indicación Registrada a Urticaria Alérgica

## Resumen en Una Frase

La dexclorfeniramina es un antihistamínico H1 de primera generación comercializado en España. Los datos recibidos no incluyen indicaciones originales registradas.
El modelo TxGNN predice que podría ser efectiva para la **urticaria alérgica**,
pero actualmente hay **0 ensayos clínicos** registrados y **6 publicaciones** recuperadas, en su mayoría estudios farmacodinámicos o de relevancia indirecta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (sin texto de indicación en las autorizaciones ni en DrugBank) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99,89 % |
| Nivel de Evidencia | L3 (estudios farmacodinámicos con marcadores indirectos; sin resultados clínicos de urticaria) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, la dexclorfeniramina es un antagonista del receptor H1 (agonista inverso) de primera generación. Mecanísticamente podría ser aplicable a la urticaria alérgica.

En la urticaria alérgica, la histamina liberada por los mastocitos provoca el habón, el eritema circundante y el prurito. Bloquear el receptor H1 es por tanto una vía plausible, y el puntaje muy alto de TxGNN (0,999) es coherente con este efecto de clase.

Dos estudios farmacodinámicos (PMID 39265704 y 29723372) miden la supresión del habón y el eritema inducidos por histamina. Son marcadores indirectos, no resultados clínicos de urticaria como escalas de síntomas o UAS7. Como no hay indicaciones originales ni MOA en los datos, no se pudo comparar con la indicación base del fármaco.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | ECA fase I | Eur J Pharm Sci | Compara bilastina oral, dexclorfeniramina parenteral y una nueva formulación parenteral de bilastina en la inhibición del habón y el eritema por histamina. La dexclorfeniramina actúa como comparador. |
| [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) | 2018 | Estudio farmacodinámico | An Bras Dermatol | Compara la supresión del habón y el eritema en la prueba de histamina por los principales antihistamínicos H1 comercializados en Brasil. |
| [28601540](https://pubmed.ncbi.nlm.nih.gov/28601540/) | 2017 | Revisión / reporte de caso | Am J Med | Fibrilación auricular en anafilaxia. Relevancia indirecta. |
| [26179134](https://pubmed.ncbi.nlm.nih.gov/26179134/) | 2015 | Reporte de caso | Contact Dermatitis | Angioedema palpebral y dermatitis alérgica de contacto por un cerumenolítico. Relevancia indirecta (sin resumen disponible). |
| [39803](https://pubmed.ncbi.nlm.nih.gov/39803/) | 1979 | Estudio clínico/inmunológico | Dermatologica | Caso de urticaria por contacto con calor adquirida. Estudio pequeño y antiguo. |
| [2523357](https://pubmed.ncbi.nlm.nih.gov/2523357/) | 1989 | In vitro | Int Arch Allergy Appl Immunol | Efecto de la cetirizina sobre la quimiotaxis de eosinófilos y la estimulación plaquetaria dependiente de IgE. Solo mecanístico, y con otro fármaco. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 75389 | Dexclorfeniramina Maleato Accord 5 mg/ml solución inyectable EFG | Solución inyectable | Accord Healthcare S.L.U. |
| 40135 | Polaramine 5 mg/ml solución inyectable | Solución inyectable | Laboratorios Farmacéuticos Rovi S.A. |
| 31195 | Polaramine 2 mg comprimidos | Comprimido | Laboratorios Farmacéuticos Rovi S.A. |
| 32801 | Polaramine 0,4 mg/ml jarabe | Jarabe | Laboratorios Farmacéuticos Rovi S.A. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente plausible, pero la evidencia se limita a marcadores farmacodinámicos indirectos, sin ensayos clínicos registrados ni resultados clínicos en urticaria. Además, faltan las advertencias y contraindicaciones de la ficha técnica de la AEMPS, lo que bloquea el cribado de seguridad. La segunda predicción, urticaria por frío (TxGNN 99,61 %), no tiene ensayos ni literatura y se mantiene solo como hipótesis (Hold).

**Para avanzar se necesita:**
- Obtener y analizar el prospecto/ficha técnica de la AEMPS (advertencias y contraindicaciones).
- Completar el mecanismo de acción y las indicaciones autorizadas para establecer la línea base.
- Buscar estudios clínicos con resultados de urticaria (escalas de síntomas, UAS7) para la dexclorfeniramina.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

