---
layout: default
title: Fedratinib
parent: Solo predicción del modelo (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "FEDRATINIB"
predicted_indications: ["benign PEComa", "lymphangiomyoma", "uterine corpus perivascular epithelioid cell tumor", "dermatofibrosarcoma protuberans", "rhabdoid tumor", "familial rhabdoid tumor", "autosomal recessive familial Mediterranean fever", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "hemophagocytic syndrome associated with an infection", "lymphangioleiomyomatosis"]
description: "Fedratinib: nueva indicación predicha, PEComa benigno (benign PEComa) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Fedratinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Fedratinib: PEComa benigno (benign PEComa)
{: .text-alpha }

## Resumen en Una Frase

Fedratinib es un inhibidor selectivo de JAK2 (que también inhibe FLT3 y BRD4), utilizado originalmente para el tratamiento de la mielofibrosis primaria.
El modelo TxGNN predice que podría ser efectivo para **PEComa benigno**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | PEComa benigno (benign PEComa) |
| Puntaje de Predicción TxGNN | 0.9984 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Fedratinib es un inhibidor selectivo de JAK2 con actividad adicional sobre FLT3 y BRD4. En la mielofibrosis, la señalización JAK/STAT está desregulada, y su inhibición reduce el tamaño del bazo y los síntomas. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción original, por lo que la descripción anterior se basa en el conocimiento general del fármaco.

Los PEComas se deben principalmente a la activación de la vía mTOR (pérdida de TSC1/TSC2), por lo que no existe un vínculo directo establecido con la inhibición de JAK2. Cualquier relación sería especulativa, por ejemplo a través de la interacción entre la señalización JAK/STAT y la vía PI3K/AKT/mTOR.

En consecuencia, la predicción tiene un puntaje alto en el modelo, pero una plausibilidad mecanística débil y sin respaldo experimental o clínico. Debe considerarse una hipótesis generadora, no una conclusión.

Otras predicciones del modelo, todas con evidencia L5 y recomendación Hold:

| Indicación predicha | Puntaje TxGNN | Comentario mecanístico |
|------|------|------|
| Linfangiomioma | 0.9983 | Biología TSC/mTOR; vínculo con JAK2 indirecto |
| Tumor de células epitelioides perivasculares del cuerpo uterino | 0.9983 | Dependencia de mTOR; sin relevancia demostrada de JAK2/FLT3 |
| Dermatofibrosarcoma protuberans | 0.9980 | Impulsado por COL1A1-PDGFB; fedratinib no actúa principalmente sobre PDGFR |
| Tumor rabdoide | 0.9978 | Pérdida de SMARCB1; vínculo especulativo vía BRD4 |
| Tumor rabdoide familiar | 0.9977 | Mismo razonamiento especulativo que el tumor rabdoide |
| Fiebre mediterránea familiar autosómica recesiva | 0.9975 | Autoinflamatoria; modulación indirecta de citocinas |
| Linfohistiocitosis hemofagocítica adquirida asociada a neoplasia | 0.9974 | Razonamiento de clase plausible (JAK/STAT, tormenta de citocinas); preocupación de seguridad |
| Síndrome hemofagocítico asociado a infección | 0.9974 | Mismo razonamiento; riesgo adicional por inmunosupresión |
| Linfangioleiomiomatosis | 0.9974 | Impulsada por TSC/mTORC1; sirolimus es el tratamiento estándar |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201514001 | INREBIC 100 mg CÁPSULAS DURAS (Bristol-Myers Squibb Pharma EEIG) | Cápsula dura | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de quinasas JAK2/FLT3) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (en las predicciones se menciona mielosupresión como preocupación) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal, y vigilancia neurológica (según el prospecto) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 100 interacciones en total; la lista compilada muestra, entre las principales:
  - **Mayores**: dexametasona, claritromicina, eliglustat, naloxegol.
  - **Moderadas**: inhibidores de la bomba de protones y antiácidos (omeprazol, rabeprazol, lansoprazol, cimetidina), corticoides (hidrocortisona, triamcinolona, betametasona, budesonida), aprepitant, saxagliptina, naldemedina, naltrexona.
- **Advertencia de contexto**: las predicciones señalan que fedratinib presenta una advertencia en recuadro por encefalopatía (incluida la de Wernicke), toxicidad gastrointestinal y mielosupresión. Esta información no procede del prospecto de la AEMPS y debe verificarse.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para PEComa benigno se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y con un vínculo mecanístico no establecido, ya que estos tumores dependen de mTOR y no de JAK2.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente un vacío bloqueante.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar estudios preclínicos que evalúen la relevancia de JAK2/STAT en PEComa.
- Revisar la literatura y los registros de ensayos para detectar evidencia directa.
- Valorar si alguna otra indicación predicha (por ejemplo, linfohistiocitosis hemofagocítica, con razonamiento de clase JAK) merece priorizarse.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

