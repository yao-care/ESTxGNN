---
layout: default
title: Fosamprenavir
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 7
---

# Fosamprenavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Fosamprenavir: De Infección por VIH a Síndrome de Inmunodeficiencia Felina (FIV)

## Resumen en Una Frase

Fosamprenavir es un profármaco de amprenavir, un inhibidor de la proteasa del VIH-1 utilizado en el tratamiento de la infección por VIH.
El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Inmunodeficiencia Adquirida Felina (FIV)**,
con un puntaje del **99.88%**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección,
y la propia justificación mecanicista del modelo señala que probablemente se trata de una asociación espuria, ya que el FIV es una enfermedad veterinaria sin relevancia clínica en humanos.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH (inhibidor de proteasa VIH-1, según mecanismo referenciado en los datos) |
| Nueva Indicación Predicha | Síndrome de Inmunodeficiencia Adquirida Felina (FIV) |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por que es Razonable esta Prediccion?

No se dispone de datos oficiales de mecanismo de acción (MOA) en la base de origen. Según la información contextual disponible en las justificaciones mecanísticas del propio modelo, fosamprenavir es un profármaco de amprenavir, perteneciente a la clase de inhibidores de la proteasa del VIH-1, cuya eficacia en el tratamiento de la infección por VIH está bien establecida.

La hipótesis detrás de esta predicción es que el FIV, al ser también un retrovirus, podría compartir alguna vulnerabilidad estructural con el VIH a nivel de la proteasa viral. Sin embargo, el propio análisis del modelo señala una limitación importante: la proteasa del FIV difiere estructuralmente de la del VIH de forma significativa, y la literatura veterinaria conocida indica que los antirretrovirales humanos suelen tener eficacia limitada frente al FIV. Además, el FIV es una enfermedad que afecta a gatos, no a humanos, por lo que no constituye una indicación válida de reposicionamiento para uso clínico humano.

La segunda predicción del modelo (infección por VIS en primates, con el mismo puntaje) presenta la misma limitación: es un modelo de investigación animal, no una indicación humana. Las cinco predicciones restantes (un trastorno neurológico raro y cuatro patologías benignas de mama) no presentan, según el propio modelo, ningún vínculo mecanístico plausible con la clase farmacológica de fosamprenavir. En conjunto, esto sugiere que el grafo de conocimiento está generalizando de forma no específica la relación "antirretroviral-infección viral", sin una señal biológica real detrás.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusion y Proximos Pasos

**Decisión: Hold**

**Justificación:**
La única indicación con mayor puntaje (FIV) es una enfermedad veterinaria sin aplicabilidad clínica en humanos, y no existe ningún ensayo clínico ni literatura que respalde esta ni ninguna de las otras seis indicaciones predichas (todas en nivel de evidencia L5). El propio razonamiento mecanístico del modelo identifica varias de estas asociaciones como probable ruido del grafo de conocimiento.

**Para avanzar se necesita:**
- Datos del prospecto/warnings de la TFDA (actualmente bloqueante para la evaluación de seguridad S1)
- Datos verificados de mecanismo de acción (MOA) desde DrugBank
- Reevaluación del candidato solo si TxGNN genera predicciones de indicaciones humanas con mayor plausibilidad mecanística
- No se recomienda invertir recursos adicionales en las 7 indicaciones actuales dado el nivel de evidencia uniformemente bajo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

