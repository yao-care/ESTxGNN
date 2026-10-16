---
layout: default
title: Sertaconazole
parent: Solo predicción del modelo (L5)
nav_order: 732
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sertaconazole: nueva indicación predicha, Dermatofitosis de la ingle y del área perianal (nivel de evidencia L5). Indicación original: Tinea pedis (según el grafo de conocimiento"
---

# Sertaconazole
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

# Sertaconazol: De Tinea Pedis a Dermatofitosis de la Ingle y del Área Perianal

## Resumen en Una Frase

Sertaconazol es un antifúngico imidazólico de uso tópico, originalmente utilizado para el tratamiento de la tinea pedis (pie de atleta).
El modelo TxGNN predice que podría ser efectivo para **dermatofitosis de la ingle y del área perianal** (tinea cruris), pero para esta indicación concreta **no se recuperaron ensayos clínicos ni publicaciones**; la predicción se apoya únicamente en el modelo.
Como dato complementario, la segunda indicación predicha (tinea corporis) cuenta con **19 publicaciones** y varios estudios comparativos aleatorizados.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tinea pedis (según el grafo de conocimiento; los textos de indicación de las autorizaciones no están disponibles) |
| Nueva Indicación Predicha | Dermatofitosis de la ingle y del área perianal |
| Puntaje de Predicción TxGNN | 99,98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, sertaconazol es un antifúngico imidazólico que inhibe la síntesis de ergosterol (mediante la inhibición de la lanosterol 14-alfa-desmetilasa) y, gracias a su anillo de benzotiofeno, podría alterar directamente la membrana fúngica.

La tinea cruris es una infección por dermatofitos de la misma familia etiológica que la tinea pedis. Por ello, el mecanismo antifúngico es plausible para esta nueva indicación. Además, la literatura revisada sobre sertaconazol menciona que en la UE está indicado en dermatofitosis, incluyendo tinea corporis, tinea cruris y tinea pedis, por lo que se trataría de una extensión dentro de la misma clase de fármaco y la misma familia de enfermedades, con baja novedad de reposicionamiento.

Cabe subrayar que, para esta indicación específica, la evidencia es solo la predicción del modelo. Sin embargo, existe un estudio comparativo aleatorizado de terbinafina frente a sertaconazol en tinea corporis y tinea cruris (PMID 24249898), que se detalla en la sección de otras indicaciones predichas.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para dermatofitosis de la ingle y del área perianal como indicación específica.

## Otras Indicaciones Predichas con Mayor Respaldo

Para contextualizar, estas son las demás indicaciones predichas y su evidencia:

| Indicación | Puntaje TxGNN | Nivel | Decisión | Comentario |
|------|------|------|------|------|
| Tinea corporis | 99,94% | L1 | Proceed with Guardrails | Varios estudios comparativos aleatorizados frente a terbinafina, clotrimazol y eberconazol. El nivel L1 debe verificarse con los textos completos, ya que la fase 3 no se confirma en los metadatos. |
| Candidiasis cutánea | 99,63% | L2 | Proceed with Guardrails | Estudio de fase II (1992) y revisiones. |
| Micosis superficial | 99,55% | L1 | Proceed with Guardrails | Categoría amplia que incluye la indicación original; incluye un ensayo multicéntrico doble ciego frente a miconazol. No es un hallazgo de reposicionamiento realmente nuevo. |
| Pitiriasis versicolor | 99,45% | L2 | Proceed with Guardrails | Estudio clínico de 1992; diseño y fase por verificar. |
| Dermatofitosis del cuero cabelludo o la barba | 99,55% | L4 | Hold | Solo revisiones y datos in vitro. |
| Enfermedad infecciosa ectotrix, granuloma de Majocchi, enfermedad infecciosa endotrix, tinea profunda | 99,37%–99,59% | L5 | Hold | Sin ensayos ni literatura; los antifúngicos tópicos penetran mal en folículos pilosos y tejido profundo, y suelen requerir tratamiento sistémico. |

### Literatura destacada (tinea corporis / tinea cruris)

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24249898](https://pubmed.ncbi.nlm.nih.gov/24249898/) | 2013 | ECA | Indian J Dermatol | Terbinafina 1% frente a sertaconazol 2% en crema en tinea corporis y tinea cruris localizadas |
| [28066103](https://pubmed.ncbi.nlm.nih.gov/28066103/) | 2016 | ECA | Indian J Pharmacol | Sertaconazol tópico frente a terbinafina tópica en dermatofitosis localizada (tinea corporis o cruris) |
| [35068526](https://pubmed.ncbi.nlm.nih.gov/35068526/) | 2021 | ECA | Indian J Dermatol | Eficacia y seguridad de eberconazol frente a sertaconazol en infección tineal localizada |
| [18039020](https://pubmed.ncbi.nlm.nih.gov/18039020/) | 2007 | ECA | Am J Clin Dermatol | Comparación de solución y crema de sertaconazol 2% en tinea corporis, tinea pedis interdigital o candidiasis equivalente |
| [25386455](https://pubmed.ncbi.nlm.nih.gov/25386455/) | 2014 | ECA (descrito como observacional) | J Clin Diagn Res | Sertaconazol frente a clotrimazol en tinea corporis |
| [24249897](https://pubmed.ncbi.nlm.nih.gov/24249897/) | 2013 | ECA abierto | Indian J Dermatol | Sertaconazol 2% frente a butenafina 1% en infecciones tineales de la piel |
| [19275277](https://pubmed.ncbi.nlm.nih.gov/19275277/) | 2009 | Revisión | Drugs | Uso de sertaconazol en micosis superficiales en dermatología y ginecología; indicado en la UE en tinea corporis, cruris, manus, barbae y pedis |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59799 | DERMOFIX 20 MG/G POLVO CUTÁNEO | Polvo cutáneo | No disponible en los datos compilados |
| 59078 | DERMOFIX 20 MG/G CREMA | Crema | No disponible en los datos compilados |
| 59803 | DERMOFIX 20 MG/G GEL | Gel | No disponible en los datos compilados |
| 62086 | GINEDERMOFIX 500 MG COMPRIMIDO VAGINAL | Comprimido vaginal | No disponible en los datos compilados |
| 62087 | GINEDERMOFIX 2% CREMA VAGINAL | Crema vaginal | No disponible en los datos compilados |

Hay 7 autorizaciones vigentes en total, todas de monofármaco y a nombre de Ferrer Internacional S.A. (se muestran las 5 principales; las otras son DERMOFIX 20 MG/ML solución cutánea, nº 59804, y ZALAIN 20 MG/G crema, nº 59077).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se identificaron interacciones farmacológicas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para dermatofitosis de la ingle y del área perianal solo existe la predicción del modelo (nivel L5), sin ensayos ni publicaciones recuperadas específicas. La plausibilidad mecanística es alta y la tinea cruris aparece en la literatura como indicación de la UE, pero ello no sustituye la evidencia directa en los datos analizados.

**Para avanzar se necesita:**
- Verificar en el prospecto de AEMPS si la tinea cruris ya figura entre las indicaciones autorizadas (los textos de indicación y los datos de advertencias y contraindicaciones no estaban disponibles).
- Revisar a texto completo los estudios comparativos en tinea corporis/cruris (p. ej., PMID 24249898 y 28066103) para extraer los resultados específicos de tinea cruris y reevaluar el nivel de evidencia.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Completar el análisis de seguridad con el prospecto.
- Como alternativa de menor riesgo, considerar priorizar tinea corporis, que tiene mayor respaldo (L1, pendiente de verificación), teniendo en cuenta su baja novedad al tratarse de una extensión dentro de la misma familia de enfermedades.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

