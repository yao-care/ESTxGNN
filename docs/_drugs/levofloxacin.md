---
layout: default
title: Levofloxacin
parent: Solo predicción del modelo (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
---

# Levofloxacin
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

# Levofloxacino: De Antibacteriano Sistémico a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Levofloxacino es un antibiótico fluoroquinolónico, comercializado en España en comprimidos y solución para perfusión.
El modelo TxGNN predice que podría ser efectivo para la **queratoconjuntivitis epitelial punteada**,
pero actualmente hay **0 ensayos clínicos** y **1 publicación** relacionada, y esa publicación no contiene datos de eficacia del fármaco.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible: los textos de indicación de las autorizaciones AEMPS están vacíos |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99,92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, levofloxacino es una fluoroquinolona que inhibe la ADN girasa y la topoisomerasa IV bacterianas, y su eficacia como antibacteriano está bien establecida. Mecanísticamente, solo podría ser aplicable a esta nueva indicación si existiera un componente bacteriano.

La única publicación asociada es un informe de brote de queratoconjuntivitis microsporidiana por contaminación del agua de piscinas en Taiwán. No contiene datos de eficacia de levofloxacino. Los microsporidios son eucariotas emparentados con los hongos, y las fluoroquinolonas no tienen actividad establecida contra ellos. Levofloxacino solo podría ayudar previniendo o tratando una sobreinfección bacteriana secundaria, lo cual no constituye una señal de reposicionamiento.

Por tanto, el puntaje alto de TxGNN refleja una predicción basada en el grafo de conocimiento, sin respaldo clínico que la sostenga.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Informe de brote | Am J Ophthalmol | Brote de queratoconjuntivitis microsporidiana asociado a contaminación del agua en piscinas de Taiwán. No incluye datos de levofloxacino. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 68868 | Levofloxacino Serraclinics 5 mg/ml solución para perfusión | Solución para perfusión |
| 74832 | Levofloxacino Aurobindo 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 72160 | Levofloxacino Kabi 5 mg/ml solución para perfusión EFG | Solución para perfusión |
| 69697 | Levofloxacino Normon 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 74700 | Levofloxacino Accord 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

Se muestran 5 de las 20 autorizaciones. Los textos de indicación aprobada no están disponibles en los datos recibidos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni datos de eficacia de levofloxacino en queratoconjuntivitis epitelial punteada (nivel L5). El mecanismo no es plausible frente a un agente microsporidiano.

**Para avanzar se necesita:**
- Estudios que evalúen levofloxacino en esta enfermedad, o una justificación mecanística de su uso, por ejemplo un componente bacteriano.
- Datos de mecanismo de acción desde DrugBank.
- Advertencias y contraindicaciones del prospecto de AEMPS, que actualmente bloquean el cribado de seguridad.
- Como referencia, otras indicaciones predichas del mismo fármaco tienen más respaldo que esta: la profilaxis de infecciones en mieloma (gammapatía monoclonal, L1, con el ECA TEAMM) y la peste septicémica (L4, evidencia preclínica). Ambas merecen evaluación por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

