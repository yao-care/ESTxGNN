---
layout: default
title: Ciclesonide
parent: Solo predicción del modelo (L5)
nav_order: 178
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Ciclesonide: nueva indicación predicha, Eccema atópico (nivel de evidencia L5). Indicación original: Asma (según el grafo de conocimiento"
monitor_inn: "Ciclesonide"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis"]
---

# Ciclesonide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Ciclesonida: De Asma a Eccema Atópico

## Resumen en Una Frase

Ciclesonida es un corticosteroide inhalado (profármaco) utilizado originalmente para el tratamiento del asma y de la rinitis alérgica.
El modelo TxGNN predice que podría ser efectivo para **eccema atópico**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Eccema atópico |
| Puntaje de Predicción TxGNN | 99,96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según la información conocida, ciclesonida es un glucocorticoide inhalado que se administra como profármaco y es activado por esterasas a desisobutiril-ciclesonida (des-ciclesonida). Esta forma activa se une al receptor de glucocorticoides (NR3C1) con una afinidad mucho mayor que el fármaco original (IC50 de 1,75 nM frente a 210 nM).

El asma alérgica y la rinitis alérgica comparten con el eccema atópico un trasfondo inflamatorio de tipo Th2. Como la acción antiinflamatoria mediada por el receptor de glucocorticoides es relevante en la inflamación cutánea atópica, existe una justificación mecanística plausible.

Sin embargo, esta justificación es de clase (los corticosteroides tópicos están establecidos en dermatitis atópica) y no constituye evidencia específica de ciclesonida. La vía de administración (tópica o sistémica) y la seguridad de la exposición cutánea no están caracterizadas para este fármaco. Otras entradas predichas con puntajes altos incluyen la dermatitis atópica (entrada sinónima, 99,73%), la sensibilización al metacrilato de 2-hidroxietilo (99,76%), la bronquitis (99,70%) y la dermatitis de contacto (99,25%); todas ellas también carecen de ensayos clínicos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para eccema atópico.

Como referencia de indicaciones alternativas predichas, se identificó la siguiente literatura indirecta:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guía/Revisión | Basic & Clinical Pharmacology & Toxicology | Guía finlandesa sobre diagnóstico y farmacoterapia de la EPOC estable; contexto indirecto del uso de corticosteroides inhalados (bronquitis) |
| [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) | 2012 | Reporte de caso | Contact Dermatitis | Dermatitis alérgica sistémica por budesonida inhalada con reactividad cruzada en pruebas epicutáneas con ciclesonida (señal de seguridad) |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 70372 | ALVESCO 160 microgramos/inhalación (Covis Pharma Europe B.V.) | Solución para inhalación en envase a presión | No disponible |
| 05-0019 | ALVESCO 160 microgramos/inhalación (Takeda GmbH) | Solución para inhalación en envase a presión | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto del prospecto): queratitis por virus del herpes simple, insuficiencia suprarrenal, enfermedad de Addison, osteoporosis (incluida la posmenopáusica), infecciones fúngicas, dermatofitosis, hipertensión ocular, glaucoma e infecciones parasitarias.
- **Interacciones farmacológicas**: solo se identificó su acción farmacológica sobre el receptor de glucocorticoides (diana principal); no hay interacciones con otros fármacos con nivel de gravedad definido.
- **Señal de sensibilización**: un reporte de caso describe reactividad cruzada entre budesonida y ciclesonida en pruebas epicutáneas, lo que sugiere un posible riesgo de alergia de contacto dentro de la clase.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción del modelo es muy alta (99,96%), pero no existe ningún ensayo clínico ni publicación que la respalde (nivel L5). Además, no se ha definido la vía de administración necesaria, y la única señal indirecta de la literatura sobre piel apunta a un riesgo de sensibilización.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS para completar advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Evaluar la compatibilidad de la vía de administración (la presentación comercializada es solo inhalatoria; el eccema requeriría formulación tópica o sistémica).
- Realizar una búsqueda sistemática de literatura preclínica y clínica sobre ciclesonida en dermatitis atópica.
- Caracterizar la seguridad de la exposición cutánea y el riesgo de sensibilización por reactividad cruzada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

