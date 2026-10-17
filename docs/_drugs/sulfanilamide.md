---
layout: default
title: Sulfanilamide
parent: Solo predicción del modelo (L5)
nav_order: 752
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Sulfanilamide: nueva indicación predicha, Vaginitis atrófica posmenopáusica (nivel de evidencia L5). Indicación original: Candidiasis vulvovaginal, vulvovaginitis…"
monitor_inn: "Sulfanilamide"
predicted_indications: ["ulceration of vulva", "vulvar neoplasm"]
---

# Sulfanilamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Sulfanilamida: De Candidiasis Vulvovaginal a Vaginitis Atrófica Posmenopáusica

## Resumen en Una Frase

Sulfanilamida es una sulfonamida antibacteriana, originalmente utilizada en el tratamiento de la candidiasis vulvovaginal, la vulvovaginitis, la vaginitis y la vaginosis bacteriana.
El modelo TxGNN predice que podría ser efectiva para **vaginitis atrófica posmenopáusica**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Candidiasis vulvovaginal, vulvovaginitis, vaginitis y vaginosis bacteriana (según el grafo de conocimiento; el texto de indicación de la autorización en AEMPS está vacío) |
| Nueva Indicación Predicha | Vaginitis atrófica posmenopáusica |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, sulfanilamida es una sulfonamida que inhibe la dihidropteroato sintasa bacteriana (síntesis de folato). Su uso en afecciones vaginales es de larga tradición, y mecanísticamente su aplicabilidad a la nueva indicación es limitada.

La vaginitis atrófica se debe principalmente a la deficiencia de estrógenos y al adelgazamiento del epitelio, no a una infección primaria. Por ello, un mecanismo antibacteriano no tiene un vínculo terapéutico claro con esta enfermedad.

El puntaje tan alto del modelo (99.93%) probablemente refleja la cercanía en el grafo de conocimiento con las indicaciones de vaginitis ya aprobadas, y no una señal basada en el mecanismo. La predicción debe interpretarse con cautela.

### Otras predicciones del modelo (para contexto)

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Valoración |
|------|------|------|------|
| Úlcera de la vulva | 99.88% | L5 | Causas diversas (infecciosas, autoinmunes, Behçet); solo podría ayudar ante un componente bacteriano secundario. Sin evidencia. |
| Neoplasia vulvar | 99.86% | L5 | No se conoce un mecanismo antineoplásico plausible; la inhibición del folato es específica de bacterias. Sin evidencia. |
| Vulvovaginitis por tricomonas | 99.23% | L4 | Vínculo indirecto; el tratamiento de primera línea son los nitroimidazoles, mucho más eficaces. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para la indicación principal (vaginitis atrófica posmenopáusica) actualmente no hay literatura relacionada disponible.

Para la predicción de rango 4 (vulvovaginitis por tricomonas) se recuperó un artículo:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7330756](https://pubmed.ncbi.nlm.nih.gov/7330756/) | 1981 | Revisión | Sexually Transmitted Diseases | Revisa el tratamiento actual de la vulvovaginitis: la tricomoniasis se trata de forma fiable con una dosis única de 2 g de metronidazol; los antifúngicos imidazólicos tópicos son superiores a los poliénicos en la candidiasis vulvovaginal. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 35027 | AZOL POLVO (Kern Pharma S.L.) | Polvo cutáneo | No se dispone del texto de indicación |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): porfiria (incluida la hereditaria) y enfermedades del metabolismo de las porfirinas, enfermedad renal, piouréter, enfermedades hematológicas, enfermedad hepática, enfermedad de la vesícula biliar, deficiencia de G6PD, enfermedad por depósito de glucógeno, cistinuria y galactosemia.

Para la información de seguridad completa (advertencias, contraindicaciones oficiales e interacciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para vaginitis atrófica posmenopáusica se basa únicamente en el modelo (L5), sin ensayos ni literatura, y carece de un vínculo mecanístico plausible: es una afección de origen hormonal y no infeccioso. El puntaje alto parece reflejar proximidad en el grafo con las indicaciones de vaginitis ya conocidas.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones oficiales del prospecto de AEMPS, para poder realizar el cribado de seguridad
- Texto de la indicación aprobada de la autorización 35027
- Estudios preclínicos o clínicos que respalden un efecto en la vaginitis atrófica (por ejemplo, un componente bacteriano secundario)
- Evaluación de compatibilidad de la vía de administración (polvo cutáneo frente a uso vaginal)
- Si se desea priorizar otra indicación, la vulvovaginitis por tricomonas podría explorarse como pregunta de investigación, aunque los nitroimidazoles son claramente superiores
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

