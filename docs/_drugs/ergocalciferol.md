---
layout: default
title: Ergocalciferol
parent: Solo predicción del modelo (L5)
nav_order: 303
evidence_level: L5
indication_count: 10
---

# Ergocalciferol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Ergocalciferol: De Osteoporosis y Trastornos del Metabolismo del Calcio y la Vitamina D a Hipoparatiroidismo Aislado Familiar por Alteración de la Secreción de PTH

## Resumen en Una Frase

Ergocalciferol (vitamina D2) es una vitamina liposoluble que se usa en la prevención y el tratamiento de la deficiencia de vitamina D y de enfermedades óseas y del metabolismo del calcio y el fósforo, como el raquitismo, la osteomalacia, la osteoporosis y el hipoparatiroidismo.
El modelo TxGNN predice que podría ser efectivo para **hipoparatiroidismo aislado familiar por alteración de la secreción de PTH**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción específica, por lo que se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Osteoporosis, hipoparatiroidismo, raquitismo, osteomalacia y deficiencia de vitamina D (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipoparatiroidismo aislado familiar por alteración de la secreción de PTH |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, ergocalciferol es una forma nutricional de vitamina D. Se convierte en el hígado y el riñón en metabolitos activos que favorecen la absorción intestinal de calcio y fósforo. Su eficacia en trastornos del metabolismo mineral y óseo está bien establecida, y mecanísticamente podría ser aplicable al hipoparatiroidismo.

La relación con la indicación original es estrecha. El hipoparatiroidismo ya figura entre las indicaciones originales del fármaco en el grafo de conocimiento. Los análogos de la vitamina D aumentan la absorción de calcio cuando falta la hormona paratiroidea (PTH), de modo que esta forma familiar rara resulta biológicamente plausible como extensión.

Conviene interpretar el puntaje con cautela. Esta predicción probablemente se solapa con la indicación de hipoparatiroidismo ya existente y no representa un uso realmente nuevo. No hay ensayos ni literatura específicos para este subtipo familiar, por lo que el puntaje alto (99.85%) es solo una predicción del modelo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61021 | VITALIPID INFANTIL | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 61020 | VITALIPID ADULTOS | Concentrado para solución para perfusión | No disponible en los datos compilados |

Ambas autorizaciones están vigentes, corresponden a Fresenius Kabi España, S.A.U., y son productos de un solo principio activo según el registro.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto de prospecto): hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, hiperparatiroidismo, osteítis fibrosa, sarcoidosis, enfermedad renal, enfermedad hepática y de la vesícula biliar, hipertensión, fibrilación auricular, diabetes mellitus y cetoacidosis diabética, trastornos de la coagulación, hiperoxaluria primaria, hemocromatosis y otros trastornos del metabolismo del hierro, enfermedad de Wilson, hiperlipidemia, y cáncer de mama y de próstata, entre otras.
- **Interacciones farmacológicas** (55 registradas):
  - **Mayores:** colecalciferol, calcifediol, calcitriol y doxercalciferol. Se trata de otros compuestos de vitamina D, con riesgo de efecto aditivo e hipercalcemia.
  - **Moderadas (principales):** diuréticos tiazídicos (hidroclorotiazida, clorotiazida, clortalidona), digoxina, carbamazepina, barbitúricos (amobarbital, butalbital), rifabutina, resinas secuestradoras de ácidos biliares (colestiramina, colesevelam, colestipol), sevelámero, óxido de magnesio y calcipotriol y calcitriol tópicos.
  - **Menor:** cimetidina.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo cuenta con el respaldo del modelo (nivel L5), sin ensayos clínicos ni literatura específica para este subtipo familiar de hipoparatiroidismo. Además, probablemente se solapa con una indicación ya existente del fármaco.

**Para avanzar se necesita:**
- Revisar el prospecto de las autorizaciones de AEMPS para obtener las advertencias, contraindicaciones e indicaciones aprobadas.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Confirmar si esta forma familiar constituye realmente un uso nuevo o queda cubierta por la indicación existente de hipoparatiroidismo.
- Buscar literatura o casos clínicos específicos sobre el hipoparatiroidismo aislado familiar con vitamina D2.
- Definir un plan de monitoreo de calcio, fósforo, PTH y 25(OH)D, con vigilancia del riesgo de hipercalcemia.
- Valorar si la formulación comercializada en España (perfusión de multivitaminas liposolubles) es adecuada para esta indicación.

**Nota complementaria:** entre las otras indicaciones predichas, la **osteodistrofia renal** (puntaje 99.67%) tiene mayor respaldo (nivel L3: un ensayo de Fase 4 de estado desconocido, un estudio comparativo con calcitriol y guías clínicas). Se recomienda evaluarla como candidata prioritaria con salvaguardas, vigilando calcio, fósforo y PTH.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

