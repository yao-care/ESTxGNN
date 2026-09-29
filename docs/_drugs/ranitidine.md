---
layout: default
title: Ranitidine
parent: Evidencia moderada (L3-L4)
nav_order: 457
evidence_level: L3
indication_count: 10
---

# Ranitidine
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

# Ranitidina: De Úlcera Gástrica a Enfermedad Ulcerosa Péptica Activa

## Resumen en Una Frase

La ranitidina es un antagonista de los receptores H2 de histamina, utilizado para tratar úlceras gástricas al reducir la secreción de ácido. El modelo TxGNN predice que podría ser efectiva para la **enfermedad ulcerosa péptica activa**, con **1 ensayo clínico** (que no evalúa la ranitidina) y **20 publicaciones** que respaldan esta dirección.
En la práctica se trata de un uso ya establecido más que de un reposicionamiento genuino.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Úlceras gástricas (según los datos farmacológicos; los registros de AEMPS recibidos no incluyen texto de indicación) |
| Nueva Indicación Predicha | Enfermedad ulcerosa péptica activa |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

La ranitidina bloquea los receptores H2 (gen *HRH2*) de las células parietales gástricas. Esto reduce la secreción de ácido gástrico, lo que permite que la úlcera cicatrice. El mecanismo coincide directamente con la indicación predicha. La ulceración péptica se produce cuando los factores agresivos (ácido, pepsina, AINE) superan las defensas de la mucosa, y la supresión ácida es un pilar del tratamiento.

Actualmente no se dispone de datos de mecanismo de acción en DrugBank. La información sobre el blanco proviene de la base de datos farmacológica incluida en el paquete de evidencia. Según ella, la ranitidina se usó en úlceras gástricas hasta su retirada en muchos países en 2020. Por ello, la predicción es consistente con su uso histórico y no representa una indicación realmente nueva.

La predicción tiene una limitación. El único ensayo clínico proporcionado no evalúa la ranitidina, por lo que el nivel L3 se apoya en la literatura. Esta incluye estudios de cicatrización y prevención de recaídas y ensayos comparativos, pero su fase y diseño no pudieron verificarse solo con los títulos.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Fase 4 | Completado | 320 | Influencia de estatinas e inhibidores de la bomba de protones sobre el efecto antiagregante del clopidogrel en pacientes con intervención coronaria percutánea. La ranitidina no es la intervención estudiada y el criterio de valoración no es la cicatrización de úlceras. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | Estudio clínico | Scand J Gastroenterol | Ranitidina 300 mg/día en 151 pacientes: cicatrización a 4 semanas del 91% (úlcera duodenal), 68% (prepilórica) y 81% (gástrica). Después se comparó el tratamiento de mantenimiento con placebo. |
| [3886404](https://pubmed.ncbi.nlm.nih.gov/3886404/) | 1985 | Ensayo doble ciego | Eur J Clin Pharmacol | Ranitidina + prazepam frente a ranitidina + placebo en úlcera duodenal activa: cicatrización a 28 días del 95.6% frente al 75%. |
| [3104657](https://pubmed.ncbi.nlm.nih.gov/3104657/) | 1986 | Ensayo comparativo | Klin Wochenschr | Rioprostil nocturno frente a ranitidina en la cicatrización de úlcera duodenal. |
| [18493408](https://pubmed.ncbi.nlm.nih.gov/18493408/) | 1996 | Estudio prospectivo | Diagn Ther Endosc | Evaluación endoscópica de la úlcera péptica durante el ayuno de Ramadán en 23 pacientes; 18 tomaron ranitidina 150 mg dos veces al día. |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Revisión | Drug Intell Clin Pharm | Monografía: ranitidina es 4 a 10 veces más potente que la cimetidina y de eficacia similar en úlcera duodenal activa. |
| [6317740](https://pubmed.ncbi.nlm.nih.gov/6317740/) | 1983 | Revisión | J Clin Gastroenterol | Comparación farmacodinámica y farmacocinética entre cimetidina y ranitidina. |
| [2905237](https://pubmed.ncbi.nlm.nih.gov/2905237/) | 1988 | Revisión | Drugs | Prostaglandinas, antagonistas H2 y enfermedad ulcerosa péptica. |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Revisión | Hepatogastroenterology | Papel de la secreción y supresión ácida en la patogenia y cicatrización de la úlcera péptica. |
| [8097411](https://pubmed.ncbi.nlm.nih.gov/8097411/) | 1993 | Revisión | Baillieres Clin Gastroenterol | Farmacología de la inhibición de la secreción ácida gástrica. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60298 | ALQUEN 150 mg comprimidos efervescentes | Comprimido efervescente | No especificada en los datos recibidos |
| 70953 | Ranitidina Aristo 300 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos recibidos |
| 63811 | Ranitidina Durban 300 mg comprimidos EFG | Comprimido recubierto | No especificada en los datos recibidos |
| 62597 | Ranitidina Pensa 300 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos recibidos |
| 57831 | Terposen 300 mg comprimidos recubiertos con película | Comprimido recubierto | No especificada en los datos recibidos |

El registro consta de 20 autorizaciones en total. También existe una forma de solución inyectable. El estado "Comercializado" procede del registro y debe confirmarse con AEMPS, dada la retirada de ranitidina en muchos países.

---

## Consideraciones de Seguridad

- **Impureza de NDMA**: en abril de 2020 la FDA retiró la autorización de comercialización de todos los productos con ranitidina, tras detectarse niveles excesivos de N-nitrosodimetilamina (NDMA), una sustancia hepatotóxica y carcinógena. Otras agencias reguladoras también retiraron sus autorizaciones. Además, se ha descrito desabastecimiento del fármaco (PMID 31848148).
- **Interacciones farmacológicas**: el paquete de evidencia no contiene interacciones fármaco-fármaco. La única entrada corresponde al blanco farmacológico (receptor H2).

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo de bloqueo H2 se corresponde directamente con la cicatrización de la úlcera. La literatura incluye estudios de cicatrización y ensayos comparativos, pero es antigua y su diseño no está verificado. El único ensayo proporcionado no evalúa la ranitidina. La preocupación por la impureza de NDMA y la disponibilidad del producto obligan a establecer salvaguardas antes de cualquier recomendación.

**Para avanzar se necesita:**
- Confirmar con AEMPS la disponibilidad actual y el estado de los lotes frente a la contaminación por NDMA.
- Obtener del prospecto de AEMPS las advertencias, contraindicaciones y la indicación aprobada.
- Verificar si los ensayos de fase 3 con esomeprazol (NCT00633412, NCT00633672 y NCT00401752, de la entrada "enfermedad ulcerosa péptica") incluyen realmente un brazo de ranitidina. Si es así, el nivel podría subir a L1.
- Comprobar el diseño y la fase de los estudios de la literatura, que no se pudieron verificar solo con los títulos.
- Completar los datos de mecanismo de acción desde DrugBank.
- Comparar con alternativas actuales (inhibidores de la bomba de protones), que en estudios comparativos mostraron mayor tasa de cicatrización (PMID 8180294).

Las demás indicaciones predichas (perforación de úlcera péptica, úlcera gastroyeyunal, reflujo duodenogástrico, obstrucción duodenal, gastroduodenitis, mastocitosis y alteración de la secreción de glucagón) tienen evidencia L3-L5 y no se recomiendan por ahora.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

