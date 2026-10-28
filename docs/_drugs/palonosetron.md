---
layout: default
title: Palonosetron
parent: Solo predicción del modelo (L5)
nav_order: 606
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
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
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 11) |
| Número de Autorizaciones | 11 (vigentes: 5) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Palonosetrón es un antagonista selectivo del receptor 5-HT3 de serotonina. No se dispone de datos detallados del mecanismo de acción en los datos compilados; esta descripción se basa en la clase farmacológica conocida del fármaco.

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

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 81572 | Palonosetron Qilu 250 microgramos solución inyectable EFG | Solución inyectable | No disponible |
| 83304 | Palonosetron Altan 250 microgramos solución inyectable EFG | Solución inyectable | No disponible |
| 1161104001 | Palonosetron Accord 250 microgramos solución inyectable EFG | Solución inyectable | No disponible |
| 83005 | Ferant 250 microgramos solución inyectable EFG | Solución inyectable | No disponible |
| 81900 | Palonosetron Fresenius Kabi 250 microgramos solución inyectable EFG | Solución inyectable | No disponible |

Se muestran 5 de las 11 autorizaciones vigentes (todas monofármaco). Entre las restantes figuran Aloxi y Akynzeo (combinación con netupitant, en cápsulas y polvo para perfusión).

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

