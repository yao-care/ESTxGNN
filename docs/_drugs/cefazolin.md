---
layout: default
title: Cefazolin
parent: Evidencia moderada (L3-L4)
nav_order: 109
evidence_level: L4
indication_count: 8
---

# Cefazolin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **8** 
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

# Cefazolina: De Indicación Original No Registrada a Otitis Media Infecciosa

## Resumen en Una Frase

Cefazolina es una cefalosporina de primera generación de uso parenteral. Los datos de AEMPS disponibles no detallan su indicación original.
El modelo TxGNN predice que podría ser efectiva para **otitis media infecciosa**,
pero solo hay **1 ensayo clínico** sin relación demostrada con cefazolina y **3 publicaciones** de valor limitado.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS (los textos de indicación están vacíos) |
| Nueva Indicación Predicha | Otitis media infecciosa |
| Puntaje de Predicción TxGNN | 99.44% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Cefazolina es un betalactámico de primera generación que inhibe la síntesis de la pared celular bacteriana mediante su unión a las proteínas fijadoras de penicilina. Es activa frente a *Staphylococcus aureus* sensible a meticilina (MSSA) y estreptococos, por lo que es plausible en algunas otitis medias bacterianas. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank; este razonamiento se basa en farmacología general.

Existen limitaciones importantes. Cefazolina tiene actividad débil frente a *Haemophilus influenzae* y *Moraxella catarrhalis*, dos patógenos clave de la otitis media. Además, solo se administra por vía parenteral, lo que restringe su uso práctico en una infección que suele tratarse de forma ambulatoria.

El puntaje de 99.44% es solo una predicción del modelo. No sustituye a la evidencia clínica directa.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Fase 2b | Terminado | 520 | Ensayo aleatorizado, doble ciego y controlado con placebo que compara 5 frente a 10 días de antibiótico en niños de 6 a 23 meses con otitis media aguda. Los datos no muestran que cefazolina sea la intervención, por lo que no cuenta como evidencia directa. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Revisión | Southern Medical Journal | Revisión general de cefalosporinas en pediatría; útiles frente a cocos grampositivos y en alergia a penicilina. No es específica de otitis media. |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Revisión | Clinical Pharmacy | Manejo del síndrome de Stevens-Johnson, con un caso pediátrico que incluye otitis media. Sin relevancia para la indicación. |
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Serie/reporte de casos | Annals of Otology, Rhinology & Laryngology | Terapia empírica ceftazidima-cefazolina en síndrome de Gradenigo pediátrico, una complicación de la otitis media aguda. Evidencia de bajo nivel. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 67021 | Cefazolina Sala 2 g polvo para solución inyectable EFG | Polvo para solución inyectable | No especificada en los datos |
| 67024 | Cefazolina Sala 1 g polvo y disolvente para solución inyectable EFG | Polvo y disolvente para solución inyectable | No especificada en los datos |
| 64848 | Cefazolina Normon 1 g polvo y disolvente para solución inyectable intramuscular EFG | Polvo y disolvente para solución inyectable | No especificada en los datos |
| 64850 | Cefazolina Normon 2 g polvo para solución inyectable intravenosa EFG | Polvo para suspensión inyectable | No especificada en los datos |
| 86542 | Cefazolina LDP Laboratorios Torlan 2 g polvo para solución inyectable y para perfusión EFG | Polvo para solución inyectable y para perfusión | No especificada en los datos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya casi solo en el puntaje del modelo. El único ensayo no muestra relación con cefazolina y la literatura es indirecta. Además, la cobertura frente a los patógenos principales de la otitis media es limitada y el fármaco solo existe en forma parenteral.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones, actualmente sin datos).
- Completar el mecanismo de acción desde DrugBank.
- Verificar si NCT01511107 utilizó cefazolina como intervención.
- Buscar ensayos que comparen cefazolina con los tratamientos de primera línea actuales en otitis media.
- Evaluar si la vía parenteral es compatible con el uso clínico previsto.
- Como alternativa más prometedora, revisar la otitis media supurativa y la crónica: cuentan con un estudio comparativo de 1982 (cefmetazol frente a cefazolina, PMID 6752467), aunque cefazolina actuó solo como comparador.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

