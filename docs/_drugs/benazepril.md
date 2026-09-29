---
layout: default
title: Benazepril
parent: Solo predicción del modelo (L5)
nav_order: 66
evidence_level: L5
indication_count: 5
---

# Benazepril
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

# Benazepril: De Indicación Original No Registrada a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Benazepril está comercializado en España con el nombre Cibacen, pero los datos disponibles no recogen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, que se basa únicamente en el puntaje del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.65% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, benazepril es un inhibidor de la enzima convertidora de angiotensina (IECA). Estos fármacos reducen la presión arterial y la presión dentro del glomérulo al bloquear el sistema renina-angiotensina-aldosterona (SRAA). Este dato procede de la clase farmacológica y no de DrugBank.

Por eso, mecanísticamente, un vínculo con el daño renal causado por hipertensión es biológicamente plausible. La hipertensión maligna daña los vasos y el riñón, y el SRAA participa en ese proceso.

Aun así, este razonamiento es solo una hipótesis. No hay ensayos ni literatura que lo confirmen, y la similitud con la indicación original no pudo evaluarse porque esta no está registrada. Hoy la predicción descansa únicamente en el puntaje de TxGNN (0.9965).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59552 | CIBACEN 20 mg comprimidos recubiertos con película | Comprimido | No especificada en los datos |
| 59551 | CIBACEN 5 mg comprimidos recubiertos con película | Comprimido | No especificada en los datos |
| 59553 | CIBACEN 10 mg comprimidos recubiertos con película | Comprimido | No especificada en los datos |

Titular de las tres autorizaciones: Meda Pharma S.L.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como aviso general de clase, los IECA pueden reducir la función renal de forma aguda en pacientes con estenosis bilateral de la arteria renal. Este riesgo debería revisarse antes de cualquier avance, sobre todo en cuadros de origen renovascular.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.65%), pero no hay ensayos clínicos ni literatura que la respalden (nivel L5, etapa S0). Además, faltan datos de seguridad y de mecanismo de acción, por lo que no se puede avanzar con criterio.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que es la brecha que bloquea el cribado de seguridad
- Completar el mecanismo de acción e indicaciones originales desde DrugBank
- Buscar ensayos clínicos y literatura específicos sobre benazepril o IECA en hipertensión maligna con daño renal
- Evaluar el riesgo renal en estenosis de la arteria renal antes de considerar cualquier uso
- Otras cuatro indicaciones predichas (hipertensión renovascular maligna, dos formas de hipertensión pulmonar y síndrome de Braddock) también están en nivel L5 y Hold. Las 20 publicaciones asociadas a la hipertensión pulmonar por enfermedad pulmonar o hipoxia tratan de hipoxia en general y no estudian benazepril, por lo que no constituyen evidencia de apoyo.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

