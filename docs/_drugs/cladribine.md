---
layout: default
title: Cladribine
parent: Solo predicción del modelo (L5)
nav_order: 130
evidence_level: L5
indication_count: 7
---

# Cladribine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Cladribina: Predicción hacia Rabdomiosarcoma Embrionario Parameníngeo

## Resumen en Una Frase

La cladribina es un análogo de nucleósido de purina comercializado en España en varias presentaciones (Leustatin, Litak y Mavenclad). El paquete de evidencia no registra el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **rabdomiosarcoma embrionario parameníngeo**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de autorización disponibles |
| Nueva Indicación Predicha | Rabdomiosarcoma embrionario parameníngeo |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos de mecanismo de acción de DrugBank no están disponibles. Según la información del análisis, la cladribina es un análogo de nucleósido de purina. La desoxicitidina cinasa lo activa y causa roturas de cadena de ADN, sobre todo en células linfoides.

**No se identifica un vínculo mecanístico establecido con la biología del rabdomiosarcoma**, que es un tumor sólido mesenquimal. La puntuación alta (0.998) probablemente refleja un efecto de vecindad en la ontología. Las 6 primeras predicciones pertenecen al mismo grupo de rabdomiosarcoma: subtipos vaginal botrioide, extrahepático de vías biliares, prostático, y el nodo padre "rabdomiosarcoma". Sus puntuaciones son casi idénticas (0.9974–0.9977), lo que apunta a propagación compartida en el grafo y no a señales independientes. Por eso no deben contarse como evidencia separada.

La séptima predicción, sarcoma hepático (99.70%), tiene una sola publicación indirecta. Es un caso clínico de 2004 (PMID 15241520) sobre cladribina en mastocitosis sistémica indolente, una neoplasia hematológica y no un sarcoma. Tampoco respalda directamente esa indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

El texto de indicación aprobada está vacío en las 5 autorizaciones registradas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 61380 | LEUSTATIN 1 MG/ML SOLUCION PARA PERFUSION | Solución inyectable | Atnahs Pharma Netherlands Bv. |
| 04275001 | LITAK 2 mg/ml SOLUCION INYECTABLE | Solución inyectable | Lipomed Gmbh |
| 90544 | LEUSTATIN 2 MG/ML SOLUCION INYECTABLE | Solución inyectable | Atnahs Pharma Netherlands Bv. |
| 1171212001 | MAVENCLAD 10 MG COMPRIMIDOS | Comprimido | Merck Europe B.V. |
| 04275002 | LITAK 2 mg/ml SOLUCION INYECTABLE | Solución inyectable | Lipomed Gmbh |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (análogo de nucleósido de purina) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto; por su naturaleza citotóxica, aplicar las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5): no hay ensayos ni literatura para rabdomiosarcoma, y no se identifica un mecanismo plausible en este tumor sólido mesenquimal. Las predicciones del grupo rabdomiosarcoma no son independientes entre sí. La información de seguridad tampoco está disponible.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), que actualmente bloquea el cribado de seguridad.
- Consultar los datos de mecanismo de acción en DrugBank.
- Realizar estudios preclínicos de actividad de la cladribina en líneas celulares de rabdomiosarcoma, incluida la expresión de desoxicitidina cinasa.
- Confirmar la indicación original aprobada a partir del prospecto para evaluar la relación con la nueva indicación.
- Revisar la evidencia de otras neoplasias sólidas con respaldo real, en lugar de priorizar este grupo de subtipos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

