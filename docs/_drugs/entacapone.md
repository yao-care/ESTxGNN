---
layout: default
title: Entacapone
parent: Solo predicción del modelo (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Entacapone: nueva indicación predicha, Neurodegeneración asociada a PLA2G6 (nivel de evidencia L5). Indicación original: Enfermedad de Parkinson (según el grafo de conocimiento"
monitor_inn: "Entacapone"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "lethal infantile mitochondrial myopathy", "Lewy body dementia", "fructose-1,6-bisphosphatase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "progressive supranuclear palsy-corticobasal syndrome"]
---

# Entacapone
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

# Entacapona: De Enfermedad de Parkinson a Neurodegeneración Asociada a PLA2G6

## Resumen en Una Frase

Entacapona es un inhibidor de la catecol-O-metiltransferasa (COMT), utilizado originalmente como complemento del tratamiento con levodopa/carbidopa en la enfermedad de Parkinson.
El modelo TxGNN predice que podría ser efectivo para **neurodegeneración asociada a PLA2G6**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, por lo que se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Neurodegeneración asociada a PLA2G6 |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La entacapona inhibe la COMT, enzima que degrada la levodopa y las catecolaminas en la periferia. Al bloquearla, prolonga la acción de la levodopa y mejora el control de las fluctuaciones motoras en la enfermedad de Parkinson. Los datos farmacológicos compilados confirman la COMT como diana principal; también figuran como dianas los transportadores mitocondriales de piruvato MPC2 y MPC1L, cuya relevancia clínica no está establecida. No se dispone de una descripción detallada del mecanismo de acción en otras fuentes.

La neurodegeneración asociada a PLA2G6 (PLAN) incluye la distrofia neuroaxonal infantil y la distonía-parkinsonismo relacionada con PLA2G6. El fenotipo parkinsoniano se solapa con la indicación original, por lo que existe una justificación dopaminérgica plausible.

Cualquier beneficio sería solo sintomático, como coadyuvante de levodopa, y no modificaría la enfermedad. Aunque el puntaje TxGNN es alto, no existen ensayos ni literatura, así que la predicción debe considerarse una hipótesis.

### Otras predicciones del modelo

| Enfermedad predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Encefalitis subaguda de Rasmussen | 99.73% | L5 | Sin vínculo mecanístico claro |
| Mielitis | 99.63% | L5 | Sin mecanismo plausible |
| Parálisis agitante juvenil de Hunt | 99.60% | L5 | Término histórico de parkinsonismo juvenil; extensión de la indicación original |
| Demencia con cuerpos de Lewy | 99.25% | L4 | Evidencia preclínica indirecta; pregunta de investigación |
| Parálisis supranuclear progresiva-síndrome corticobasal | 99.04% | L5 | Poca respuesta a levodopa; pregunta de investigación |

Otras predicciones (deficiencia de transaldolasa, miopatía mitocondrial infantil letal, deficiencia de fructosa-1,6-bisfosfatasa, polimicrogiria perisilviana) carecen de vínculo mecanístico identificado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para neurodegeneración asociada a PLA2G6.

Para otras indicaciones predichas solo se encontraron ensayos tangenciales (relevancia baja, grado C), ninguno evalúa la entacapona como tratamiento:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Fase 1 | Reclutando | 40 | Imagen con [18F]F-DOPA en fallo autonómico; estudio diagnóstico, relacionado con demencia con cuerpos de Lewy |
| [NCT02994719](https://clinicaltrials.gov/study/NCT02994719) | N/A | Activo, sin reclutar | 120 | Análisis observacional de la marcha en enfermedades neurológicas; relacionado con PSP-síndrome corticobasal |

## Evidencia de Literatura

No hay literatura disponible para neurodegeneración asociada a PLA2G6. Para la demencia con cuerpos de Lewy se identificaron estudios preclínicos:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Preclínico (organoides corticales derivados de iPSC) | Science Advances | Modelo de enfermedad por cuerpos de Lewy con triplicación de SNCA; no evalúa eficacia de la entacapona |
| [23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/) | 2013 | Estudio mecanístico in vitro | Journal of Neuroscience Research | Efecto de fármacos antiparkinsonianos sobre la formación de oligómeros de β-amiloide y α-sinucleína |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 77488 | Entacapona Aurovitas 200 mg EFG | Comprimido recubierto con película | No disponible |
| 76383 | Entacapona Viatris 200 mg EFG | Comprimido recubierto con película | No disponible |
| 82845 | Medapia 200 mg EFG | Comprimido recubierto con película | No disponible |
| 10655003 | Entacapona Teva 200 mg EFG | Comprimido recubierto con película | No disponible |
| 98081003 | Comtan 200 mg | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): atrofia multisistémica, hipotensión ortostática, síndrome de taquicardia postural ortostática, discinesia inducida por fármacos, epilepsia, trastornos psicóticos y mentales (incluidos esquizoafectivo y esquizofreniforme), trastornos de ansiedad, enfermedad hepática, renal y de la vesícula biliar, úlcera gástrica y péptica, glaucoma de ángulo abierto y cerrado, diabetes y cetoacidosis diabética, melanoma, infarto de miocardio, trombosis coronaria, parada cardíaca súbita, enfermedad de conducción cardíaca, hemoglobinopatía y enfermedad diarreica.
- **Interacciones farmacológicas**: la consulta se completó, pero solo devolvió dianas farmacológicas (COMT, MPC2, MPC1L), no interacciones con otros fármacos.
- Para demencia con cuerpos de Lewy, los agentes dopaminérgicos pueden empeorar la psicosis y las alucinaciones.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal es solo computacional (nivel L5), sin ensayos ni literatura. La plausibilidad se limita a un posible beneficio sintomático en el componente parkinsoniano, sin efecto modificador de la enfermedad.

**Para avanzar se necesita:**
- Revisión de la literatura clínica sobre parkinsonismo/distonía en PLA2G6 y respuesta a levodopa
- Prospecto oficial de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas)
- Datos detallados del mecanismo de acción
- Evaluación del perfil de seguridad en población pediátrica y neurodegenerativa
- Si hay interés en demencia con cuerpos de Lewy o PSP-síndrome corticobasal, estudios preclínicos y clínicos específicos con entacapona
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

