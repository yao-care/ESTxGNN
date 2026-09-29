---
layout: default
title: Carfilzomib
parent: Solo predicción del modelo (L5)
nav_order: 104
evidence_level: L5
indication_count: 5
---

# Carfilzomib
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

# Carfilzomib: De Mieloma Múltiple a CMM7 (Melanoma Cutáneo Maligno)

## Resumen en Una Frase

Carfilzomib es un inhibidor irreversible del proteasoma, conocido como antineoplásico para el mieloma múltiple. Esta indicación no consta en los textos de autorización recibidos, así que procede de su uso clínico general.
El modelo TxGNN predice que podría ser efectivo para **CMM7**, una entidad de melanoma cutáneo maligno, con un puntaje de 99.37 %.
Para esta indicación hay **0 ensayos clínicos** y **0 publicaciones**. Solo existen **5 publicaciones preclínicas o indirectas** sobre melanoma en general.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Mieloma múltiple (uso conocido del fármaco; los textos de indicación de las autorizaciones AEMPS recibidas están vacíos) |
| Nueva Indicación Predicha | CMM7 |
| Puntaje de Predicción TxGNN | 99.37 % |
| Nivel de Evidencia | L5 para CMM7 (L4 para melanoma en general, solo preclínica) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Hold |

Otras indicaciones predichas por el modelo, todas en el ámbito del melanoma:

| Rank | Indicación | Puntaje TxGNN | Nivel | Evidencia recuperada |
|------|------|------|------|------|
| 2 | Melanoma leptomeníngeo pediátrico | 99.30 % | L5 | Ninguna |
| 3 | Melanoma uveal de células epitelioides | 99.23 % | L5 | Ninguna |
| 4 | Melanoma vulvar | 99.19 % | L5 | Ninguna |
| 5 | Melanoma | 99.03 % | L4 | 5 publicaciones preclínicas o indirectas |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la farmacología general, carfilzomib inhibe de forma irreversible la subunidad beta-5 del proteasoma 20S. Esto puede acumular proteínas proapoptóticas, provocar estrés del retículo endoplásmico y suprimir la vía NF-κB. Su eficacia en mieloma múltiple está establecida.

Mecanísticamente, esa presión sobre la degradación de proteínas podría promover la apoptosis en células de melanoma. El único apoyo experimental directo es un estudio in vitro (PMID 33671902), que mostró mayor apoptosis en células murinas B16-F1 al combinar carfilzomib con bortezomib.

Este vínculo es **general y no está respaldado por datos específicos de CMM7**. Además, la evidencia disponible es preclínica y no hay datos de eficacia ni seguridad en humanos con melanoma. En las otras variantes hay dudas específicas:
- **Melanoma leptomeníngeo:** no se ha establecido la penetración de carfilzomib en el sistema nervioso central.
- **Melanoma uveal:** es biológicamente distinto del cutáneo, por lo que los hallazgos in vitro no son directamente extrapolables.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para CMM7 no hay literatura disponible. La única evidencia del paquete corresponde a la indicación predicha más amplia, **melanoma** (rank 5). Se muestra como contexto indirecto:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | Preclínico in vitro | Biology | Carfilzomib combinado con bortezomib aumenta la apoptosis (activación de caspasas 3, 8, 9 y 12) en células de melanoma B16-F1. |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclínico (mecanístico) | Matrix Biology | Bortezomib y carfilzomib activan NF-κB e inducen la expresión de heparanasa en células tumorales, lo que se asocia a un fenotipo más agresivo. |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Preclínico (mecanístico) | Molecular Cancer Research | El gen ZFAND2A (AIRAP) regula la supervivencia celular en melanoma humano mediante la E3-ligasa cIAP2. Relación con carfilzomib no confirmada. |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computacional (docking/dinámica) | J Biomol Struct Dyn | Reposicionamiento de fármacos clínicos frente a dianas de quinasas en varios cánceres, incluido melanoma. Relevancia directa no confirmada. |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Preclínico (mecanístico) | Leukemia | PROTACs dirigidos a proteínas BET son activos en modelos de mieloma múltiple. Relevancia para carfilzomib en melanoma no confirmada. |

## Información de Mercado en España

Hay 9 autorizaciones en total; se listan 5.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151060002IP | KYPROLIS 10 mg polvo para solución para perfusión | Polvo para solución inyectable | No especificada en los datos recibidos |
| 1151060003IP | KYPROLIS 30 mg polvo para solución para perfusión | Polvo para solución inyectable | No especificada en los datos recibidos |
| 1151060003 | KYPROLIS 30 mg polvo para solución para perfusión | Polvo para solución inyectable | No especificada en los datos recibidos |
| 1151060002IP1 | KYPROLIS 10 mg polvo para solución para perfusión | Polvo para solución inyectable | No especificada en los datos recibidos |
| 1151060002 | KYPROLIS 10 mg polvo para solución para perfusión | Polvo para solución inyectable | No especificada en los datos recibidos |

Titular: Amgen Europe B.V. Todas las presentaciones son de administración parenteral (perfusión).

## Citotoxicidad

Esta clasificación se basa en la farmacología general del fármaco, no en datos de toxicidad del paquete de evidencia.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor del proteasoma) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto. En general se describen trombocitopenia, anemia y neutropenia. |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, electrolitos; vigilancia cardiovascular y pulmonar según prospecto |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos/peligrosos de la institución |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se consultaron interacciones farmacológicas en la base de datos usada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de CMM7 se apoya solo en el puntaje del modelo (99.37 %), sin ensayos ni literatura (nivel L5). Para melanoma en general solo hay estudios preclínicos, sin datos humanos de eficacia ni seguridad. Tampoco se pudo revisar la seguridad del prospecto de AEMPS, lo que impide avanzar a cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un bloqueo actual para el cribado de seguridad.
- Confirmar el mecanismo de acción y las indicaciones originales desde DrugBank y los textos de autorización.
- Verificar la definición de CMM7 y buscar evidencia específica (modelos celulares y animales de melanoma cutáneo).
- Evaluar la viabilidad en las variantes especiales: penetración en el sistema nervioso central (leptomeníngeo) y diferencias biológicas (uveal).
- Si aparece evidencia preclínica sólida, plantear un estudio exploratorio en fase temprana antes de reconsiderar la decisión.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

