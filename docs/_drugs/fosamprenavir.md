---
layout: default
title: Fosamprenavir
parent: Solo predicción del modelo (L5)
nav_order: 356
evidence_level: L5
indication_count: 7
---

# Fosamprenavir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Fosamprenavir: De VIH/SIDA a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Fosamprenavir es un profármaco de amprenavir, un inhibidor de la proteasa del VIH, utilizado originalmente para el tratamiento de la infección por VIH y el SIDA.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, aunque con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH / SIDA (según las relaciones de indicación del grafo de conocimiento; los textos de las autorizaciones españolas no incluyen indicación) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 (solo predicción del modelo, sin estudios reales; el análisis mecanístico preliminar la sitúa como pregunta de investigación) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen información detallada sobre el mecanismo de acción original. Según la información conocida, fosamprenavir es un profármaco de amprenavir, inhibidor de la proteasa del VIH-1, y su eficacia en la infección por VIH está establecida. Mecanísticamente, podría ser aplicable a otros lentivirus con proteasas relacionadas.

El virus de la inmunodeficiencia felina (VIF) es un lentivirus emparentado con el VIH y codifica su propia proteasa, por lo que la actividad de amprenavir frente a ella es plausible. Sin embargo, la proteasa del VIF difiere de la del VIH-1 en especificidad de sustrato y sensibilidad a inhibidores, y no existe evidencia directa en los datos disponibles.

El puntaje elevado de TxGNN probablemente refleja la proximidad en la red de conocimiento con la indicación original (VIH/SIDA) y no una evidencia independiente. Además, se trata de una indicación veterinaria, por lo que su relevancia para el reposicionamiento en humanos es limitada.

**Otras predicciones del modelo (todas sin ensayos ni literatura):**

| Indicación predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Infección por virus de inmunodeficiencia simia (SIV) | 99.88% | L4 | Modelo preclínico; la proteasa del SIV es más parecida a la del VIH que la del VIF. No es una diana terapéutica humana |
| Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminución de la sustancia blanca cortical | 99.86% | L5 | Sin vínculo mecanístico identificable; no se aborda la penetración en el sistema nervioso central |
| Enfermedad fibroquística de la mama | 99.57% | L5 | Sin fundamento mecanístico |
| Adenosis apocrina de la mama | 99.34% | L5 | Probable artefacto computacional |
| Adenosis de conductos romos de la mama | 99.34% | L5 | Puntaje idéntico al anterior, señal de grafo compartida |
| Displasia mamaria benigna | 99.10% | L5 | Grupo de predicciones benignas mamarias con probable señal espuria |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 04282002 | TELZIR 50 MG/ML SUSPENSIÓN ORAL | Suspensión oral | No especificada en los datos |
| 04282001 | TELZIR 700 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No especificada en los datos |

Ambas autorizaciones están vigentes, son de medicamento único y pertenecen a Viiv Healthcare B.V.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, infección crónica por virus de la hepatitis C y B, hipertrigliceridemia, enfermedad coronaria, infarto de miocardio, obesidad, hemoglobinopatías, nefrolitiasis, nefropatía aguda por uratos, anemia hemolítica, hemofilia y lipodistrofia.
- **Interacciones farmacológicas**: se registran 100 interacciones. Entre las principales:
  - **Mayor**: budesonida.
  - **Moderadas**: acarbosa, famotidina, ranitidina, rabeprazol, cimetidina, dexlansoprazol, hidrocortisona, betametasona, dexametasona oftálmica, budesonida nasal, albiglutida, alogliptina, dulaglutida, canagliflozina, dapagliflozina, clorpropamida, alosetrón y aprepitant.
  - **Menor**: claritromicina.
- Las interacciones por efectos sobre CYP3A4 deberían considerarse en cualquier nuevo uso.
- Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal carece de ensayos clínicos y literatura, y el puntaje alto del modelo probablemente refleja la cercanía con la indicación original de VIH. Al ser una indicación veterinaria, tiene poca relevancia como oportunidad de reposicionamiento en humanos. Las demás predicciones carecen de fundamento mecanístico.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Descarga y análisis del prospecto de la AEMPS (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Estudios preclínicos de actividad de amprenavir frente a la proteasa del VIF o del SIV, si se desea explorar la hipótesis.
- Evaluación del perfil de interacciones (CYP3A4) y de las contraindicaciones antes de considerar cualquier nuevo uso.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

