---
layout: default
title: Etonogestrel
parent: Solo predicción del modelo (L5)
nav_order: 317
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Etonogestrel: nueva indicación predicha, Amenorrea (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (la autorización no incluye tex…"
monitor_inn: "ETONOGESTREL"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia"]
---

# Etonogestrel
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Etonogestrel: De Anticoncepción (implante) a Amenorrea

## Resumen en Una Frase

Etonogestrel es un progestágeno (metabolito activo del desogestrel) que se comercializa en España como implante subdérmico (Implanon NXT).
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero actualmente hay **0 ensayos clínicos** y solo **1 publicación** sin relación directa con esta indicación, por lo que la evidencia se limita a la predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (la autorización no incluye texto de indicación) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, etonogestrel es un progestágeno potente que suprime la ovulación y adelgaza el endometrio.

La amenorrea es un efecto frecuente y conocido del implante de etonogestrel, por lo que la asociación es biológicamente plausible. Sin embargo, se trata de un efecto esperado sobre el patrón de sangrado, no de una indicación terapéutica: el fármaco no está establecido como tratamiento de la amenorrea (de hecho, la amenorrea es un efecto secundario o resultado de su uso).

El puntaje alto de TxGNN probablemente refleja esta asociación farmacológica y no una verdadera señal de reposicionamiento. Otras predicciones del modelo (enfermedad fibroquística de la mama, adenosis apocrina, adenosis de conductos romos y displasia mamaria benigna, con puntajes de 99.2%–99.6%) se apoyan en una justificación hormonal teórica, también sin datos clínicos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | Protocolo de ECA (tema no relacionado) | Trials | Protocolo del estudio COVA sobre BIO101 para prevenir el deterioro respiratorio en COVID-19; no guarda relación con etonogestrel ni con amenorrea |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62628 | IMPLANON NXT 68 mg IMPLANTE | Implante | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (no proceden del prospecto)**: hipertensión, epilepsia, trastornos de ansiedad y neuróticos, distimia, porfirias, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico, asma, diabetes mellitus y cetoacidosis diabética, hipertrigliceridemia, hiperlipidemia, carcinoma de mama femenino, tromboflebitis, migraña, enfermedad coronaria y obesidad, entre otras.
- **Interacciones Farmacológicas** (100 registradas; interacciones de nivel moderado, entre ellas): antidiabéticos (acarbosa, metformina, glimepirida, clorpropamida, inhibidores de SGLT2 como canagliflozina, dapagliflozina y empagliflozina, inhibidores de DPP-4 como alogliptina y saxagliptina, agonistas de GLP-1 como semaglutida, dulaglutida y albiglutida), insulinas (aspart, degludec, detemir, glargina, glulisina), aprepitant, claritromicina y linaclotida.

Para la información de seguridad completa, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura relevante. Además, la amenorrea es un efecto esperado del implante y no una indicación terapéutica, por lo que el puntaje alto probablemente no representa una oportunidad real de reposicionamiento.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación autorizada), ya que su ausencia impide el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir si se busca un beneficio terapéutico (p. ej., en sangrado uterino anómalo o patología mamaria benigna) distinto del efecto secundario conocido.
- Buscar literatura y ensayos específicos para las indicaciones predichas de patología mamaria benigna.
- Evaluar la compatibilidad de la vía de administración (implante) con las indicaciones propuestas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

