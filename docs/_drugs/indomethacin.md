---
layout: default
title: Indomethacin
parent: Solo predicción del modelo (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Indomethacin
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

# Indometacina: De Afecciones Inflamatorias Reumáticas a Síndrome de Braquidactilia-Sindactilia

## Resumen en Una Frase

La indometacina es un antiinflamatorio no esteroideo (AINE) que se usa ampliamente en afecciones inflamatorias como la artritis reumatoide, la artrosis, la espondilitis anquilosante, la bursitis, la tendinitis y la artritis gotosa aguda.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de braquidactilia-sindactilia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Afecciones inflamatorias (artritis reumatoide, artrosis, espondilitis anquilosante, gota aguda). Fuente: datos de farmacología, porque las fichas de la AEMPS no traen texto de indicación |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La indometacina es un inhibidor no selectivo de la ciclooxigenasa (COX-1 y COX-2). Al bloquear la síntesis de prostaglandinas, reduce la inflamación, el dolor y la fiebre. Los datos de farmacología también la vinculan con otras dianas, como PPARγ, el receptor DP2 y el transportador de folato acoplado a protones. Actualmente no se dispone de una descripción detallada del mecanismo de acción en DrugBank.

**Esta predicción no tiene un vínculo mecanístico plausible.** El síndrome de braquidactilia-sindactilia es una malformación congénita del desarrollo de las extremidades, y la inhibición de COX no tiene relevancia conocida en su patogénesis. La indicación original es inflamatoria y la nueva es un trastorno genético del desarrollo, por lo que no comparten mecanismo.

El puntaje alto (99.97%) refleja solo una asociación en el grafo de conocimiento. Otras predicciones de la lista, como el síndrome WHIM o la braquiolmia, presentan la misma situación: puntajes altos sin ningún respaldo clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan 5 de las 10 autorizaciones. Las fichas de la AEMPS no incluyen texto de indicación aprobada, por lo que esa columna se omite.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 42582 | ARTRINOVO 25 MG CÁPSULAS DURAS | Cápsula dura | Laboratorios Llorens S.L. |
| 45894 | ALIVIOSIN 100 mg SUPOSITORIOS | Supositorio | Especialidades Farmacéuticas Centrum S.A. |
| 42846 | ARTRINOVO 100 MG SUPOSITORIOS | Supositorio | Laboratorios Llorens S.L. |
| 56980 | REUSIN 8 MG/ML SOLUCIÓN PARA PULVERIZACIÓN CUTÁNEA | Solución cutánea | Laboratorio Stada S.L. |
| 41723 | INACID 100 mg SUPOSITORIOS | Supositorio | H.A.C. Pharma |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los 5 registros de "interacciones" del Evidence Pack son dianas moleculares (COX-1, COX-2, PPARγ, DP2 y SLC46A1), no interacciones con otros fármacos. No hay datos de interacciones farmacológicas clínicas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura, y no existe un vínculo plausible entre la inhibición de COX y una malformación congénita de las extremidades.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones). Este dato es bloqueante para el cribado de seguridad.
- Completar el mecanismo de acción desde DrugBank.
- Una hipótesis biológica que conecte la vía de las prostaglandinas con esta enfermedad, antes de cualquier estudio.
- Si se busca una línea con algo de sustento, la **artritis idiopática juvenil** (posición 8, TxGNN 99.84%, nivel L3) tiene literatura: un ensayo doble ciego de 1978 comparó ketoprofeno e indometacina en 30 niños, y hay revisiones farmacológicas. Es un uso sintomático de AINE ya establecido y puede no ser un reposicionamiento genuino. Merece evaluarse como pregunta de investigación aparte, una vez resuelta la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

