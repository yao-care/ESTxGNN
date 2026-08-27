---
layout: default
title: Catumaxomab
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 3
---

# Catumaxomab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Catumaxomab: De Ascitis Maligna a Retinopatía Diabética No Proliferativa Grave

## Resumen en Una Frase

Catumaxomab es un anticuerpo biespecífico trifuncional (anti-EpCAM x anti-CD3), conocido internacionalmente por su uso en ascitis maligna asociada a tumores epiteliales EpCAM-positivos.
El modelo TxGNN predice que podría ser efectivo para **Retinopatía Diabética No Proliferativa Grave**,
pero **actualmente no existe ningún ensayo clínico ni publicación** que respalde esta dirección — se trata de una predicción puramente algorítmica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ascitis maligna en tumores epiteliales EpCAM-positivos (uso internacional conocido; sin ficha técnica registrada en España) |
| Nueva Indicación Predicha | Retinopatía diabética no proliferativa grave |
| Puntaje de Predicción TxGNN | 99.64% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de catumaxomab en la base de datos consultada. Según la información conocida, catumaxomab es un anticuerpo biespecífico trifuncional que une simultáneamente EpCAM (expresado en células tumorales epiteliales) y CD3 (en linfocitos T), reclutando además células accesorias con receptor Fc, para destruir células tumorales malignas. Su uso conocido es en ascitis maligna.

No existe una relación biológica establecida entre este mecanismo inmuno-oncológico y la retinopatía diabética no proliferativa grave, cuya fisiopatología involucra daño microvascular, hiperpermeabilidad capilar y vías como VEGF — procesos no relacionados con el reclutamiento de células T mediado por EpCAM/CD3. El propio Evidence Pack señala explícitamente que esta predicción "carece de soporte mecanístico" y es únicamente resultado de la similitud de embeddings del modelo TxGNN.

Cabe señalar que el mismo Evidence Pack incluye otras dos indicaciones candidatas de menor rango (osteoporosis inducida por fármacos y retinopatía diabética general), ambas con el mismo problema: puntajes altos de TxGNN pero sin ningún fundamento mecanístico ni evidencia real que las respalde.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Citotoxicidad

*(Sección incluida por tratarse de un agente antineoplásico/inmunoterapia oncológica.)*

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo biespecífico trifuncional, T-cell engager) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (sin datos disponibles) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto (sin datos disponibles) |
| Items de Monitoreo | Hemograma completo y signos de síndrome de liberación de citocinas, dado que es un anticuerpo T-cell engager; función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones estándar de manejo de agentes antineoplásicos/biológicos citotóxicos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las tres indicaciones predichas por TxGNN (incluida la de mayor rango, retinopatía diabética no proliferativa grave) son de Nivel de Evidencia L5 — puntaje de modelo únicamente, sin ensayos clínicos, sin literatura y sin relación mecanística plausible. Además, el fármaco no está comercializado en España y faltan datos regulatorios bloqueantes (advertencias/contraindicaciones de ficha técnica).

**Para avanzar se necesita:**
- Ficha técnica oficial (AEMPS/TFDA) con advertencias, contraindicaciones e interacciones farmacológicas
- Justificación mecanística real que conecte el eje EpCAM/CD3 con patología retiniana diabética u ósea
- Al menos un estudio preclínico o clínico que respalde alguna de las tres indicaciones predichas
- Evaluación de viabilidad regulatoria, dado que el fármaco carece de autorización de comercialización en España
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

