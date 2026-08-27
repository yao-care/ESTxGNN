---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 3
---

# Galcanezumab
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

# GALCANEZUMAB: De Migraña/Cefalea en Racimos a Deficiencia de Cofactor II de Heparina

## Resumen en Una Frase

Galcanezumab es un anticuerpo monoclonal anti-CGRP, utilizado originalmente para la prevención de la migraña y la cefalea en racimos.
El modelo TxGNN predice que podría ser efectivo para la **Deficiencia de Cofactor II de Heparina**,
pero actualmente **no existen ensayos clínicos ni publicaciones** que respalden esta direccion — la prediccion se apoya unicamente en el puntaje del modelo.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Migraña / cefalea en racimos (segun mecanismo de accion conocido; sin licencias registradas en España) |
| Nueva Indicacion Predicha | Deficiencia de Cofactor II de Heparina |
| Puntaje de Prediccion TxGNN | 99.50% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Los datos detallados de mecanismo de accion (MOA) de galcanezumab estan marcados como no disponibles en esta evaluacion. Segun la informacion contenida en el propio analisis de reposicionamiento, galcanezumab es un anticuerpo monoclonal dirigido contra CGRP (peptido relacionado con el gen de la calcitonina), con un mecanismo centrado en la via trigeminovascular, empleado en la prevencion de la migraña y la cefalea en racimos.

Este mecanismo no tiene una relacion biologica conocida con la deficiencia de cofactor II de heparina, un trastorno relacionado con la regulacion de la actividad de la trombina por una serpina (SERPIND1). El propio analisis mecanistico incluido en el expediente concluye que **no existe evidencia de que la via de CGRP module la expresion o funcion de esta proteina**, y que el efecto vasodilatador leve del CGRP no es suficiente para justificar el vinculo.

Es relevante notar que las otras dos indicaciones predichas para este farmaco (deficiencia de antitrombina tipo 2 y exceso de factor V con trombosis espontanea) pertenecen tambien al mismo grupo de trastornos raros de la coagulacion, con puntajes TxGNN muy similares (99.41–99.41%). Este patron sugiere que la prediccion podria originarse de la proximidad de nodos en el grafo de conocimiento, mas que de una señal farmacologica real — de ahi que el propio analisis la califique como sin plausibilidad biologica.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
No existe ningun ensayo clinico ni publicacion que respalde esta direccion, y el propio analisis mecanistico indica ausencia de plausibilidad biologica entre la via anti-CGRP y los trastornos de coagulacion predichos. El patron de puntajes similares entre las tres indicaciones (todas relacionadas con coagulacion) sugiere una posible senal artefactual del grafo de conocimiento, no una hipotesis farmacologica solida.

**Para avanzar se necesita:**
- Confirmar el mecanismo de accion (MOA) detallado de galcanezumab (actualmente brecha de datos de severidad Alta)
- Obtener el prospecto/ficha tecnica de TFDA con advertencias y contraindicaciones (brecha de datos bloqueante — DG001)
- Estudios preclinicos que exploren una posible relacion entre la via de CGRP y la regulacion de proteinas de la coagulacion (cofactor II de heparina, antitrombina, factor V)
- Registro de ensayos clinicos dirigidos, unicamente si se identifica una senal mecanistica real que justifique la investigacion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

