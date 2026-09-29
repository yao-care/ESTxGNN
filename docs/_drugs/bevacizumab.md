---
layout: default
title: Bevacizumab
parent: Solo predicción del modelo (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: De Cáncer (indicaciones autorizadas no detalladas) a Neoplasia de Epiglotis

## Resumen en Una Frase

Bevacizumab es un anticuerpo monoclonal que actúa sobre el factor de crecimiento endotelial vascular (VEGF) y se utiliza en oncología. En los datos recibidos no figura el texto de sus indicaciones autorizadas.
El modelo TxGNN predice que podría ser efectivo para **neoplasia de epiglotis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es, por tanto, una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible: los textos de indicación de las autorizaciones están vacíos |
| Nueva Indicación Predicha | Neoplasia de epiglotis |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, bevacizumab es un anticuerpo dirigido contra el VEGF, que participa en la formación de nuevos vasos sanguíneos (angiogénesis) de los tumores. Sus estudios en otros cánceres aparecen en los datos recibidos, y mecanísticamente podría ser aplicable a la neoplasia de epiglotis.

La única base de la hipótesis es que la angiogénesis dependiente de VEGF es plausible en los tumores de cabeza y cuello. No se recuperó ningún ensayo ni publicación para esta indicación. La relación con la indicación original tampoco está evaluada (estado "pendiente").

Con una puntuación TxGNN muy alta (99.90%), pero sin ningún estudio real que la respalde, esta predicción debe considerarse una hipótesis inicial y no una recomendación terapéutica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 13 autorizaciones. El texto de la indicación aprobada no está disponible en los datos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 04300002IP | Avastin 25 mg/ml | Concentrado para solución para perfusión | Roche Registration GmbH |
| 1201454001 | Aybintio 25 mg/ml | Concentrado para solución para perfusión | Samsung Bioepis NL B.V. |
| 04300001 | Avastin 25 mg/ml | Concentrado para solución para perfusión | Roche Registration GmbH |
| 1181344002 | Zirabev 25 mg/ml | Concentrado para solución para perfusión | Pfizer Europe MA EEIG |
| 1201509001 | Alymsys 25 mg/ml | Concentrado para solución para perfusión | Mabxience Research S.L. |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-VEGF); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Presión arterial (un ensayo del paquete estudia la hipertensión inducida por bevacizumab), hemograma, función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia de epiglotis es de nivel L5: solo hay puntuación del modelo, sin ensayos ni publicaciones que la respalden. Tampoco se dispone de datos de mecanismo de acción ni de seguridad del prospecto, por lo que no se puede avanzar a un cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío bloqueante.
- Obtener el mecanismo de acción desde DrugBank.
- Obtener los textos de indicación autorizada de las licencias para definir la indicación original.
- Hacer una búsqueda dirigida de ensayos y literatura sobre bevacizumab en neoplasias de epiglotis o de laringe y cabeza y cuello.
- Como referencia, entre las otras predicciones del paquete, "neoplasia quística" alcanza el nivel L2 por evidencia en cáncer de ovario. La correspondencia con la enfermedad es indirecta, así que su interpretación es limitada.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

