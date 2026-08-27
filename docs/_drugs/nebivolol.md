---
layout: default
title: Nebivolol
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 5
---

# Nebivolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Nebivolol: De Hipertensión Arterial a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Nebivolol es un betabloqueante β1 altamente selectivo con efecto vasodilatador mediado por óxido nítrico, utilizado como antihipertensivo (la indicación original exacta no está confirmada en las fuentes disponibles para este informe — ver nota más abajo). El modelo TxGNN predice que podría ser efectivo para **Hipertensión Renovascular Maligna**, pero esta dirección **no cuenta actualmente con ningún ensayo clínico ni publicación** que la respalde directamente; la predicción se apoya únicamente en una extrapolación mecanística de clase farmacológica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (inferida de la clase farmacológica descrita en el propio paquete de evidencia; no confirmada por ficha técnica — dato bloqueante pendiente, ver DG001/DG002) |
| Nueva Indicación Predicha | Hipertensión Renovascular Maligna |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L5 (solo predicción del modelo, sin ensayos ni literatura de respaldo) |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos oficiales sobre el mecanismo de acción de nebivolol (dato pendiente de alta prioridad, DG002). Según la información recogida en el propio paquete de evidencia, nebivolol es un betabloqueante β1 altamente selectivo de tercera generación que además posee un componente vasodilatador mediado por óxido nítrico (NO); este perfil farmacológico ya está validado como antihipertensivo convencional.

La hipertensión renovascular maligna y la enfermedad renal hipertensiva maligna son subtipos graves de hipertensión, caracterizados por hiperactivación del eje renina-angiotensina-aldosterona (RAAS) y desequilibrio de la presión de perfusión renal. Farmacológicamente es plausible que la inhibición de la secreción de renina y el descenso de la presión arterial sistémica que produce nebivolol aporten un beneficio indirecto en estos cuadros.

Sin embargo, el propio razonamiento del modelo señala que se trata de una extrapolación a nivel de clase terapéutica, no de evidencia dirigida a este subtipo grave en concreto. No existe ningún ensayo clínico ni publicación que estudie específicamente nebivolol en esta indicación, por lo que la predicción debe tratarse como una hipótesis de investigación temprana, no como una señal clínica consolidada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Hipertensión Renovascular Maligna.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Hipertensión Renovascular Maligna.

**Nota de contexto:** TxGNN generó en total 5 indicaciones candidatas para nebivolol en este ciclo. Ninguna de las otras cuatro (enfermedad renal hipertensiva maligna, hipertensión pulmonar de mecanismo multifactorial incierto, hipertensión pulmonar por enfermedad pulmonar/hipoxia, síndrome de Braddock) cuenta con ensayos clínicos. Una de ellas —hipertensión pulmonar por enfermedad pulmonar/hipoxia— sí arrojó 20 artículos en PubMed, pero al revisarlos se trata de literatura genérica sobre biología de la hipoxia, HIF-1α y envejecimiento cerebral, sin ninguna referencia específica a nebivolol; se interpreta como ruido de coocurrencia en el grafo de conocimiento, no como evidencia farmacológica real.

---

## Información de Mercado en España

El fármaco no está comercializado en España; no hay autorizaciones registradas en este Evidence Pack (0 de 0).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

*(No se dispone actualmente de advertencias, contraindicaciones ni datos de interacción farmacológica verificados; la obtención del prospecto oficial de TFDA está marcada como dato bloqueante para la evaluación de seguridad — ver DG001.)*

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La predicción se sustenta únicamente en una extrapolación mecanística de clase (betabloqueo/antihipertensivo), sin ningún ensayo clínico ni publicación específica sobre nebivolol en hipertensión renovascular maligna (nivel de evidencia L5).
- El dato de advertencias/contraindicaciones (DG001) está marcado como bloqueante y actualmente impide una evaluación de seguridad S1.
- El mecanismo de acción oficial (DG002) tampoco está confirmado, lo que limita el análisis de plausibilidad mecanística.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto/ficha técnica oficial (advertencias, contraindicaciones, interacciones) para desbloquear la evaluación de seguridad S1.
- Confirmar el mecanismo de acción vía consulta directa a DrugBank API.
- Buscar estudios preclínicos o de mecanismo específicos de nebivolol en hipertensión renovascular maligna / enfermedad renal hipertensiva maligna, dado que actualmente no existe ninguno.
- Reevaluar la señal si aparecen nuevos ensayos o publicaciones específicas; de lo contrario, mantener como pregunta de investigación de baja prioridad.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

