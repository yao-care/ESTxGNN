---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Durvalumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Durvalumab: De Carcinoma Urotelial a Carcinoma Urotelial de la Uretra Prostática

## Resumen en Una Frase

Durvalumab es un anticuerpo monoclonal anti-PD-L1, cuya clase ya cuenta con aprobación internacional para el carcinoma urotelial (incluida la vejiga), aunque en este mercado figura actualmente como no comercializado. El modelo TxGNN predice que podría ser efectivo para el **Carcinoma Urotelial de la Uretra Prostática**, con una puntuación de predicción del **99.98%**, pero por el momento **no hay ensayos clínicos ni literatura específica** que respalden esta dirección — la evidencia se limita a una extrapolación mecanística de clase.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Carcinoma urotelial (incluida vejiga) — según aprobaciones de clase en otros mercados; no verificado vía licencia local |
| Nueva Indicacion Predicha | Carcinoma Urotelial de la Uretra Prostática |
| Puntaje de Prediccion TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción procedentes de DrugBank (brecha de datos DG002). Según la información recogida en el propio evidence pack, durvalumab es un anticuerpo monoclonal anti-PD-L1 que bloquea las interacciones PD-L1/PD-1 y PD-L1/CD80, restaurando la actividad antitumoral de los linfocitos T. Este mecanismo ya cuenta con precedente de aprobación de clase para el carcinoma urotelial en general (incluida la vejiga) en otros mercados.

El carcinoma urotelial de la uretra prostática es, histológicamente, un subtipo anatómico dentro del mismo linaje tumoral que el carcinoma urotelial vesical — comparten origen en el epitelio de transición del tracto urinario. Esto sustenta una extrapolación mecanística razonable: si el bloqueo de PD-L1 restaura la respuesta inmune antitumoral en el urotelio vesical, en principio podría aplicar igual de forma teórica al urotelio de la uretra prostática.

Sin embargo, esta relación es puramente teórica en este momento: no existe ningún ensayo clínico ni publicación que evalúe durvalumab específicamente en este subtipo anatómico, por lo que la aplicabilidad real del mecanismo permanece sin verificar.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Inmunoterapia (inhibidor de checkpoint anti-PD-L1) |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Pese a tener la puntuación TxGNN más alta del pack (99.98%), esta indicación carece por completo de ensayos clínicos y literatura específica — el razonamiento se apoya únicamente en una extrapolación mecanística de clase, sin evidencia real que la respalde.

**Para avanzar se necesita:**
- Datos de mecanismo de acción vía DrugBank API (DG002)
- Ficha técnica/prospecto de TFDA para evaluación de seguridad S1 (DG001, bloqueante)
- Búsqueda dirigida de ensayos o series de casos sobre carcinoma urotelial de uretra prostática específicamente
- Evaluar en paralelo el candidato "endocervical carcinoma" (rank 6) del mismo evidence pack, que presenta mayor madurez de evidencia (L2, ensayo Fase 2 en curso con n=174 y revisión publicada) y podría priorizarse antes que esta indicación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

