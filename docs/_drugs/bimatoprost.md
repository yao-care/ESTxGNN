---
layout: default
title: Bimatoprost
parent: Solo predicción del modelo (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: De Glaucoma e Hipertensión Ocular a Síndrome de Malformación con Componente Odontal y/o Periodontal

## Resumen en Una Frase

Bimatoprost es un análogo de prostamida (tipo prostaglandina F2α) que se usa en colirios, originalmente para el glaucoma de ángulo abierto y la hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de malformación con componente odontal y/o periodontal**,
pero hay **0 ensayos clínicos** y las **20 publicaciones** asociadas tratan de periodontitis en general, sin relación con bimatoprost.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión ocular y glaucoma de ángulo abierto (según la literatura; las autorizaciones no incluyen texto de indicación) |
| Nueva Indicación Predicha | Síndrome de malformación con componente odontal y/o periodontal |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, bimatoprost es un análogo de prostamida/prostaglandina F2α, con eficacia comprobada en glaucoma e hipertensión ocular. También se le conoce un efecto sobre el crecimiento del pelo (prolonga la fase anágena).

En este caso, **la predicción no tiene un vínculo mecanístico plausible**. Un síndrome de malformación con componente dental o periodontal es un trastorno estructural del desarrollo, y no hay ninguna razón conocida por la que un análogo de prostamida ocular lo trate. Las 20 publicaciones vinculadas son literatura general sobre periodontitis, y ninguno de sus títulos menciona bimatoprost.

El puntaje TxGNN es muy alto (0.99997), pero es solo una predicción del modelo, probablemente una asociación del grafo de conocimiento, sin respaldo clínico.

## Evidencia de Literatura

Ninguna de estas publicaciones estudia bimatoprost. Son trabajos generales sobre periodontitis.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | Guía clínica | J Clin Periodontol | Guía de práctica clínica EFP (nivel S3) para el tratamiento de la periodontitis en estadio IV |
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | Revisión sistemática | Cochrane Database Syst Rev | Tratamiento de la periodontitis para el control glucémico en personas con diabetes |
| [29291254](https://pubmed.ncbi.nlm.nih.gov/29291254/) | 2018 | Revisión sistemática | Cochrane Database Syst Rev | Terapia periodontal de soporte para mantener la dentición en adultos tratados por periodontitis |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Revisión | Diabetologia | Relación bidireccional entre periodontitis y diabetes |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Revisión | Periodontology 2000 | Complicaciones y errores de tratamiento en la cirugía periodontal regenerativa |
| [39233377](https://pubmed.ncbi.nlm.nih.gov/39233377/) | 2024 | Revisión | Periodontology 2000 | Relación entre el sueño y la salud periodontal |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Revisión | J Dent Res | Papel de los fibroblastos gingivales en la patogenia de la periodontitis |
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | Revisión | J Nanobiotechnology | Inmunoterapia de macrófagos mediada por biomateriales en periodontitis |
| [9495612](https://pubmed.ncbi.nlm.nih.gov/9495612/) | 1998 | Observacional | J Clin Periodontol | Complejos microbianos en la placa subgingival de 185 sujetos |
| [38362600](https://pubmed.ncbi.nlm.nih.gov/38362600/) | 2024 | Estudio clínico | J Dent Res | Efecto de la periodontitis y su tratamiento sobre la microbiota oral e intestinal (n=47) |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Información de Mercado en España

Bimatoprost está comercializado en España con 20 autorizaciones. Estas son las principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 81694 | Bimatoprost Aristo 0,3 mg/ml colirio en solución | Colirio en solución |
| 86578 | Visuplain 0,1 mg/ml colirio en solución | Colirio en solución |
| 102205006 | Lumigan 0,3 mg/ml colirio en solución en envase unidosis | Colirio en solución en envase unidosis |
| 02205003 | Lumigan 0,1 mg/ml colirio en solución | Colirio en solución |
| 83498 | Bimatoprost Qualigen 0,3 mg/ml colirio en solución en envase unidosis | Colirio en solución en envase unidosis |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos clínicos, la literatura asociada no menciona bimatoprost y no existe un mecanismo plausible que conecte el fármaco con una malformación estructural del desarrollo dental o periodontal.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que justifiquen un vínculo biológico con esta malformación
- Estudios preclínicos o de mecanismo que respalden la hipótesis
- Descartar que la predicción sea un artefacto del grafo de conocimiento
- Revisar el prospecto de AEMPS para completar la información de seguridad y las indicaciones autorizadas

**Nota:** en el mismo paquete, la predicción de **alopecia** (posición 8) tiene mucha más evidencia. Incluye varios ensayos de Fase 2 completados en alopecia androgenética (por ejemplo NCT01325350, NCT01325337 y NCT01904721) y una calificación L2 con recomendación *Proceed with Guardrails*. Conviene evaluarla como candidato independiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

