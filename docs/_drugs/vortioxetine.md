---
layout: default
title: Vortioxetine
parent: Evidencia moderada (L3-L4)
nav_order: 568
evidence_level: L3
indication_count: 5
---

# Vortioxetine
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **5** 
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

# Vortioxetina: De Trastorno Depresivo Mayor a Trastorno Neurótico

## Resumen en Una Frase

Vortioxetina es un antidepresivo multimodal, utilizado originalmente para el trastorno depresivo mayor (TDM). El modelo TxGNN predice que podría ser efectivo para **trastorno neurótico**, una categoría diagnóstica antigua y amplia. Actualmente lo respaldan solo **1 ensayo clínico** (observacional) y **1 publicación** (de baja calidad metodológica).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno depresivo mayor (según la base de farmacología; el texto de indicación de la AEMPS no está disponible) |
| Nueva Indicación Predicha | Trastorno neurótico |
| Puntaje de Predicción TxGNN | 99.24% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos de mecanismo de acción en DrugBank. Los datos de farmacología muestran que vortioxetina actúa sobre el transportador de serotonina (SERT) y sobre varios receptores serotoninérgicos (5-HT1A, 5-HT1B, 5-HT1D, 5-HT3, 5-HT5A, 5-HT6 y 5-HT7). La literatura la describe como inhibidora de SERT, agonista 5-HT1A, agonista parcial 5-HT1B y antagonista 5-HT3/5-HT7.

"Trastorno neurótico" es una categoría antigua y muy amplia, y por eso el vínculo con la indicación original es **indirecto**. El puntaje alto de TxGNN probablemente refleja la cercanía de este término a los trastornos depresivos en el grafo de conocimiento, no un mecanismo propio. Por ello, la predicción debe leerse con cautela.

Mecanísticamente, un fármaco serotoninérgico con perfil antidepresivo y ansiolítico podría ser aplicable a cuadros depresivos y ansiosos englobados bajo este término. Sin embargo, la evidencia actual no permite confirmarlo para el trastorno neurótico como tal.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04446039](https://clinicaltrials.gov/study/NCT04446039) | N/A | Completado | 370,212 | Estudio de cohorte retrospectivo con datos de reclamaciones nacionales. Compara patrones de uso y riesgo de eventos adversos entre antidepresivos comunes. Aporta contexto general de seguridad y efectividad, pero no es específico del trastorno neurótico. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Revisión / reporte de caso | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Presenta un caso de depresión neurótica y destaca las ventajas de un abordaje integrado con antidepresivos y terapia cognitivo-conductual. No es específico de vortioxetina. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 89290 | VORTIOXETINA STADA 15 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película |
| 113891028IP1 | BRINTELLIX 20 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película |
| 89288 | VORTIOXETINA STADA 5 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película |
| 90983 | VORTIOXETINA KRKA 20 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película |
| 90972 | VORTIOXETINA CINFA 15 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La consulta de interacciones devolvió solo dianas farmacológicas (SERT y receptores de serotonina), no interacciones entre fármacos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia para "trastorno neurótico" es indirecta: un estudio observacional no específico y una publicación de bajo nivel. Además, el término es antiguo y ambiguo, y el puntaje alto de TxGNN probablemente refleja su proximidad a los trastornos depresivos.

**Para avanzar se necesita:**
- Obtener del prospecto de la AEMPS las advertencias, contraindicaciones y la indicación aprobada.
- Completar los datos de mecanismo de acción en DrugBank.
- Traducir "trastorno neurótico" a diagnósticos actuales (depresión, trastornos de ansiedad, distimia) y evaluar la evidencia por separado.
- Nota: la evidencia de "melancolía" (5 ensayos, 4 de ellos aleatorizados de Fase 2/3 o 3) corresponde en realidad al TDM, ya comercializado, y no a un reposicionamiento propiamente dicho.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

