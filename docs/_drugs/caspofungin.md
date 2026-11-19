---
layout: default
title: Caspofungin
parent: Solo predicción del modelo (L5)
nav_order: 151
evidence_level: L5
indication_count: 1
monitor_inn: "caspofungin"
predicted_indications: ["gastrin secretion abnormality"]
last_modified_at: 2026-11-05
description: "Caspofungin: nueva indicación predicha, Anomalía de la secreción de gastrina (gastrin secretion abnormality) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Caspofungin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Caspofungina: antifúngico equinocandina → Anomalía de la secreción de gastrina (gastrin secretion abnormality)
{: .text-alpha }

## Resumen en Una Frase

Caspofungina es un antifúngico de la clase de las equinocandinas, de administración intravenosa.
El modelo TxGNN predice que podría ser efectivo para **Anomalía de la secreción de gastrina (gastrin secretion abnormality)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Anomalía de la secreción de gastrina (gastrin secretion abnormality) |
| Puntaje de Predicción TxGNN | 0,9944 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 6; autorizadas no comercializadas: 5; revocadas o suspendidas: 9) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Caspofungin (traducción no oficial): «La caspofungina es un fármaco antifúngico de la clase de las equinocandinas. […] La caspofungina, una equinocandina, inhibe la síntesis del beta (1,3)-D-glucano, un componente esencial de la pared celular de las especies sensibles de Aspergillus y de Candida. El beta (1,3)-D-glucano no está presente en las células de los mamíferos.» Texto original en inglés: "Caspofungin is an echinocandin antifungal drug. […] Caspofungin, an echinocandin, inhibits the synthesis of beta (1,3)-D-glucan, an essential component of the cell wall of susceptible Aspergillus species and Candida species. Beta (1,3)-D-glucan is not present in mammalian cells." ([DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c), versión del 2024-10-11; consultado el 2026-11-19). Según la información farmacológica conocida, caspofungina es una equinocandina que inhibe la beta-(1,3)-D-glucano sintasa de la pared celular de los hongos. Las células de mamífero carecen de esta diana.

No se ha identificado ninguna vía biológica que conecte este mecanismo con la regulación de la gastrina, la función de las células G o la secreción de ácido gástrico. Por tanto, no se establece un vínculo mecanístico entre el uso antifúngico del fármaco y la nueva indicación predicha.

El puntaje alto (0,9944) es solo una predicción del modelo y no está respaldado por ningún fundamento biológico, ensayo clínico ni publicación. Además, caspofungina se administra por vía intravenosa y tiene biodisponibilidad oral limitada, lo que condicionaría cualquier uso dirigido al aparato digestivo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

El fármaco figura como comercializado en España, con autorizaciones válidas de medicamentos de un solo principio activo. La lista puede ser parcial. Principales autorizaciones registradas:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 85533 | Caspofungina Stadafarma 70 mg | Polvo para concentrado para solución para perfusión |
| 89229 | Caspofungina Tillomed 50 mg | Polvo para concentrado para solución para perfusión |
| 83627 | Fornega 50 mg | Polvo para concentrado para solución para perfusión |
| 01196001 | Cancidas 50 mg | Polvo para concentrado para solución para perfusión |
| 82746 | Caspofungina Altan 50 mg | Polvo para concentrado para solución para perfusión |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 81 interacciones. Las principales son:
  - Dexametasona: nivel Mayor
  - Naltrexona: nivel Moderado
  - Otras interacciones registradas, de nivel no clasificado: calcitriol, pantoprazol, doxiciclina, morfina, omeprazol, vancomicina, anfotericina B e hidrocortisona, entre otras.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin estudios que evalúen directamente esta enfermedad y sin vínculo mecanístico plausible con la acción antifúngica del fármaco.

**Para avanzar se necesita:**
- Un fundamento biológico que conecte la inhibición de la glucano sintasa fúngica con la regulación de la gastrina
- Estudios preclínicos que evalúen el efecto sobre la secreción de gastrina
- Datos de mecanismo de acción verificados
- Revisión de advertencias y contraindicaciones del prospecto
- Evaluación de la vía de administración y de las interacciones farmacológicas para cualquier uso nuevo

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

