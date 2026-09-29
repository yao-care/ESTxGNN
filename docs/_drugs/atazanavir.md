---
layout: default
title: Atazanavir
parent: Solo predicción del modelo (L5)
nav_order: 50
evidence_level: L5
indication_count: 6
---

# Atazanavir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Atazanavir: De Infección por VIH-1 a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Atazanavir es un inhibidor de la proteasa del VIH-1, utilizado en el tratamiento de la infección por VIH-1 (según su uso conocido, ya que los textos de AEMPS proporcionados no detallan la indicación).
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina (FIV)**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción concreta. Es una indicación veterinaria, sin relevancia clínica humana.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (uso conocido del fármaco; no detallada en el texto de AEMPS) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99,98 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 19 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Atazanavir inhibe la proteasa del VIH-1, bloquea el procesamiento de la poliproteína Gag-Pol e impide la maduración de viriones infecciosos. Los datos de mecanismo de acción de DrugBank no están disponibles en el paquete de evidencia; esta descripción proviene del conocimiento farmacológico general del fármaco.

La proteasa del virus de la inmunodeficiencia felina (FIV) es una aspartil proteasa retroviral emparentada con la del VIH-1, por lo que existe una justificación a nivel de clase. Sin embargo, no hay datos enzimáticos ni animales sobre FIV, y la especificidad de sustrato de ambas proteasas es distinta. El puntaje alto de TxGNN es solo una predicción del modelo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Otras Indicaciones Predichas (Contexto)

El paquete incluye otras predicciones. Solo las de VIH tienen evidencia sustancial, y corresponden a la indicación ya comercializada, no a un reposicionamiento real.

| Indicación Predicha | Puntaje | Nivel | Evidencia disponible | Decisión |
|------|------|------|------|------|
| Infección por el virus de inmunodeficiencia simia (SIV) | 99,98 % | L4 | 1 estudio en macacos (2010, J Infect Dis) con TARGA; el papel de atazanavir no se puede confirmar | Hold |
| Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminución de sustancia blanca cortical | 99,98 % | L5 | Ninguna; no hay vínculo mecanístico plausible | Hold |
| Hiperlipidemia familiar combinada (término obsoleto) | 99,82 % | L5 | Ninguna; probable artefacto del grafo (posible asociación con efectos adversos) | Hold |
| VIH congénito | 99,71 % | L1 | Más de 30 ensayos (incl. Fase 3, estudios pediátricos y de farmacocinética en embarazo) y 7 publicaciones (cohortes de exposición intrauterina, PK en embarazo) | Proceed with Guardrails |
| Complejo relacionado con el SIDA | 99,71 % | L1 | 2 ensayos (NCT00035932 Fase 3, NCT01099579 Fase 3 pediátrico) y 3 publicaciones | Proceed with Guardrails |

Nota: en varios ensayos los títulos aparecen truncados, por lo que no se puede confirmar si atazanavir es el brazo en investigación, el comparador o parte del régimen de base. Para VIH congénito, la evidencia específica se limita a datos de PK y seguridad en embarazo y a cohortes de exposición intrauterina.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 83678 | ATAZANAVIR DR. REDDYS 200 MG CAPSULAS DURAS EFG | Cápsula dura | No indicada en los datos disponibles |
| 1191353001 | ATAZANAVIR KRKA 150 MG CAPSULAS DURAS EFG | Cápsula dura | No indicada en los datos disponibles |
| 80655 | ATAZANAVIR TEVA 300 MG CAPSULAS DURAS EFG | Cápsula dura | No indicada en los datos disponibles |
| 83676 | ATAZANAVIR DR. REDDYS 300 MG CAPSULAS DURAS EFG | Cápsula dura | No indicada en los datos disponibles |
| 84067 | ATAZANAVIR STADA 200 MG CAPSULAS DURAS EFG | Cápsula dura | No indicada en los datos disponibles |

Se muestran 5 de las 19 autorizaciones.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación principal (FIV) es veterinaria, carece por completo de ensayos y literatura, y solo cuenta con una predicción del modelo (nivel L5). Las predicciones con evidencia sólida (VIH congénito, complejo relacionado con el SIDA) corresponden al uso ya comercializado del fármaco y pueden avanzar como "Proceed with Guardrails".

**Para avanzar se necesita:**
- Datos enzimáticos y animales de atazanavir frente a la proteasa de FIV, si se quisiera explorar el uso veterinario
- Descargar y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación autorizada)
- Datos del mecanismo de acción desde DrugBank
- Para las indicaciones de VIH: confirmar el etiquetado y la dosificación pediátrica y neonatal, vigilar la hiperbilirrubinemia y revisar interacciones (potenciadores ritonavir/cobicistat, supresores de ácido, tenofovir)
- Confirmar el papel de atazanavir en los ensayos con títulos truncados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

