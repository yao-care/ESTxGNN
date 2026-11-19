---
layout: default
title: Granisetron
parent: Solo predicción del modelo (L5)
nav_order: 385
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Granisetron: nueva indicación predicha, Trastorno afectivo bipolar maníaco (manic bipolar affective disorder) (nivel de evidencia L5). Indicación original: No disponible en los datos de licencias de …"
monitor_inn: "granisetron"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
---

# Granisetron
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

## Granisetrón: De Indicación Original No Registrada a Trastorno Bipolar Maníaco
{: .text-alpha }

## Resumen en Una Frase

Granisetrón es un antagonista selectivo de los receptores 5-HT3, comercializado en España en múltiples presentaciones (inyectable, comprimidos, perfusión y parche transdérmico). El texto de indicación aprobada no está disponible en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **trastorno afectivo bipolar maníaco**, pero **no existe ningún ensayo clínico ni publicación** que respalde esta dirección; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de licencias de la AEMPS |
| Nueva Indicación Predicha | Trastorno afectivo bipolar maníaco (manic bipolar affective disorder) |
| Puntaje de Predicción TxGNN | 0,9962 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 7 de 11; autorizadas no comercializadas: 1; revocadas o suspendidas: 3) |
| Número de Autorizaciones | 11 (comercializadas: 7) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Granisetrón es un antagonista selectivo del receptor 5-HT3 de serotonina. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Granisetron (traducción no oficial): «El granisetrón es un antagonista selectivo de los receptores de 5-hidroxitriptamina 3 (5-HT 3 ) con poca o ninguna afinidad por otros receptores de serotonina, incluidos 5-HT 1, 5-HT 1A, 5-HT 1B/C, 5-HT 2; por los adrenorreceptores alfa 1, alfa 2 o beta; por los receptores de dopamina D 2; ni por los receptores de histamina H 1, de benzodiazepinas, de picrotoxina ni opioides. Los receptores de serotonina del tipo 5-HT 3 se localizan periféricamente en las terminaciones nerviosas vagales y centralmente en la zona gatillo quimiorreceptora del área postrema.» Texto original en inglés: "Granisetron is a selective 5-hydroxytryptamine 3 (5-HT 3 ) receptor antagonist with little or no affinity for other serotonin receptors, including 5-HT 1, 5-HT 1A, 5-HT 1B/C, 5-HT 2; for alpha 1-, alpha 2-, or beta-adrenoreceptors; for dopamine-D 2; or for histamine-H 1; benzodiazepine; picrotoxin or opioid receptors. Serotonin receptors of the 5-HT 3 type are located peripherally on vagal nerve terminals and centrally in the chemoreceptor trigger zone of the area postrema." ([DailyMed: Sustol (granisetron) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7c7ffdd-8270-4030-bc1e-a1cb28a6de56), versión del 2026-04-30; consultado el 2026-11-19).

La relación con el trastorno bipolar maníaco es **especulativa**. Se ha planteado que la modulación de 5-HT3 podría influir en la señalización dopaminérgica y serotoninérgica relacionada con la regulación del ánimo, pero no hay ensayos ni literatura que lo confirmen. La puntuación alta de TxGNN (0,9962) refleja únicamente una predicción del modelo TxGNN (aprendizaje profundo).

Cabe señalar que no se pudo establecer una similitud formal entre la indicación original y la nueva indicación, al no disponerse del texto de indicación aprobada.

### Otras indicaciones predichas (referencia)

| Rango | Indicación predicha | Puntaje TxGNN | Plausibilidad mecanística |
|---|------|------|------|
| 2 | Síndrome de Tourette | 0,9952 | Hipotética (se han explorado otros 5-HT3 como ondansetrón en estudios pequeños) |
| 3 | Conjuntivitis contagiosa aguda | 0,9949 | Sin vínculo plausible; la puntuación procede del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes aprendidas por el modelo entre enfermedades relacionadas, no evidencia biológica |
| 4 | Angioedema | 0,9936 | Débil (vías de histamina/bradicinina) |
| 5 | Urticaria alérgica | 0,9932 | Especulativa (serotonina y mastocitos) |
| 6 | Síndrome nefrogénico de antidiuresis inapropiada | 0,9932 | Sin vínculo aparente (mutaciones del receptor V2) |
| 7 | Tricotilomanía | 0,9923 | Hipotética (espectro obsesivo-compulsivo) |
| 8 | Bronquitis | 0,9918 | Sin fundamento mecanístico claro |
| 9 | Urticaria por frío | 0,9910 | Especulativa |
| 10 | Conjuntivitis | 0,9909 | Sin vínculo establecido |

Todas ellas tienen nivel de evidencia L5 y recomendación Hold.

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
| 59867 | KYTRIL 3MG/3ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible |
| 68225 | GRANISETRON ALTAN 1 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película | No disponible |
| 71577 | GRANISETRON AUROVITAS SPAIN 1 mg COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película | No disponible |
| 61803 | KYTRIL 1MG/1ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible |
| 60204 | KYTRIL 1 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible |

El resto incluye presentaciones en solución para perfusión, concentrado para solución inyectable y el parche transdérmico SANCUSO 3,1 mg/24 h.

<!-- review:begin es-lic-20261105-granisetron-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se muestran 5 de las 11 autorizaciones vigentes (todas de monofármaco). El resto incluye presentaciones en solución para perfusión, concentrado para solución inyectable y el parche transdérmico SANCUSO 3,1 mg/24 h." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 11 autorizaciones (comercializadas: 7); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-granisetron-1 -->

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del texto del prospecto)**: síndrome de QT largo, síndrome de QT largo familiar, deficiencia de potasio, paro cardíaco súbito y enfermedad de la conducción cardíaca. En conjunto, indican un riesgo de prolongación del QT y de arritmias.
- **Interacciones Farmacológicas**: se identificaron 461 interacciones en total. Entre las principales de nivel **Mayor**: fentanilo, dextrometorfano, tramadol, alfentanilo, almotriptán, sumatriptán, amiodarona, amisulprida, amitriptilina y anagrelida. Varias se relacionan con prolongación del QT o con riesgo de síndrome serotoninérgico. Entre las de nivel **Moderado**: abametapir, abiraterona, dihidrocodeína, codeína, famotidina, formoterol, adenosina, salbutamol, alfuzosina y propofol.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para trastorno bipolar maníaco se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y con un vínculo mecanístico especulativo. Además, el perfil de riesgo cardíaco (QT) y las numerosas interacciones mayores exigirían cautela en una población que a menudo usa antipsicóticos y antidepresivos.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente sin datos.
- Completar los datos del mecanismo de acción.
- Realizar una revisión sistemática de literatura preclínica y clínica sobre antagonistas 5-HT3 en trastorno bipolar y manía.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original.
- Evaluar el riesgo de prolongación del QT y de interacciones con estabilizadores del ánimo y antipsicóticos antes de plantear cualquier estudio.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se muestran 5 de las 11 autorizaciones vigentes (todas de monofármaco)" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Sustol (granisetron) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7c7ffdd-8270-4030-bc1e-a1cb28a6de56) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

