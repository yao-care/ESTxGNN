---
layout: default
title: Tapentadol
parent: Solo predicción del modelo (L5)
nav_order: 511
evidence_level: L5
indication_count: 3
---

# Tapentadol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Tapentadol: De Analgésico Opioide a Trastorno de Migraña

## Resumen en Una Frase

Tapentadol es un analgésico comercializado en España en varias formas de liberación inmediata y prolongada. El texto de indicación aprobada no figura en los datos recibidos.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero actualmente hay **0 ensayos clínicos** y **2 publicaciones** que no estudian tapentadol, por lo que la predicción carece de respaldo real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L5 (el paquete de evidencia indica L4, pero la literatura hallada no estudia tapentadol) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según el análisis del paquete de evidencia, tapentadol combina agonismo del receptor opioide mu con inhibición de la recaptación de noradrenalina. En teoría esto podría modular las vías centrales del dolor, y ese es el único vínculo mecanístico que se puede plantear.

Este vínculo es débil. El puntaje de 0.997 es una predicción de un grafo de conocimiento, no evidencia clínica. Además, los opioides se desaconsejan en general en la migraña por el riesgo de cefalea por abuso de medicación, cronificación y eficacia limitada. Nada en los datos respalda a tapentadol específicamente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27096438](https://pubmed.ncbi.nlm.nih.gov/27096438/) | 2016 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Sumatriptán más naproxeno en crisis agudas de migraña en adultos. No incluye tapentadol. |
| [27096578](https://pubmed.ncbi.nlm.nih.gov/27096578/) | 2016 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Dosis única de dipirona (metamizol) en dolor postoperatorio agudo. Menciona la migraña solo como uso del fármaco. No incluye tapentadol. |

Ninguna de las dos publicaciones evalúa tapentadol, así que no aportan evidencia directa para esta indicación.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 73613 | YANTIL 100 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 88378 | TAPENTADOL TEVA 100 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada |
| 88377 | TAPENTADOL TEVA 50 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada |
| 88288 | TAPENTADOL RETARD STADA 100 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada |
| 73243 | PALEXIA RETARD 50 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada |

Se muestran 5 de las 20 autorizaciones. También existe una forma de solución oral (vía oral).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo, sin ensayos clínicos ni literatura sobre tapentadol en migraña. Las guías generales desaconsejan los opioides en esta enfermedad. Las otras dos predicciones (migraña con aura de tronco encefálico y susceptibilidad genética a migraña con o sin aura) tienen evidencia L5 y tampoco justifican avanzar. La tercera es un fenotipo de susceptibilidad genética, no una condición tratable, y su literatura trata sobre epilepsia.

**Para avanzar se necesita:**
- Obtener del prospecto de la AEMPS las advertencias y contraindicaciones, y las indicaciones aprobadas. Esta falta es un bloqueo para pasar al cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar estudios preclínicos o clínicos que evalúen específicamente tapentadol en migraña.
- Evaluar el riesgo de cefalea por abuso de medicación frente a las alternativas ya establecidas.

*Este informe es solo de referencia para la investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

