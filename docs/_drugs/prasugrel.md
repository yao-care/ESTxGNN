---
layout: default
title: Prasugrel
parent: Solo predicción del modelo (L5)
nav_order: 655
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
description: "Prasugrel: nueva indicación predicha, Hipertensión pulmonar (nivel de evidencia L5). Indicación original: Síndrome coronario agudo"
monitor_inn: "PRASUGREL"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "leprosy"]
---

# Prasugrel
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Prasugrel: De Síndrome Coronario Agudo a Hipertensión Pulmonar
{: .text-alpha }

## Resumen en Una Frase

Prasugrel es un antiagregante plaquetario que se utiliza originalmente en el síndrome coronario agudo.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero actualmente hay **0 ensayos clínicos** y **2 publicaciones** de relevancia indirecta, ninguna de las cuales evalúa prasugrel en esta enfermedad. La predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome coronario agudo |
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 0,9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 8) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según la información conocida, prasugrel es un antagonista del receptor plaquetario P2Y12 (clase de las tienopiridinas). Su eficacia en el síndrome coronario agudo, donde previene la formación de trombos, está establecida.

La relación con la hipertensión pulmonar es plausible pero no está demostrada. La activación plaquetaria y la trombosis in situ contribuyen a la remodelación vascular pulmonar, por lo que bloquear P2Y12 podría, en teoría, modificar ese proceso.

Las dos publicaciones recuperadas tratan sobre la adherencia a clopidogrel en pacientes con síndrome coronario agudo y sobre el efecto de terapias previas en el desenlace de COVID-19. Ninguna prueba prasugrel en hipertensión pulmonar, así que el vínculo sigue siendo especulativo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohorte | Current Medical Research and Opinion | Factores asociados al uso, la adherencia y la persistencia de clopidogrel en pacientes con síndrome coronario agudo tras intervención coronaria percutánea. No aborda hipertensión pulmonar. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohorte (registro) | Kardiologiia | Influencia de las terapias previas para comorbilidades sobre el riesgo de muerte por COVID-19 en el registro internacional ACTIV. No evalúa prasugrel en hipertensión pulmonar. |

## Información de Mercado en España

Hay 20 autorizaciones vigentes, todas de medicamentos de un solo principio activo (comprimidos recubiertos con película, 5 mg y 10 mg). A continuación se listan las 5 principales; el texto de indicación aprobada no estaba disponible en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 08503009 | Efient 10 mg (Substipharm) | Comprimido recubierto con película |
| 82930 | Prasugrel Teva 10 mg EFG | Comprimido recubierto con película |
| 83098 | Prasugrel Stada 10 mg EFG | Comprimido recubierto con película |
| 83508 | Prasugrel Krka 5 mg EFG | Comprimido recubierto con película |
| 83730 | Prasugrel Lesvi 10 mg EFG | Comprimido recubierto con película |

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (no proceden del prospecto): insuficiencia hepática, trastornos hipotensivos, enfermedades de la coagulación, ictus y trastornos cerebrovasculares, infarto cerebral, ataque isquémico transitorio, insuficiencia vertebrobasilar, hemorragia intracraneal, púrpura trombocitopénica y lesiones o traumatismos.
- **Interacciones farmacológicas** (100 registradas; se muestran las de mayor gravedad):
  - **Mayor**: deferasirox e ibritumomab tiuxetán.
  - **Moderada**: ácido acetilsalicílico, morfina, opio, fenfluramina, dexfenfluramina y sibutramina.
  - **Menor**: varios antagonistas H2 (famotidina, ranitidina, cimetidina, nizatidina) e inhibidores de la bomba de protones (omeprazol, esomeprazol, pantoprazol, lansoprazol, rabeprazol, dexlansoprazol), además de bupropión.

Para las advertencias principales y las contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertensión pulmonar tiene un puntaje alto en el modelo, pero no cuenta con ensayos clínicos ni con literatura que pruebe prasugrel en esta enfermedad (nivel L5). El perfil de riesgo hemorrágico del fármaco exige una base de evidencia mayor antes de plantear su uso en esta población.

**Para avanzar se necesita:**
- Estudios preclínicos que respalden el papel de P2Y12 en la remodelación vascular pulmonar.
- Datos detallados del mecanismo de acción para analizar el vínculo mecanístico.
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones) para completar el cribado de seguridad, sobre todo el riesgo hemorrágico.
- Valorar la migraña asociada a foramen oval permeable, que en los mismos datos tiene mejor respaldo (nivel L3, con un ensayo de Fase 3 en reclutamiento y revisiones retrospectivas de tienopiridinas) como alternativa prioritaria.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

