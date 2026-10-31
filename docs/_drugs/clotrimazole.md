---
layout: default
title: Clotrimazole
parent: Solo predicción del modelo (L5)
nav_order: 202
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
monitor_inn: "Clotrimazole"
predicted_indications: ["acne (disease)", "vulvovaginitis", "postmenopausal atrophic vaginitis"]
description: "Clotrimazole: nueva indicación predicha, Acné (acne (disease)) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Clotrimazole: Acné (acne (disease))
{: .text-alpha }

## Resumen en Una Frase

Clotrimazol es un antifúngico azólico de uso tópico, originalmente indicado para infecciones cutáneas por hongos (como la tiña del pie, la tiña corporal y la pitiriasis versicolor) y para candidiasis oral y vulvovaginal.
El modelo TxGNN predice que podría ser efectivo para **acné**, pero solo existe **1 ensayo clínico** suspendido, que evalúa una combinación de tres fármacos, y **ninguna publicación** que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Acné (acne (disease)) |
| Puntaje de Predicción TxGNN | 0.9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 18) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, clotrimazol es un antifúngico azólico que inhibe la CYP51 (lanosterol 14-alfa-desmetilasa) del hongo. Esto bloquea la síntesis de ergosterol y altera la integridad de la membrana fúngica. Su eficacia en micosis cutáneas y candidiasis está bien establecida. También se le atribuyen efectos antiinflamatorios y antimicrobianos modestos.

Un posible vínculo con el acné sería el papel de *Malassezia* (*Pityrosporum*) en la inflamación folicular. Otra posibilidad sería el efecto de una combinación tópica con antibiótico y corticoide. Sin embargo, esta relación es hipotética. El único ensayo disponible usa una combinación fija (beclometasona + gentamicina + clotrimazol), por lo que no se puede aislar la contribución del clotrimazol.

El puntaje TxGNN (0.9986) es una predicción computacional y no está respaldado por evidencia clínica directa. Debe interpretarse con cautela.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Fase 2/3 | Suspendido | 80 | Compara la eficacia de la crema tópica de beclometasona 0,025% + gentamicina 0,1% + clotrimazol 1% en dermatosis contaminada con lesiones bilaterales simétricas. Sin resultados disponibles. |

**Valoración:** la relevancia es baja (grado C). El ensayo está suspendido, no tiene resultados y prueba una combinación de varios fármacos. Además, el título está truncado y no permite confirmar si la población es realmente de acné o de otra dermatosis. La evidencia es, como mucho, indirecta.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes, todas de fármaco único. Los datos disponibles no incluyen el texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 52626 | Canesten 10 mg/g crema | Crema |
| 52625 | Canesten 10 mg/ml solución para pulverización cutánea | Solución para pulverización cutánea |
| 56826 | Canesten 10 mg/g polvo cutáneo | Polvo cutáneo |
| 82837 | Clotrimazol Nutra Essential 10 mg/g espuma cutánea | Espuma cutánea |
| 90227 | Clotic 10 mg/ml gotas óticas en solución en envase unidosis | Gotas óticas en solución |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto de prospecto): insuficiencia suprarrenal, enfermedad de Addison, atrofia cutánea, telangiectasia, enfermedad capilar, telangiectasia hemorrágica hereditaria, enfermedad vascular periférica, claudicación vascular intermitente y enfermedad arterial periférica.
- **Interacciones farmacológicas:** no se dispone de interacciones con otros fármacos. Los datos farmacológicos solo muestran dianas moleculares de clotrimazol: canales de potasio activados por calcio (KCa1.1 y KCa3.1), canales TRP (TRPM2, TRPM3, TRPM4 y TRPM8), receptor X de pregnano (PXR) y receptor constitutivo de androstano (CAR). Estas dianas no equivalen a interacciones clínicamente confirmadas.

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para acné se basa únicamente en el modelo. El único ensayo es de una combinación de tres fármacos, está suspendido y no tiene resultados, y no hay publicaciones que lo respalden. Por ello no es posible atribuir ningún efecto al clotrimazol en esta indicación.

**Para avanzar se necesita:**
- Aclarar la población real del ensayo NCT01244256 (acné frente a otra dermatosis) y obtener sus resultados, si existen.
- Estudios preclínicos o de mecanismo que justifiquen el uso de clotrimazol en acné, por ejemplo su papel frente a *Malassezia* o su actividad antiinflamatoria.
- Datos detallados del mecanismo de acción.
- Ensayos controlados con clotrimazol en monoterapia frente a un comparador estándar para el acné.
- Revisar las advertencias y contraindicaciones del prospecto oficial en la AEMPS.

**Nota adicional:** entre las demás predicciones del modelo, la vulvovaginitis (candidiasis vulvovaginal) es una indicación ya establecida de clotrimazol, con ensayos de Fase 3 completados. No constituye un reposicionamiento real, sino una confirmación de un uso existente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

