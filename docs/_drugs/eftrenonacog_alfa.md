---
layout: default
title: Eftrenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 3
---

# Eftrenonacog Alfa
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

# Eftrenonacog Alfa: De Hemofilia B a Pseudo-Enfermedad de Von Willebrand

## Resumen en Una Frase

Eftrenonacog alfa es un factor IX de coagulación recombinante, utilizado como terapia de reemplazo en la Hemofilia B.
El modelo TxGNN predice que podria ser efectivo para **Pseudo-Enfermedad de Von Willebrand**,
pero actualmente **no existen ensayos clinicos ni publicaciones** que respalden esta direccion — se trata unicamente de una senal computacional del modelo.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Hemofilia B (terapia de reemplazo de Factor IX) — no hay ficha tecnica registrada en Taiwan/España, dato basado en identidad conocida del farmaco |
| Nueva Indicacion Predicha | Pseudo-Enfermedad de Von Willebrand |
| Puntaje de Prediccion TxGNN | 99.48% (rank 8020) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion registrados en las fuentes consultadas. Segun la informacion conocida, eftrenonacog alfa es un factor IX de coagulacion recombinante que actua reemplazando el factor deficiente en la cascada de coagulacion, con eficacia comprobada en la Hemofilia B.

Sin embargo, el vinculo mecanistico con la Pseudo-Enfermedad de Von Willebrand es debil. Esta enfermedad esta causada por una mutacion de ganancia de funcion en el receptor plaquetario GpIb, que provoca una union anomala entre las plaquetas y el factor de von Willebrand — es decir, un defecto del receptor plaquetario, no una alteracion de la via de los factores de coagulacion. La suplementacion con Factor IX no puede corregir esta disfuncion del receptor plaquetario.

En consecuencia, esta prediccion procede unicamente de la similitud de embeddings del modelo TxGNN, sin respaldo biologico ni clinico identificado hasta el momento.

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
No existe ningun ensayo clinico ni publicacion que respalde esta direccion, el propio analisis mecanistico senala una relacion biologica debil, y el farmaco no esta comercializado en España. La evidencia es insuficiente para avanzar mas alla de la etapa de prediccion (S0).

**Para avanzar se necesita:**
- Datos de advertencias/contraindicaciones del prospecto de TFDA (actualmente bloqueante para la evaluacion inicial de seguridad S1)
- Datos detallados del mecanismo de accion (MOA) via DrugBank u otra fuente
- Validacion biologica o preclinica que conecte la via del Factor IX con el defecto del receptor plaquetario GpIb en la Pseudo-Enfermedad de Von Willebrand
- Evaluacion equivalente para los candidatos de rango 2 (Trastorno Primario de Liberacion Plaquetaria) y rango 3 (Trombastenia de Glanzmann), que presentan el mismo patron: L5, sin evidencia real, y vinculo mecanistico debil
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

