---
layout: default
title: Fosinopril
parent: Solo predicción del modelo (L5)
nav_order: 247
evidence_level: L5
indication_count: 5
---

# Fosinopril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Fosinopril: De Indicación Original No Registrada a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Fosinopril es un inhibidor de la enzima convertidora de angiotensina (IECA) comercializado en España, pero el Evidence Pack no incluye el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**,
con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (las 4 autorizaciones no tienen texto de indicación) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, fosinopril es un inhibidor de la ECA que reduce la angiotensina II y atenúa la vasoconstricción dependiente del sistema renina-angiotensina-aldosterona (SRAA), incluida la hipertensión intraglomerular.

Esto es plausible frente al daño renal hipertensivo, porque el SRAA participa en la lesión renal por presión elevada. Sin embargo, la relación con la indicación original no pudo evaluarse, ya que no hay texto de indicación y la similitud con la indicación original figura como pendiente.

Además, la hipertensión maligna es una emergencia hipertensiva que normalmente se maneja con fármacos intravenosos titulables. Fosinopril se comercializa solo en comprimidos orales, así que la compatibilidad de vía de administración también está pendiente de evaluar. El puntaje alto del grafo de conocimiento no debe interpretarse como respaldo clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 59716 | FOSITENS 20 mg COMPRIMIDOS | Comprimido | Bausch Health Ireland Limited |
| 83239 | FOSINOPRIL AUROVITAS 20 MG COMPRIMIDOS EFG | Comprimido | Aurovitas Spain, S.A.U. |
| 74975 | FOSINOPRIL AUROBINDO 20 mg COMPRIMIDOS EFG | Comprimido | Laboratorios Aurobindo S.L.U. |
| 66779 | FOSINOPRIL TEVA 20 mg COMPRIMIDOS EFG | Comprimido | Teva Pharma S.L.U. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como precaución derivada del análisis de las predicciones, los IECA pueden provocar lesión renal aguda en caso de estenosis bilateral de la arteria renal o estenosis de un riñón único. Esto es relevante para la predicción vecina de hipertensión renovascular maligna y exige una revisión de seguridad antes de cualquier avance.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura específica. Además, faltan datos regulatorios y de seguridad, y la vía oral podría no ser adecuada para una emergencia hipertensiva.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS para completar advertencias, contraindicaciones e indicación original (brecha bloqueante)
- Obtener datos del mecanismo de acción desde DrugBank
- Realizar una búsqueda de literatura dirigida a fosinopril o IECA en hipertensión maligna y nefropatía hipertensiva
- Evaluar la compatibilidad de vía de administración (oral frente a intravenosa)
- Realizar una revisión de seguridad renal previa a cualquier paso posterior

**Nota sobre otras predicciones:** las otras cuatro predicciones (hipertensión renovascular maligna, dos formas de hipertensión pulmonar y síndrome de Braddock) también tienen nivel L5 y recomendación Hold. La literatura recuperada para la hipertensión pulmonar por enfermedad pulmonar o hipoxia trata la hipoxia en general y no aborda fosinopril ni hipertensión pulmonar, por lo que no constituye evidencia de apoyo.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

