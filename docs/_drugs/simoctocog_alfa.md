---
layout: default
title: Simoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
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

# Simoctocog Alfa: De Hemofilia A a Pseudo-enfermedad de von Willebrand

## Resumen en Una Frase

Simoctocog alfa es una proteína recombinante de Factor VIII (FVIII) humano, utilizada originalmente como terapia de reemplazo en la **Hemofilia A**.
El modelo TxGNN predice que podria ser efectivo para la **Pseudo-enfermedad de von Willebrand**,
con un score de **99.99%**, pero actualmente **no existe ningun ensayo clinico ni publicacion** que respalde esta direccion, y el propio analisis mecanistico del pipeline senala una relacion causal debil.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No consta en licencias espanolas (farmaco no comercializado en Espana); segun la informacion recogida en el propio evidence pack, Hemofilia A (terapia de reemplazo de Factor VIII) |
| Nueva Indicacion Predicha | Pseudo-enfermedad de von Willebrand |
| Puntaje de Prediccion TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion (MOA) desde DrugBank. Segun la informacion conocida, simoctocog alfa es una proteina recombinante de Factor VIII humano (FVIII), cuya funcion es sustituir al FVIII endogeno deficiente, unirse al factor de von Willebrand (vWF) circulante para estabilizarse, y activar el Factor X en la cascada de coagulacion; su eficacia en la Hemofilia A esta bien establecida.

La Pseudo-enfermedad de von Willebrand, sin embargo, no es un trastorno de deficiencia de FVIII, sino una alteracion del receptor plaquetario GPIbα que provoca una afinidad anormalmente alta hacia el vWF, con el consiguiente consumo y aclaramiento de los multimeros de alto peso molecular. El defecto reside en la plaqueta, no en la concentracion de factores de coagulacion, por lo que aportar FVIII exogeno no corrige el mecanismo patologico subyacente.

Segun el propio analisis mecanistico incluido en el evidence pack, el score elevado de TxGNN probablemente refleja la proximidad de ambas entidades en el grafo de conocimiento (nodo comun de "trastorno hemorragico") mas que una relacion causal real entre FVIII y esta patologia plaquetaria. Esto, sumado a la ausencia total de ensayos clinicos y literatura, respalda una postura conservadora ante esta prediccion concreta.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
- El nivel de evidencia es L5 (unicamente prediccion del modelo, sin ningun ensayo clinico ni publicacion real que la respalde).
- El propio analisis mecanistico del evidence pack senala que la relacion causal entre FVIII y la Pseudo-enfermedad de von Willebrand es debil y probablemente artefactual (comorbilidad de fenotipo hemorragico en el grafo), no una via terapeutica plausible.
- Existe un data gap bloqueante (DG001: advertencias/contraindicaciones de TFDA) que impide, en cualquier caso, iniciar la evaluacion de seguridad S1.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha tecnica de TFDA con advertencias y contraindicaciones (DG001, bloqueante).
- Completar los datos de mecanismo de accion (MOA) via API de DrugBank (DG002).
- Buscar estudios preclinicos o de mecanismo sobre el efecto de FVIII en trastornos de la funcion plaquetaria, para intentar elevar el nivel de evidencia de L5 a L4 si existieran.
- Dado que otros candidatos del mismo evidence pack (p. ej. "hemophilia A with vascular abnormality", rank 9) muestran mayor coherencia mecanistica con la indicacion original, se recomienda una revision comparativa antes de descartar el reposicionamiento de este farmaco en su conjunto.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

