---
layout: default
title: Clofazimine
parent: Solo predicción del modelo (L5)
nav_order: 136
evidence_level: L5
indication_count: 3
---

# Clofazimine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Clofazimina: De Lepra a Neumocistosis

## Resumen en Una Frase

Clofazimina es un antibacteriano que se usa en la lepra, dentro de la terapia multifarmaco junto con otros antibacterianos. El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero la evidencia directa es prácticamente nula: hay **1 ensayo clínico** y **4 publicaciones**, ninguno demuestra actividad contra *Pneumocystis*. La predicción parece reflejar más la coocurrencia de infecciones en pacientes con sida que un efecto terapéutico real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lepra (fuente: base de datos de farmacología del pack; el registro de la AEMPS no incluye texto de indicación) |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 (el pack indica L4, pero no hay estudios preclínicos ni clínicos sobre *Pneumocystis*) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el pack. Según la información conocida, la clofazimina es un colorante de tipo riminofenazina con actividad contra micobacterias, mediante alteración de membrana y ciclado redox. Su eficacia está establecida en lepra y se usa también en regímenes para tuberculosis resistente.

**No hay un vínculo mecanístico establecido con la neumocistosis.** *Pneumocystis jirovecii* es un hongo, y la actividad de la clofazimina se conoce en micobacterias. Ningún ensayo ni publicación revisada describe actividad frente a *Pneumocystis*.

La explicación más probable del puntaje alto (99.90%) es un confusor del grafo de conocimiento. La clofazimina se estudió como profilaxis de la infección por *Mycobacterium avium* complex (MAC) en pacientes con sida. Esos mismos pacientes tienen alto riesgo de neumocistosis, por lo que ambas enfermedades aparecen asociadas. Esa asociación no indica eficacia contra *Pneumocystis*.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00002058](https://clinicaltrials.gov/study/NCT00002058) | No aplica | Completado | No reportada | Ensayo aleatorizado de profilaxis con clofazimina contra la infección por MAC en personas con VIH. No evalúa neumocistosis, por lo que no aporta evidencia directa (relevancia: C). |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | Ensayo aleatorizado abierto (el pack lo clasifica como revisión) | J Infect Dis | 110 pacientes con VIH (primer episodio de neumonía por *P. carinii* o CD4 ≤100/mm³) recibieron clofazimina como profilaxis de MAC diseminado. El estudio evalúa MAC, no neumocistosis. |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Revisión | PI Perspective | Actualización general sobre infecciones oportunistas. Sin resumen disponible. |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Reporte de caso | Infection | Paciente con sida y enfermedad pulmonar por *M. kansasii* tratado con isoniazida, etambutol, clofazimina y ciprofloxacino. La neumonía por *P. carinii* se trató con trimetoprim-sulfametoxazol, no con clofazimina. |
| [6299154](https://pubmed.ncbi.nlm.nih.gov/6299154/) | 1983 | Reporte de caso | Ann Intern Med | Paciente hemofílico con sida, neumonía por *P. carinii* y bacteriemia por *M. avium-intracellulare*. Describe la coexistencia de ambas infecciones. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 48886 | LAMPREN CÁPSULAS | Cápsula blanda | Novartis Farmacéutica S.A. |

El registro no incluye texto de indicación aprobada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio, clínico ni preclínico, que muestre actividad de la clofazimina contra *Pneumocystis*. El puntaje de 99.90% probablemente proviene de la coocurrencia de infecciones en pacientes con sida. Para la neumocistosis ya existen tratamientos establecidos, como trimetoprim-sulfametoxazol.

**Para avanzar se necesita:**
- Demostrar actividad *in vitro* de la clofazimina contra *Pneumocystis* antes de considerar cualquier estudio clínico.
- Obtener datos de mecanismo de acción (MOA) desde DrugBank.
- Descargar y revisar el prospecto de la AEMPS para advertencias y contraindicaciones.

**Otras predicciones del modelo (para referencia):**
- **Malaria** (TxGNN 99.60%, L4): hay actividad antiplasmódica *in vitro* solo con análogos de clofazimina (PMID 29026393). Se clasifica como pregunta de investigación. Falta confirmar la actividad de la clofazimina misma.
- **Anomalía de la secreción de gastrina** (TxGNN 99.57%, L5): sin ensayos ni literatura, sin mecanismo plausible. Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

