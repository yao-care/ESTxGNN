---
layout: default
title: Mizolastine
parent: Solo predicción del modelo (L5)
nav_order: 537
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mizolastine: nueva indicación predicha, Porfiria aguda intermitente (nivel de evidencia L5). Indicación original: Rinitis alérgica y rinitis vasomotora (según las relaciones de indica…"
---

# Mizolastine
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

# Mizolastina: De Rinitis Alérgica a Porfiria Aguda Intermitente

## Resumen en Una Frase

Mizolastina es un antihistamínico H1 de segunda generación, utilizado originalmente para el tratamiento de la rinitis alérgica y la rinitis vasomotora.
El modelo TxGNN predice que podría ser efectivo para **porfiria aguda intermitente**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica y rinitis vasomotora (según las relaciones de indicación del grafo de conocimiento; los textos de las autorizaciones españolas no incluyen indicación) |
| Nueva Indicación Predicha | Porfiria aguda intermitente |
| Puntaje de Predicción TxGNN | 99,76 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, mizolastina es un antihistamínico H1 de segunda generación, y su diana farmacológica registrada es el receptor H1 de histamina (gen HRH1). Su eficacia en rinitis alérgica y vasomotora es la base de su uso clínico.

Con los datos compilados para este informe, **no se logra establecer un vínculo mecanístico** entre el antagonismo del receptor H1 y la porfiria aguda intermitente. Esta enfermedad es un trastorno de la biosíntesis del hemo (déficit de porfobilinógeno desaminasa) sin un mecanismo histaminérgico reconocido. Por ello, el puntaje elevado (0,998) debe interpretarse como un resultado del modelo, probablemente reflejo de similitudes en la red de conocimiento, y no como una justificación farmacológica verificada.

Además, la seguridad de los antihistamínicos en porfiria (consideraciones sobre el metabolismo hepático/vía del hemo) requeriría una revisión específica antes de cualquier uso en esta población.

### Otras predicciones del modelo

El modelo generó otras nueve predicciones con puntajes similares (todas con nivel de evidencia L5, sin ensayos ni literatura y con recomendación Hold):

| Posición | Indicación predicha | Puntaje TxGNN |
|------|------|------|
| 2 | Trastornos del movimiento psicógenos | 99,71 % |
| 3 | Discinesia lingual-facial-bucal | 99,71 % |
| 4 | Trastorno de tics crónico | 99,71 % |
| 5 | Enfermedad extrapiramidal y del movimiento | 99,70 % |
| 6 | Ataques de estremecimiento benignos | 99,70 % |
| 7 | Temblor ortostático primario | 99,69 % |
| 8 | Síndrome de temblor-nistagmo-úlcera duodenal | 99,69 % |
| 9 | Mirada tónica paroxística benigna de la infancia con ataxia | 99,68 % |
| 10 | Deficiencia de carbamoil fosfato sintetasa I | 99,47 % |

Ninguna de ellas cuenta con un vínculo mecanístico respaldado por los datos. En los trastornos del movimiento se ha planteado de forma especulativa una modulación histaminérgica central, pero mizolastina es un agente periférico, no sedante y con penetración limitada en el sistema nervioso central. En los tics, el interés preclínico se centra en el receptor H3, una diana distinta del H1.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61658 | MIZOLEN 10 mg comprimidos de liberación modificada (Opella Healthcare Spain S.L.) | Comprimido de liberación modificada | No disponible en los datos compilados |
| 61976 | ZOLISTAN 10 mg comprimidos de liberación modificada (Sanofi Aventis S.A.) | Comprimido de liberación modificada | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta se completó y registró una entrada de tipo farmacológico, no una interacción con otro fármaco: mizolastina se une al receptor H1 de histamina humano (HRH1), lo que confirma su diana principal. No se identificaron interacciones con otros medicamentos con nivel de gravedad asignado.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de porfiria aguda intermitente se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos, literatura ni un mecanismo plausible: la enfermedad es un trastorno metabólico del hemo sin relación conocida con el antagonismo H1. Además, existe una preocupación de seguridad específica en porfiria que no está evaluada.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) de mizolastina, por ejemplo mediante consulta a DrugBank.
- Descarga y análisis del prospecto de la AEMPS para obtener advertencias y contraindicaciones, necesarios para el cribado de seguridad (carencia bloqueante).
- Revisión de la seguridad de mizolastina en porfiria (metabolismo hepático y vía del hemo).
- Revisión bibliográfica dirigida para identificar cualquier indicio biológico que conecte la señalización histaminérgica con la porfiria aguda intermitente.
- Evidencia preclínica que respalde un vínculo mecanístico antes de plantear estudios clínicos.
- Compatibilidad de vías de administración y similitud con la indicación original, actualmente pendientes de evaluación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

