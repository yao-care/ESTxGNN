---
layout: default
title: Glimepiride
parent: Solo predicción del modelo (L5)
nav_order: 259
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Glimepirida: De Diabetes Tipo 2 a Síndrome de Extremidad Rígida Focal

## Resumen en Una Frase

Glimepirida es una sulfonilurea que se usa para tratar la diabetes mellitus tipo 2. La indicación original procede del conocimiento general del fármaco, porque los datos de AEMPS no incluyen el texto de indicación.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de extremidad rígida focal**, con un puntaje muy alto (99.75%).
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Síndrome de extremidad rígida focal |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, glimepirida bloquea los canales de potasio sensibles a ATP (K-ATP) de las células beta pancreáticas y así estimula la liberación de insulina. Su eficacia en la diabetes tipo 2 es conocida.

Sin embargo, no existe un vínculo mecanístico establecido entre este bloqueo y el síndrome de extremidad rígida focal. Este síndrome pertenece al espectro del síndrome de la persona rígida, que tiene un componente autoinmune (anti-GAD65) y una alteración de la inhibición neuronal GABAérgica. Glimepirida no actúa sobre ninguno de estos procesos.

La predicción probablemente se explica por la cercanía entre los nodos de diabetes y de autoinmunidad anti-GAD65 en el grafo de conocimiento. El puntaje alto (0.997) es solo una predicción del modelo y no equivale a evidencia clínica.

El mismo análisis dio otras 8 indicaciones predichas: síndrome de la persona rígida clásico, opsismodisplasia, síndrome de disfunción sensible a tiamina, varias lipodistrofias localizadas y agenesia pancreática. Todas son de nivel L5 y ninguna tiene ensayos clínicos. Para la agenesia pancreática solo hay un artículo sobre imagen de insulinomas, que no respalda un uso terapéutico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 76838 | GLIMEPIRIDA AUROBINDO 2 MG COMPRIMIDOS EFG | Comprimido | Laboratorios Aurobindo S.L.U. |
| 76841 | GLIMEPIRIDA AUROBINDO 4 MG COMPRIMIDOS EFG | Comprimido | Laboratorios Aurobindo S.L.U. |
| 67533 | GLIMEPIRIDA NORMON 2 mg COMPRIMIDOS EFG | Comprimido | Laboratorios Normon S.A. |
| 67669 | GLIMEPIRIDA KERN PHARMA 2 mg COMPRIMIDOS EFG | Comprimido | Kern Pharma S.L. |
| 67670 | GLIMEPIRIDA KERN PHARMA 4 mg COMPRIMIDOS EFG | Comprimido | Kern Pharma S.L. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura que respalden el uso de glimepirida en el síndrome de extremidad rígida focal. Tampoco existe un vínculo mecanístico plausible: la predicción parece un artefacto del grafo de conocimiento, ligado a la asociación entre diabetes y autoinmunidad anti-GAD65.

**Para avanzar se necesita:**
- Prospecto de AEMPS con advertencias y contraindicaciones, para completar el cribado de seguridad
- Datos del mecanismo de acción (MOA) desde DrugBank
- Una búsqueda dirigida de literatura preclínica o clínica sobre sulfonilureas y síndromes de rigidez
- Una hipótesis mecanística explícita antes de considerar cualquier estudio
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

