---
layout: default
title: Selumetinib
parent: Solo predicción del modelo (L5)
nav_order: 489
evidence_level: L5
indication_count: 10
---

# Selumetinib
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

# Selumetinib: De Neurofibroma Plexiforme asociado a NF1 a Lentiginosis Generalizada Familiar

## Resumen en Una Frase

Selumetinib es un inhibidor de MEK1/2 comercializado en España como Koselugo. Según la información del paquete de evidencia, está indicado en el neurofibroma plexiforme asociado a NF1. El modelo TxGNN predice que podría ser efectivo para **lentiginosis generalizada familiar**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, que se basa solo en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Neurofibroma plexiforme asociado a NF1 (según el análisis de otra indicación del paquete; los textos de autorización de AEMPS están vacíos) |
| Nueva Indicación Predicha | Lentiginosis generalizada familiar |
| Puntaje de Predicción TxGNN | 99,96 % (puntaje saturado, no discrimina entre candidatos) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados de mecanismo de acción en DrugBank para este paquete. Según la información conocida, selumetinib inhibe MEK1/2 en la vía RAS/MAPK. Su eficacia se ha comprobado en el neurofibroma plexiforme asociado a NF1, un tumor con activación de esta vía.

La relación con la lentiginosis generalizada familiar es **especulativa**. Los datos no muestran que esta enfermedad esté causada por una desregulación de la vía MAPK. Un vínculo con trastornos de la pigmentación no se puede establecer con la información disponible.

El puntaje TxGNN (~0,9996) está saturado y no permite distinguir esta predicción de otras. Por tanto, no debe interpretarse como señal de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1211552004 | KOSELUGO 7,5 MG granulado en cápsula para abrir | Granulado en envase unidosis |
| 1211552001 | KOSELUGO 10 mg cápsulas duras | Cápsula dura |
| 1211552003 | KOSELUGO 5 MG granulado en cápsula para abrir | Granulado en envase unidosis |
| 1211552002 | KOSELUGO 25 mg cápsulas duras | Cápsula dura |

Titular de las cuatro autorizaciones: AstraZeneca AB.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de MEK1/2) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos ni literatura, y el mecanismo hacia esta enfermedad no está respaldado por los datos. Además, faltan los datos de seguridad del prospecto de AEMPS.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), pendiente y bloqueante para el cribado de seguridad.
- Obtener el mecanismo de acción desde DrugBank.
- Demostrar si la lentiginosis generalizada familiar tiene una base genética o funcional en la vía RAS/MAPK.
- Como referencia, entre las 10 predicciones principales, **schwannoma de nervio periférico** (L3) es la que tiene más respaldo. Incluye un ensayo de Fase 2 terminado en NF2 (NCT03095248, n=10, sin resultados de eficacia) y estudios preclínicos con inhibidores de MEK en células de schwannoma. Podría priorizarse antes que esta indicación.

*Este informe es solo para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

