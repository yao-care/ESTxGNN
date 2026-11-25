---
layout: default
title: Palonosetron
parent: Solo predicción del modelo (L5)
nav_order: 606
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-25
description: "Palonosetron: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (las autorizaciones no incluyen…"
monitor_inn: "palonosetron"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Palonosetron
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Palonosetrón: De Prevención de Náuseas y Vómitos a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Palonosetrón es un antagonista selectivo del receptor 5-HT3, comercializado en España como antiemético. Los datos compilados para este informe no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero actualmente hay **0 ensayos clínicos** y solo **1 publicación** (un reporte de caso que describe cefalea tipo migraña *inducida* por palonosetrón), por lo que la predicción carece de respaldo clínico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (las autorizaciones no incluyen texto de indicación) |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0,9974 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 5 de 12; autorizadas no comercializadas: 3; revocadas o suspendidas: 4) |
| Número de Autorizaciones | 12 (comercializadas: 5) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Palonosetrón es un antagonista selectivo del receptor 5-HT3 de serotonina. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Palonosetron (traducción no oficial): «El palonosetrón es un antagonista del receptor 5-HT 3 con una fuerte afinidad de unión por este receptor y escasa o nula afinidad por otros receptores. La quimioterapia oncológica puede asociarse con una incidencia elevada de náuseas y vómitos, en particular cuando se utilizan ciertos agentes, como el cisplatino.» Texto original en inglés: "Palonosetron is a 5-HT 3 receptor antagonist with a strong binding affinity for this receptor and little or no affinity for other receptors. Cancer chemotherapy may be associated with a high incidence of nausea and vomiting, particularly when certain agents, such as cisplatin, are used." ([DailyMed: Posfrea (palonosetron) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=13a201ba-c86d-48c5-a0e1-a3e0b4e6a2a7), versión del 2025-04-29; consultado el 2026-11-19).

La señalización serotoninérgica participa en la fisiopatología de la migraña, lo que ofrece una justificación plausible pero indirecta para el puntaje elevado (0,9974). Además, las náuseas y los vómitos son síntomas frecuentes de la migraña, lo que acerca superficialmente ambos contextos clínicos.

Sin embargo, la única publicación disponible (PMID 21132477) describe cefalea tipo migraña **inducida** por palonosetrón, es decir, un posible efecto adverso y no un beneficio terapéutico. La predicción no está respaldada y podría estar contradicha por la señal clínica existente.

Otras predicciones del modelo TxGNN (aprendizaje profundo) son migraña con aura del tronco encefálico (0,9967), atrodermia vermiculada (0,9913) y uleritema ofriogenes (0,9907), también en nivel L5. Las dos últimas carecen de vínculo mecanístico evidente con el antagonismo 5-HT3; sus puntajes provienen del modelo TxGNN (aprendizaje profundo) y pueden reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Reporte de caso | Canadian Journal of Anaesthesia | Describe cefalea tipo migraña inducida por palonosetrón; es una señal de seguridad, no de eficacia |

Nota: para la entidad "susceptibilidad a migraña con o sin aura" se asoció además una revisión de 2026 (PMID [42748473](https://pubmed.ncbi.nlm.nih.gov/42748473/), *European Heart Journal – Cardiovascular Pharmacotherapy*) sobre prolongación del QT asociada a antieméticos. Es relevante para la seguridad cardiaca, pero no para la eficacia en migraña.

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 81572 | PALONOSETRON QILU 250 MICROGRAMOS SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Qilu Pharma Spain S.L. | Comercializada |
| 1161104001 | PALONOSETRON ACCORD 250 MICROGRAMOS SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Accord Healthcare S.L.U. | Comercializada |
| 83005 | FERANT 250 MICROGRAMOS SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Medochemie Limited | Comercializada |
| 80893 | PALONOSETRON SALA 250 MICROGRAMOS SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Laboratorio Reig Jofre, S.A. | Comercializada |
| 1151001001 | AKYNZEO 300 MG/0,5 MG CAPSULAS DURAS | CÁPSULA DURA | Helsinn Birex Pharmaceuticals Limited | Comercializada |
| 04306001 | ALOXI 250 microgramos SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Helsinn Birex Pharmaceuticals Limited | Autorizada, no comercializada |
| 1151001003 | AKYNZEO 235 MG/0,25 MG POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Helsinn Birex Pharmaceuticals Limited | Autorizada, no comercializada |
| 1151001005 | AKYNZEO 300 MG/0,5 MG SUSPENSION ORAL EN SOBRE | SUSPENSIÓN ORAL | Helsinn Birex Pharmaceuticals Limited | Autorizada, no comercializada |
| 83304 | PALONOSETRON ALTAN 250 MICROGRAMOS SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Altan Pharmaceuticals Sa | Revocada |
| 81900 | PALONOSETRON FRESENIUS KABI 250 MCROGRAMOS SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Fresenius Kabi España, S.A.U. | Revocada |

Se muestran 10 de 12 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Entre las autorizaciones figuran Aloxi y Akynzeo (combinación con netupitant en cápsulas y con fosnetupitant en polvo para perfusión).

<!-- review:begin es-lic-20261105-palonosetron-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 11 autorizaciones vigentes (todas monofármaco). Entre las restantes figuran Aloxi y Akynzeo (combinación con netupitant, en cápsulas y polvo para perfusión)." Corregido: la frase hablaba de autorizaciones que no figuraban en la tabla anterior; según CIMA (AEMPS), AKYNZEO 235 mg/0,25 mg polvo (1151001003) contiene fosnetupitant + palonosetrón y AKYNZEO 300 mg/0,5 mg cápsulas (1151001001) netupitant + palonosetrón. La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS) e incluye ambas. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-palonosetron-1 -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 398 interacciones en total. Entre las de nivel **mayor** figuran: fentanilo, dextrometorfano, tramadol, alfentanilo, almotriptán, sumatriptán, amiodarona, amisulprida, amitriptilina y anagrelida. Entre las de nivel moderado: abiraterona, dihidrocodeína, codeína, famotidina, formoterol, adenosina, salbutamol, alfuzosina, propofol y loperamida. Varias se relacionan con riesgo serotoninérgico o de prolongación del QT.
- **Señales adicionales de la literatura**: reporte de cefalea tipo migraña inducida y una revisión sobre prolongación del QT por antieméticos.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es puramente computacional (L5): no hay ensayos clínicos y la única literatura vinculada apunta a un posible efecto adverso (cefalea tipo migraña) en lugar de un beneficio. El mecanismo aporta solo una plausibilidad indirecta.

**Para avanzar se necesita:**
- Revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada)
- Datos detallados del mecanismo de acción
- Revisión sistemática de la literatura sobre antagonistas 5-HT3 en migraña y la señal de cefalea inducida
- Evidencia preclínica o clínica de eficacia en migraña antes de reconsiderar la decisión
- Evaluación de riesgo cardiaco (QT) e interacciones con triptanes y otros serotoninérgicos, relevantes en pacientes con migraña

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | «Entre las restantes» → «Entre las autorizaciones»; Akynzeo en polvo es fosnetupitant + palonosetrón | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Posfrea (palonosetron) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=13a201ba-c86d-48c5-a0e1-a3e0b4e6a2a7) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

