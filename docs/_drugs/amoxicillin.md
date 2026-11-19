---
layout: default
title: Amoxicillin
parent: Solo predicción del modelo (L5)
nav_order: 53
evidence_level: L5
indication_count: 8
monitor_inn: "Amoxicillin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-11-20
description: "Amoxicillin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Amoxicillin
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

## Amoxicilina: antibacteriano betalactámico (inhibidor de la síntesis de pared celular bacteriana) → síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Resumen en Una Frase

Amoxicilina es un antibiótico betalactámico de uso antibacteriano, comercializado en España en múltiples presentaciones.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) |
| Puntaje de Predicción TxGNN | 0,9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 13; autorizadas no comercializadas: 4; revocadas o suspendidas: 3) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Amoxicillin (traducción no oficial): «La amoxicilina es un fármaco antibacteriano. […] La amoxicilina es similar a la penicilina en su acción bactericida contra las bacterias sensibles durante la fase de multiplicación activa. Actúa mediante la inhibición de la biosíntesis de la pared celular, lo que provoca la muerte de las bacterias.» Texto original en inglés: "Amoxicillin is an antibacterial drug. […] Amoxicillin is similar to penicillin in its bactericidal action against susceptible bacteria during the stage of active multiplication. It acts through the inhibition of cell wall biosynthesis that leads to the death of the bacteria." ([DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77), versión del 2026-11-13; consultado el 2026-11-19). Según la información conocida, la amoxicilina es un betalactámico que inhibe la síntesis de la pared celular bacteriana.

El síndrome de hiperviscosidad policlonal se debe a un aumento de inmunoglobulinas u otras proteínas séricas, un proceso que la amoxicilina no actúa sobre. No se identifica un vínculo mecanístico plausible entre ambos.

Por ello, el puntaje elevado (0,9963) debe interpretarse con cautela: no está respaldado por ningún dato clínico ni bibliográfico y probablemente es un artefacto del modelo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Los datos compilados muestran al menos 20 autorizaciones, por lo que la lista puede ser parcial. Principales autorizaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 62337 | AMOXICILINA PENSA 1 g comprimidos recubiertos EFG | Comprimido recubierto |
| 64117 | AMOXICILINA CINFA 1000 mg polvo para suspensión oral en sobres EFG | Polvo para suspensión oral |
| 50239 | CLAMOXYL 500 mg cápsulas duras | Cápsula dura |
| 64390 | AMOXICILINA NORMON 1000 mg comprimidos EFG | Comprimido |
| 56265 | AMITRON 500 mg polvo para solución inyectable | Polvo para solución inyectable |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 registradas; principales):
  - Mayor: metotrexato; vacuna viva de *Vibrio cholerae* (cepa CVD 103-HgR).
  - Moderada: doxiciclina, minociclina, demeclociclina, etinilestradiol, estradiol, anisindiona, dicumarol, balsalazida, entecavir, micofenolato de mofetilo, entre otros.
  - Menor: alopurinol, amilorida, azitromicina, claritromicina, eritromicina.

No se dispone de advertencias ni contraindicaciones de prospecto en los datos compilados; consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y de literatura, no tiene un mecanismo plausible y su nivel de evidencia es L5. No hay base para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la amoxicilina y una hipótesis biológica que la vincule con la hiperviscosidad policlonal
- Estudios preclínicos o clínicos que investiguen directamente esta enfermedad
- Advertencias y contraindicaciones del prospecto de la AEMPS para el cribado de seguridad

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

