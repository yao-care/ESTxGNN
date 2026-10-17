---
layout: default
title: Dextromethorphan
parent: Solo predicción del modelo (L5)
nav_order: 244
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Dextromethorphan: nueva indicación predicha, Enfermedad de la cavidad nasal (nivel de evidencia L5). Indicación original: Rinitis alérgica, rinitis vasomotora, faringitis, resfriado común…"
monitor_inn: "Dextromethorphan"
predicted_indications: ["acute laryngopharyngitis", "faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
---

# Dextromethorphan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Dextrometorfano: De Rinitis Alérgica y Cuadros de Vías Respiratorias Altas a Enfermedad de la Cavidad Nasal

## Resumen en Una Frase

Dextrometorfano es un antitusivo de uso muy extendido, cuyas indicaciones originales en el grafo de conocimiento incluyen rinitis alérgica, rinitis vasomotora, faringitis, resfriado común, nasofaringitis y cefalea.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal**, con **0 ensayos clínicos** y **0 publicaciones** que respalden actualmente esta dirección.
La predicción se basa únicamente en el modelo (nivel de evidencia L5).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica, rinitis vasomotora, faringitis, resfriado común, rinitis, nasofaringitis y cefalea (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 99,98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el dextrometorfano actúa como antagonista del receptor NMDA y agonista del receptor sigma-1, con actividad antitusiva central. Los datos farmacológicos compilados también lo asocian con GluN2C (GRIN2C), TAS2R1 y SIGMAR1.

La predicción parece derivarse de la cercanía en el grafo con indicaciones nasales ya conocidas (rinitis y rinitis vasomotora). La enfermedad de la cavidad nasal es una categoría amplia que engloba esas condiciones, por lo que el resultado podría reflejar en gran parte un solapamiento con indicaciones existentes y no un uso realmente nuevo.

No se ha establecido un vínculo mecanístico directo entre el dextrometorfano y la patología nasal. Sin ensayos ni literatura, la razonabilidad de la predicción no puede verificarse.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 57623 | Cinfatos Antitusivo 2 mg/ml solución oral | Solución oral | No disponible |
| 83679 | Intertos 15 mg comprimidos | Comprimido | No disponible |
| 67400 | Bicasan 2 mg/ml jarabe | Jarabe | No disponible |
| 24381 | Propalcof 15 mg comprimidos | Comprimido | No disponible |
| 57174 | Bisolvon Antitusivo 2 mg/ml jarabe | Jarabe | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): hipertensión, síndrome de QT largo (incluido el familiar), torsades de pointes, insuficiencia y enfermedad hepática, epilepsia, EPOC, úlcera gástrica y péptica, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, trombocitopenia, insuficiencia suprarrenal (enfermedad de Addison), hipotiroidismo, enfermedad inflamatoria intestinal, déficit de potasio, diabetes y cetoacidosis diabética, hiperplasia prostática benigna, bronquitis y trastornos hipotensivos, entre otras.
- **Interacciones y dianas farmacológicas**: se identificaron 3 dianas, GluN2C (GRIN2C), TAS2R1 y el receptor sigma-1 (SIGMAR1). Son interacciones de tipo farmacológico con dianas, no interacciones con otros fármacos con nivel de gravedad asignado.

Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles; consultar el prospecto para la información de seguridad oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje TxGNN muy alto, pero carece de ensayos clínicos y de literatura (nivel L5), y probablemente refleja la cercanía con indicaciones nasales ya conocidas más que una nueva indicación. Además, la información de seguridad del prospecto y el mecanismo de acción no están disponibles.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), ya que su ausencia bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, consultando DrugBank).
- Realizar una búsqueda sistemática de literatura y ensayos sobre dextrometorfano en patología nasal.
- Aclarar si la «enfermedad de la cavidad nasal» aporta algo realmente distinto de las indicaciones de rinitis ya conocidas.
- Evaluar la compatibilidad de las vías de administración y formas farmacéuticas, hoy pendiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

