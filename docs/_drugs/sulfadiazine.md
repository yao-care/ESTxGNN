---
layout: default
title: Sulfadiazine
parent: Evidencia moderada (L3-L4)
nav_order: 503
evidence_level: L4
indication_count: 2
---

# Sulfadiazine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Sulfadiazina: De Indicación Original No Registrada a Neumocistosis

## Resumen en Una Frase

Sulfadiazina es una sulfonamida comercializada en España en comprimidos de 500 mg. Los datos regulatorios disponibles no recogen su indicación aprobada, aunque la literatura la describe sobre todo como tratamiento de la toxoplasmosis, junto con pirimetamina.
El modelo TxGNN predice que podría ser efectiva para **neumocistosis**, pero actualmente hay **0 ensayos clínicos** y **19 publicaciones**, casi todas revisiones narrativas y sin datos específicos de sulfadiazina en esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el registro de la AEMPS |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.39% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, sulfadiazina es una sulfonamida y, como clase, inhibe la dihidropteroato sintetasa en la vía del folato. Mecanísticamente podría ser aplicable a la neumocistosis.

Esa vía es la que explota el sulfametoxazol dentro de trimetoprim-sulfametoxazol (TMP-SMX), tratamiento establecido de la neumonía por *Pneumocystis*. Sin embargo, sulfadiazina se usa principalmente con pirimetamina contra la toxoplasmosis, así que el vínculo con *Pneumocystis* es **indirecto y a nivel de clase**.

Ninguno de los registros aportados contiene datos específicos de sulfadiazina en neumocistosis que puedan verificarse. El puntaje alto de TxGNN (0.994) probablemente refleja asociaciones de la clase de las sulfonamidas en el grafo de conocimiento, más que evidencia directa sobre este fármaco.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Todas las publicaciones son revisiones, reportes de caso o textos no clasificados. No hay ECAs. Se muestran las más relevantes.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2645082](https://pubmed.ncbi.nlm.nih.gov/2645082/) | 1989 | No clasificado | Clinical Pharmacy | Por el título, trata pirimetamina-sulfadiazina en neumonía por *P. carinii* y toxoplasmosis en SIDA (sin resumen disponible) |
| [12645193](https://pubmed.ncbi.nlm.nih.gov/12645193/) | 2002 | Reporte de caso | J Formos Med Assoc | Paciente con SIDA con absceso cerebral por *Toxoplasma* tratado con clindamicina y sulfadiazina, junto con neumonía atípica por *P. carinii* |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Revisión | Drugs | Resume terapia y profilaxis de infecciones protozoarias sistémicas, incluidas *P. carinii* y *T. gondii* |
| [2969023](https://pubmed.ncbi.nlm.nih.gov/2969023/) | 1988 | No clasificado | J Infect Dis | Terapia y profilaxis de la neumonía por *P. carinii* (sin resumen disponible) |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Revisión | Am Fam Physician | Antiparasitarios de elección; TMP-SMX para neumonía por *Pneumocystis*, y quinina-pirimetamina-sulfadiazina para malaria resistente a cloroquina |
| [3914245](https://pubmed.ncbi.nlm.nih.gov/3914245/) | 1985 | Revisión | Arch Fr Pediatr | Infección por *P. carinii* en niños; el tratamiento recomendado es TMP-SMX |
| [2011633](https://pubmed.ncbi.nlm.nih.gov/2011633/) | 1991 | Revisión | Primary Care | Infecciones protozoarias asociadas al SIDA; *P. carinii* es la infección oportunista más frecuente |
| [7909657](https://pubmed.ncbi.nlm.nih.gov/7909657/) | 1994 | Revisión | Ann Intern Med | Avances en el manejo de infecciones oportunistas asociadas al SIDA |
| [16732870](https://pubmed.ncbi.nlm.nih.gov/16732870/) | 2006 | No clasificado | Intern Med J | Cristales de sulfonamida e insuficiencia renal aguda (sin resumen disponible) |
| [9562233](https://pubmed.ncbi.nlm.nih.gov/9562233/) | 1998 | No clasificado | Int J Clin Pharmacol Ther | Nefrotoxicidad de antiinfecciosos, incluido el efecto tubulo-obstructivo por precipitación del fármaco |

Varias de estas publicaciones se centran en TMP-SMX y no en sulfadiazina. Otras tratan la toxoplasmosis y sirven solo como apoyo indirecto.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 06960 | SULFADIAZINA REIG JOFRE 500 MG COMPRIMIDOS (Laboratorio Reig Jofre, S.A.) | Comprimido | No disponible en el registro |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta no devolvió interacciones registradas.
- **Nefrotoxicidad (según la literatura)**: los artículos recuperados describen cristaluria e insuficiencia renal aguda con sulfonamidas por precipitación del fármaco. Esta información procede de publicaciones y no del prospecto.

Consultar el prospecto para informacion de seguridad, advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni datos específicos de sulfadiazina en neumocistosis. El respaldo es una predicción del modelo y una analogía con el sulfametoxazol, tratamiento de referencia en esta enfermedad. Además, TMP-SMX ya cubre esta necesidad clínica.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), un paso bloqueante para el cribado de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Buscar evidencia específica de sulfadiazina en neumonía por *Pneumocystis*, con estudios comparativos frente a TMP-SMX.
- Completar la clasificación de las publicaciones pendientes, con revisión manual de su relevancia.

**Nota sobre la segunda predicción:** la neuroqueratoconjuntivitis... corrijo: la **queratoconjuntivitis epitelial punteada** (puntaje TxGNN 99.36%) no tiene ensayos ni literatura. Es una hipótesis puramente especulativa (nivel L5, Hold), porque suele ser viral o inmunomediada y no hay justificación clara para una sulfonamida sistémica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

