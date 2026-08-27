---
layout: default
title: Lonoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Lonoctocog Alfa: De Hemofilia A a Pseudo-Enfermedad de von Willebrand

## Resumen en Una Frase

Lonoctocog alfa es un Factor VIII de coagulación recombinante, utilizado como terapia de reemplazo en la Hemofilia A (deficiencia de FVIII) — esta indicación original no consta en el registro formal del dossier, pero se desprende del propio texto de racionalidad mecanistica incluido en los datos. El modelo TxGNN predice que podria ser efectivo para **Pseudo-Enfermedad de von Willebrand (tipo plaquetario)**, pero actualmente **no existe ningun ensayo clinico ni publicacion** que respalde esta direccion, y el propio analisis de racionalidad mecanistica incluido en los datos senala que no hay una via farmacologica plausible que conecte ambas condiciones.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Hemofilia A (deficiencia de Factor VIII), segun descripcion mecanistica del dossier — sin indicacion oficial registrada en Espana |
| Nueva Indicacion Predicha | Pseudo-Enfermedad de von Willebrand (tipo plaquetario) |
| Puntaje de Prediccion TxGNN | 99.85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en el registro formal (DrugBank). Segun la informacion disponible en el analisis de racionalidad del propio dossier, lonoctocog alfa es un Factor VIII de coagulacion recombinante, cuya indicacion conocida es la Hemofilia A (deficiencia de FVIII), donde actua como cofactor en la activacion del Factor X dentro de la cascada de coagulacion.

La Pseudo-Enfermedad de von Willebrand, sin embargo, es una alteracion distinta: se origina por una mutacion de ganancia de funcion en la glicoproteina plaquetaria GPIbα, que provoca una union anormalmente fuerte entre las plaquetas y el factor de von Willebrand. No se trata de un deficit o disfuncion del Factor VIII, por lo que el reemplazo de FVIII no tiene, en principio, una via farmacologica directa para corregir este defecto plaquetario.

De hecho, el propio texto de racionalidad mecanistica incluido en los datos es explicito al respecto: senala que **no existe una via de soporte farmacologico** entre ambas condiciones, y que la asociacion proviene unicamente de la co-ocurrencia detectada por el grafo de conocimiento de TxGNN, sin respaldo mecanistico ni clinico adicional. Esto se refleja de forma consistente en las otras tres indicaciones predichas para este farmaco (trastorno primario de liberacion plaquetaria, trombastenia de Glanzmann, sindrome de Scott), todas ellas trastornos de la funcion plaquetaria mecanisticamente distintos de la deficiencia de FVIII, y todas con la misma recomendacion de Hold.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La evidencia es de nivel L5 (unicamente prediccion del modelo, sin ensayos clinicos ni literatura), y el propio analisis mecanistico del dossier indica que no existe una via farmacologica plausible entre el reemplazo de Factor VIII y un trastorno de la funcion plaquetaria como la Pseudo-Enfermedad de von Willebrand. Ademas, existe una brecha de datos bloqueante (DG001: advertencias/contraindicaciones de TFDA no disponibles), lo que impide avanzar siquiera a la evaluacion inicial de seguridad (S1).

**Para avanzar se necesita:**
- Datos del prospecto oficial (TFDA/AEMPS): advertencias, contraindicaciones e interacciones (actualmente bloqueante)
- Confirmacion formal del mecanismo de accion (MOA) en fuente primaria (DrugBank u otra)
- Estudios preclinicos o de mecanismo que exploren alguna via indirecta entre FVIII y la funcion plaquetaria en Pseudo-EvW, dado que la evidencia actual no identifica ninguna
- Evaluar si el interes real reside en otro objetivo terapeutico, ya que las cuatro indicaciones predichas (rangos 1-4) comparten la misma limitacion mecanistica y el mismo nivel de evidencia (L5)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

