---
layout: default
title: Ebastine
parent: Solo predicción del modelo (L5)
nav_order: 274
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Ebastine"
predicted_indications: ["coronary artery disease", "myocardial ischemia"]
description: "Ebastine: nueva indicación predicha, Enfermedad de las arterias coronarias (coronary artery disease) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Ebastine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Ebastine: Enfermedad de las arterias coronarias (coronary artery disease)
{: .text-alpha }

## Resumen en Una Frase

Ebastina es un antihistamínico H1 de segunda generación, utilizado originalmente para el tratamiento de la rinitis alérgica, la rinitis vasomotora y la urticaria idiopática.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de las arterias coronarias**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad de las arterias coronarias (coronary artery disease) |
| Puntaje de Predicción TxGNN | 0.9918 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 17; autorizadas no comercializadas: 1; revocadas o suspendidas: 2) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

Nota: el modelo también predijo **isquemia miocárdica** (puntaje 0,9910, nivel de evidencia L5, decisión Hold). Esta indicación está estrechamente relacionada con la enfermedad coronaria, por lo que ambas predicciones probablemente no son independientes.

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Ebastine es (traducción no oficial): «Agonista inverso del receptor H1 de histamina». Texto original en inglés: "Histamine H1 receptor inverse agonist" ([ChEMBL CHEMBL305660 (ebastine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL305660), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, ebastina es un antagonista del receptor H1 de histamina de segunda generación, con eficacia comprobada en rinitis alérgica, rinitis vasomotora y urticaria idiopática.

Una posible vía especulativa sería la participación de la histamina y de los mastocitos en el vasoespasmo coronario y en la inestabilidad de la placa aterosclerótica. Sin embargo, **ninguna evidencia incluida en los datos compilados para este informe respalda esta hipótesis**. Las indicaciones originales (alérgicas y respiratorias) y la nueva indicación (cardiovascular) pertenecen a áreas terapéuticas distintas, y la similitud entre ambas aún está pendiente de análisis.

El puntaje elevado de TxGNN (0,9918) es una predicción basada en el modelo, no corroborada por ensayos ni literatura. Además, la seguridad cardiaca requiere atención: algunos antihistamínicos presentan preocupaciones de prolongación del intervalo QT, y esto no se ha evaluado en los datos disponibles.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin es-lic-20261105-ebastine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único, ninguna cancelada)." Eliminado: afirmaba que el medicamento no está autorizado o comercializado en España, o que sus autorizaciones están revocadas o suspendidas, lo que no coincide con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-ebastine-1 -->

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 67663 | EBASTINA TARBIS 10 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tarbis Farma S.L. | Comercializada |
| 80256 | EBASTINA FLAS STADA 10 MG COMPRIMIDOS BUCODISPERSABLES EFG | COMPRIMIDO BUCODISPERSABLE | Laboratorio Stada S.L. | Comercializada |
| 74992 | EBASTINA TEVA-RATIOPHARM 20 MG COMPRIMIDOS BUCODISPERSABLES EFG | COMPRIMIDO BUCODISPERSABLE | Teva Pharma S.L.U. | Comercializada |
| 67708 | EBASTINA VIATRIS 20 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Viatris Pharmaceuticals S.L. | Comercializada |
| 74991 | EBASTINA TEVA-RATIOPHARM 10 MG COMPRIMIDOS BUCODISPERSABLES EFG | COMPRIMIDO BUCODISPERSABLE | Teva Pharma S.L.U. | Comercializada |
| 76459 | EBASTINA KERN PHARMA 20 MG COMPRIMIDOS BUCODISPERSABLES EFG | COMPRIMIDO BUCODISPERSABLE | Kern Pharma S.L. | Comercializada |
| 78491 | EBASTINA SANDOZ 20 MG COMPRIMIDOS BUCODISPERSABLES EFG | COMPRIMIDO BUCODISPERSABLE | Sandoz Farmaceutica S.A. | Comercializada |
| 69521 | EBASTINA TECNIGEN 20 mg COMPRIMIDOS EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tecnimede España Industria Farmaceutica S.A. | Comercializada |
| 63366 | EBASTEL FORTE 20 mg COMPRIMIDOS RECUBIERTOS CON PELÍCULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Almirall S.A. | Comercializada |
| 67655 | EBASTINA KERN PHARMA 20 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Kern Pharma S.L. | Comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

Los textos de indicación aprobada no figuran en los datos compilados. Las formas farmacéuticas disponibles son comprimidos recubiertos con película y comprimidos bucodispersables, ambos de administración oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura que la respalden, y sin datos de mecanismo de acción ni de seguridad. Además, existe una preocupación potencial de seguridad cardiaca (prolongación del QT) con algunos antihistamínicos.

**Para avanzar se necesita:**
- Obtener los datos del mecanismo de acción (por ejemplo, desde DrugBank) y analizar el vínculo mecanístico con la enfermedad coronaria.
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), paso necesario antes del cribado de seguridad.
- Evaluar específicamente el riesgo cardiaco, incluida la prolongación del QT.
- Buscar estudios preclínicos, observacionales o ensayos clínicos que relacionen antihistamínicos H1 con enfermedad coronaria o isquemia miocárdica.
- Consultar interacciones farmacológicas, ya que la consulta no arrojó resultados.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único, ninguna cancelada)" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL305660 (ebastine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL305660) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

