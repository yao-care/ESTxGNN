---
layout: default
title: Foscarnet
parent: Solo predicción del modelo (L5)
nav_order: 358
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "FOSCARNET"
predicted_indications: ["autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "rheumatoid arthritis", "diabetic nephropathy"]
description: "Foscarnet: nueva indicación predicha, Síndrome de hematuria familiar autosómico dominante con tortuosidad arteriolar retiniana y contracturas (autosomal domi… (nivel de evidencia L5). Indicación orig…"
---

# Foscarnet
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

## Foscarnet: Síndrome de hematuria familiar autosómico dominante con tortuosidad arteriolar retiniana y contracturas (autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome)
{: .text-alpha }

## Resumen en Una Frase

Foscarnet es un antiviral de administración intravenosa que está comercializado en España; los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hematuria familiar autosómico dominante con tortuosidad arteriolar retiniana y contracturas**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, y el análisis mecanístico la considera probablemente un artefacto del modelo TxGNN (aprendizaje profundo).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de hematuria familiar autosómico dominante con tortuosidad arteriolar retiniana y contracturas (autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome) |
| Puntaje de Predicción TxGNN | 0.9956 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 3; autorizadas no comercializadas: 1) |
| Número de Autorizaciones | 3 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Foscarnet (traducción no oficial): «El foscarnet ejerce su actividad antiviral mediante una inhibición selectiva en el sitio de unión del pirofosfato de las ADN polimerasas específicas del virus, a concentraciones que no afectan a las ADN polimerasas celulares. El foscarnet no requiere activación (fosforilación) por la timidina cinasa ni por otras cinasas.» Texto original en inglés: "Foscarnet exerts its antiviral activity by a selective inhibition at the pyrophosphate binding site on virus-specific DNA polymerases at concentrations that do not affect cellular DNA polymerases. Foscarnet does not require activation (phosphorylation) by thymidine kinase or other kinases." ([DailyMed: Foscavir (foscarnet sodium) prescribing information, Clinigen Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=90e3da4e-3b1f-428b-99ca-e4bed1c80028), versión del 2025-12-11; consultado el 2026-11-19). Según el conocimiento farmacológico general, foscarnet es un análogo del pirofosfato que inhibe la ADN polimerasa viral y la transcriptasa inversa.

La enfermedad predicha es un trastorno genético raro (vasculopatía relacionada con COL4A1) sin etiología viral. El análisis realizado concluye que **no existe un vínculo mecanístico que respalde la predicción**. El puntaje alto de TxGNN (modelo de aprendizaje profundo) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, como fenotipos retinianos compartidos, y no evidencia biológica ni una justificación farmacológica.

Por tanto, esta predicción debe considerarse una señal computacional sin sustento biológico demostrado, y no una hipótesis de reposicionamiento plausible.

Otras predicciones del modelo tampoco muestran respaldo: enfermedad de vasos pequeños cerebrales tipo 1 (0.9954), artritis reumatoide (0.9952) y nefropatía diabética (0.9943). En esta última existe además una preocupación de seguridad, ya que foscarnet es nefrotóxico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 59712 | FOSCAVIR 24 mg/ml SOLUCION PARA PERFUSION | SOLUCIÓN PARA PERFUSIÓN | Clinigen Healthcare B.V. | Comercializada |
| 85153 | FOSCARNET KABI 24 MG/ML SOLUCION PARA PERFUSION EFG | SOLUCIÓN PARA PERFUSIÓN | Fresenius Kabi España, S.A.U. | Comercializada |
| 88760 | FOSCARNET TILLOMED 24 MG/ML SOLUCION PARA PERFUSION EFG | SOLUCIÓN PARA PERFUSIÓN | Laboratorios Tillomed Spain S.L.U | Autorizada, no comercializada |

Se muestran las 3 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto):** síndrome de QT largo (incluida la forma familiar), torsades de pointes, epilepsia, enfermedad renal, déficit de potasio, neutropenia y agranulocitosis (incluidas formas congénitas), hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo (hiperfosfatemia e hipofosfatemia) y anemia.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las de nivel **mayor** figuran anfotericina B (incluido el complejo lipídico), dolasetrón y bupropión. Entre las de nivel moderado se incluyen famotidina, omeprazol, rabeprazol, dexlansoprazol, claritromicina, loperamida, mesalazina, balsalazida y varios corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, beclometasona).
- Consultar el prospecto para información de seguridad adicional, ya que no se dispone de advertencias de etiqueta.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre un antiviral y una vasculopatía genética por defecto de colágeno IV. El puntaje alto parece un artefacto del modelo TxGNN (aprendizaje profundo).

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones)
- Completar los datos del mecanismo de acción desde DrugBank
- Justificación biológica independiente que vincule foscarnet con la patología de COL4A1 antes de considerar cualquier estudio
- Si se retomara el caso, evaluar la nefrotoxicidad y las alteraciones electrolíticas, que son riesgos relevantes para esta población

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Foscavir (foscarnet sodium) prescribing information, Clinigen Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=90e3da4e-3b1f-428b-99ca-e4bed1c80028) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

