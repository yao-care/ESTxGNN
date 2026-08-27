---
layout: default
title: Vernakalant
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 6
---

# Vernakalant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Vernakalant: De Fibrilación Auricular a Ictus (Accidente Cerebrovascular)

## Resumen en Una Frase

Vernakalant es un antiarrítmico selectivo auricular utilizado para la cardioversión farmacológica de la fibrilación auricular (FA) de reciente inicio.
El modelo TxGNN predice que podría ser efectivo para **Ictus (stroke disorder)**, con **3 ensayos clínicos** y **7 publicaciones** disponibles como contexto —
sin embargo, ninguno de estos estudios tiene el ictus como variable de resultado directa; todos evalúan la cardioversión de la FA, por lo que la señal debe interpretarse con cautela.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fibrilación auricular de reciente inicio (cardioversión farmacológica) — inferido de la evidencia clínica disponible; no hay texto de indicación oficial registrado |
| Nueva Indicación Predicha | Ictus (Accidente Cerebrovascular) |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

No se dispone de un registro formal de mecanismo de acción (MOA) en DrugBank para este candidato (brecha de datos DG002, severidad Alta). Según la evidencia recopilada en los ensayos y la literatura, vernakalant es un antiarrítmico auricular-selectivo que bloquea las corrientes de potasio IKur e IKACh, junto con un bloqueo uso-dependiente del canal de sodio (INa). Este perfil lo hace eficaz para revertir la FA a ritmo sinusal con menor efecto sobre el ventrículo, en comparación con antiarrítmicos clásicos.

La FA es un factor de riesgo mayor de ictus isquémico, y en teoría, terminar la arritmia de forma eficaz podría reducir indirectamente el riesgo de ictus. Sin embargo, esta es una relación **indirecta**: el fármaco actúa sobre la arritmia, no sobre el ictus en sí. Los 3 ensayos clínicos y las 7 publicaciones disponibles tratan exclusivamente sobre cardioversión de FA (eficacia, seguridad, contractilidad auricular); ninguno mide el ictus como variable primaria de resultado.

Por esta razón, es probable que la etiqueta "stroke disorder" generada por TxGNN refleje una asociación de grafo de conocimiento entre FA y su complicación (el ictus), más que una evidencia real de que vernakalant trate el ictus de forma directa. Esta interpretación coincide con el análisis de razonamiento mecanístico incluido en el paquete de evidencia.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04485195](https://clinicaltrials.gov/study/NCT04485195) | Fase 4 | Completado | 350 | Ensayo RAFF4: vernakalant IV vs. procainamida IV para cardioversión de FA aguda en urgencias; el mayor y más riguroso de los tres, pero el criterio de valoración sigue siendo la conversión a ritmo sinusal, no la prevención de ictus |
| [NCT01447862](https://clinicaltrials.gov/study/NCT01447862) | Fase 4 | Completado | 101 | Vernakalant vs. ibutilida en FA de reciente inicio; evalúa tasa de conversión y seguridad, sin criterio de valoración relacionado con ictus |
| [NCT01646281](https://clinicaltrials.gov/study/NCT01646281) | Fase 4 | Desconocido | 70 | Efecto de vernakalant y flecainida sobre la contractilidad auricular tras cardioversión; estado no actualizado, evidencia más débil |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Revisión | Lancet | Revisión general del manejo de la FA, incluyendo estratificación de riesgo de ictus y anticoagulación |
| [17371199](https://pubmed.ncbi.nlm.nih.gov/17371199/) | 2007 | Revisión | Expert Opin Investig Drugs | Revisión mecanística de vernakalant (RSD1235) como agente antifibrilatorio auricular-selectivo |
| [27292602](https://pubmed.ncbi.nlm.nih.gov/27292602/) | 2016 | Cohorte | Am J Emerg Med | Seguridad y eficacia de cardioversión farmacológica de FA reciente en urgencias; evalúa tromboembolismo/muerte a 30 días |
| [22576674](https://pubmed.ncbi.nlm.nih.gov/22576674/) | 2012 | Revisión | Curr Hypertens Rep | Ensayos recientes en FA en pacientes hipertensos; menciona la FA como factor de riesgo de ictus |
| [23553811](https://pubmed.ncbi.nlm.nih.gov/23553811/) | 2013 | Revisión | Pharmacotherapy | Actualización clínica sobre manejo de la FA, incluyendo control de ritmo con vernakalant |
| [19678722](https://pubmed.ncbi.nlm.nih.gov/19678722/) | 2009 | Revisión | J Manag Care Pharm | Opciones farmacológicas establecidas y emergentes para el manejo de la FA |
| [25024989](https://pubmed.ncbi.nlm.nih.gov/25024989/) | 2014 | Revisión | Heart Lung Vessels | Avances 2013 en anestesia cardiotorácica; incluye oclusión de orejuela izquierda para reducción de ictus y nuevos antiarrítmicos |

---

## Información de Mercado en España

Actualmente vernakalant no cuenta con autorizaciones de comercialización registradas (0 autorizaciones, estado "no comercializado").

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No hay datos de advertencias, contraindicaciones ni interacciones farmacológicas disponibles en las fuentes consultadas (brecha de datos DG001, severidad **Bloqueante**: impide la evaluación de seguridad inicial S1).

> Nota informativa: la ficha técnica conocida de vernakalant contraindica su uso en pacientes con síndrome del seno enfermo sin marcapasos, por el riesgo de bradicardia o pausa sinusal. Este dato aparece únicamente en el análisis de una de las indicaciones predichas de menor rango (no en el campo formal de seguridad) y debe verificarse contra la ficha técnica oficial antes de cualquier uso clínico.

---

## Otras Señales del Modelo (Baja Confianza)

El paquete de evidencia incluye 5 indicaciones adicionales predichas por TxGNN, todas en nivel **L5** (solo predicción del modelo, sin ensayos ni literatura) y con recomendación **Hold**:

- **Síndrome del seno enfermo tipo 2** — contradice una contraindicación farmacológica conocida; señal de alto riesgo, probable falso positivo.
- **Susceptibilidad obsoleta a ictus isquémico** — término ontológico obsoleto, solapado con la señal principal de ictus, sin valor analítico independiente.
- **Sarcoglicanopatía** — posible relación indirecta solo si el paciente desarrolla FA secundaria; no es una indicación real.
- **Síndrome de Wildervanck**, **Amiloidosis ABri** — sin relación mecanística conocida; artefactos de cercanía en el espacio de embeddings del modelo.

Ninguna de estas señales requiere acción adicional en este momento.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque existen ensayos clínicos de Fase 4 completados y de buen tamaño muestral (p. ej. RAFF4, n=350), toda la evidencia disponible respalda el uso ya conocido de vernakalant en cardioversión de FA, no un efecto directo sobre el ictus. Además, la brecha de datos de seguridad (DG001) es bloqueante y el mecanismo de acción no está formalmente documentado (DG002), por lo que no es posible completar siquiera la evaluación de seguridad inicial (S1).

**Para avanzar se necesita:**
- Ficha técnica/prospecto oficial (TFDA/AEMPS) con advertencias y contraindicaciones (DG001, bloqueante)
- Confirmación del mecanismo de acción desde DrugBank (DG002)
- Aclarar si la señal "ictus" es un artefacto de mapeo ontológico (FA↔ictus) o una hipótesis real que merece estudio dirigido
- Verificar la contraindicación conocida en síndrome del seno enfermo antes de cualquier expansión de indicación
- Diseño de un estudio con el ictus como variable primaria, si se decide continuar la línea de investigación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

