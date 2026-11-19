---
layout: default
title: Natalizumab
parent: Solo predicción del modelo (L5)
nav_order: 554
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-05
monitor_inn: "NATALIZUMAB"
predicted_indications: ["bronchitis", "parapsoriasis", "psoriasis", "severe nonproliferative diabetic retinopathy", "acute lichenoid pityriasis"]
description: "Natalizumab: nueva indicación predicha, Bronquitis (bronchitis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 3 (comercializadas: 3)"
---

# Natalizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Natalizumab: Bronquitis (bronchitis)
{: .text-alpha }

## Resumen en Una Frase

Natalizumab es un anticuerpo monoclonal utilizado originalmente para el tratamiento de la enfermedad de Crohn, la enfermedad inflamatoria intestinal y la esclerosis múltiple.
El modelo TxGNN (aprendizaje profundo) predice que podría ser efectivo para **bronquitis**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo, que puede reflejar similitudes que este aprendió entre enfermedades relacionadas, no evidencia biológica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Bronquitis (bronchitis) |
| Puntaje de Predicción TxGNN | 0.9946 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 3) |
| Número de Autorizaciones | 3 (comercializadas: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Natalizumab (traducción no oficial): «El natalizumab se une a la subunidad α4 de las integrinas α4β1 y α4β7 expresadas en la superficie de todos los leucocitos, excepto los neutrófilos, e inhibe la adhesión mediada por α4 de los leucocitos a su(s) contrarreceptor(es). Los receptores de la familia α4 de integrinas incluyen la molécula de adhesión celular vascular 1 (VCAM-1), que se expresa en el endotelio vascular activado, y la molécula de adhesión celular adresina de la mucosa 1 (MAdCAM-1), presente en las células endoteliales vasculares del tubo digestivo.» Texto original en inglés: "Natalizumab binds to the α4-subunit of α4β1 and α4β7 integrins expressed on the surface of all leukocytes except neutrophils, and inhibits the α4-mediated adhesion of leukocytes to their counter-receptor(s). The receptors for the α4 family of integrins include vascular cell adhesion molecule-1 (VCAM-1), which is expressed on activated vascular endothelium, and mucosal addressin cell adhesion molecule-1 (MAdCAM-1) present on vascular endothelial cells of the gastrointestinal tract." ([DailyMed: Tysabri (natalizumab) prescribing information, Biogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c5fdde91-1989-4dd2-9129-4f3323ea2962), versión del 2026-10-09; consultado el 2026-11-19). Según la información conocida, natalizumab bloquea la integrina alfa-4 (VLA-4) y limita el tránsito de leucocitos hacia los tejidos, lo que explica su uso en enfermedades inflamatorias mediadas por el sistema inmune como la esclerosis múltiple y la enfermedad de Crohn.

Mecanísticamente, esta limitación del reclutamiento leucocitario podría atenuar la inflamación de las vías respiratorias impulsada por leucocitos. Sin embargo, no existe evidencia clínica ni bibliográfica que lo apoye, y la alta puntuación de TxGNN (0,9946) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Además, la bronquitis crónica está dirigida principalmente por neutrófilos y con frecuencia es de origen infeccioso. Natalizumab conlleva riesgo de infecciones (por ejemplo, leucoencefalopatía multifocal progresiva, LMP), por lo que el balance riesgo-beneficio resulta desfavorable.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1231745001 | TYRUKO 300 MG concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 106346002 | TYSABRI 150 MG solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible en los datos compilados |
| 06346001 | TYSABRI 300 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**: leucoencefalopatía multifocal progresiva (LMP).
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las principales, de gravedad **mayor**:
  - Corticosteroides: hidrocortisona, triamcinolona (incluida la oftálmica), dexametasona, betametasona, budesonida, prednisolona y prednisona.
  - Radiofármacos y anticuerpos: iobenguano (I-131), ibritumomab tiuxetan, tositumomab y tositumomab (I-131).
  - Otros: levamisol, trimetrexato y mercaptopurina.

  Interacciones de gravedad **moderada**: naltrexona. De gravedad **menor**: sales de zinc (sulfato, acetato, gluconato y cloruro).
- Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones oficiales).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para bronquitis se apoya solo en el modelo (nivel L5), sin ensayos ni publicaciones, y el riesgo de infección y de LMP asociado a natalizumab hace que el balance riesgo-beneficio sea desfavorable en una enfermedad frecuentemente infecciosa.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto oficial (advertencias y contraindicaciones) de la AEMPS.
- Estudios preclínicos o de mecanismo que respalden un papel de la integrina alfa-4 en la bronquitis.
- Evaluación del balance riesgo-beneficio frente a las alternativas terapéuticas existentes.
- Revisión de las demás indicaciones predichas (parapsoriasis, psoriasis, retinopatía diabética no proliferativa grave, pitiriasis liquenoide aguda), ya que la evidencia disponible para varias de ellas (en especial psoriasis) sugiere reacciones paradójicas o inducidas por el fármaco, y no beneficio terapéutico.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Tysabri (natalizumab) prescribing information, Biogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c5fdde91-1989-4dd2-9129-4f3323ea2962) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

