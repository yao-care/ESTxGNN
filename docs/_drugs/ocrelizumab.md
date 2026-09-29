---
layout: default
title: Ocrelizumab
parent: Solo predicción del modelo (L5)
nav_order: 388
evidence_level: L5
indication_count: 5
---

# Ocrelizumab
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

# Ocrelizumab: De Indicación Original No Registrada a Carcinoma de Mama HER2 Positivo

## Resumen en Una Frase

Ocrelizumab es un anticuerpo monoclonal anti-CD20 que depleciona linfocitos B. Los datos disponibles no incluyen su indicación original.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama HER2 positivo**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. La predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación aprobada de la autorización está vacío) |
| Nueva Indicación Predicha | Carcinoma de mama HER2 positivo |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, ocrelizumab es un anticuerpo anti-CD20 que depleciona los linfocitos B. Los tumores de mama no dependen de CD20, y no existe un mecanismo directo que relacione la depleción de células B con la enfermedad HER2 positiva.

Un posible vínculo, aunque especulativo, es que los linfocitos B infiltrantes del tumor podrían influir en el microambiente tumoral, ya sea a favor o en contra del tumor. No hay datos que confirmen esta hipótesis.

El puntaje TxGNN es muy alto (0.9989), pero es solo una predicción basada en el grafo de conocimiento. Además, podría ser un artefacto, ya que el fármaco no tiene indicaciones originales registradas en este paquete de evidencia. Las otras cuatro indicaciones predichas (subtipo *normal breast-like*, cáncer de mama con receptor de progesterona positivo, tumor de mama luminal A o B, y cáncer de mama con receptor de progesterona negativo) tienen puntajes entre 99.80% y 99.81%. Tampoco cuentan con vínculo mecanístico establecido ni con evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

Nota: para la indicación de rango 4 (tumor de mama luminal A o B) se recuperaron 19 artículos. Parecen coincidencias por la letra "B" (células B, vacunas contra hepatitis B, alelos HLA-B, bacterioclorofila b). Ninguno trata sobre ocrelizumab, la depleción de CD20 ni el cáncer de mama, por lo que no constituyen evidencia.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171231001 | OCREVUS 300 MG CONCENTRADO PARA SOLUCION PARA PERFUSION (Roche Registration GmbH) | Concentrado para solución para perfusión | No especificada en los datos disponibles |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene nivel de evidencia L5: solo puntaje del modelo, sin ensayos clínicos ni literatura relevante. Además, no hay un vínculo mecanístico plausible entre la depleción de células B anti-CD20 y el carcinoma de mama HER2 positivo.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS con advertencias y contraindicaciones, ya que sin esos datos no se puede pasar al cribado de seguridad.
- Confirmar la indicación original y el mecanismo de acción (por ejemplo, mediante DrugBank).
- Realizar una búsqueda dirigida de literatura sobre anti-CD20, linfocitos B y cáncer de mama, para reemplazar los resultados irrelevantes.
- Revisar si la predicción es un artefacto del grafo, dado que el fármaco no tiene indicaciones originales registradas.
- Obtener evidencia preclínica que respalde un rol de las células B en el microambiente tumoral mamario antes de reconsiderar la decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

