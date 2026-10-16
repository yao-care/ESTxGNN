---
layout: default
title: Metronidazole
parent: Solo predicción del modelo (L5)
nav_order: 520
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Metronidazole: nueva indicación predicha, Neumocistosis (nivel de evidencia L5). Indicación original: Infecciones por bacterias anaerobias (peritonitis, endocarditis…"
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Metronidazol: De Infecciones Anaerobias y Protozoarias a Neumocistosis

## Resumen en Una Frase

Metronidazol es un antimicrobiano utilizado originalmente para infecciones por bacterias anaerobias y protozoos (peritonitis, giardiasis, vaginosis bacteriana, abscesos intracraneales, rosácea, entre otras).
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero **no hay ensayos clínicos** y solo **10 publicaciones** de carácter general (revisiones y reportes de caso), sin evidencia directa que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones por bacterias anaerobias (peritonitis, endocarditis, vaginosis bacteriana, giardiasis, rosácea, absceso intracraneal, entre otras; según el grafo de conocimiento, ya que los textos de indicación de AEMPS no estaban disponibles) |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 17 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, metronidazol es un nitroimidazol cuya eficacia en infecciones anaerobias y por protozoos está bien establecida; actúa mediante la activación reductora de su grupo nitro en microorganismos anaerobios.

**En este caso, la predicción no tiene un fundamento mecanístico plausible.** *Pneumocystis* es un hongo y carece de la vía de activación que hace sensible a metronidazol a bacterias anaerobias y protozoos. El puntaje elevado de TxGNN probablemente es un artefacto de proximidad en la red del grafo de conocimiento.

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

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62224 | Metronidazol Normon 5 mg/ml solución para perfusión EFG | Solución para perfusión | No disponible |
| 85883 | Metronidazol Montvel 250 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 60536 | Rozex 7,5 mg/g gel | Gel | No disponible |
| 59325 | Flagyl 1500 mg solución para perfusión | Solución para perfusión | No disponible |
| 34985 | Flagyl 500 mg comprimidos vaginales | Comprimido vaginal | No disponible |

Se muestran 5 de las 17 autorizaciones vigentes (todas de monofármaco). Incluyen formas de perfusión, orales, vaginales y tópicas.

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
La predicción se apoya solo en el modelo (L5): no hay ensayos clínicos, la literatura es general o incidental, y el mecanismo de metronidazol no es plausible frente a un hongo como *Pneumocystis*. El puntaje alto parece un artefacto de la red del grafo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y evidencia preclínica que justifique actividad frente a *Pneumocystis*
- Texto oficial de indicaciones, advertencias y contraindicaciones del prospecto de AEMPS
- Priorizar otras candidatas con mejor respaldo (por ejemplo, cap poliposis, con reportes de caso y un vínculo antiinflamatorio/disbiosis plausible, o poliposis, úlcera vulvar y miasis de herida como preguntas de investigación)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

