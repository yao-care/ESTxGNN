---
layout: default
title: Remdesivir
parent: Solo predicción del modelo (L5)
nav_order: 691
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Remdesivir: nueva indicación predicha, Neoplasia endocrina múltiple (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "REMDESIVIR"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "homozygous familial hypercholesterolemia"]
---

# Remdesivir
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

# Remdesivir: De Indicación Original No Especificada a Neoplasia Endocrina Múltiple

## Resumen en Una Frase

Remdesivir es un análogo de nucleótido (profármaco) comercializado en España como Veklury, en formulación para perfusión intravenosa; los datos compilados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **neoplasia endocrina múltiple** (puntaje de 99.5%), pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.
Se trata de una predicción puramente computacional, sin vínculo mecanístico identificable, y probablemente sea un artefacto del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Neoplasia endocrina múltiple |
| Puntaje de Predicción TxGNN | 99.50% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en las fuentes consultadas. Según la información conocida, remdesivir es un profármaco análogo de nucleótido que inhibe la ARN polimerasa dependiente de ARN (RdRp) viral, y su uso establecido es antiviral.

La neoplasia endocrina múltiple es un síndrome tumoral hereditario (por ejemplo, mutaciones en MEN1 o RET) sin etiología viral ni diana viral. No se identifica ningún vínculo mecanístico entre la inhibición de la polimerasa viral y esta enfermedad.

El puntaje elevado (0.995) proviene de una predicción basada en grafos de conocimiento, sin ensayos ni literatura de apoyo. Debe interpretarse con mucha cautela, ya que probablemente sea un artefacto del modelo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201459001 | VEKLURY 100 MG CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Concentrado para solución para perfusión | No disponible |
| 1201459002 | VEKLURY 100 MG POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Polvo para concentrado para solución para perfusión | No disponible |

Ambas autorizaciones corresponden a Gilead Sciences Ireland Unlimited Company, son de componente único y están vigentes.

## Consideraciones de Seguridad

**Interacciones Farmacológicas**: la consulta de interacciones se completó y devolvió 100 interacciones registradas. Las primeras 20 mostradas son todas de nivel moderado, entre ellas: acarbosa, doxiciclina, pioglitazona, anfotericina B (y su complejo lipídico), bupropión, mesalazina, balsalazida, ácido quenodesoxicólico, claritromicina, minociclina, oxandrolona, oximetolona, tetraciclina, vancomicina, kanamicina, naltrexona, levofloxacino, neomicina y olsalazina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia endocrina múltiple es de nivel L5: no hay ensayos, ni literatura, ni vínculo mecanístico plausible, por lo que el puntaje alto de TxGNN no basta para avanzar.

**Para avanzar se necesita:**
- Datos de advertencias y contraindicaciones del prospecto de AEMPS (descargar y analizar el PDF), indispensables antes de cualquier evaluación de seguridad
- Texto de la indicación aprobada de las autorizaciones españolas
- Datos del mecanismo de acción desde DrugBank
- Estudios preclínicos que justifiquen una hipótesis biológica para esta enfermedad
- Valorar si otras predicciones del modelo (por ejemplo, VIH) tienen mejor sustento, aunque la evidencia actual tampoco demuestra eficacia de remdesivir en esa indicación (nivel L4)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

