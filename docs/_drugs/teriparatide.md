---
layout: default
title: Teriparatide
parent: Solo predicción del modelo (L5)
nav_order: 782
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "Teriparatide"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
description: "Teriparatide: nueva indicación predicha, Úlcera duodenal (duodenal ulcer (disease)) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Teriparatide
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

## Teriparatide: Úlcera duodenal (duodenal ulcer (disease))
{: .text-alpha }

## Resumen en Una Frase

Teriparatida es un análogo de la hormona paratiroidea (PTH 1-34) utilizado originalmente para tratar la osteoporosis, incluida la posmenopáusica.
El modelo TxGNN predice que podría ser efectivo para la **úlcera duodenal**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Úlcera duodenal (duodenal ulcer (disease)) |
| Puntaje de Predicción TxGNN | 0.9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 8 de 15; autorizadas no comercializadas: 6; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 15 (comercializadas: 8) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, teriparatida es un fragmento activo de la hormona paratiroidea humana (PTH 1-34). Los datos farmacológicos compilados indican que actúa sobre los receptores PTH1 (PTH1R) y PTH2 (PTH2R). Su eficacia en osteoporosis en pacientes con alto riesgo de fractura está establecida, y su acción anabólica sobre el hueso se ejerce a través de la estimulación de la actividad osteoblástica.

**En este caso, el vínculo mecanístico con la nueva indicación no es evidente.** No se identifica un mecanismo plausible por el cual la señalización anabólica ósea de la PTH favorezca la cicatrización de una úlcera duodenal, y no se aportaron ensayos ni literatura que lo apoyen. La relación entre la indicación original (enfermedad ósea metabólica) y la nueva (enfermedad gastrointestinal) tampoco ha podido establecerse. El puntaje alto (0.9986) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Principales autorizaciones:

<!-- review:begin es-lic-20261105-teriparatide-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Teriparatida está comercializada en España, con 15 autorizaciones vigentes, todas de medicamentos de un solo principio activo y ninguna cancelada. Principales autorizaciones:" Eliminado: afirmaba que el medicamento no está autorizado o comercializado en España, o que sus autorizaciones están revocadas o suspendidas, lo que no coincide con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 15 autorizaciones (comercializadas: 8); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-teriparatide-1 -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 03247001 | FORSTEO 20 microgramos/80 microlitros, solución inyectable (Eli Lilly) | Solución inyectable en pluma precargada | No especificada en los datos compilados |
| 82563 | TETRIDAR 20 microgramos/80 microlitros solución inyectable en pluma precargada (Teva) | Solución inyectable | No especificada en los datos compilados |
| 82562 | TERIPARATIDA TEVA 20 microgramos/80 microlitros solución inyectable en pluma precargada (Teva) | Solución inyectable | No especificada en los datos compilados |
| 85653 | DURATIL 20 microgramos/80 microlitros solución inyectable en pluma precargada EFG (Gp Pharm) | Solución inyectable en pluma precargada | No especificada en los datos compilados |
| 89727 | OSDY 20 microgramos/80 microlitros solución inyectable en pluma precargada (Reddy Pharma Iberia) | Solución inyectable en pluma precargada | No especificada en los datos compilados |

Existen además autorizaciones de TERROSA, MOVYMIA, LIVOGIVA, TERIPARATIDA SUN y SONDELBAY. Todas son soluciones inyectables, en su mayoría en pluma precargada.

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto): hipotensión, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, osteosarcoma óseo, enfermedad ósea de Paget (incluida la juvenil), osteomalacia, raquitismo, urolitiasis, osteodistrofia renal, osteítis fibrosa e hiperparatiroidismo.
- **Interacciones farmacológicas:** la consulta se completó, pero solo devolvió las dianas farmacológicas (receptores PTH1 y PTH2), no interacciones con otros medicamentos.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto autorizado por la AEMPS.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para úlcera duodenal se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un mecanismo plausible que conecte la señalización de la PTH con la cicatrización de la úlcera. No hay base para avanzar en esta indicación en este momento.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y un análisis mecanístico que justifique la relación con la patología duodenal.
- Revisión de la literatura preclínica para determinar si existe alguna señal biológica en el tracto gastrointestinal.
- Obtener y analizar el prospecto oficial de la AEMPS (advertencias y contraindicaciones) para completar la revisión de seguridad.
- Si se desea priorizar el reposicionamiento de teriparatida, evaluar otras predicciones del mismo análisis con mayor respaldo. Por ejemplo, la **osteoporosis asociada al embarazo y la lactancia** tiene nivel de evidencia L3, con estudios observacionales y revisiones centrados en teriparatida. Su uso exigiría precauciones específicas, ya que el fármaco no debe usarse durante el embarazo ni la lactancia.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Teriparatida está comercializada en España, con 15 autorizaciones vigentes, todas de medicamentos de un solo principio activo y ninguna canc" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

