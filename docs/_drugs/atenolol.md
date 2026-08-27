---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Atenolol: De Hipertensión Arterial a Infarto de Miocardio Posterolateral

## Resumen en Una Frase

Atenolol es un betabloqueante β1-selectivo (cardioselectivo) de uso establecido en enfermedad cardiovascular, principalmente hipertensión arterial y angina de pecho. El modelo TxGNN predice que podria ser efectivo para **Infarto de Miocardio Posterolateral**, pero actualmente **no existe ningun ensayo clinico ni publicacion** que respalde especificamente esta direccion — se trata de una prediccion puramente computacional.

*Nota: el Evidence Pack no incluye datos estructurados de la indicacion original de atenolol (`original_indications` vacio); "Hipertension arterial" se infiere del contexto farmacologico de clase (betabloqueante) mencionado repetidamente en la literatura del propio pack.*

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Hipertension arterial (dato no incluido explicitamente en el Evidence Pack; inferido de la clase farmacologica) |
| Nueva Indicacion Predicha | Infarto de Miocardio Posterolateral |
| Puntaje de Prediccion TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion (MOA) de atenolol en este Evidence Pack. Segun la informacion conocida a partir de la literatura recogida en el propio pack, atenolol es un **betabloqueante β1-selectivo (cardioselectivo)**, cuya eficacia en hipertension arterial y cardiopatia isquemica esta ampliamente comprobada.

Los betabloqueantes constituyen la clase terapeutica estandar para reducir la mortalidad tras un infarto de miocardio, al disminuir el consumo de oxigeno miocardico y la carga isquemica. Bajo esta logica, mecanisticamente seria plausible que atenolol tuviera un rol en el manejo posterior a un infarto posterolateral, como lo tendria en cualquier subtipo anatomico de infarto.

Sin embargo, esta prediccion especifica de TxGNN **no cuenta con ningun ensayo clinico ni publicacion que la respalde directamente** — es una extrapolacion del modelo basada en similitud de red, no en evidencia real observada para este subtipo anatomico concreto. Cabe destacar que el mismo Evidence Pack contiene otras indicaciones relacionadas con infarto de miocardio (posteroinferior, septal) y con cardiopatia pulmonar cronica que si cuentan con literatura de apoyo directo (nivel L3), lo que sugiere que el "cluster" de infarto de miocardio es, en conjunto, mas prometedor que esta prediccion aislada.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados para Infarto de Miocardio Posterolateral.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Infarto de Miocardio Posterolateral.

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion de TxGNN para Infarto de Miocardio Posterolateral no cuenta con ningun ensayo clinico ni publicacion de respaldo (nivel de evidencia L5); solo existe la plausibilidad mecanistica generica de la clase betabloqueante. Ademas, faltan datos criticos de seguridad (MOA, advertencias TFDA/EMA, contraindicaciones) que impiden una evaluacion de seguridad inicial (bloqueo S1).

**Para avanzar se necesita:**
- Datos de mecanismo de accion (MOA) de atenolol desde DrugBank
- Ficha tecnica/prospecto (advertencias, contraindicaciones, interacciones) desde la agencia reguladora correspondiente, dado que atenolol no esta comercializado actualmente en Espana
- Busqueda dirigida de literatura y ensayos que evaluen especificamente el subtipo anatomico "posterolateral", no solo infarto de miocardio en general
- Evaluar en paralelo las indicaciones relacionadas del mismo Evidence Pack con mayor evidencia (Infarto de Miocardio Posteroinferior y Septal, nivel L3 con RCT/estudio funcional; Cardiopatia Pulmonar Cronica, nivel L3 con ensayo Fase 4 y 15 publicaciones), ya que podrian representar candidatos de reposicionamiento mas solidos que la indicacion de mayor rango aqui evaluada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

