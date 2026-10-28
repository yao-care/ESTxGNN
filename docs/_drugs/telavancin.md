---
layout: default
title: Telavancin
parent: Solo predicción del modelo (L5)
nav_order: 769
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "telavancin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "septicemic plague", "premalignant hematological system disease", "hematological disease associated with an acquired peripheral neuropathy", "monoclonal gammopathy", "congenital hematological disorder"]
description: "Telavancin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Telavancin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Telavancin: Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Resumen en Una Frase

Telavancina es un antibiótico lipoglucopéptido, originalmente utilizado para el tratamiento de la neumonía bacteriana y la neumonía por *Staphylococcus aureus*.
El modelo TxGNN predice que podría ser efectivo para **síndrome de hiperviscosidad policlonal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, telavancina es un antibiótico lipoglucopéptido que inhibe la síntesis de la pared celular bacteriana y altera la integridad de la membrana, con eficacia demostrada en infecciones por bacterias Gram-positivas como la neumonía.

La hiperviscosidad policlonal se debe a niveles elevados de inmunoglobulinas o proteínas séricas. Este proceso no es una diana del mecanismo antibacteriano de telavancina, por lo que **no se identifica un vínculo mecanístico plausible** entre la indicación original y la nueva.

El puntaje elevado (0.9963) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni clínica. Otras predicciones del modelo (hiperamilasemia, analbuminemia congénita, gammapatía monoclonal, entre otras) presentan el mismo patrón: puntajes altos sin respaldo mecanístico. La única con cierta plausibilidad indirecta es la peste septicémica, aunque *Yersinia pestis* es Gram-negativa y existen tratamientos eficaces establecidos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 111705001 | Vibativ 250 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |
| 111705002 | Vibativ 750 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |

Ambas autorizaciones están vigentes, corresponden a medicamentos de principio activo único y su titular es Theravance Biopharma Ireland Limited.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, síndrome de QT largo (incluido el familiar), torsades de pointes, enfermedad renal y deterioro de la función renal, piouréter, diabetes mellitus, cetoacidosis diabética, colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones farmacológicas**: se registraron 131 interacciones. Entre las principales:
  - **Mayor**: dolasetrón.
  - **Moderadas**: ondansetrón, palonosetrón, levofloxacino, claritromicina, famotidina, loperamida, mesalazina, sulfasalazina, balsalazida, olsalazina, bisacodilo, ácido picosulfúrico, polietilenglicol, sulfato de sodio, lactitol, lactulosa y aceite de ricino.
  - **Menor**: metronidazol.

  Varias de estas interacciones (antieméticos y quinolonas/macrólidos) son coherentes con el riesgo de prolongación del intervalo QT.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos, literatura y vínculo mecanístico plausible (nivel de evidencia L5). El puntaje alto del modelo no basta para avanzar, y el perfil de seguridad (QT, función renal) exige cautela.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS
- Una hipótesis biológica que justifique el efecto sobre la hiperviscosidad, con datos in vitro o en modelos animales
- Valorar otras indicaciones predichas con mayor plausibilidad antes de invertir recursos en esta
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

