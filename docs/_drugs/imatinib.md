---
layout: default
title: Imatinib
parent: Solo predicción del modelo (L5)
nav_order: 406
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "IMATINIB"
predicted_indications: ["heart fibrosarcoma", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "low grade fibromyxoid sarcoma", "liposarcoma", "liver fibrosarcoma", "autosomal recessive familial Mediterranean fever", "ovarian myxoid liposarcoma", "familial rhabdoid tumor"]
description: "Imatinib: nueva indicación predicha, Heart fibrosarcoma (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Imatinib
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

## Imatinib: Heart fibrosarcoma
{: .text-alpha }

## Resumen en Una Frase

Imatinib es un inhibidor de tirosina quinasas, utilizado originalmente para el tratamiento de la leucemia mieloide crónica BCR-ABL1 positiva, los tumores del estroma gastrointestinal (GIST) y otras enfermedades hematológicas y sarcomatosas.
El modelo TxGNN predice que podría ser efectivo para **fibrosarcoma cardíaco**, aunque por ahora solo hay **1 publicación de carácter general** y **ningún ensayo clínico** que respalde esta dirección.
La evidencia es muy limitada y se basa casi exclusivamente en la predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Heart fibrosarcoma |
| Puntaje de Predicción TxGNN | 0.9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 8) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico general, imatinib inhibe las quinasas ABL, KIT y PDGFR. Su eficacia en leucemia mieloide crónica y GIST está bien establecida, y mecanísticamente podría ser aplicable a tumores impulsados por estas vías.

Los fibrosarcomas y tumores fibroblásticos similares, en particular los dirigidos por la fusión COL1A1-PDGFB (como el dermatofibrosarcoma protuberans, que ya es una indicación original de imatinib), podrían responder mediante la inhibición de PDGFRB. Esto aporta una base biológica plausible para la predicción.

Sin embargo, no existen datos específicos en localización cardíaca. La única publicación asociada es un comentario general sobre nuevas indicaciones de imatinib que señala que la evidencia no es sólida. La predicción debe considerarse, por tanto, una hipótesis de investigación y no una evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para fibrosarcoma cardíaco.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Revisión | Prescrire International | Comentario sobre las nuevas indicaciones de imatinib (p. ej., leucemia linfoblástica aguda Ph+); concluye que la evidencia de varias de ellas no es sólida. No aporta datos cardíacos específicos |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 81933 | Imatinib Aristo 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 81037 | Imatinib Normon 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 113845002 | Imatinib Accord 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 01198010 | Glivec 400 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 01198008 | Glivec 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

Hay 20 autorizaciones vigentes en total (todas de monofármaco), incluidas presentaciones en comprimidos y cápsulas duras; arriba se muestran 5 de ellas.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasas) |
| Riesgo de Mielosupresión | Medio (el grafo de conocimiento asocia imatinib con neutropenia, trombocitopenia y anemia como condiciones de precaución) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo, función hepática y renal, control de peso y signos de retención de líquidos, función cardíaca |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Condiciones de precaución según el modelo TxGNN (deep learning)** (no proceden del texto del prospecto): insuficiencia hepática y enfermedad hepática, enfermedad renal, neutropenia, trombocitopenia, anemia, agranulocitosis, insuficiencia cardíaca congestiva e insuficiencia cardíaca, enfermedad de las arterias coronarias, valvulopatías, derrame pericárdico, edema pulmonar, edema cerebral, hipertensión, diabetes mellitus y cetoacidosis diabética, hipofosfatemia, úlcera péptica activa, síndrome de Gilbert e hiperbilirrubinemia, entre otras. Esta información proviene del modelo y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las incluidas en la muestra revisada, las de nivel **mayor** son con **eliglustat** y **naloxegol**. Las de nivel moderado incluyen corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), cimetidina, claritromicina, aprepitant, pioglitazona, glimepirida, saxagliptina, lansoprazol, dexlansoprazol, morfina, naltrexona, naldemedina y metreleptina.

Dado que el propio candidato tiene una localización cardíaca, las condiciones cardiovasculares señaladas (insuficiencia cardíaca, derrame pericárdico) son especialmente relevantes. Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción del fibrosarcoma cardíaco tiene un puntaje alto del modelo, pero no cuenta con ensayos clínicos ni con literatura específica; solo hay un comentario general. Además, las condiciones cardíacas señaladas como precaución para imatinib exigen cautela adicional en esta localización.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y búsqueda de evidencia específica en sarcomas cardíacos (series de casos, informes de casos).
- Confirmar si estos tumores presentan alteraciones de PDGFR/KIT o la fusión COL1A1-PDGFB.
- Obtener las advertencias y contraindicaciones oficiales del prospecto de la AEMPS.
- Evaluar el perfil de seguridad cardiovascular en la población de interés.
- Como alternativas con más respaldo dentro de las predicciones del modelo, considerar priorizar tumores fibroblásticos relacionados con el dermatofibrosarcoma (con evidencia de revisiones y guías, aunque se trata en gran parte de una indicación ya existente) y sarcomas de tejidos blandos en general (ensayos de Fase 2 completados, pero sin resultados específicos por histología).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

