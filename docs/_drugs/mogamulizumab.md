---
layout: default
title: Mogamulizumab
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Mogamulizumab: De Linfoma de Células T a Carcinoma Urotelial de Uretra Prostática

## Resumen en Una Frase

Mogamulizumab es un anticuerpo monoclonal anti-CCR4, utilizado originalmente para linfomas de células T (Micosis Fungoide/Síndrome de Sézary y Leucemia/Linfoma de Células T del Adulto).
El modelo TxGNN predice que podría ser efectivo para **Carcinoma Urotelial de Uretra Prostática**,
pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección — la señal proviene únicamente del score del modelo. Existen además 6 candidatos adicionales de menor rango, todos en la misma situación (L5, Hold).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Linfoma de Células T (Micosis Fungoide/Síndrome de Sézary, Leucemia/Linfoma de Células T del Adulto) — según texto de racional mecanístico, no consta en campo estructurado |
| Nueva Indicación Predicha | Carcinoma Urotelial de Uretra Prostática |
| Puntaje de Predicción TxGNN | 99.44% |
| Nivel de Evidencia | L5 |
| Estado de Mercado | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

El campo estructurado de mecanismo de acción (DrugBank MOA) está marcado como dato faltante (DG002, severidad Alta). Sin embargo, el racional mecanístico incluido en el evidence pack indica que Mogamulizumab es un anticuerpo monoclonal anti-CCR4 que elimina células T CCR4+ (incluidas las Treg) mediante citotoxicidad celular dependiente de anticuerpos (ADCC). Este mecanismo está directamente relacionado con su uso conocido en linfomas de células T (MF/Sézary, ATL), donde las células malignas expresan CCR4.

Para el carcinoma urotelial de uretra prostática, la relación es únicamente hipotética: el único vínculo plausible es la depleción de Treg en el microambiente tumoral, lo que podría potenciar la inmunidad antitumoral de forma indirecta. No hay evidencia de que las células de este carcinoma expresen CCR4 como mecanismo patogénico directo.

Por lo tanto, el score alto de TxGNN debe interpretarse como similitud topológica dentro de la red de conocimiento, **no como validación mecanística**. El mismo patrón de vínculo indirecto/hipotético se repite en los 6 candidatos restantes (carcinoma de pelvis renal, carcinoma urotelial vesical sarcomatoide, tumores relacionados con VHH-8, ectomesenquimoma, tumor de células granulares cutáneo maligno).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida / Inmunoterapia (anticuerpo monoclonal anti-CCR4, mecanismo ADCC) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las 7 indicaciones predichas se apoyan únicamente en el score de TxGNN (Nivel de Evidencia L5), sin ningún ensayo clínico, literatura o registro ICTRP. Además, existe un data gap bloqueante (DG001) sobre advertencias/contraindicaciones del prospecto TFDA, que impide siquiera iniciar la evaluación de seguridad S1. El fármaco tampoco está comercializado actualmente.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial (TFDA/AEMPS) para completar la evaluación de seguridad S1 (DG001, bloqueante)
- Completar los datos estructurados de mecanismo de acción vía API de DrugBank (DG002)
- Estudios preclínicos o mecanísticos sobre expresión de CCR4 en los tumores predichos, para elevar el nivel de evidencia de L5 a L4
- Confirmar la vía de administración y evaluar la disponibilidad de mercado en España/Taiwán, dado que el fármaco no está actualmente comercializado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

