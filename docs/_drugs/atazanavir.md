---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 6
---

# Atazanavir
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

# Atazanavir: De la Infección por VIH a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Atazanavir es un inhibidor de la proteasa del VIH-1, utilizado como componente de la terapia antirretroviral combinada (ART) para el tratamiento de la infección por VIH.
El modelo TxGNN predice que podría ser efectivo para **Síndrome de Inmunodeficiencia Adquirida Felina (FIV)**, con una puntuación muy alta (99.98%),
pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH (uso conocido como inhibidor de proteasa antirretroviral; sin ficha técnica TFDA/AEMPS registrada en este pack) |
| Nueva Indicación Predicha | Síndrome de Inmunodeficiencia Adquirida Felina (FIV) |
| Puntaje de Predicción TxGNN | 99.98% (rank #802) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de atazanavir en este pack de evidencia. Según la información contextual disponible, atazanavir es un inhibidor de la proteasa del VIH-1 que bloquea la escisión de la poliproteína Gag-Pol viral, y su eficacia en el tratamiento de la infección por VIH en humanos está bien establecida.

La FIV (virus de inmunodeficiencia felina) es un retrovirus que afecta a gatos, filogenéticamente relacionado con el VIH dentro de la familia *Lentivirus*. Sin embargo, la estructura de la proteasa de FIV difiere significativamente de la del VIH-1, lo que limita la plausibilidad de una inhibición cruzada directa por atazanavir.

Según el propio razonamiento del modelo, esta puntuación alta probablemente refleja **similitud topológica en el grafo de conocimiento** (proximidad a nodos de VIH/lentivirus) más que una señal biológica real. No existe ningún estudio preclínico o clínico, ni en humanos ni en medicina veterinaria, que respalde esta hipótesis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar de la puntuación TxGNN muy alta, el nivel de evidencia es L5 (solo predicción del modelo, sin estudios reales). La propia justificación mecanística señala diferencias estructurales relevantes entre las proteasas de VIH y FIV, y la ausencia total de ensayos clínicos o literatura de soporte. Además, se trata de una indicación veterinaria (FIV es una enfermedad felina), lo que la sitúa fuera del ámbito habitual de reposicionamiento para uso humano.

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) verificados vía DrugBank (gap bloqueante identificado en el pack: DG002)
- Ficha técnica/prospecto TFDA para evaluación de seguridad inicial (gap bloqueante identificado en el pack: DG001)
- Estudios preclínicos que evalúen actividad inhibitoria de atazanavir frente a la proteasa de FIV
- Nota: este mismo pack de evidencia contiene otras indicaciones predichas para atazanavir (p. ej. infección congénita por VIH, AIDS related complex) con evidencia L1 y recomendación "Proceed with Guardrails" — se recomienda evaluarlas en un informe separado, ya que representan candidatos con base de evidencia sustancialmente más sólida.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

