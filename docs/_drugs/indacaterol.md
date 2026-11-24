---
layout: default
title: Indacaterol
parent: Solo predicción del modelo (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Indacaterol: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (nivel de evidencia L5). Indicación original: No consta en los textos de autorización de AEMPS (uso conocido: …"
monitor_inn: "INDACATEROL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "paratenonitis", "calcific tendinitis", "hypertrichosis (disease)", "bronchial disease", "myositis", "anaphylaxis", "Ambras type hypertrichosis universalis congenita"]
---

# Indacaterol
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

## Indacaterol: De Enfermedad Pulmonar Obstructiva Crónica (EPOC) a Síndrome Nefrogénico de Antidiuresis Inapropiada
{: .text-alpha }

## Resumen en Una Frase

Indacaterol es un agonista beta-2 adrenérgico inhalado de acción ultra-larga, utilizado como broncodilatador en enfermedades obstructivas de las vías respiratorias (EPOC y, en combinación, asma).
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los textos de autorización de AEMPS (uso conocido: broncodilatador para EPOC) |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 0.9954 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 12; autorizadas no comercializadas: 6; revocadas o suspendidas: 4) |
| Número de Autorizaciones | 12 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Indacaterol actúa como agonista del receptor beta-2 adrenérgico. Relaja el músculo liso bronquial a través de la señalización mediada por AMPc. Esto encaja con la fisiopatología de la obstrucción de las vías aéreas, pero no con la de la nueva indicación predicha.

El síndrome nefrogénico de antidiuresis inapropiada se debe a mutaciones activadoras del receptor V2 de la vasopresina (AVPR2). No se conoce ninguna relación entre esa vía y el agonismo beta-2 de indacaterol. El puntaje alto (0.9954) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Por tanto, esta predicción **no resulta mecanísticamente plausible** con los datos actuales. Los datos compilados tampoco incluyen una descripción detallada del mecanismo de acción del fármaco, y la similitud con la indicación original queda pendiente de análisis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Indacaterol está comercializado en España; sus autorizaciones son todas de monofármaco, de Novartis Europharm Limited y en forma de polvo para inhalación (cápsula dura). A continuación se muestran las 5 principales. Los textos de indicación aprobada no figuran en los datos compilados.

<!-- review:begin es-lic-20261112-indacaterol-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Indacaterol está comercializado en España con 12 autorizaciones vigentes, todas de monofármaco," Corregido: no todas las autorizaciones están vigentes. Según CIMA (AEMPS) hay autorizaciones comercializadas, autorizadas pero no comercializadas y revocadas (el estado de cada una figura en la tabla de Información de Mercado en España); todas son de un único principio activo y de Novartis Europharm Limited. Las cifras actuales están en el Resumen rápido. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261112-indacaterol-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 09593007 | ONBREZ BREEZHALER 300 microgramos POLVO PARA INHALACION (CAPSULA DURA) | POLVO PARA INHALACIÓN (CÁPSULA DURA) | Novartis Europharm Limited | Comercializada |
| 09593002 | ONBREZ BREEZHALER 150 microgramos POLVO PARA INHALACION (CAPSULA DURA) | POLVO PARA INHALACIÓN (CÁPSULA DURA) | Novartis Europharm Limited | Comercializada |
| 09594007IP | HIROBRIZ BREEZHALER 300microgramos polvo para inhalacion (capsula dura) | POLVO PARA INHALACIÓN (CÁPSULA DURA) | Novartis Europharm Limited | Autorizada, no comercializada |
| 09593007IP | ONBREZ BREEZHALER 300microgramos polvo para inhalacion (capsula dura) | POLVO PARA INHALACIÓN (CÁPSULA DURA) | Novartis Europharm Limited | Autorizada, no comercializada |
| 09594002IP | HIROBRIZ BREEZHALER 150microgramos polvo para inhalacion (capsula dura) | POLVO PARA INHALACIÓN (CÁPSULA DURA) | Novartis Europharm Limited | Autorizada, no comercializada |

Se muestran 5 de 12 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Enfermedades de precaución según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN/PrimeKG, no texto del prospecto): hipertensión, síndrome de QT largo (incluido el familiar), epilepsia, hiperglucemia, diabetes mellitus, cetoacidosis diabética, déficit de potasio, parada cardíaca súbita, enfermedad de la conducción cardíaca, tirotoxicosis/hipertiroidismo, enfermedad de Graves y enfermedad coronaria.
- **Interacciones farmacológicas** (100 interacciones registradas; se muestran las principales):
  - Moderadas: acarbosa, metformina, pioglitazona, alogliptina, saxagliptina, albiglutida, canagliflozina, dapagliflozina, clorpropamida, famotidina, epinefrina, isometepteno y claritromicina.
  - Leves: corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona, beclometasona) y aprepitant.

Para advertencias y contraindicaciones oficiales, consultar el prospecto de AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos ni literatura, y no se identifica un mecanismo plausible entre el agonismo beta-2 y la activación del receptor V2 de la vasopresina. No hay base para avanzar.

**Para avanzar se necesita:**
- Una hipótesis mecanística creíble que conecte la vía beta-2 adrenérgica con la fisiopatología de la nueva indicación, y estudios preclínicos que la respalden.
- Confirmar las indicaciones aprobadas y la ficha técnica en AEMPS (advertencias y contraindicaciones), cuyos textos no están disponibles en los datos compilados.
- Datos detallados del mecanismo de acción de DrugBank.
- Como referencia, entre las demás predicciones, la de **enfermedad bronquial** (puesto 7) sí tiene respaldo clínico (nivel L1, "Proceed with Guardrails"). Sin embargo, corresponde a un uso respiratorio ya establecido y no a un reposicionamiento real.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | "12 autorizaciones vigentes" → 12 autorizaciones (2 comercializadas, 6 autorizadas no comercializadas, 4 revocadas) | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

