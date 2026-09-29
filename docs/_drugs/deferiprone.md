---
layout: default
title: Deferiprone
parent: Evidencia moderada (L3-L4)
nav_order: 163
evidence_level: L4
indication_count: 9
---

# Deferiprone
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **9** 
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

# Deferiprona: De Indicación Original No Registrada a Porfiria Hepática

## Resumen en Una Frase

La deferiprona es un quelante de hierro comercializado en España como Ferriprox (comprimidos y solución oral). El registro disponible no incluye el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **porfiria hepática**, pero solo la respaldan **2 publicaciones preclínicas en ratón** y **ningún ensayo clínico**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el registro (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Porfiria hepática |
| Puntaje de Predicción TxGNN | 99.20% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, la deferiprona es un quelante de hierro de administración oral. Mecanísticamente podría ser aplicable a la porfiria hepática porque el hierro interviene en la acumulación de porfirinas.

La hipótesis es que quelar el hierro reduciría la acumulación de porfirinas dependiente del hierro y el daño oxidativo asociado. Dos estudios en ratón respaldan esta idea: uno en un modelo de porfiria eritropoyética congénita y otro en un modelo de uroporfiria, similar a la porfiria cutánea tardía. No hay datos en humanos.

No se pudo comparar con la indicación original porque el registro no la incluye. Antes de clasificar este caso como reposicionamiento, conviene verificar en la ficha técnica si la deferiprona ya tiene un uso autorizado relacionado con la sobrecarga de hierro.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Preclínico (modelo murino) | Blood | Según el título, la quelación de hierro corrige la anemia hemolítica y la fotosensibilidad cutánea en un modelo de porfiria eritropoyética congénita. El extracto disponible no confirma que el quelante usado fuera deferiprona. |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Preclínico (modelo murino) | Hepatology | Compara la quelación con deferiprona (L1) frente a dietas deficientes en hierro sobre la acumulación de uroporfirina hepática en ratones Hfe-/- alimentados con ALA (modelo de porfiria cutánea tardía). El extracto disponible está truncado y no incluye los resultados. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 99108001 | FERRIPROX 500 mg comprimidos con cubierta pelicular | Comprimido recubierto | No consta en el registro |
| 99108003 | FERRIPROX 100 mg/ml solución oral | Solución oral | No consta en el registro |

Ambas autorizaciones pertenecen a Chiesi Farmaceutici S.P.A.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo un puntaje del grafo de conocimiento, respaldado por dos estudios preclínicos en ratón, sin datos en humanos y sin información de seguridad disponible. Con este nivel de evidencia (L4) no se justifica avanzar todavía.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de AEMPS (advertencias y contraindicaciones), un requisito bloqueante antes de cualquier evaluación de seguridad.
- Confirmar la indicación autorizada en la ficha técnica y obtener el mecanismo de acción desde DrugBank.
- Buscar estudios en humanos (series de casos o ensayos) de deferiprona en porfirias.
- Completar el texto de estudio de los resultados del PMID 17854053 y confirmar qué quelante se usó en el PMID 32678895.
- Considerar la talasemia beta (L4), que tiene el mecanismo más directo (quelación del hierro transfusional) entre las demás predicciones. Las otras siete predicciones (L5) tienen puntajes similares pero ninguna evidencia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

