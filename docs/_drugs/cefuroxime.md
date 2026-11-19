---
layout: default
title: Cefuroxime
parent: Solo predicción del modelo (L5)
nav_order: 160
evidence_level: L5
indication_count: 8
monitor_inn: "Cefuroxime"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "Peptostreptococcus infectious disease", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy"]
last_modified_at: 2026-11-05
description: "Cefuroxime: nueva indicación predicha, hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Cefuroxime
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Cefuroxima: antibiótico betalactámico cefalosporínico → hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Cefuroxima es una cefalosporina de segunda generación, un antibiótico betalactámico que inhibe la síntesis de la pared celular bacteriana.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia (hyperamylasemia)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0,9976 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 11; autorizadas no comercializadas: 2; revocadas o suspendidas: 7) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Cefuroxime (traducción no oficial): «La cefuroxima es un agente bactericida que actúa mediante la inhibición de la síntesis de la pared celular bacteriana. La cefuroxima tiene actividad en presencia de algunas betalactamasas, tanto penicilinasas como cefalosporinasas, de bacterias gramnegativas y grampositivas.» Texto original en inglés: "Cefuroxime is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Cefuroxime has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: cefuroxime sodium prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a145288-733a-4966-b7ae-dc96eb103d8c), versión del 2025-03-27; consultado el 2026-11-19). Por conocimiento general, cefuroxima es una cefalosporina que bloquea la síntesis de la pared celular de las bacterias y se usa contra infecciones bacterianas.

Para la hiperamilasemia, que es una elevación de la amilasa en sangre, no se identifica un vínculo mecanístico plausible. Cefuroxima no tiene efecto conocido sobre la amilasa sérica. La puntuación elevada proviene únicamente de asociaciones calculadas por el modelo y no de una base biológica o clínica.

Por tanto, esta predicción debe considerarse una señal sin respaldo, útil solo como hipótesis de partida y no como candidata de reposicionamiento con fundamento actual.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Los datos locales indican que el fármaco está comercializado, con autorizaciones vigentes para varias presentaciones (comprimidos recubiertos y polvo para solución inyectable). El registro de autorizaciones puede ser parcial.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 80366 | Cefuroxima Tecnigen 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No registrada |
| 62909 | Cefuroxima Normon 250 mg polvo y disolvente para solución inyectable EFG | Polvo y disolvente para solución inyectable | No registrada |
| 64949 | Cefuroxima Sala 1.500 mg polvo para solución inyectable y para perfusión EFG | Polvo para solución inyectable y para perfusión | No registrada |
| 15-061-88-C-C | Zinnat 500 mg comprimidos recubiertos con película | Comprimido recubierto con película | No registrada |
| 76098 | Prokam 50 mg polvo para solución inyectable | Polvo para solución inyectable | No registrada |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; las principales de nivel moderado incluyen antiácidos y reductores de la acidez gástrica (famotidina, ranitidina, cimetidina, nizatidina, omeprazol, esomeprazol, lansoprazol, pantoprazol, rabeprazol, hidróxido de aluminio, carbonato de calcio, sales de magnesio) y aminoglucósidos (kanamicina, neomicina), además de balsalazida.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura sobre cefuroxima en hiperamilasemia, no hay un mecanismo plausible y la puntuación (0,9976) refleja únicamente una predicción del modelo. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Una hipótesis mecanística biológicamente fundamentada que relacione cefuroxima con la amilasa sérica
- Estudios preclínicos o clínicos que investiguen directamente esta indicación
- Datos del mecanismo de acción y de advertencias y contraindicaciones del prospecto

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: cefuroxime sodium prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a145288-733a-4966-b7ae-dc96eb103d8c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

