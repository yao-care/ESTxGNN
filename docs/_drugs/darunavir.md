---
layout: default
title: Darunavir
parent: Evidencia moderada (L3-L4)
nav_order: 158
evidence_level: L4
indication_count: 4
---

# Darunavir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Darunavir: De Infección por VIH-1 a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Darunavir es un inhibidor de la proteasa del VIH-1, comercializado en España para el tratamiento de la infección por VIH-1 (esta indicación no figura en el texto de las autorizaciones y se deduce del contexto de los ensayos).
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina (FIV)**, pero solo hay **1 ensayo clínico** (en pacientes humanos con VIH-1, evidencia indirecta) y **ninguna publicación** que respalde esta indicación concreta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (deducida del contexto; el texto de indicación no consta en las autorizaciones) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Darunavir inhibe la proteasa del VIH-1, una enzima que el virus necesita para madurar y producir partículas infecciosas. No se dispone de datos detallados de mecanismo de acción procedentes de DrugBank; la descripción anterior se basa en la información mecanística del propio análisis.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus emparentado con el VIH y también tiene su propia proteasa. Esa cercanía explica que el modelo relacione ambas enfermedades.

Sin embargo, las proteasas del FIV y del VIH-1 son diferentes a nivel estructural, por lo que no se puede asumir que darunavir inhiba también la del FIV. El puntaje tan alto probablemente refleja la proximidad en el grafo de conocimiento entre enfermedades por VIH y lentivirus, no evidencia veterinaria. No hay datos de eficacia ni de seguridad en gatos.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Fase 4 | Completado | 145 | Darunavir/ritonavir con lamivudina frente a darunavir/ritonavir con tenofovir + emtricitabina o lamivudina, en adultos con VIH-1 sin tratamiento previo. Población humana; solo contexto mecanístico indirecto (relevancia C). |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el síndrome de inmunodeficiencia adquirida felina.

Como dato contextual, para otra predicción (infección por el virus de inmunodeficiencia simia, SIV) existen 4 estudios preclínicos en macacos con terapia antirretroviral combinada. Sus títulos están truncados y no se puede confirmar que darunavir sea un componente de cada régimen, por lo que no constituyen respaldo para el FIV.

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones. El texto de indicación aprobada no está disponible en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 85186 | Darunavir Tarbis 800 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos |
| 85184 | Darunavir Tarbis 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos |
| 83578 | Darunavir Dr. Reddys 600 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos |
| 84777 | Darunavir Accord 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos |
| 83163 | Darunavir Stada 600 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene respaldo veterinario directo: el único ensayo es en humanos con VIH-1 y no hay literatura sobre FIV. Además, las diferencias estructurales entre las proteasas del FIV y del VIH-1 impiden asumir eficacia cruzada. Las autorizaciones españolas corresponden a medicamentos de uso humano.

**Para avanzar se necesita:**
- Estudios in vitro de actividad de darunavir frente a la proteasa del FIV y comparación estructural con la del VIH-1
- Datos de farmacocinética, eficacia y seguridad en gatos
- Confirmar con veterinaria si el objetivo es realmente un uso animal, dado que las autorizaciones existentes son de uso humano
- Obtener del prospecto de la AEMPS las advertencias y contraindicaciones, hoy sin datos
- Datos detallados del mecanismo de acción (MOA) desde DrugBank
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

