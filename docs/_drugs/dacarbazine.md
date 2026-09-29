---
layout: default
title: Dacarbazine
parent: Evidencia moderada (L3-L4)
nav_order: 153
evidence_level: L4
indication_count: 1
---

# Dacarbazine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Dacarbazina: De Agente Alquilante Antineoplásico a Neoplasia de las Vías Aerodigestivas Superiores

## Resumen en Una Frase

Dacarbazina es un agente alquilante citotóxico que se administra por perfusión intravenosa.
El modelo TxGNN predice que podría ser efectivo para **neoplasia de las vías aerodigestivas superiores**, pero solo hay **1 ensayo clínico** indirecto (con temozolomida, no con dacarbazina) y ninguna publicación con datos directos de dacarbazina en esta indicación.
La predicción es por ahora una hipótesis del modelo, sin respaldo clínico propio.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Neoplasia de las vías aerodigestivas superiores |
| Puntaje de Predicción TxGNN | 99,26 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, dacarbazina es un agente alquilante que metila el ADN. Se activa en el hígado a MTIC, el mismo metabolito activo que libera espontáneamente la temozolomida. Por eso los datos de temozolomida son un sustituto plausible a nivel de clase, aunque no una prueba directa.

La lógica de la predicción es que un alquilante de esta clase podría actuar sobre tumores de cabeza, cuello y esófago. La sensibilidad depende del estado de MGMT (la enzima que repara el daño por metilación), y así lo plantea el ensayo de temozolomida seleccionado por metilación del promotor de MGMT.

Hay dos motivos de cautela. El puntaje de 0,993 proviene solo del grafo de conocimiento y no de datos clínicos. Además, los cánceres escamosos de las vías aerodigestivas no suelen responder a los alquilantes. No hay datos clínicos de dacarbazina en esta indicación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Fase 2 | Terminado | 86 | Temozolomida (no dacarbazina) en cánceres avanzados de vías aerodigestivas, colorrectal y pulmón no microcítico, seleccionados por metilación del promotor de MGMT. Es evidencia indirecta de clase. No se aportó resultado de eficacia. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Ensayo fase II | Mol Cancer Ther | Publicación del ensayo NCT00423150: evalúa si la metilación de MGMT predice la respuesta a temozolomida en cánceres aerodigestivos y colorrectales avanzados. |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Estudio clínico | Ann Oncol | Dacarbazina con 5-fluorouracilo en cáncer medular de tiroides avanzado. No corresponde a la indicación predicha. |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | Revisión | Gan To Kagaku Ryoho | Quimioterapia del angiosarcoma de cabeza y cuello. Menciona el esquema CYVADIC, que incluye dacarbazina (DTIC). |
| [25772801](https://pubmed.ncbi.nlm.nih.gov/25772801/) | 2015 | Revisión | J Clin Neurosci | Papel de temozolomida en tumores hipofisarios agresivos. |
| [17987262](https://pubmed.ncbi.nlm.nih.gov/17987262/) | 2008 | Ensayo fase II | J Neurooncol | Vinorelbina con temozolomida intensiva en metástasis cerebrales. Indicación distinta. |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Serie de casos | Ear Nose Throat J | Seis pacientes con paraganglioma maligno de cabeza y cuello, con análisis de opciones de tratamiento. |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | Cohorte retrospectiva | Int J Radiat Oncol Biol Phys | Radioterapia del estesioneuroblastoma (tumor intranasal). No evalúa dacarbazina. |
| [34705104](https://pubmed.ncbi.nlm.nih.gov/34705104/) | 2022 | Revisión | J Cancer Res Clin Oncol | Carga global de cánceres asociados al virus de Epstein-Barr. Contexto epidemiológico. |

Ninguna publicación aporta datos directos de eficacia de dacarbazina en neoplasias de las vías aerodigestivas superiores.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62334 | DACARBAZINA MEDAC 1000 mg | Polvo para solución para perfusión | No consta en el registro |
| 62333 | DACARBAZINA MEDAC 500 mg | Polvo para solución para perfusión | No consta en el registro |

Ambas autorizaciones pertenecen a Medac Gesellschaft für Klinische Spezialpräparate GmbH.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante, profármaco activado a MTIC) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal (recomendación general para citotóxicos) |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La consulta de interacciones farmacológicas no devolvió resultados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L4: el único ensayo es de temozolomida (terminado, sin resultados de eficacia) y no hay datos clínicos de dacarbazina en esta indicación. El puntaje alto de TxGNN no compensa esa falta, y los tumores escamosos aerodigestivos no suelen responder a alquilantes.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS con advertencias y contraindicaciones (bloqueante para el cribado de seguridad).
- Completar el mecanismo de acción desde DrugBank.
- Buscar datos clínicos propios de dacarbazina en cáncer de cabeza, cuello o esófago.
- Evaluar si el estado de MGMT puede servir como criterio de selección de pacientes.
- Confirmar la indicación original aprobada, hoy vacía en el registro.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

