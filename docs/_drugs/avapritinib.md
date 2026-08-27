---
layout: default
title: Avapritinib
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib: De Indicacion Original No Documentada a Axial Spondylometaphyseal Dysplasia

## Resumen en Una Frase

No hay datos disponibles en este Evidence Pack sobre la indicacion original ni el mecanismo de accion de avapritinib (brecha de datos bloqueante en la fuente TFDA). El modelo TxGNN predice una posible relacion con **axial spondylometaphyseal dysplasia**, con una puntuacion de **99.92%**, pero esta prediccion no cuenta actualmente con **ningun ensayo clinico ni publicacion** que la respalde.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en la evidencia actual (sin autorizaciones registradas, MOA en brecha) |
| Nueva Indicacion Predicha | Axial spondylometaphyseal dysplasia |
| Puntaje de Prediccion TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Taiwan | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion de avapritinib en este informe (brecha de datos de severidad alta, DG002). Tampoco hay indicacion original registrada ni autorizaciones de mercado en Taiwan, por lo que no es posible establecer una comparacion mecanistica entre un uso previo y la neoplasia/enfermedad predicha.

Segun la propia evidencia recopilada, la puntuacion de TxGNN para axial spondylometaphyseal dysplasia refleja unicamente similitud de embeddings dentro del grafo de conocimiento, no una relacion mecanistica verificada: no existe ningun ensayo clinico, registro ICTRP ni publicacion en PubMed que conecte el farmaco con esta displasia osea rara.

Es relevante notar que, de las 10 indicaciones predichas en este paquete, 5 pertenecen al espectro de esclerosis lateral amiotrofica (ALS) y sindromes de neurona motora relacionados (rangos 3, 5, 6, 7, 9, 10), todas con el mismo patron: puntuaciones de TxGNN muy altas y cercanas entre si, pero cero evidencia clinica o bibliografica. Este agrupamiento sugiere que las predicciones en este rango del modelo podrian estar influenciadas por nodos de alta conectividad en el grafo (posible artefacto de "hub"), y no por una senal farmacologica especifica. Todas las 10 indicaciones fueron clasificadas por el propio sistema como L5 / Hold.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
No existe evidencia clinica ni bibliografica para ninguna de las 10 indicaciones predichas (todas en nivel L5), y faltan datos criticos de seguridad y mecanismo de accion (brecha bloqueante DG001 sobre advertencias/contraindicaciones TFDA, y brecha alta DG002 sobre MOA). El farmaco tampoco esta comercializado en Taiwan. No hay base suficiente para avanzar a evaluacion de seguridad (S1) en ninguna de las direcciones predichas.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha tecnica de TFDA con advertencias y contraindicaciones (DG001, bloqueante)
- Obtener el mecanismo de accion (MOA) desde DrugBank API (DG002)
- Confirmar la(s) indicacion(es) original(es) aprobada(s) del farmaco, actualmente ausentes en este paquete
- Evaluar si la agrupacion de predicciones tipo ALS refleja una senal real o un artefacto del modelo antes de priorizar recursos de validacion
- Revisar interacciones farmacologicas (DDI), actualmente sin datos ("not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

