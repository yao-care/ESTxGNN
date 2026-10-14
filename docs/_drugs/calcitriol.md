---
layout: default
title: Calcitriol
parent: Solo predicción del modelo (L5)
nav_order: 135
evidence_level: L5
indication_count: 7
---

# Calcitriol
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

# Calcitriol: De Trastornos del Metabolismo del Calcio y el Fósforo a Deficiencia de Vitamina D (entrada obsoleta)

## Resumen en Una Frase

Calcitriol es la forma activa de la vitamina D, utilizada en trastornos del metabolismo del calcio y el fósforo, como el hipoparatiroidismo y la osteodistrofia renal.
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de vitamina D (entrada catalogada como obsoleta)**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción concreta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Las licencias españolas no incluyen texto de indicación. Según el grafo de conocimiento (PrimeKG): hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, hipofosfatemia, hipoparatiroidismo y osteodistrofia renal |
| Nueva Indicación Predicha | Deficiencia de vitamina D (entrada obsoleta) |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por conocimiento general, calcitriol es el metabolito activo de la vitamina D (1,25-dihidroxivitamina D3). Actúa sobre el receptor de la vitamina D y regula la absorción intestinal de calcio y fosfato, la mineralización ósea y la secreción de hormona paratiroidea (PTH). Su eficacia en trastornos del calcio y el fósforo está establecida.

Existe un vínculo biológico plausible con la deficiencia de vitamina D, porque calcitriol es la forma activa de esa vitamina. Sin embargo, hay varias razones para ser prudente:

- La entrada de enfermedad está marcada como **obsoleta** en la ontología.
- No se recuperó ningún ensayo ni publicación.
- En la deficiencia nutricional se usa normalmente la vitamina D nativa (colecalciferol o ergocalciferol), no el metabolito activo.

El puntaje alto de TxGNN (99.96%) es solo una predicción y probablemente refleja la cercanía en la ontología, no evidencia clínica nueva.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55973 | ROCALTROL 0,25 mcg cápsulas blandas | Cápsula blanda | No disponible en los datos compilados |
| 55974 | ROCALTROL 0,50 mcg cápsulas blandas | Cápsula blanda | No disponible en los datos compilados |
| 68934 | CALCITRIOL KERN PHARMA 1 microgramo/ml solución inyectable EFG | Solución inyectable | No disponible en los datos compilados |
| 64527 | SILKIS 3 microgramos/g pomada | Pomada | No disponible en los datos compilados |

Las cuatro autorizaciones están vigentes y son de monofármaco. Ninguna está cancelada.

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el texto del prospecto)**: enfermedad renal, sarcoidosis, hipercalcemia, nefrocalcinosis, nefrolitiasis, hiperfosfatemia, hipervitaminosis, nefropatía aguda por uratos, piouréter, trastornos del metabolismo del fósforo y arteriosclerosis obliterante.
- **Interacciones farmacológicas**: se registraron 100 interacciones. Las principales son:
  - **Mayores**: colecalciferol, calcifediol y burosumab.
  - **Moderadas**:
    - Diuréticos tiazídicos (hidroclorotiazida, clortalidona, clorotiazida, bendroflumetiazida, benztiazida).
    - Anticonvulsivantes y barbitúricos (fosfenitoína, carbamazepina, amobarbital, butabarbital, butalbital).
    - Resinas secuestradoras de ácidos biliares (colestiramina, colesevelam, colestipol).
    - Digoxina y digitoxina.
    - Hidróxido de aluminio.
    - Calcipotriol tópico.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para la deficiencia de vitamina D solo tiene respaldo del modelo (nivel L5). No hay ensayos ni literatura, la entrada de enfermedad es obsoleta y la práctica clínica usa vitamina D nativa para esta condición.

**Para avanzar se necesita:**
- Confirmar si existe una entrada de enfermedad vigente que sustituya a la obsoleta.
- Datos detallados del mecanismo de acción.
- Revisión del prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas).
- Evidencia clínica o de literatura específica.

**Nota sobre otras predicciones del mismo fármaco:** el análisis incluye otra candidata con mejor respaldo, el **raquitismo hipofosfatémico hereditario** (puntaje TxGNN 99.28%). Tiene nivel L2, una recomendación de *Proceed with Guardrails* y dos ensayos clínicos:
- NCT03748966, fase 1 temprana, completado, 16 participantes.
- NCT03820518, fase 4, estado desconocido, 100 participantes.

Los controles necesarios serían calcio, PTH y ecografía renal, por el riesgo de hipercalciuria y nefrocalcinosis. Esa indicación merece priorizarse en una evaluación posterior.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

