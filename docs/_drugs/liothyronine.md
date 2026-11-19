---
layout: default
title: Liothyronine
parent: Solo predicción del modelo (L5)
nav_order: 473
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-05
monitor_inn: "Liothyronine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Carney complex", "peripheral dysostosis", "Potter sequence", "acrodysostosis with or without hormone resistance", "myxoma", "angiomyxoma", "hypotrichosis simplex of the scalp"]
description: "Liothyronine: nueva indicación predicha, Hipodisplasia/aplasia renal (renal hypodysplasia/aplasia) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 0)"
---

# Liothyronine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Liothyronine: Hipodisplasia/aplasia renal (renal hypodysplasia/aplasia)
{: .text-alpha }

## Resumen en Una Frase

La liotironina (triyodotironina, T3) es una hormona tiroidea sintética, utilizada originalmente para tratar el hipotiroidismo y otras enfermedades de la tiroides, como el bocio.
El modelo TxGNN predice que podría ser efectiva para **hipodisplasia/aplasia renal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipodisplasia/aplasia renal (renal hypodysplasia/aplasia) |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Liothyronine (traducción no oficial): «Las hormonas tiroideas ejercen sus acciones fisiológicas mediante el control de la transcripción del DNA y de la síntesis de proteínas. La triyodotironina (T3) y la L-tiroxina (T4) difunden al núcleo celular y se unen a proteínas receptoras tiroideas unidas al DNA.» Texto original en inglés: "Thyroid hormones exert their physiologic actions through control of DNA transcription and protein synthesis. Triiodothyronine (T3) and L-thyroxine (T4) diffuse into the cell nucleus and bind to thyroid receptor proteins attached to DNA." ([DailyMed: Cytomel (liothyronine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51452b31-ff68-4e0c-b982-c15502ebf1d3), versión del 2026-05-18; consultado el 2026-11-19). Según la información conocida, la liotironina es la forma activa de la hormona tiroidea (T3): su eficacia en el hipotiroidismo y en enfermedades tiroideas está bien establecida, y actúa sustituyendo la hormona deficiente y suprimiendo la TSH.

Sin embargo, **no se identifica un vínculo mecanístico plausible** con la nueva indicación. La hipodisplasia o aplasia renal es una malformación congénita del desarrollo, de carácter estructural, y es improbable que una hormona administrada después del nacimiento pueda revertirla. El puntaje elevado proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas (fenotipos de anomalías congénitas compartidos), no evidencia biológica ni una justificación terapéutica.

Conviene señalar que otras predicciones del mismo análisis siguen patrones similares. Entre ellas figuran la agenesia renal bilateral, la secuencia de Potter, el complejo de Carney, el mixoma y el angiomixoma, todas sin evidencia clínica. El bocio nodular ya forma parte de las indicaciones originales, por lo que no constituye un verdadero reposicionamiento. La acrodisostosis, con hormonas resistentes, es mecanísticamente concebible pero no está demostrada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hipodisplasia/aplasia renal.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 45503 | TRIYODOTIRONINA LEO | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, hipopituitarismo y déficits de hormona de crecimiento o hipogonadismo hipogonadotrópico, osteoporosis (incluida la posmenopáusica), diabetes mellitus y cetoacidosis diabética, enfermedad coronaria e infarto de miocardio, y enfermedades del timo.
- **Interacciones farmacológicas**: se identificaron 100 interacciones; las 20 mostradas son todas de nivel moderado. Destacan:
  - Antidiabéticos: acarbosa, metformina, pioglitazona, alogliptina, linagliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida, albiglutida y dulaglutida.
  - Inhibidores de la bomba de protones: omeprazol, rabeprazol y dexlansoprazol.
  - Simpaticomiméticos: epinefrina, isometepteno y dietilpropión.
  - Sales de calcio y magnesio: fosfato de calcio, acetato de calcio y óxido de magnesio.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni literatura, y no existe un mecanismo plausible para corregir una malformación renal congénita con hormona tiroidea. Además, el perfil de seguridad (cardiovascular, óseo y metabólico) no justifica un uso especulativo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y análisis del vínculo mecanístico con la nueva indicación
- Texto de indicaciones, advertencias y contraindicaciones del prospecto de AEMPS
- Estudios preclínicos o de mecanismo que justifiquen un efecto sobre el desarrollo renal
- Reevaluar candidatos con mayor sustento biológico antes de invertir más recursos en esta predicción

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cytomel (liothyronine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51452b31-ff68-4e0c-b982-c15502ebf1d3) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

