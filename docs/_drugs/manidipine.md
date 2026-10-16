---
layout: default
title: Manidipine
parent: Solo predicción del modelo (L5)
nav_order: 493
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Manidipine: nueva indicación predicha, Trastorno de migraña (nivel de evidencia L5). Indicación original: No disponible en las autorizaciones de la AEMPS (el texto de indicaci…"
---

# Manidipine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Manidipino: De Hipertensión Arterial a Trastorno de Migraña

## Resumen en Una Frase

Manidipino es un antagonista del calcio de tipo dihidropiridina, comercializado en España en comprimidos de 10 mg y 20 mg (el texto de indicación no figura en los datos compilados; el uso habitual es la hipertensión arterial).
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones de la AEMPS (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 99,80% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, manidipino es un bloqueador de los canales de calcio de tipo dihidropiridina (con actividad sobre canales de tipo L y T), y su uso en hipertensión es conocido.

Otros bloqueadores de los canales de calcio, como la flunarizina, se utilizan en la profilaxis de la migraña, por lo que existe una justificación mecanística a nivel de clase farmacológica. Esto hace biológicamente plausible la predicción, aunque no sustituye la evidencia específica del manidipino.

Es importante subrayar que no se aportó ninguna evidencia clínica ni bibliográfica específica de manidipino para migraña. El puntaje elevado del modelo es solo una predicción.

**Otras indicaciones predichas (todas sin ensayos clínicos):**

| Posición | Indicación | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|------|
| 2 | Migraña con aura del tronco encefálico | 99,73% | L5 | Subtipo de migraña; mismo vínculo plausible, subtipo raro y difícil de estudiar |
| 3 | Síndrome nefrogénico de antidiuresis inapropiada | 99,63% | L5 | Sin vía mecanística clara desde el bloqueo del calcio |
| 4 | Hipertensión pulmonar | 99,52% | L5 | Vasodilatación plausible; la literatura recuperada no respalda eficacia |
| 5 | Angina de Prinzmetal | 99,41% | L4 | Los bloqueadores del calcio son tratamiento de primera línea; evidencia indirecta de clase |
| 6 | Cardiopatía cifoescoliótica | 99,41% | L5 | Beneficio indirecto y especulativo |
| 7 | Hiperplasia prostática benigna | 99,36% | L5 | Vínculo débil; las clases establecidas actúan por otros mecanismos |
| 8 | Susceptibilidad a migraña con o sin aura | 99,24% | L5 | Fenotipo genético, no directamente accionable |
| 9 | Atrofodermia vermiculada | 99,04% | L5 | Sin conexión mecanística identificable |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para la indicación principal (trastorno de migraña) actualmente no hay literatura relacionada disponible.

Para la cuarta indicación predicha (hipertensión pulmonar) se recuperaron tres publicaciones, que no aportan evidencia de eficacia:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9341290](https://pubmed.ncbi.nlm.nih.gov/9341290/) | 1997 | Reporte de caso | Nihon Kyobu Shikkan Gakkai Zasshi | Neumonía intersticial atribuida a manidipino en una mujer de 62 años con pulmón reumatoide; mejoró al suspender el fármaco y administrar metilprednisolona. Señal de seguridad |
| [11457745](https://pubmed.ncbi.nlm.nih.gov/11457745/) | 2001 | Estudio clínico (otro fármaco) | Circulation | Compara candesartán y antagonistas del calcio sobre la tos y la hiperreactividad bronquial en pacientes hipertensos con asma; no es relevante para manidipino |
| [8667194](https://pubmed.ncbi.nlm.nih.gov/8667194/) | 1996 | Estudio preclínico en animales | J Pharmacol Exp Ther | Efectos vasculares regionales de MPC-1304 comparado con nifedipino y manidipino en ratas; no es evidencia clínica |

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de monofármaco, ninguna cancelada):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 73352 | Manidipino Viatris 20 mg comprimidos EFG | Comprimido | No disponible |
| 75033 | Manidipino Kern Pharma 20 mg comprimidos EFG | Comprimido | No disponible |
| 75034 | Manidipino Vir 10 mg comprimidos EFG | Comprimido | No disponible |
| 77260 | Manidipino Combix 20 mg comprimidos EFG | Comprimido | No disponible |
| 64634 | Artedil 10 mg comprimidos | Comprimido | No disponible |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como señal a vigilar, se identificó un reporte de caso de neumonía intersticial asociada a manidipino (1997). No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las indicaciones predichas se apoyan solo en la predicción del modelo (nivel L5; la angina de Prinzmetal L4 por evidencia de clase), sin ensayos clínicos ni literatura específica de manidipino. Además, faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), ya que su ausencia impide el cribado de seguridad
- Completar los datos del mecanismo de acción y las indicaciones aprobadas
- Realizar una búsqueda bibliográfica dirigida de manidipino y otros antagonistas del calcio en migraña
- Priorizar la angina de Prinzmetal como pregunta de investigación por su sustento de clase
- Evaluar la señal de neumonía intersticial antes de cualquier uso en indicaciones pulmonares
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

