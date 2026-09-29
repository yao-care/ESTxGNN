---
layout: default
title: Mercaptopurine
parent: Solo predicción del modelo (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurina: Hacia una Nueva Indicación en Leucemia Mieloide

## Resumen en Una Frase

La mercaptopurina es un antimetabolito de las purinas que se usa en oncohematología. Los datos disponibles no indican su indicación original en España.
El modelo TxGNN predice que podría ser eficaz en **leucemia mieloide**, con **30 ensayos clínicos** y **20 publicaciones** asociados a esta dirección.
Estos ensayos evalúan sobre todo regímenes combinados, por lo que el efecto propio de la mercaptopurina no está aislado.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Leucemia mieloide |
| Puntaje de Predicción TxGNN | 99,94 % |
| Nivel de Evidencia | L1 (≥2 ECA de Fase 3 completados, pero de regímenes combinados) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados del mecanismo de acción en la ficha del fármaco. Según la información conocida, la mercaptopurina es un antimetabolito de las purinas. Sus nucleótidos de tioguanina se incorporan al ADN y bloquean la síntesis de novo de purinas. Esto es plausible frente a blastos mieloides de proliferación rápida.

En leucemia mieloide, la mercaptopurina se usa principalmente como componente de regímenes y no como agente único. El ejemplo más claro es el mantenimiento de la leucemia promielocítica aguda (LPA) con ATRA y metotrexato. También aparece en esquemas de inducción de LMA de adultos, como daunorrubicina, citarabina y 6-MP.

Existe evidencia de Fase 3, pero los ensayos comparan regímenes completos. Por eso la contribución individual de la mercaptopurina no puede aislarse con los datos actuales.

---

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes de 30. Se priorizan los que nombran la mercaptopurina o su rol de mantenimiento.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Fase 3 | Completado | 420 | Aleatoriza mantenimiento con tretinoína intermitente frente a tretinoína + mercaptopurina + metotrexato en LPA no tratada, con o sin trióxido de arsénico en la consolidación |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Fase 4 | Completado | 300 | PETHEMA LPA 2005: mantenimiento con ATRA + metotrexato + mercaptopurina a dosis bajas en LPA |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | N/A | Desconocido | 1068 | Protocolo AIDA: evalúa el mantenimiento con ATRA, con metotrexato + 6-mercaptopurina, o con ambos |
| [NCT00180128](https://clinicaltrials.gov/study/NCT00180128) | Fase 4 | Desconocido | 80 | AIDA2000: terapia adaptada al riesgo en LPA, con dos años de mantenimiento con 6-MP, metotrexato y ATRA |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Fase 4 | Completado | N/D | AIDA adaptado al riesgo en LPA, con mantenimiento y rescate con ATRA + metotrexato + mercaptopurina |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Fase 3 | Completado | 105 | S0521: mantenimiento frente a observación en LPA de riesgo bajo/intermedio. Los brazos exactos deben confirmarse en el registro |
| [NCT00962767](https://clinicaltrials.gov/study/NCT00962767) | Fase 3 | Completado | 168 | Dos dosis de gemtuzumab frente a dos años de mantenimiento con ATRA + quimioterapia en LPA de riesgo intermedio y alto. El resumen no especifica la quimioterapia |
| [NCT00599937](https://clinicaltrials.gov/study/NCT00599937) | Fase 3 | Completado | 576 | Evalúa el momento óptimo de la quimioterapia con ATRA y el papel del mantenimiento |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Fase 1/2 | Reclutando | 48 | 6-mercaptopurina + ácido valproico frente a hidroxiurea + ácido valproico en LMA o SMD de alto riesgo no aptos para terapia estándar |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Fase 1 | Reclutando | 10 | Venetoclax + 6-mercaptopurina oral en LMA en recaída o refractaria. Estudio pequeño y temprano |

---

## Evidencia de Literatura

Se muestran 10 de 20 publicaciones. Ninguna es reciente ni de gran tamaño en esta indicación.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | ECA | Int J Hematol | Añadir etopósido a daunorrubicina, citarabina y 6-MP en la inducción de LMA de adultos no aportó beneficio (JALSG-AML92) |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | ECA | Cancer Chemother Pharmacol | 433 casos en Japón. Comparó daunorrubicina frente a aclarubicina con BH-AC, 6-MP y prednisolona. Remisión completa: 63,7 % frente a 53,9 % |
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohorte | J Korean Med Sci | Mantenimiento oral con 6-MP diaria + metotrexato semanal durante 2 años en LMA no candidata a trasplante |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Estudio piloto | Cancer Invest | 6-MP en dosis altas + citarabina a dosis intermedia en primera remisión de LMA pediátrica. De 17 niños, 14 lograron remisión completa con la inducción convencional |
| [15124700](https://pubmed.ncbi.nlm.nih.gov/15124700/) | 2004 | No clasificado | Ann Hematol | Analiza si el mantenimiento aporta ventaja tras inducción y consolidación muy intensivas en LMA infantil |
| [1059498](https://pubmed.ncbi.nlm.nih.gov/1059498/) | 1975 | Cohorte | Cancer | 18 niños con LMA tratados con citarabina, daunorrubicina, prednisolona y mercaptopurina o tioguanina. Remisión inicial del 78 %; supervivencia mediana de 7 meses |
| [4518586](https://pubmed.ncbi.nlm.nih.gov/4518586/) | 1973 | No clasificado | Cancer | Citarabina con 6-mercaptopurina en LMA de adultos (histórico, sin resumen disponible) |
| [265178](https://pubmed.ncbi.nlm.nih.gov/265178/) | 1977 | Serie de casos | Blood | Tres casos de leucemia mieloide crónica juvenil con respuesta clínica y hematológica a citarabina subcutánea + mercaptopurina oral |
| [28835099](https://pubmed.ncbi.nlm.nih.gov/28835099/) | 2017 | Preclínico | Biomacromolecules | Profármaco de mercaptopurina con ácido hialurónico dirigido a CD44 para LMA, en fase experimental |
| [28152123](https://pubmed.ncbi.nlm.nih.gov/28152123/) | 2017 | Cohorte | JAMA Oncol | Señal de seguridad: la terapia de enfermedades autoinmunes se asocia con neoplasias mieloides relacionadas con el tratamiento |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 80570 | Mercaptopurina Silver 50 mg comprimidos | Comprimido | Silver Pharma S.L. |
| 34565 | Mercaptopurina Aspen 50 mg comprimidos | Comprimido | Aspen Pharma Trading Limited |
| 85931 | Mercaptopurina Zentiva 50 mg comprimidos EFG | Comprimido | Zentiva K.S. |
| 11727001 | Xaluprine 20 mg/ml suspensión oral | Solución oral | Nova Laboratories Limited |
| 84602 | Mercaptopurina Silver Pharma 50 mg comprimidos EFG | Comprimido | Silver Pharma S.L. |

Los textos de indicación aprobada no figuran en los datos recibidos de AEMPS.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, análogo de purinas / tiopurina) |
| Riesgo de Mielosupresión | Alto. La dosis se titula según el grado de mielosupresión. El riesgo aumenta con variantes de TPMT y NUDT15 (mayor neutropenia) |
| Clasificación de Emetogenicidad | Baja (clasificación general de un antimetabolito oral; no procede del Evidence Pack) |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, glucemia (se han descrito hipoglucemias graves), genotipo TPMT/NUDT15 y, si es posible, metabolitos (6-TGN y 6-MMP) |
| Protección en Manejo | Seguir la normativa de manejo de fármacos citotóxicos. Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ECA de Fase 3 completados en leucemia mieloide, sobre todo en LPA. En ellos la mercaptopurina forma parte del mantenimiento o de esquemas de inducción. Sin embargo, esos ensayos comparan regímenes completos, y la literatura específica es antigua o de poco tamaño.

**Para avanzar se necesita:**
- Descargar y revisar la ficha técnica de AEMPS (advertencias y contraindicaciones), pendiente y bloqueante para el cribado de seguridad.
- Obtener el mecanismo de acción detallado desde DrugBank.
- Confirmar en los registros los brazos exactos de los ensayos S0521 (NCT00492856) y NCT00962767, y el uso de mercaptopurina en los ensayos marcados como no verificados.
- Definir cómo aislar la contribución de la mercaptopurina frente al resto del régimen.
- Establecer medidas de protección: genotipado TPMT/NUDT15, monitoreo de metabolitos, hemograma, función hepática y glucemia, y apoyo a la adherencia.

*Los resultados son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

