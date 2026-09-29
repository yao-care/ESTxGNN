---
layout: default
title: Doxazosin
parent: Evidencia moderada (L3-L4)
nav_order: 183
evidence_level: L4
indication_count: 2
---

# Doxazosin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Doxazosina: De Hipertensión e Hiperplasia Prostática Benigna a Migraña

## Resumen en Una Frase

La doxazosina es un bloqueante alfa-1 adrenérgico, utilizado originalmente para tratar la hipertensión y mejorar la micción en la hiperplasia prostática benigna.
El modelo TxGNN predice que podría ser efectiva para **migraña**,
pero actualmente hay **0 ensayos clínicos** y solo **1 publicación** (una serie pequeña de 10 pacientes de 1997) que respalda esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión e hiperplasia prostática benigna (según datos farmacológicos; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Migraña (*migraine disorder*) |
| Puntaje de Predicción TxGNN | 99.20% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La doxazosina es un antagonista selectivo de los receptores alfa-1 adrenérgicos. Los datos farmacológicos disponibles la vinculan con los subtipos α1A, α1B y α1D (genes ADRA1A, ADRA1B y ADRA1D). El campo de mecanismo de acción de la fuente original no está disponible, por lo que esta descripción se basa en la clase del fármaco y no en una ficha de mecanismo confirmada.

Su uso original (hipertensión e hiperplasia prostática) se apoya en la relajación del músculo liso vascular y prostático mediante el bloqueo alfa-1. Para la migraña, la hipótesis es que este bloqueo podría modular el tono cerebrovascular y simpático. Es el mismo razonamiento que planteó la revisión de 1997 sobre bloqueantes alfa-1 en la profilaxis de la migraña. La relación con la indicación original es indirecta: comparten el blanco farmacológico, pero no la fisiopatología.

El puntaje de 99.20% es una predicción computacional y no constituye evidencia clínica. También se predijo la *migraña con aura del tronco encefálico* (99.19%), pero no tiene ensayos ni literatura propios. Su puntaje probablemente refleja la cercanía en el grafo con la migraña general, y su fisiopatología podría ser distinta, por lo que la hipótesis no está verificada para ese subtipo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Revisión / serie de casos | Headache | Diez pacientes con migraña recibieron terazosina o doxazosina. Todos menos uno mostraron menor frecuencia o gravedad de las crisis, pero 5 abandonaron el tratamiento por efectos secundarios. No se notificaron reacciones adversas graves. |

## Información de Mercado en España

Hay 20 autorizaciones en total. Estas son las 5 principales. Los textos de indicación aprobada no figuran en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 75010 | Doxazosina Neo Viatris 4 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | Viatris Limited |
| 70679 | Doxazosina Neo Aurovitas Spain 4 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | Aurovitas Spain, S.A.U. |
| 62930 | Progandol Neo 8 mg comprimidos de liberación modificada | Comprimido de liberación modificada | Almirall S.A. |
| 58861 | Progandol 4 mg comprimidos | Comprimido | Almirall S.A. |
| 3400937625784 | Carduran Neo 8 mg comprimidos de liberación modificada | Comprimido de liberación prolongada | Viatris Up |

## Consideraciones de Seguridad

- **Tolerabilidad en migraña**: en la única serie disponible, 5 de 10 pacientes suspendieron el fármaco por efectos secundarios, aunque no hubo reacciones graves.

Para advertencias, contraindicaciones e interacciones, consultar el prospecto. La ficha de AEMPS aún no se ha incorporado a este análisis.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un puntaje computacional y en una serie pequeña, sin control, de 1997. No hay ensayos clínicos, y la mitad de los pacientes de esa serie abandonó el tratamiento por efectos secundarios.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un vacío que bloquea el cribado de seguridad
- Confirmar el mecanismo de acción en DrugBank
- Revisar la literatura más reciente sobre bloqueantes alfa-1 en migraña
- Si se continúa, diseñar un estudio exploratorio controlado con seguimiento de hipotensión y tolerabilidad
- Verificar por separado la hipótesis para el subtipo con aura del tronco encefálico, que hoy carece de evidencia propia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

