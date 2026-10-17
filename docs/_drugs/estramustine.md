---
layout: default
title: Estramustine
parent: Solo predicción del modelo (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Estramustine: nueva indicación predicha, Susceptibilidad al cáncer de próstata/cáncer cerebral (nivel de evidencia L5). Indicación original: Cáncer de próstata (según el grafo de conocimiento"
monitor_inn: "Estramustine"
predicted_indications: ["fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "prostate leiomyoma", "benign prostate phyllodes tumor", "female breast carcinoma", "HIV infectious disease", "breast fibrocystic disease"]
---

# Estramustine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Estramustina: De Cáncer de Próstata a Susceptibilidad Genética al Cáncer de Próstata/Cerebro

## Resumen en Una Frase

Estramustina es un conjugado de estradiol con una mostaza nitrogenada (carbamato), utilizado originalmente para el tratamiento del cáncer de próstata.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad al cáncer de próstata/cáncer cerebral**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta.
Se trata de una entidad de predisposición genética, no de una enfermedad tratable, por lo que la predicción es puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de próstata (según el grafo de conocimiento; el texto de indicación de la autorización española no está disponible) |
| Nueva Indicación Predicha | Susceptibilidad al cáncer de próstata/cáncer cerebral |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente principal. Según la información conocida, estramustina combina estradiol con una mostaza nitrogenada en forma de carbamato. Actúa como agente antimicrotúbulos: se une a las proteínas asociadas a microtúbulos y a la tubulina, y detiene las células en la fase G2/M. En el tejido prostático se concentra gracias a una proteína de unión específica (EMBP).

El puntaje tan alto probablemente refleja la **cercanía en el grafo de conocimiento** con el cáncer de próstata, que es su indicación aprobada. No refleja una relación terapéutica real. Una susceptibilidad genética no es un estado patológico que un fármaco citotóxico pueda tratar, y no existe un vínculo demostrado entre estramustina y la modificación de dicha susceptibilidad.

Por tanto, la predicción no aporta una hipótesis de reposicionamiento mecanísticamente defendible. La similitud con la indicación original queda pendiente de evaluación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 54190 | ESTRACYT 140 mg cápsulas duras (Pfizer S.L.) | Cápsula dura | No disponible en los datos compilados |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimicrotúbulos; conjugado estradiol-mostaza nitrogenada) |
| Riesgo de Mielosupresión | Bajo a medio como agente único (un estudio en cáncer de mama lo describe con escasa toxicidad hematológica); aumenta al combinarse con taxanes u otros citotóxicos |
| Clasificación de Emetogenicidad | Baja a media (estimación según la clase del fármaco; confirmar en el prospecto) |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, calcio sérico, glucemia, presión arterial y signos de eventos tromboembólicos o retención de líquidos |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): trastornos hipertensivos, epilepsia, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, diabetes mellitus y cetoacidosis diabética, hipercalcemia y alteraciones del metabolismo del fósforo, tromboflebitis, enfermedad coronaria e infarto de miocardio, trastornos cerebrovasculares, migraña, hemoglobinopatías, hiperbilirrubinemia (incluido el síndrome de Gilbert), ginecomastia e hipertrofia mamaria, y disfunciones sexuales como la disfunción eréctil y la eyaculación precoz.
- **Interacciones farmacológicas**: se registran 100 interacciones conocidas. Las 20 primeras analizadas son de nivel moderado. Los grupos principales son:
  - **Corticoides**: hidrocortisona, dexametasona, betametasona, triamcinolona y budesonida.
  - **Antidiabéticos**: acarbosa, metformina, clorpropamida, alogliptina, linagliptina, canagliflozina, dapagliflozina, empagliflozina, albiglutida y dulaglutida.
  - **Otros**: anfotericina B (y su complejo lipídico) y sales de calcio (fosfato y acetato de calcio, calcitriol tópico).

La información de advertencias y contraindicaciones del prospecto de la AEMPS no está disponible. Consultar el prospecto para completarla.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción corresponde a una entidad de susceptibilidad genética sin ensayos ni publicaciones, con evidencia de nivel L5 y sin mecanismo plausible. El puntaje alto parece un artefacto de la cercanía al cáncer de próstata en el grafo de conocimiento.

**Para avanzar se necesita:**
- Aclarar si esta entidad puede considerarse una indicación tratable. Lo más probable es que deba descartarse como candidata.
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un paso bloqueante para el cribado de seguridad.
- Completar los datos de mecanismo de acción en DrugBank.
- Revisar otras predicciones del mismo análisis con más respaldo:
  - **Carcinoma de mama femenino** (nivel L2): un ensayo de Fase 2 de docetaxel con estramustina de estado desconocido y estudios de Fase 1/2 y Fase 2 con actividad en cáncer de mama avanzado. La evidencia es antigua, de escasa potencia y no aleatorizada.
  - **Cáncer de órganos reproductivos masculinos** (nivel L1): corresponde en esencia al cáncer de próstata ya aprobado, por lo que no constituye un hallazgo de reposicionamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

