---
layout: default
title: Fedratinib
parent: Solo predicción del modelo (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Fedratinib: De Mielofibrosis a PEComa Benigno

## Resumen en Una Frase

Fedratinib es un inhibidor de JAK2 (también de FLT3 y BRD4) comercializado en España como INREBIC; el registro de la AEMPS no incluye el texto de la indicación, pero por conocimiento general se usa en la mielofibrosis. El modelo TxGNN predice que podría ser efectivo para **PEComa benigno**, aunque hoy hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, y la relación mecanística no está sustentada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en el registro de la AEMPS (texto vacío); por conocimiento general, mielofibrosis |
| Nueva Indicación Predicha | PEComa benigno |
| Puntaje de Predicción TxGNN | 99,84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Fedratinib inhibe principalmente JAK2, y también FLT3 y BRD4. No hay datos detallados de mecanismo de acción en DrugBank. La descripción anterior proviene del análisis mecanístico de las predicciones.

Para el PEComa benigno **no se identifica un vínculo directo**. Esta neoplasia depende sobre todo de la activación de la vía mTOR (pérdida de TSC1/TSC2, reordenamiento de TFE3). Cualquier conexión a través de la comunicación cruzada JAK/STAT es especulativa. El puntaje alto de TxGNN probablemente refleja cercanía en el grafo de conocimiento con tumores relacionados, no respaldo farmacológico.

Las otras predicciones de mayor puntaje tampoco cuentan con evidencia en el paquete:

| # | Enfermedad | Puntaje | Comentario mecanístico |
|---|---|---|---|
| 2 | Linfangiomioma | 99,83% | Espectro de LAM (mTOR); sin vínculo con JAK2 |
| 3 | PEC tumoral perivascular de cuerpo uterino | 99,83% | Mismo razonamiento que el PEComa |
| 4 | Dermatofibrosarcoma protuberans | 99,80% | Impulsado por PDGFRB (imatinib); sin acción directa |
| 5-6 | Tumor rabdoide (y familiar) | 99,78% / 99,77% | Pérdida de SMARCB1; el ángulo BRD4 es débil |
| 7 | Fiebre mediterránea familiar AR | 99,75% | Autoinflamatoria (IL-1); fedratinib es selectivo de JAK2 |
| 8-9 | Linfohistiocitosis hemofagocítica (asociada a neoplasia / a infección) | 99,74% | La más plausible: hiperinflamación vía JAK/STAT; el precedente es ruxolitinib, no fedratinib |
| 10 | Linfangioleiomiomatosis | 99,74% | Enfermedad dependiente de mTORC1 (sirolimus) |

Las dos formas de linfohistiocitosis hemofagocítica (puestos 8 y 9) se clasificaron como "Research Question". Ese precedente de clase no se transfiere automáticamente a fedratinib.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201514001 | INREBIC 100 mg cápsulas duras | Cápsula dura | No disponible en el registro |

Titular: Bristol-Myers Squibb Pharma EEIG.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de quinasas) |
| Riesgo de Mielosupresión | Preocupación por citopenias señalada en el análisis; consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma; función hepática y renal; consultar el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Advertencias principales**: el análisis menciona una advertencia en recuadro por encefalopatía (incluida la de Wernicke) y por citopenias. Es un riesgo relevante en pacientes críticos, como en la linfohistiocitosis hemofagocítica. Esta información no se ha verificado contra el prospecto de la AEMPS.
- **Interacciones farmacológicas**: no se encontraron registros en la consulta realizada.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura, y la biología del PEComa (mTOR) no se conecta con la inhibición de JAK2. La hipótesis más defendible es la linfohistiocitosis hemofagocítica, pero solo como pregunta de investigación.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias y contraindicaciones), un bloqueo para el cribado de seguridad.
- Completar el mecanismo de acción desde DrugBank.
- Revisión sistemática de literatura preclínica sobre inhibición de JAK2 en PEComa y en linfohistiocitosis hemofagocítica.
- Si se prioriza la linfohistiocitosis hemofagocítica, evaluar la viabilidad frente a ruxolitinib y el perfil de seguridad en pacientes críticos.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

