---
layout: default
title: Belimumab
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 6
---

# Belimumab
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

# Belimumab: De Lupus Eritematoso Sistémico a Trastorno Primario de Liberación Plaquetaria

*(Nota: el Evidence Pack no registra la indicación original ni el MOA de belimumab — `original_indications` viene vacío y `original_moa` marcado como dato faltante. La indicación "Lupus Eritematoso Sistémico" se incluye aquí como conocimiento público/regulatorio externo sobre este fármaco, no como dato extraído del Evidence Pack; ver DG002 en la sección de razonabilidad.)*

## Resumen en Una Frase

Belimumab es un anticuerpo monoclonal anti-BLyS/BAFF, conocido públicamente por su uso en lupus eritematoso sistémico, aunque el Evidence Pack actual no contiene datos verificados sobre su indicación original ni su MOA. El modelo TxGNN predice que podría ser efectivo para **trastorno primario de liberación plaquetaria** (*primary release disorder of platelets*), con un **score de 99.96%**, pero solo **1 ensayo clínico** vinculado (cuya relevancia real para esta indicación está pendiente de verificación) y **0 publicaciones** que la respalden directamente.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el Evidence Pack (sin licencias registradas en Taiwan; `original_indications` vacío) |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99.96% (rank interno #1159) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Taiwan | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por que es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de belimumab en este Evidence Pack (dato marcado como faltante, severidad Alta según el registro de brechas DG002). Según información pública conocida, belimumab es un anticuerpo monoclonal que inhibe BLyS/BAFF (B-lymphocyte stimulator), una citocina clave en la supervivencia de linfocitos B autorreactivos, y su uso está establecido en enfermedades autoinmunes mediadas por linfocitos B como el lupus eritematoso sistémico.

La relación mecanística entre esa indicación autoinmune y un "trastorno primario de liberación plaquetaria" no es evidente: este último es típicamente un defecto intrínseco de la función plaquetaria (liberación de gránulos), no un proceso mediado primariamente por linfocitos B. El único ensayo clínico vinculado en el Evidence Pack tampoco estudia esta indicación (ver más abajo), por lo que la razonabilidad mecanicista de esta predicción no puede confirmarse con los datos actuales — se trata de una señal generada por el modelo TxGNN sin respaldo mecanístico ni clínico directo disponible.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Fase 2 | Completado | 14 | Estudio mecanístico de belimumab en glomerulonefritis membranosa idiopática (IMGN) positiva para autoanticuerpo anti-PLA2R; evalúa eficacia, seguridad y relación entre biomarcadores y respuesta clínica. **Nota importante: este ensayo estudia glomerulonefritis membranosa, no trastorno de liberación plaquetaria — su relevancia para la indicación predicha está marcada como "pending" en el Evidence Pack y no ha sido confirmada.** |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Taiwan

Actualmente no hay autorizaciones de comercialización registradas en Taiwan (estado: no comercializado, 0 licencias).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Cabe destacar que el Evidence Pack registra la ausencia de datos del prospecto/advertencias de TFDA como una brecha de severidad **Bloqueante** (DG001), con impacto explícito: "no se puede proceder a la evaluación inicial de seguridad S1". Tampoco se identificaron interacciones farmacológicas (búsqueda DDI: no encontrada).

## Otras Señales Predichas por TxGNN (Referencia)

El mismo modelo generó otras 5 señales para belimumab, ninguna con ensayos clínicos ni literatura de respaldo directo:

| Indicación | Score TxGNN | Nota |
|------|------|------|
| Pseudo-von Willebrand disease | 99.96% | Sin evidencia clínica registrada |
| Glanzmann thrombasthenia | 99.88% | Evaluado internamente como L5 / Hold — trastorno estructural (déficit GPIIb/IIIa), sin vínculo mecanístico con terapia anti-BAFF |
| Trombocitopenia aloinmune fetal y neonatal | 99.59% | Sin evidencia clínica registrada |
| Retinopatía diabética no proliferativa grave | 99.05% | Sin evidencia clínica registrada |
| Macrotrombocitopenia autosómica dominante | 99.04% | Sin evidencia clínica registrada |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única evidencia clínica vinculada a la indicación de mayor rango no estudia realmente el trastorno predicho, no hay literatura de respaldo, el fármaco no está comercializado en Taiwan, y existe una brecha de datos **bloqueante** (DG001) que impide completar la evaluación inicial de seguridad (S1). Con esta combinación de vacíos, no es razonable avanzar más allá de una fase de observación.

**Para avanzar se necesita:**
- Obtener el prospecto/warnings de TFDA (o de la agencia reguladora del mercado objetivo) para desbloquear la evaluación de seguridad S1
- Obtener datos verificados del mecanismo de acción (MOA) de belimumab vía DrugBank
- Confirmar si existe algún ensayo clínico o publicación que estudie directamente belimumab en trastornos de liberación plaquetaria (el ensayo actual no aplica)
- Reevaluar la indicación original real del fármaco a partir de fuentes regulatorias verificadas, no solo de conocimiento público
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

