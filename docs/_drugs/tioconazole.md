---
layout: default
title: Tioconazole
parent: Solo predicción del modelo (L5)
nav_order: 796
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Tioconazole: nueva indicación predicha, Vulvovaginitis (nivel de evidencia L5). Indicación original: Candidiasis vulvovaginal"
monitor_inn: "tioconazole"
predicted_indications: ["vulvovaginitis", "vulvitis", "postmenopausal atrophic vaginitis"]
---

# Tioconazole
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

## Tioconazol: De Candidiasis Vulvovaginal a Vulvovaginitis
{: .text-alpha }

## Resumen en Una Frase

Tioconazol es un antifúngico imidazólico de uso tópico, originalmente utilizado para el tratamiento de la candidiasis vulvovaginal.
El modelo TxGNN predice que podría ser efectivo para **vulvovaginitis**, con **0 ensayos clínicos registrados** y **20 publicaciones** que respaldan esta dirección (principalmente estudios de candidiasis vaginal de las décadas de 1980 y 1990).
Se trata en esencia de un uso ya cubierto por la indicación original, más que de un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Candidiasis vulvovaginal |
| Nueva Indicación Predicha | Vulvovaginitis |
| Puntaje de Predicción TxGNN | 99,23% |
| Nivel de Evidencia | L1 (ver matices en la sección de mecanismo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento general de la clase, tioconazol es un antifúngico imidazólico que inhibe la lanosterol 14-α-desmetilasa fúngica (CYP51/ERG11), enzima que convierte el lanosterol en ergosterol, un componente esencial de la membrana celular fúngica. Sin ergosterol, el hongo no sobrevive. Los datos farmacológicos compilados indican además que tioconazol inhibe la enzima humana CYP8B1, implicada en la síntesis de ácidos biliares.

La candidiasis vulvovaginal es una forma frecuente de vulvovaginitis, por lo que la predicción es coherente: la vulvovaginitis candidiásica es la indicación original. Por ello no es un reposicionamiento genuino, sino un uso dentro de la indicación conocida.

**Matiz sobre el nivel L1:** no hay ensayos registrados y la literatura es antigua (1983-1988). El nivel L1 se apoya en estudios aleatorizados o controlados (doble ciego frente a placebo y comparativos con clotrimazol) cuya fase no se indica en los datos. Debe leerse como evidencia directa controlada para la indicación en ficha, no como una confirmación de ECA de Fase 3.

Respecto a las otras predicciones del modelo: la **vulvitis** (puntaje 99,20%, nivel L3) solo está respaldada de forma indirecta y únicamente en su forma candidiásica; la **vaginitis atrófica posmenopáusica** (puntaje 99,19%, nivel L5, Hold) carece de mecanismo plausible, ya que su causa es el déficit estrogénico, y su puntaje probablemente refleja proximidad en el grafo con otros diagnósticos de vaginitis.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | ECA | Antimicrob Agents Chemother | 80 pacientes: dosis única de tioconazol 6,5% vs clotrimazol 3 días; 84% vs 85% asintomáticas a las 4 semanas |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | ECA | Gynakol Rundsch | Comparación doble ciego de tioconazol frente a placebo en candidiasis vaginal, con evaluación de absorción sistémica |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Revisión | Drugs | Amplio espectro in vitro; ensayos abiertos y controlados demuestran eficacia y seguridad tópica en micosis superficiales y candidiasis vaginal |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Revisión | Expert Rev Anti Infect Ther | Opciones azólicas no invasivas futuras para candidiasis vulvovaginal, incluida la recurrente |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Ensayo aleatorizado abierto | J Int Med Res | 40 pacientes: tioconazol tópico 6% en dosis única vs ketoconazol oral 5 días; ambos eficaces, con respuesta sintomática más rápida con tioconazol |
| [3216880](https://pubmed.ncbi.nlm.nih.gov/3216880/) | 1988 | Estudio clínico | Mycoses | Tioconazol en el tratamiento de la candidosis vaginal |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Ensayo comparativo abierto | Gynakol Rundsch | Tioconazol vs econazol en tratamiento de 3 días de candidiasis vaginal |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | Ensayo comparativo abierto | Gynakol Rundsch | Crema de tioconazol vs óvulos de econazol en tratamiento de 3 días |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Estudio clínico | Acta Obstet Gynecol Scand | Crema vaginal de tioconazol 2%: curación micológica del 88,5% en mujeres sintomáticas |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Estudio abierto no comparativo | J Int Med Res | 20 pacientes con T. vaginalis o infecciones mixtas; curación del 95% con crema al 2% durante 3 días |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 67439 | TIOCONAZOL KORHISPANA 280 mg/ml BARNIZ DE UÑAS MEDICAMENTOSO EFG | Barniz de uñas medicamentoso | No disponible |
| 58758 | TROSID 280 mg/ml BARNIZ DE UÑAS MEDICAMENTOSO | Barniz de uñas medicamentoso | No disponible |
| 70801 | SERNAX 280 mg/ml SOLUCIÓN CUTÁNEA EFG | Solución cutánea | No disponible |

Nota: las tres autorizaciones españolas vigentes corresponden a formulaciones tópicas de 280 mg/ml (barniz de uñas y solución cutánea), no a formas vaginales. La evidencia de literatura se refiere a cremas y ungüentos vaginales, por lo que la compatibilidad de vía y forma farmacéutica con la indicación vulvovaginal debe confirmarse.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (2 registros):
  - Omeprazol: nivel de gravedad desconocido (fuente: DDInter).
  - CYP8B1: tioconazol inhibe esta enzima humana de la síntesis de ácidos biliares (dato farmacológico, no una interacción clínica clasificada).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La indicación predicha coincide en esencia con el uso original (candidiasis vulvovaginal) y cuenta con estudios controlados, aunque antiguos, que respaldan eficacia y tolerabilidad. Las limitaciones son la ausencia de ensayos registrados, la antigüedad de la evidencia y que los productos autorizados en España son de uso cutáneo y no vaginal.

**Para avanzar se necesita:**
- Revisar el prospecto de AEMPS (advertencias y contraindicaciones) y confirmar las indicaciones aprobadas de cada autorización.
- Obtener datos detallados del mecanismo de acción desde fuentes primarias.
- Confirmar la disponibilidad de una forma farmacéutica vaginal adecuada en España.
- Restringir la recomendación a la vulvovaginitis candidiásica; no extrapolar a vulvitis no infecciosa ni a vaginitis atrófica posmenopáusica (esta última, Hold).
- Complementar con evidencia más reciente, dado que gran parte de la literatura es de 1983-1988.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

