---
layout: default
title: Piroxicam
parent: Solo predicción del modelo (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam: De AINE (indicación autorizada no especificada) a Síndrome de displasia rizomélica con microftalmia colobomatosa

## Resumen en Una Frase

Piroxicam es un antiinflamatorio no esteroideo (AINE) comercializado en España en cápsulas, geles y cremas. Los datos de autorización disponibles no detallan su indicación original.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de displasia rizomélica con microftalmia colobomatosa**, una malformación congénita rara.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción: es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los datos de autorización disponibles (los textos de indicación están vacíos) |
| Nueva Indicación Predicha | Síndrome de displasia rizomélica con microftalmia colobomatosa |
| Puntaje de Predicción TxGNN | 99,996% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Piroxicam es un inhibidor no selectivo de la ciclooxigenasa (COX-1 y COX-2). Reduce la síntesis de prostaglandinas y, con ello, la inflamación y el dolor. Los datos de DrugBank no traen una descripción detallada del mecanismo de acción, pero esta es la acción conocida de los AINE.

**En este caso no se identifica un vínculo mecanístico plausible.** Se trata de un síndrome de desarrollo raro sin un componente inflamatorio claro. La inhibición de COX no debería modificar un defecto del desarrollo esquelético u ocular.

El puntaje TxGNN es muy alto (~0,99996), pero lo más probable es que refleje la cercanía en el grafo de conocimiento con fenotipos musculoesqueléticos y no una justificación biológica. Debe leerse solo como una hipótesis del modelo, sin respaldo clínico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Los registros de autorización disponibles no incluyen el texto de la indicación aprobada, por lo que esa columna se omite.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 58708 | SASULEN 5 MG/G GEL | Gel | Laboratorios Veris S.A. |
| 55382 | FELDENE 10 MG CÁPSULAS DURAS | Cápsula dura | Pfizer S.L. |
| 58986 | SALVACAM 5 mg/g GEL | Gel | Laboratorios Salvat S.A. |
| 55806 | FELDENE 20 MG CÁPSULAS DURAS | Cápsula dura | Pfizer S.L. |
| 58198 | IMPRONTAL 5 mg/g CREMA | Crema | Meda Pharma S.L. |

Hay 9 autorizaciones en total. También existen otras formas, como solución inyectable, liofilizado oral y comprimido dispersable.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos, publicaciones ni un mecanismo biológico plausible (nivel L5). El puntaje alto del modelo no basta por sí solo para avanzar.

**Nota sobre otras indicaciones predichas:** entre las 10 indicaciones predichas, la única con literatura específica de piroxicam es la **artritis idiopática juvenil (AIJ)**, con nivel L3 y recomendación "Research Question". Incluye dos estudios pediátricos antiguos: [PMID 2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) (1987, piroxicam vs naproxeno, 26 pacientes) y [PMID 3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) (1986, estudio multicéntrico doble ciego cruzado, 47 niños). También hay metaanálisis en red de AINE en AIJ de 2021 y 2024, aunque no está verificado que incluyan piroxicam. Esta indicación es una línea de investigación más razonable que la de mayor puntaje. Podría subir a L2 si se confirma que el estudio de 1986 es un ensayo aleatorizado. Antes conviene revisar la seguridad pediátrica (toxicidad gastrointestinal y renal, vida media larga de piroxicam).

**Para avanzar se necesita:**
- Prospecto de AEMPS con advertencias y contraindicaciones (falta bloqueante para el cribado de seguridad)
- Datos del mecanismo de acción desde DrugBank
- Texto de las indicaciones autorizadas en España
- Una hipótesis biológica que conecte la inhibición de COX con la enfermedad predicha, antes de invertir más esfuerzo
- Verificación del diseño y las fases de los estudios pediátricos, y si los metaanálisis incluyen piroxicam, si se prioriza la AIJ
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

