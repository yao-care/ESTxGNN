---
layout: default
title: Sulfanilamide
parent: Solo predicción del modelo (L5)
nav_order: 752
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
monitor_inn: "Sulfanilamide"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vulvar neoplasm", "trichomonal vulvovaginitis"]
description: "Sulfanilamide: nueva indicación predicha, Vaginitis atrófica posmenopáusica (postmenopausal atrophic vaginitis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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

## Sulfanilamide: Vaginitis atrófica posmenopáusica (postmenopausal atrophic vaginitis)
{: .text-alpha }

## Resumen en Una Frase

Sulfanilamida es una sulfonamida antibacteriana, originalmente utilizada en el tratamiento de la candidiasis vulvovaginal, la vulvovaginitis, la vaginitis y la vaginosis bacteriana.
El modelo TxGNN predice que podría ser efectiva para **vaginitis atrófica posmenopáusica**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Vaginitis atrófica posmenopáusica (postmenopausal atrophic vaginitis) |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, sulfanilamida es una sulfonamida que inhibe la dihidropteroato sintasa bacteriana (síntesis de folato). Su uso en afecciones vaginales es de larga tradición, y mecanísticamente su aplicabilidad a la nueva indicación es limitada.

La vaginitis atrófica se debe principalmente a la deficiencia de estrógenos y al adelgazamiento del epitelio, no a una infección primaria. Por ello, un mecanismo antibacteriano no tiene un vínculo terapéutico claro con esta enfermedad.

El puntaje tan alto del modelo TxGNN (aprendizaje profundo) (0.9993) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, y no evidencia biológica. La predicción debe interpretarse con cautela.

### Otras predicciones del modelo (para contexto)

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Valoración |
|------|------|------|------|
| Úlcera de la vulva | 0.9988 | L5 | Causas diversas (infecciosas, autoinmunes, Behçet); solo podría ayudar ante un componente bacteriano secundario. Sin evidencia. |
| Neoplasia vulvar | 0.9986 | L5 | No se conoce un mecanismo antineoplásico plausible; la inhibición del folato es específica de bacterias. Sin evidencia. |
| Vulvovaginitis por tricomonas | 0.9923 | L5 | Vínculo indirecto; el tratamiento de primera línea son los nitroimidazoles, mucho más eficaces. |

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
La predicción para vaginitis atrófica posmenopáusica proviene únicamente del modelo TxGNN (aprendizaje profundo) (L5), sin ensayos ni literatura, y carece de un vínculo mecanístico plausible: es una afección de origen hormonal y no infeccioso. El puntaje alto puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

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

