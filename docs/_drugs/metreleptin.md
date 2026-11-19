---
layout: default
title: Metreleptin
parent: Solo predicción del modelo (L5)
nav_order: 519
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-05
monitor_inn: "metreleptin"
predicted_indications: ["familial generalized lentiginosis", "gastrocutaneous syndrome", "Moynahan syndrome", "rhabdoid tumor", "osteopathia striata-pigmentary dermopathy-white forelock syndrome", "acromelanosis", "congenital multiple café-au-lait macules-increased sister chromatid exchange syndrome", "leukonychia totalis-acanthosis-nigricans-like lesions-abnormal hair syndrome", "benign neoplasm of adrenal gland", "peripheral nerve schwannoma"]
description: "Metreleptin: nueva indicación predicha, Lentiginosis generalizada familiar (familial generalized lentiginosis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 3 (comercializadas: 3)"
---

# Metreleptin
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

## Metreleptin: Lentiginosis generalizada familiar (familial generalized lentiginosis)
{: .text-alpha }

## Resumen en Una Frase

La metreleptina es un análogo de la leptina, utilizado originalmente para tratar la lipodistrofia (incluida la lipodistrofia congénita generalizada o síndrome de Berardinelli-Seip).
El modelo TxGNN predice que podría ser efectiva para **lentiginosis generalizada familiar**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Lentiginosis generalizada familiar (familial generalized lentiginosis) |
| Puntaje de Predicción TxGNN | 0.9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 3) |
| Número de Autorizaciones | 3 (comercializadas: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Metreleptin (traducción no oficial): «Los adipocitos almacenan lípidos para satisfacer los requerimientos energéticos de los tejidos no adiposos durante el ayuno. En pacientes con lipodistrofia generalizada, la deficiencia de tejido adiposo provoca hipertrigliceridemia y depósito ectópico de grasa en tejidos no adiposos, como el hígado y el músculo, lo que contribuye a anomalías metabólicas, incluida la resistencia a la insulina. […] MYALEPT (metreleptina) para inyección ejerce su función mediante la unión al receptor de leptina humano (ObR) y su activación; este receptor pertenece a la familia de receptores de citocinas de clase I, que transmite señales a través de la vía de transducción JAK/STAT.» Texto original en inglés: "Adipocytes store lipids to meet the fuel requirements of non-adipose tissues during fasting. In patients with generalized lipodystrophy, the deficiency of adipose tissue leads to hypertriglyceridemia and ectopic deposition of fat in non-adipose tissues such as liver and muscle, contributing to metabolic abnormalities including insulin resistance. […] MYALEPT (metreleptin) for injection exerts its function by binding to and activating the human leptin receptor (ObR), which belongs to the Class I cytokine family of receptors that signals through the JAK/STAT transduction pathway." ([DailyMed: Myalept (metreleptin) prescribing information, Chiesi USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d3b50bbd-140b-425c-b5ec-d4682aad62bc), versión del 2024-03-25; consultado el 2026-11-19). Según la información conocida, la metreleptina actúa a través de la señalización del receptor de leptina para corregir la deficiencia de leptina en la lipodistrofia.

Los datos compilados no identifican un vínculo mecanístico claro con la lentiginosis generalizada familiar, que es un trastorno de la pigmentación sin participación establecida de la vía de la leptina. La puntuación elevada proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Por tanto, la razonabilidad de esta predicción es baja: no se sustenta en estudios clínicos ni en literatura, y debe considerarse una hipótesis exploratoria.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181276004 | MYALEPTA 3 MG polvo para solución inyectable | Polvo para solución inyectable | No disponible en los datos compilados |
| 1181276006 | MYALEPTA 5,8 MG polvo para solución inyectable | Polvo para solución inyectable | No disponible en los datos compilados |
| 1181276002 | MYALEPTA 11,3 MG polvo para solución inyectable | Polvo para solución inyectable | No disponible en los datos compilados |

Las tres autorizaciones están vigentes y pertenecen a Chiesi Farmaceutici S.P.A.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 145 interacciones potenciales. Entre las principales (muestra de las listadas) figuran las de nivel **moderado** con abemaciclib, fentanilo, acalabrutinib, etinilestradiol, alfentanilo, alpelisib, noretisterona, desogestrel, avapritinib, benzhidrocodona, bictegravir, brigatinib, buspirona, butorfanol, cabozantinib, capmatinib, cariprazina, ceritinib y clorpropamida; y de nivel **menor** con bortezomib.
- **Consideración teórica**: la señalización de la leptina se ha discutido como posible promotora tumoral en algunos cánceres, lo que plantea una preocupación teórica de seguridad en las indicaciones oncológicas predichas (p. ej., tumor rabdoide).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible entre la reposición de leptina y la lentiginosis generalizada familiar. Las otras nueve indicaciones predichas presentan el mismo perfil (L5, Hold).

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de la metreleptina para analizar posibles vínculos mecanísticos
- Advertencias y contraindicaciones del prospecto de AEMPS (brecha de datos bloqueante para el cribado de seguridad)
- Estudios preclínicos o de mecanismo que justifiquen una relación entre la señalización de leptina y la pigmentación
- Análisis de similitud con la indicación original y de compatibilidad de vía de administración (actualmente pendientes)

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Myalept (metreleptin) prescribing information, Chiesi USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d3b50bbd-140b-425c-b5ec-d4682aad62bc) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

