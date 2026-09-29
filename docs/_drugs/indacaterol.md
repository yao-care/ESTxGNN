---
layout: default
title: Indacaterol
parent: Solo predicción del modelo (L5)
nav_order: 277
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: De Uso Respiratorio (EPOC/Asma) a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Indacaterol es un agonista beta2 de acción ultra-prolongada, comercializado en España en inhaladores de polvo seco. Los datos de AEMPS del paquete no incluyen el texto de la indicación aprobada, pero los ensayos y la literatura asociados lo sitúan en enfermedades respiratorias (EPOC y asma).
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada (NSIAD)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, y el análisis mecanístico no encuentra una base terapéutica plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS del paquete (el texto de indicación está vacío en todas las autorizaciones). Por el contexto de ensayos y literatura, uso respiratorio (EPOC/asma) |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada (NSIAD) |
| Puntaje de Predicción TxGNN | 99,54 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, indacaterol es un agonista beta2-adrenérgico de acción ultra-prolongada que relaja el músculo liso de las vías respiratorias mediante la vía del receptor beta2 y el AMPc, con broncodilatación una vez al día. Su uso está establecido en enfermedades respiratorias, solo o en combinaciones con glicopirronio y mometasona.

Aquí la predicción **no es mecanísticamente razonable**. El NSIAD se debe a variantes con ganancia de función del receptor AVPR2, que también actúa por AMPc en el túbulo colector. Un agonista beta2 elevaría el AMPc intracelular, por lo que cabría esperar que empeorara la antidiuresis o no tuviera efecto. No hay una hipótesis terapéutica que sostenga el uso de indacaterol en esta enfermedad.

El puntaje alto del modelo (99,54 %) debe interpretarse con cautela. No hay ensayos, literatura ni vía mecanística identificada, y la similitud con la indicación original está pendiente de análisis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan 5 de las 12 autorizaciones. Todas corresponden a Novartis Europharm Limited.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 09593007 | ONBREZ BREEZHALER 300 microgramos | Polvo para inhalación (cápsula dura) | No especificada en los datos |
| 09594002 | HIROBRIZ BREEZHALER 150 microgramos | Polvo para inhalación (cápsula dura) | No especificada en los datos |
| 09594007IP | HIROBRIZ BREEZHALER 300 microgramos | Polvo para inhalación (cápsula dura) | No especificada en los datos |
| 09593002 | ONBREZ BREEZHALER 150 microgramos | Polvo para inhalación (cápsula dura) | No especificada en los datos |
| 09586002 | OSLIF BREEZHALER 150 microgramos | Polvo para inhalación (cápsula dura) | No especificada en los datos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura. Además, el mecanismo del fármaco (aumento del AMPc) va en sentido contrario a la fisiopatología del NSIAD, por lo que no hay base para avanzar.

**Para avanzar se necesita:**
- Una hipótesis mecanística que explique por qué un agonista beta2 podría beneficiar al NSIAD, lo cual actualmente no existe.
- Datos de seguridad y contraindicaciones del prospecto de AEMPS.
- Datos del mecanismo de acción en DrugBank y el texto de indicación aprobada de las autorizaciones españolas, para fijar la indicación original.
- Evidencia preclínica o clínica específica para NSIAD, antes de reconsiderar la decisión.

**Nota sobre otras predicciones del paquete:** la indicación "enfermedad bronquial" (posición 7) tiene evidencia L1 (varios ensayos de Fase 3 en asma) y podría permitir "Proceed with Guardrails". Sin embargo, corresponde esencialmente al uso respiratorio ya conocido del fármaco y no a un reposicionamiento real. Habría que reconciliarla con la ficha técnica antes de presentarla como tal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

