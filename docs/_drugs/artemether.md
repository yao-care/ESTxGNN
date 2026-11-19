---
layout: default
title: Artemether
parent: Solo predicción del modelo (L5)
nav_order: 66
evidence_level: L5
indication_count: 8
monitor_inn: "artemether"
predicted_indications: ["acquired angioedema", "angioedema", "hereditary angioedema", "nephrogenic syndrome of inappropriate antidiuresis", "acute contagious conjunctivitis", "scleroderma (disease)", "conjunctivitis", "renin-angiotensin-aldosterone system-blocker-induced angioedema"]
last_modified_at: 2026-11-20
description: "Artemether: nueva indicación predicha, angioedema adquirido (acquired angioedema) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 0)"
---

# Artemether
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

## Artemeter: derivado de artemisinina (endoperóxido antipalúdico) → angioedema adquirido (acquired angioedema)
{: .text-alpha }

## Resumen en Una Frase

Artemeter es un derivado de la artemisinina de tipo endoperóxido, perteneciente a la clase de los antipalúdicos. El modelo TxGNN predice que podría ser efectivo para **angioedema adquirido (acquired angioedema)**, pero actualmente no hay **ningún ensayo clínico** ni **ninguna publicación** en los datos compilados para este informe que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | angioedema adquirido (acquired angioedema) |
| Puntaje de Predicción TxGNN | 0,9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 0) |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Artemether es (traducción no oficial): «Inhibidor de la ferriprotoporfirina IX» Texto original en inglés: "Ferriprotoporphyrin IX inhibitor" ([ChEMBL CHEMBL566534 (artemether): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL566534), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, artemeter es un antipalúdico del grupo de las artemisininas (endoperóxidos) y, en la presentación registrada en España, se utiliza combinado con otro principio activo.

No se identifica un vínculo mecanístico entre artemeter y el angioedema adquirido. Esta forma de angioedema está mediada por bradicinina o por el complemento, y no se conoce ninguna vía que conecte a artemeter con ella. El puntaje elevado de TxGNN es una predicción basada solo en el modelo, sin respaldo clínico ni bibliográfico.

Por tanto, esta predicción debe considerarse puramente hipotética hasta que se disponga de estudios preclínicos o clínicos que la sustenten.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el modelo**: las relaciones fármaco-enfermedad compiladas apuntan a síndrome de QT largo, síndrome de QT largo familiar, torsades de pointes y deficiencia de potasio. No proceden del texto del prospecto y deben confirmarse con la ficha técnica.
- **Interacciones Farmacológicas**: se identificaron 95 interacciones. Entre las de gravedad **mayor** figuran claritromicina, cobicistat, amprenavir, apalutamida, atazanavir y boceprevir. Entre las de gravedad **moderada** figuran dexametasona, miconazol, troglitazona, deferasirox, fostamatinib, bosentán y brigatinib, entre otras.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel de evidencia L5), sin ensayos clínicos, sin literatura y sin un mecanismo plausible. Además, el perfil de seguridad (riesgo de prolongación del QT e interacciones mayores) exige cautela.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de artemeter y evaluación de su relación con las vías de bradicinina y complemento
- Estudios preclínicos que respalden un efecto en angioedema adquirido
- Advertencias y contraindicaciones de la ficha técnica de AEMPS
- Evaluación de la compatibilidad de vía de administración y de la seguridad cardiaca (QT)

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [ChEMBL CHEMBL566534 (artemether): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL566534) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

