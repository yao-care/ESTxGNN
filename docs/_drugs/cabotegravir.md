---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 5
---

# Cabotegravir
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

# Cabotegravir: De VIH a Artritis Reumatoide

## Resumen en Una Frase

Cabotegravir es un inhibidor de la integrasa del VIH (INSTI), utilizado originalmente en el tratamiento antirretroviral y la profilaxis pre-exposición (PrEP) frente al VIH. El modelo TxGNN predice que podría ser efectivo para **Artritis Reumatoide**, con un puntaje de **99,45%**, pero **sin ningún ensayo clínico ni publicación** que respalde actualmente esta direccion.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | VIH (terapia antirretroviral y profilaxis pre-exposicion) — no consta en registro español, medicamento no comercializado |
| Nueva Indicacion Predicha | Artritis Reumatoide |
| Puntaje de Prediccion TxGNN | 99,45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos estructurados sobre el mecanismo de accion (MOA) en la ficha tecnica del farmaco. Segun la informacion recogida en el analisis, cabotegravir actua como inhibidor de la transferencia de cadena de la integrasa del VIH (INSTI), bloqueando la insercion del ADN viral en el genoma de la celula huesped — un mecanismo antirretroviral especifico.

Este mecanismo no presenta ninguna conexion biologica conocida con las vias autoinmunes/inflamatorias implicadas en la artritis reumatoide (TNF-α, IL-6, RANKL). La ausencia total de ensayos clinicos y literatura que respalden esta asociacion, junto con la posicion relativamente baja del ranking interno del modelo (rank 8291), sugiere que el puntaje elevado podria deberse a un efecto de "hub" en el espacio de embeddings de TxGNN (nodos de enfermedad muy conectados que reciben puntajes altos de forma generalizada) mas que a una relacion farmacologica real.

En conjunto, la plausibilidad mecanistica de esta prediccion es baja y no se recomienda avanzar sin evidencia adicional independiente.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
No existe evidencia clinica ni bibliografica que respalde la asociacion entre cabotegravir y la artritis reumatoide, y el vinculo mecanistico propuesto es biologicamente inconsistente con el modo de accion antirretroviral conocido del farmaco. El nivel de evidencia (L5) corresponde unicamente a una prediccion del modelo, sin ningun estudio real de respaldo.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha tecnica de la TFDA con advertencias y contraindicaciones (actualmente bloqueante para la evaluacion de seguridad S1)
- Confirmar el mecanismo de accion (MOA) mediante consulta directa a DrugBank u otra fuente farmacologica primaria
- Identificar estudios preclinicos o de mecanismo que exploren alguna relacion inmunomoduladora de cabotegravir, de existir
- Evaluar si el puntaje TxGNN es reproducible o corresponde a ruido del modelo antes de invertir en investigacion adicional
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

