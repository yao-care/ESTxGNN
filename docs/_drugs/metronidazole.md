---
layout: default
title: Metronidazole
parent: Solo predicción del modelo (L5)
nav_order: 520
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
description: "Metronidazole: nueva indicación predicha, Neumocistosis (pneumocystosis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 17 (comercializadas: 12; autorizadas no comercializadas: 2)"
---

# Metronidazole
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

## Metronidazole: Neumocistosis (pneumocystosis)
{: .text-alpha }

## Resumen en Una Frase

Metronidazol es un antimicrobiano utilizado originalmente para infecciones por bacterias anaerobias y protozoos (peritonitis, giardiasis, vaginosis bacteriana, abscesos intracraneales, rosácea, entre otras).
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero **no hay ensayos clínicos** y solo **10 publicaciones** de carácter general (revisiones y reportes de caso), sin evidencia directa que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neumocistosis (pneumocystosis) |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 12 de 17; autorizadas no comercializadas: 2; revocadas o suspendidas: 3) |
| Número de Autorizaciones | 17 (comercializadas: 12) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Metronidazole (traducción no oficial): «El metronidazol, un nitroimidazol, ejerce efectos antibacterianos en un entorno anaerobio contra la mayoría de los anaerobios obligados. Una vez que el metronidazol ingresa en el microorganismo por difusión pasiva y se activa en el citoplasma de las bacterias anaerobias sensibles, se reduce; este proceso incluye donantes intracelulares de transporte de electrones, como la ferredoxina, y la transferencia de un electrón al grupo nitro del metronidazol, lo que conduce a la formación de un radical libre nitroso de vida corta.» Texto original en inglés: "Metronidazole, a nitroimidazole, exerts antibacterial effects in an anaerobic environment against most obligate anaerobes. Once metronidazole enters the organism by passive diffusion and activated in the cytoplasm of susceptible anaerobic bacteria, it is reduced; this process includes intra-cellular electron transport donors such as ferredoxin and transfer of an electron to the nitro group of the metronidazole leading to formation of a short-lived nitroso free radical." ([DailyMed: metronidazole prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49360d6f-c8b3-420e-af75-154cf7b05255), versión del 2026-11-02; consultado el 2026-11-19). Según la información conocida, metronidazol es un nitroimidazol cuya eficacia en infecciones anaerobias y por protozoos está bien establecida; actúa mediante la activación reductora de su grupo nitro en microorganismos anaerobios.

**En este caso, la predicción no tiene un fundamento mecanístico plausible.** *Pneumocystis* es un hongo y carece de la vía de activación que hace sensible a metronidazol a bacterias anaerobias y protozoos. El puntaje elevado proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

La literatura recuperada se compone de revisiones generales sobre antiparasitarios e infecciones oportunistas en VIH, así como reportes de caso en los que metronidazol se menciona de forma incidental (por ejemplo, tratamiento de amebiasis en pacientes que luego desarrollaron neumonía por *Pneumocystis*). El tratamiento de referencia para neumocistosis es trimetoprima-sulfametoxazol, algo que la propia literatura recuperada refleja.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Revisión | Mayo Clinic Proceedings | Panorama de agentes antiparasitarios, resistencias y toxicidades; sin evidencia específica de metronidazol en neumocistosis |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Revisión | American Family Physician | Metronidazol indicado para amebiasis y tricomoniasis; para neumocistosis se cita trimetoprima-sulfametoxazol |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Revisión | Clinical Pharmacokinetics | Justificación farmacocinética de terapias antiprotozoarias en huéspedes normales e inmunodeprimidos |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Revisión | Clinical Pharmacy | Tratamiento de complicaciones infecciosas del SIDA, entre ellas la neumonía por *P. carinii* |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Revisión | Topics in Antiviral Medicine | Infecciones oportunistas relacionadas con VIH y guías vigentes |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Revisión | Reviews of Infectious Diseases | Crítica de ensayos de profilaxis antimicrobiana; sin relación directa |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Reporte de caso | Am Rev Respir Dis | Neumonía por *P. carinii* y citomegalovirus en adulto previamente tratado con metronidazol y tetraciclina por diarrea |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Reporte de caso | Kansenshogaku Zasshi | Dos pacientes con SIDA; metronidazol usado para amebiasis, no para neumocistosis |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Reporte de caso | J Formos Med Assoc | Perforación de colon con peritonitis en paciente con SIDA por citomegalovirus y colitis amebiana |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | Reporte de caso | J Med Case Rep | Absceso cerebeloso por *Streptococcus intermedius* como primera manifestación de sarcoidosis; sin relación directa |

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 62224 | METRONIDAZOL NORMON 5 MG/ML SOLUCIÓN PARA PERFUSIÓN EFG | SOLUCIÓN PARA PERFUSIÓN | Laboratorios Normon S.A. | Comercializada |
| 60536 | ROZEX 7,5 MG/G GEL | GEL | Laboratorios Galderma S.A. | Comercializada |
| 34985 | FLAGYL 500 mg COMPRIMIDOS VAGINALES | COMPRIMIDO VAGINAL | Laboratorios Fidia Farmaceutica S.L. | Comercializada |
| 68162 | METRONIDAZOL SERRACLINICS 5mg/ml SOLUCION PARA PERFUSION EFG | SOLUCIÓN PARA PERFUSIÓN | Laboratorios Serra Pamies S.A. | Comercializada |
| 47656 | FLAGYL 125mg/5 ml SUSPENSION ORAL | SUSPENSIÓN ORAL | Laboratorios Fidia Farmaceutica S.L. | Comercializada |
| 89284 | INTIZOL VAGINAL 1.000 MG OVULOS | ÓVULO | Seid S.A. | Comercializada |
| 84614 | METRONIDAZOL AUROVITAS 250 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Aurovitas Spain, S.A.U. | Comercializada |
| 63884 | METRONIDAZOL VIÑAS 7,5 MG/G GEL | GEL | Laboratorios Vinas S.A. | Comercializada |
| 68091 | METRONIDAZOL ALTAN 5 MG/ML SOLUCION PARA PERFUSION EFG | SOLUCIÓN PARA PERFUSIÓN | Altan Pharmaceuticals Sa | Comercializada |
| 62223 | METRONIDAZOL NORMON 250 mg COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Normon S.A. | Comercializada |

Se muestran 10 de 17 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Incluyen formas de perfusión, orales, vaginales y tópicas.

<!-- review:begin es-lic-20261105-metronidazole-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 17 autorizaciones vigentes (todas de monofármaco). Incluyen formas de perfusión, orales, vaginales y tópicas." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-metronidazole-1 -->

---

## Consideraciones de Seguridad

- **Contraindicaciones o precauciones según el grafo de conocimiento** (no provienen del texto del prospecto): insuficiencia y enfermedad hepática, epilepsia, enfermedad renal, enfermedades hematológicas (neutropenia, agranulocitosis, leucopenia), trastornos de la coagulación, neuropatía periférica y enfermedades del sistema nervioso central (incluida enfermedad cerebral y del nervio óptico), insuficiencia cardíaca congestiva, diabetes mellitus y cetoacidosis diabética, gota, enfermedad de la vesícula biliar, dermatitis y abuso de sustancias.
- **Interacciones farmacológicas** (se identificaron 100 en total; se listan las principales):
  - **Mayor:** etanol.
  - **Moderadas:** paclitaxel, adalimumab, trastuzumab emtansina, etinilestradiol, estradiol, butalbital, amobarbital, amiodarona, celecoxib, loperamida.
  - **Menores:** abiraterona, tramadol, famotidina, salbutamol, alfuzosina, amisulprida, amitriptilina, anagrelida, propofol.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5): no hay ensayos clínicos, la literatura es general o incidental, y el mecanismo de metronidazol no es plausible frente a un hongo como *Pneumocystis*. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y evidencia preclínica que justifique actividad frente a *Pneumocystis*
- Texto oficial de indicaciones, advertencias y contraindicaciones del prospecto de AEMPS
- Priorizar otras candidatas con mejor respaldo (por ejemplo, cap poliposis, con reportes de caso y un vínculo antiinflamatorio/disbiosis plausible, o poliposis, úlcera vulvar y miasis de herida como preguntas de investigación)

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Se muestran 5 de las 17 autorizaciones vigentes (todas de monofármaco)" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: metronidazole prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49360d6f-c8b3-420e-af75-154cf7b05255) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

