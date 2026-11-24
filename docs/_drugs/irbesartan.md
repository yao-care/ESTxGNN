---
layout: default
title: Irbesartan
parent: Solo predicción del modelo (L5)
nav_order: 430
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "irbesartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
description: "Irbesartan: nueva indicación predicha, Malignant hypertensive renal disease (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Irbesartan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Irbesartan: Malignant hypertensive renal disease
{: .text-alpha }

## Resumen en Una Frase

Irbesartán es un antagonista del receptor AT1 de la angiotensina II, utilizado originalmente para el tratamiento de la hipertensión y la nefropatía diabética.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**, aunque actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Malignant hypertensive renal disease |
| Puntaje de Predicción TxGNN | 0.9931 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 11; autorizadas no comercializadas: 4; revocadas o suspendidas: 5) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Irbesartan (traducción no oficial): «La angiotensina II es un potente vasoconstrictor que se forma a partir de la angiotensina I en una reacción catalizada por la enzima convertidora de angiotensina (ECA, cininasa II). La angiotensina II es la principal hormona vasoactiva del sistema renina-angiotensina y un componente importante de la fisiopatología de la hipertensión. […] El irbesartán bloquea los efectos vasoconstrictores y secretores de aldosterona de la angiotensina II al unirse selectivamente al receptor AT 1 de la angiotensina II, presente en muchos tejidos (p. ej., músculo liso vascular, glándula suprarrenal).» Texto original en inglés: "Angiotensin II is a potent vasoconstrictor formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the primary vasoactive hormone of the renin-angiotensin system, and an important component in the pathophysiology of hypertension. […] Irbesartan blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively binding to the AT 1 angiotensin II receptor found in many tissues (e.g., vascular smooth muscle, adrenal gland)." ([DailyMed: Avapro (irbesartan) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7885b2a8-be4e-48ab-8113-4e6ab791eb98), versión del 2026-08-24; consultado el 2026-11-19). Según la información conocida, irbesartán pertenece a la clase de los antagonistas del receptor de angiotensina II tipo 1 (ARA-II), bloquea la vía renina-angiotensina-aldosterona y su eficacia en hipertensión y nefropatía diabética está comprobada.

La hipertensión renovascular maligna está impulsada por una intensa activación del sistema renina-angiotensina, por lo que existe una justificación mecanística plausible para el bloqueo del receptor AT1. La relación con la indicación original es estrecha: se trata de una forma grave de hipertensión con afectación renal.

Sin embargo, el único respaldo es la puntuación del modelo. Además, los bloqueadores del receptor de angiotensina conllevan un riesgo conocido en la estenosis bilateral de la arteria renal (lesión renal aguda), de modo que cualquier uso exigiría una evaluación de seguridad muy cuidadosa. La base de conocimiento también lista la obstrucción de la arteria renal entre las contraindicaciones del fármaco.

**Otras predicciones del modelo (para contexto):**

| Indicación predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Enfermedad renal hipertensiva maligna | 0,9931 | L5 | Se solapa en gran medida con las indicaciones actuales; probablemente sea un refinamiento y no un reposicionamiento real |
| Hipertensión pulmonar de mecanismo multifactorial poco claro | 0,9925 | L5 | Vínculo mecanístico débil; el bloqueo AT1 sistémico no es una terapia establecida |
| Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia | 0,9925 | L4 | Evidencia preclínica indirecta (véase la sección de literatura); sin ensayos en humanos |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación principal (hipertensión renovascular maligna).

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal.

Como referencia, para la indicación alternativa de **hipertensión pulmonar por enfermedad pulmonar y/o hipoxia** se identificó la siguiente literatura relevante (todo preclínico o de revisión):

<!-- review:begin es-lic-20261105-irbesartan-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamentos con un único principio activo; ninguna cancelada)." Eliminado: afirmaba que el medicamento no está autorizado o comercializado en España, o que sus autorizaciones están revocadas o suspendidas, lo que no coincide con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-irbesartan-1 -->

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Revisión | Inflammopharmacology | Efectos pleiotrópicos de los antagonistas del receptor AT-1 en la hipoxia inducida por isquemia cardíaca |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | Preclínico (in vitro) | PLoS One | Irbesartán protege a los cardiomiocitos bajo estrés hipóxico |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Preclínico (animal) | Sleep & Breathing | Irbesartán atenúa la apoptosis cardíaca inducida por apnea del sueño y aumenta la expresión de Sirtuina 1 |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Preclínico (animal) | Am J Physiol Heart Circ Physiol | Irbesartán inhibe la angiogénesis coronaria estimulada por hipoxia intermitente crónica en ratas neonatas |
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Preclínico (animal) | Biomed Pharmacother | Irbesartán mejora el mal de montaña crónico en un modelo de rata mediante el metabolismo del colesterol |
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Estudio en animales | Eur Rev Med Pharmacol Sci | Irbesartán mejora el estrés oxidativo en ratas con hipertensión pulmonar de altura, mediante la regulación de la flora intestinal |
| [15526904](https://pubmed.ncbi.nlm.nih.gov/15526904/) | 2004 | Preclínico (animal) | Renal Failure | Irbesartán atenúa la nefrotoxicidad por ciclosporina (relevancia tangencial) |
| [30525078](https://pubmed.ncbi.nlm.nih.gov/30525078/) | 2018 | Preclínico (animal) | Regenerative Therapy | El pretratamiento con un ARA-II anuló los efectos beneficiosos de láminas de células madre tras infarto de miocardio (relevancia tangencial) |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 70117 | IRBESARTAN CINFA 75 mg COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Cinfa S.A. | Comercializada |
| 88577 | IRBESARTAN TARBIS FARMA 75 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tarbis Farma S.L. | Comercializada |
| 74941 | IRBESARTAN COMBIX 75 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Combix S.L.U. | Comercializada |
| 74162 | IRBESARTAN TECNIGEN 150 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tecnimede España Industria Farmaceutica S.A. | Comercializada |
| 70158 | IRBESARTAN SANDOZ 75 mg COMPRIMIDOS EFG | COMPRIMIDO | Sandoz Farmaceutica S.A. | Comercializada |
| 70221 | IRBESARTAN NORMON 300 mg COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Normon S.A. | Comercializada |
| 08480002 | IFIRMASTA 75 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Krka D.D. Novo Mesto | Comercializada |
| 74943 | IRBESARTAN COMBIX 300 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Combix S.L.U. | Comercializada |
| 97046027IP1 | APROVEL 300 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Sanofi Winthrop Industrie | Comercializada |
| 97046027IP2 | APROVEL 300 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Sanofi Winthrop Industrie | Comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto): angioedema (incluido el hereditario y el inducido por bloqueadores del sistema renina-angiotensina), obstrucción de la arteria renal, anuria, hipotensión, diabetes mellitus y cetoacidosis diabética, gota e hiperuricemia, hipercalcemia, hiperparatiroidismo, encefalopatía hepática, lupus eritematoso sistémico, pancreatitis, miopatía y rabdomiólisis, deficiencia de potasio y parálisis periódica familiar, entre otras.
- **Interacciones farmacológicas**: se identificaron 216 interacciones. Entre las principales:
  - **Mayores**: citrato de potasio y bicarbonato de potasio (riesgo de hiperpotasemia).
  - **Moderadas**: corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), ácido acetilsalicílico, bupropión, aprepitant, morfina, inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), insulinas (aspart, degludec), dronabinol y algunos preparados laxantes/de limpieza intestinal.
- Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles en los datos compilados; consultar el prospecto para la información de seguridad oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertensión renovascular maligna se basa únicamente en la puntuación del modelo (nivel L5), sin ensayos clínicos ni literatura, y además el bloqueo del receptor AT1 conlleva un riesgo conocido en la estenosis bilateral de la arteria renal. La hipertensión pulmonar por hipoxia (L4) solo cuenta con evidencia preclínica indirecta y justificaría, como mucho, trabajo preclínico basado en hipótesis.

**Para avanzar se necesita:**
- Recuperar y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción.
- Búsqueda sistemática de ensayos clínicos y literatura en humanos sobre ARA-II en hipertensión renovascular maligna.
- Evaluación de seguridad específica en estenosis de la arteria renal y función renal.
- Para hipertensión pulmonar: estudios preclínicos específicos de la vasculatura pulmonar antes de plantear estudios clínicos.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamentos con un único principio activo; ninguna cancelada)" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Avapro (irbesartan) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7885b2a8-be4e-48ab-8113-4e6ab791eb98) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

