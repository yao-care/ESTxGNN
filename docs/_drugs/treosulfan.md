---
layout: default
title: Treosulfan
parent: Solo predicción del modelo (L5)
nav_order: 820
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Treosulfan: nueva indicación predicha, Catarata diabética (nivel de evidencia L5). Indicación original: No disponible en los datos de autorización (el texto de indicación es…"
monitor_inn: "treosulfan"
predicted_indications: ["diabetic cataract"]
---

# Treosulfan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Treosulfán: De Indicación Original No Registrada a Catarata Diabética
{: .text-alpha }

## Resumen en Una Frase

Treosulfán es un agente alquilante bifuncional que, según los datos compilados para este informe, no tiene un texto de indicación aprobada registrado en las autorizaciones españolas; en la práctica clínica se utiliza para el acondicionamiento previo al trasplante de progenitores hematopoyéticos y en cáncer de ovario.
El modelo TxGNN predice que podría ser efectivo para **catarata diabética**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Catarata diabética |
| Puntaje de Predicción TxGNN | 99,01% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, treosulfán es un profármaco alquilante bifuncional que se convierte en especies epóxido que entrecruzan el ADN. Este efecto citotóxico es la base de su uso en acondicionamiento previo al trasplante hematopoyético y en cáncer de ovario.

La relación con la nueva indicación es muy débil. La catarata diabética se asocia con la activación de la vía de los polioles (aldosa reductasa), el estrés oxidativo y la opacificación del cristalino mediada por productos de glicación avanzada (AGE) y osteopontina. Ninguno de estos procesos tiene un vínculo mecanístico establecido con el entrecruzamiento del ADN.

La predicción probablemente refleja la proximidad en el grafo de conocimiento y no una plausibilidad biológica real. Además, la toxicidad sistémica mielosupresora y genotóxica haría muy improbable un perfil beneficio-riesgo favorable en una enfermedad ocular no maligna y de progresión lenta.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181351003 | TRECONDI 5 G polvo para solución para perfusión | Polvo para solución para perfusión | No registrada en los datos disponibles |
| 83122 | Treosulfano Zentiva 5 g polvo para solución para perfusión EFG | Polvo para solución inyectable y para perfusión | No registrada en los datos disponibles |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante bifuncional) |
| Riesgo de Mielosupresión | Alto (mielosupresión profunda inherente al uso en acondicionamiento) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base es un puntaje alto del modelo TxGNN, sin ensayos clínicos ni literatura, y sin un vínculo mecanístico plausible entre el entrecruzamiento del ADN y la patogenia de la catarata diabética. El perfil de toxicidad sistémica tampoco es compatible con una enfermedad ocular no maligna.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), requisito bloqueante para el cribado de seguridad
- Datos detallados del mecanismo de acción (MOA) desde DrugBank
- Evidencia preclínica que respalde un vínculo biológico con la vía de los polioles o el estrés oxidativo del cristalino
- Evaluación de compatibilidad de vía de administración (ocular frente a perfusión intravenosa)
- Confirmar las indicaciones aprobadas en las autorizaciones españolas
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

