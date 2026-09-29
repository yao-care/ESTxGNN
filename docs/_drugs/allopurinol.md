---
layout: default
title: Allopurinol
parent: Evidencia moderada (L3-L4)
nav_order: 30
evidence_level: L4
indication_count: 10
---

# Allopurinol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Alopurinol: De Hiperuricemia y Gota a Porfiria Hepática

## Resumen en Una Frase

El alopurinol es un inhibidor de la xantina oxidasa que se usa para tratar la hiperuricemia y sus complicaciones, entre ellas la gota crónica.
El modelo TxGNN predice que podría ser efectivo para **porfiria hepática**,
pero hay **0 ensayos clínicos** y solo **2 publicaciones** indirectas (una hipótesis y un estudio preclínico en ratas), por lo que la evidencia es muy débil.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperuricemia y gota crónica (según la ficha farmacológica de la fuente de interacciones; los textos de indicación de las autorizaciones AEMPS vienen vacíos) |
| Nueva Indicación Predicha | Porfiria hepática |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

El alopurinol inhibe la xantina deshidrogenasa/oxidasa (gen *XDH*), la enzima que produce ácido úrico. No se dispone de una descripción detallada del mecanismo de acción en la fuente principal, así que este es el único mecanismo que se puede afirmar con los datos disponibles.

El vínculo con la porfiria hepática es solo indirecto. La literatura en roedores asocia el alopurinol con cambios en el recambio del hemo y del citocromo P450 hepáticos, lo que puede afectar a la actividad de la ALAS1 (5-aminolevulinato sintasa), la enzima limitante de la síntesis del hemo. Esa dirección podría ser **porfirinogénica y no terapéutica**. Es decir, el fármaco podría empeorar la enfermedad en lugar de mejorarla.

El puntaje de 99.95% proviene de la estructura del grafo de conocimiento y no está corroborado clínicamente. Ninguno de los dos artículos recuperados muestra beneficio en pacientes con porfiria.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hipótesis/Revisión | Medical Hypotheses | Propone actuar sobre la ALAS1 hepática, mediante triptófano o inhibiendo el uso del hemo por la triptófano 2,3-dioxigenasa, como terapia de las porfirias hepáticas agudas. No estudia el alopurinol como tratamiento. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Estudio preclínico en animales | Biochemical Pharmacology | En hígado de rata, la carbamazepina agota el hemo utilizado por la triptófano pirrolasa, un mecanismo por el que agrava las porfirias hepáticas. Es un estudio sobre exacerbación por fármacos, no sobre beneficio terapéutico. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 81288 | Alopurinol Bluefish 300 mg comprimidos EFG | Comprimido | Bluefish Pharmaceuticals AB |
| 63478 | Alopurinol Cinfa 300 mg comprimidos EFG | Comprimido | Laboratorios Cinfa S.A. |
| 69156 | Alopurinol Teva 100 mg comprimidos EFG | Comprimido | Teva Pharma S.L.U. |
| 84086 | Alopurinol Cinfamed 300 mg comprimidos EFG | Comprimido | Laboratorios Cinfa S.A. |
| 69155 | Alopurinol Teva 300 mg comprimidos EFG | Comprimido | Teva Pharma S.L.U. |

Se muestran 5 de las 20 autorizaciones. Los textos de indicación aprobada no están disponibles en los datos recibidos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como precaución específica para esta predicción: la evidencia indirecta sugiere que el alopurinol podría ser porfirinogénico, por lo que su seguridad en pacientes con porfiria debe revisarse antes de cualquier reposicionamiento.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la literatura es solo hipotética o preclínica. Además, el vínculo mecanístico podría ir en sentido contrario al terapéutico. El puntaje alto de TxGNN no basta por sí solo. Las otras 9 indicaciones predichas (por ejemplo, hipertensión portal familiar de inicio temprano o síndrome hepatopulmonar) están en nivel L5, solo con predicción del modelo.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias y contraindicaciones), ya que no se dispone de esos datos.
- Completar los datos del mecanismo de acción desde DrugBank.
- Hacer una revisión de seguridad del alopurinol en porfiria, incluida su posible acción porfirinogénica.
- Buscar estudios in vitro o en modelos animales que evalúen el efecto del alopurinol sobre la ALAS1 y el metabolismo del hemo.
- Reevaluar solo si aparece evidencia clínica o preclínica directa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

