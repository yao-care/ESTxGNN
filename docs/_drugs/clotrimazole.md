---
layout: default
title: Clotrimazole
parent: Solo predicción del modelo (L5)
nav_order: 141
evidence_level: L5
indication_count: 3
---

# Clotrimazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Clotrimazol: De Infecciones Fúngicas y por Levaduras a Acné

## Resumen en Una Frase

Clotrimazol es un antifúngico azólico de uso local, empleado en infecciones de la piel por hongos y levaduras y en la candidiasis vaginal.
El modelo TxGNN predice que podría ser efectivo para **acné**, pero la evidencia es muy débil: **1 ensayo clínico** suspendido, con una combinación de tres fármacos, y **ninguna publicación** que lo respalde.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones locales de la piel por hongos y levaduras (tiña, pie de atleta) y candidiasis vaginal (según datos farmacológicos; las autorizaciones de la AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99,86% |
| Nivel de Evidencia | L4 (indirecta) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Clotrimazol es un antifúngico azólico. Inhibe la enzima fúngica lanosterol 14-alfa-desmetilasa (CYP51), bloquea la síntesis de ergosterol y daña la membrana del hongo. Los datos del paquete de evidencia no incluyen una descripción detallada del mecanismo de acción, así que esta descripción procede del razonamiento del análisis.

El vínculo con el acné es plausible pero **no está demostrado**. Se podría pensar en una actividad frente a levaduras del género *Malassezia* asociadas a inflamación cutánea, pero no hay datos que lo confirmen. El único ensayo disponible prueba una combinación fija (beclometasona + gentamicina + clotrimazol). Cualquier efecto se explicaría mejor por el corticoide y el antibiótico que por clotrimazol.

El puntaje de 99,86% es una predicción del modelo, no un respaldo clínico. Probablemente refleja la cercanía en el grafo de conocimiento entre clotrimazol y las afecciones dermatológicas.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Fase 2/3 | Suspendido | 80 | Compara la combinación de beclometasona + gentamicina + clotrimazol en crema tópica en pacientes con dermatosis contaminada con lesiones bilaterales simétricas. Sin resultados. Relevancia baja (grado C): el efecto de clotrimazol no puede aislarse y el enfoque no es específicamente acné. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 11003-29-03-1999 | GINE-CANESTEN 20 MG/G CREMA VAGINAL | Crema vaginal |
| 90227 | CLOTIC 10 MG/ML GOTAS ÓTICAS EN SOLUCIÓN EN ENVASE UNIDOSIS | Gotas óticas en solución |
| 56755 | GINE-CANESTEN 500 mg COMPRIMIDO VAGINAL | Comprimido vaginal |
| 52626 | CANESTEN 10 mg/g CREMA | Crema |
| 56825 | GINE-CANESTEN 20 mg/g CREMA VAGINAL | Crema vaginal |

Existen además otras formas comercializadas: cápsula vaginal blanda, solución para pulverización cutánea, polvo cutáneo y espuma cutánea.

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: los datos disponibles describen dianas farmacológicas de clotrimazol, no interacciones con otros medicamentos. Incluyen los canales KCa1.1 y KCa3.1, los canales TRPM (TRPM2, TRPM4, TRPM8), y los receptores nucleares PXR y CAR, que regulan el metabolismo de fármacos. La relevancia clínica de estas dianas no está establecida en los datos.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única evidencia es un ensayo suspendido, sin resultados, con una combinación triple en la que no se puede atribuir efecto a clotrimazol. Sin literatura ni un vínculo mecanístico establecido, la predicción no basta para avanzar.

**Para avanzar se necesita:**
- Datos de mecanismo de acción y estudios preclínicos sobre la actividad de clotrimazol en acné (por ejemplo, frente a *Malassezia* o *Cutibacterium*)
- Un ensayo con clotrimazol en monoterapia, comparado con placebo o tratamiento estándar en acné
- Advertencias y contraindicaciones del prospecto de la AEMPS
- Aclarar la indicación original (los datos de autorización de la AEMPS no incluyen texto de indicación)

**Nota sobre otras predicciones del modelo:**
- **Vulvovaginitis** (98,96%... véase abajo) es con alta probabilidad un uso ya establecido y comercializado, no un reposicionamiento real. Tiene evidencia de nivel L2 y decisión Proceed with Guardrails, pero hay que confirmar qué ensayos incluyen realmente clotrimazol. Aplica solo a la vaginitis candidiásica.
- **Vaginitis atrófica posmenopáusica** carece de vínculo mecanístico creíble (L5, Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

