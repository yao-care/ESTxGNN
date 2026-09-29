---
layout: default
title: Pentamidine
parent: Solo predicción del modelo (L5)
nav_order: 416
evidence_level: L5
indication_count: 5
---

# Pentamidine
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

# Pentamidina: De Antiprotozoario a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

La pentamidina es un antiprotozoario inyectable comercializado en España como PENTACARINAT 300 mg. El texto de su indicación autorizada no figura en los datos disponibles.
El modelo TxGNN predice que podría ser efectiva para la **queratoconjuntivitis epitelial punteada**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los datos de la AEMPS (fármaco antiprotozoario) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99,73% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la pentamidina es un antiprotozoario con actividad antiparasitaria, y se le atribuye la unión al surco menor del ADN. Mecanísticamente, esto solo tendría sentido si la queratoconjuntivitis fuera de origen infeccioso (por ejemplo, protozoario). Los datos no especifican la etiología.

El puntaje de 99,73% proviene de la proximidad en el grafo de conocimiento y no de evidencia clínica. No hay ensayos ni literatura que lo sostengan. Tampoco existe una formulación oftálmica establecida. La toxicidad sistémica conocida de la pentamidina (nefrotoxicidad, alteraciones de la glucemia, prolongación del QT) refuerza la cautela.

Las otras cuatro predicciones del modelo son queratopatía neurotrófica, queratitis por exposición, "enfermedad animal no humana" y analbuminemia congénita. Todas están en nivel L5 y sin respaldo mecanístico. "Enfermedad animal no humana" es una categoría inespecífica de la ontología, probablemente un artefacto del grafo, y debe excluirse de cualquier priorización clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59621 | PENTACARINAT 300 MG POLVO PARA SOLUCION INYECTABLE | Polvo para suspensión inyectable | No especificada en los datos disponibles |

Titular: The Simple Pharma Company Limited.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos, sin literatura y sin mecanismo plausible documentado. Además, el fármaco solo existe en forma inyectable sistémica, con un perfil de toxicidad relevante.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicación autorizada).
- Obtener datos del mecanismo de acción desde DrugBank.
- Definir la etiología concreta de la queratoconjuntivitis (¿infecciosa/protozoaria?) y buscar evidencia preclínica.
- Evaluar la viabilidad de una vía de administración oftálmica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

