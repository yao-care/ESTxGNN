---
layout: default
title: Salbutamol
parent: Solo predicción del modelo (L5)
nav_order: 722
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-29
monitor_inn: "SALBUTAMOL"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "bronchitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
description: "Salbutamol: nueva indicación predicha, Conjuntivitis papilar (papillary conjunctivitis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Salbutamol
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

## Salbutamol: Conjuntivitis papilar (papillary conjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Salbutamol es un agonista beta-2 adrenérgico, utilizado originalmente para el tratamiento del asma y de las enfermedades bronquiales.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis papilar**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Conjuntivitis papilar (papillary conjunctivitis) |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 9 de 15) |
| Número de Autorizaciones | 15 (vigentes: 9) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, salbutamol es un agonista beta-2 adrenérgico de acción corta, su eficacia en asma y enfermedad bronquial está bien establecida, y mecanísticamente podría ser aplicable a la conjuntivitis papilar solo de forma especulativa.

Los datos compilados indican que los agonistas beta-2 han mostrado cierta actividad antiinflamatoria en tejido conjuntival en modelos animales. Esto sugiere una posible vía de acción local, pero no se recuperó ningún ensayo clínico ni publicación específica sobre salbutamol en esta indicación. El vínculo mecanístico es, por tanto, hipotético.

La relación con la indicación original (una enfermedad respiratoria obstructiva) es débil. La conjuntivitis papilar es una inflamación ocular de naturaleza alérgica o mecánica, y la broncodilatación no tiene relevancia directa en ella. La similitud con la indicación original aún no ha sido evaluada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Hay 15 autorizaciones vigentes, todas de salbutamol como principio activo único y ninguna cancelada. Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 90819 | Salbutamol Glenmark 100 microgramos/pulsación | Suspensión para inhalación en envase a presión |
| 55148 | Ventolin 0,5 mg/ml | Solución inyectable |
| 53932 | Ventolin 2 mg/5 ml | Jarabe |
| 89256 | Salbutamol Neutec 2,5 mg | Solución para inhalación por nebulizador |
| 53931 | Ventolin 4 mg | Comprimido |

Las formas farmacéuticas autorizadas incluyen inhalación (suspensión en envase a presión, polvo y solución para nebulizador), inyectable, jarabe y comprimido. No figura ninguna forma oftálmica, lo que es relevante para la nueva indicación predicha. Los textos de indicación aprobada no están disponibles en los datos compilados.

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de precaución según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, síndrome de QT largo (incluido el familiar), epilepsia, déficit de potasio, diabetes mellitus, cetoacidosis diabética, hiperplasia benigna de próstata, hipertensión ocular, acidosis (incluida la metabólica), paro cardíaco súbito, enfermedad de la conducción cardíaca, glaucoma de ángulo cerrado, hipertiroidismo (enfermedad de Graves, tirotoxicosis), obstrucción del cuello vesical, isquemia miocárdica y enfermedad coronaria.
  - Destaca la hipertensión ocular y el glaucoma de ángulo cerrado, por su relevancia si se considerara una vía oftálmica.
- **Interacciones farmacológicas**: se identificaron 100 interacciones; se muestran las 20 primeras.
  - **Moderadas**: acarbosa, isometepteno, famotidina, epinefrina, albiglutida, acetohexamida, alogliptina, bisacodilo, canagliflozina, aceite de ricino, clorpropamida, cisaprida, claritromicina, dapagliflozina y dietilpropión.
  - **Leves**: hidrocortisona, beclometasona, betametasona, budesonida y dexametasona.

No se dispone de las advertencias principales ni de las contraindicaciones del prospecto. Consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel de evidencia L5), sin ensayos clínicos ni literatura que la respalden, y el vínculo mecanístico es especulativo. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del salbutamol (DrugBank).
- Advertencias y contraindicaciones del prospecto en AEMPS, necesarias para el cribado de seguridad.
- Revisión de la literatura preclínica sobre agonistas beta-2 en tejido conjuntival y de su posible traslación a conjuntivitis papilar.
- Evaluación de la compatibilidad de vía de administración, ya que no existe formulación oftálmica autorizada y habría que valorar el riesgo en pacientes con hipertensión ocular o glaucoma de ángulo cerrado.
- Evaluación de la similitud con la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

