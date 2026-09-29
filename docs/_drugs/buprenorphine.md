---
layout: default
title: Buprenorphine
parent: Evidencia moderada (L3-L4)
nav_order: 89
evidence_level: L4
indication_count: 6
---

# Buprenorphine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **6** 
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

# Buprenorfina: De Dolor Intenso y Dependencia de Opioides a Porfiria Aguda Intermitente

## Resumen en Una Frase

La buprenorfina se utiliza originalmente para tratar el dolor intenso y la dependencia de opioides.
El modelo TxGNN predice que podría ser efectiva para **porfiria aguda intermitente**,
pero solo hay **0 ensayos clínicos** y **1 publicación** (un reporte de caso sobre manejo anestésico), que no respalda un efecto terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dolor intenso y dependencia de opioides (según datos farmacológicos; los registros de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Porfiria aguda intermitente |
| Puntaje de Predicción TxGNN | 99.41% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de DrugBank. Según la información farmacológica disponible, la buprenorfina es un agonista parcial del receptor opioide mu (OPRM1) y antagonista del receptor kappa (OPRK1). Se usa como analgésico potente y en el tratamiento de mantenimiento de la dependencia de opioides.

**Con la evidencia actual, la predicción no es razonable desde el punto de vista mecanístico.** No existe un vínculo terapéutico conocido entre la buprenorfina y la porfiria aguda intermitente. El único artículo asociado es un reporte de caso sobre el manejo anestésico de una paciente con porfiria, es decir, sobre la seguridad de la analgesia durante una cirugía y no sobre el tratamiento de la enfermedad.

El puntaje alto de TxGNN (0.994) probablemente es un artefacto del grafo de conocimiento y no está respaldado por evidencia clínica.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Reporte de caso | Masui (Revista japonesa de anestesiología) | Manejo anestésico de una mujer de 40 años con sospecha de porfiria aguda intermitente, operada por un tumor maligno de ovario. Trata la seguridad perioperatoria, no un tratamiento de la porfiria. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 80670 | GEXANA 52,5 microgramos/hora parche transdérmico EFG | Parche transdérmico |
| 82322 | Buprenorfina Sandoz Farmacéutica 70 microgramos/hora parches transdérmicos EFG | Parche transdérmico |
| 1191369001 | SIXMO 74,2 mg implante | Implante |
| 82066 | Buprenorfina Semanal Stada 10 microgramos/hora parche transdérmico | Parche transdérmico |
| 70804 | FELIBEN 35 microgramos/hora parches transdérmicos | Parche transdérmico |

Se muestran 5 de las 20 autorizaciones. Los registros no incluyen el texto de la indicación aprobada. También existe una forma de solución inyectable de liberación prolongada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Dado que la indicación propuesta es una porfiria aguda, conviene verificar en la ficha técnica la seguridad del fármaco en pacientes con porfiria antes de cualquier uso.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos, y la única publicación es un reporte de caso sobre manejo anestésico que no muestra ningún efecto terapéutico. El puntaje de TxGNN por sí solo no basta para avanzar. Las otras cinco predicciones (discinesia lingual-facial-bucal, trastorno de tics crónico, punta-onda continua durante el sueño, enfermedad extrapiramidal y del movimiento, y ataques de estremecimiento benigno) tampoco tienen respaldo clínico. Cuatro de ellas están en nivel L4 o L5 sin ensayos, y en la discinesia solo hay señales indirectas o de seguridad.

**Para avanzar se necesita:**
- Una hipótesis mecanística concreta que vincule los receptores mu y kappa con la fisiopatología de la porfiria aguda intermitente
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de AEMPS, incluyendo la seguridad en porfiria
- Estudios preclínicos o clínicos que evalúen la eficacia, no solo el manejo anestésico

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

