---
layout: default
title: Reslizumab
parent: Solo predicción del modelo (L5)
nav_order: 693
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Reslizumab: nueva indicación predicha, Trombocitopenia por destrucción inmune (nivel de evidencia L5). Indicación original: Neumonía eosinofílica / eosinofilia pulmonar (según el grafo de conoc…"
monitor_inn: "RESLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets"]
---

# Reslizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Reslizumab: De Neumonía Eosinofílica a Trombocitopenia por Destrucción Inmune

## Resumen en Una Frase

Reslizumab es un anticuerpo monoclonal anti-IL-5, asociado originalmente a enfermedades eosinofílicas pulmonares (neumonía eosinofílica y eosinofilia pulmonar).
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia por destrucción inmune**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Neumonía eosinofílica / eosinofilia pulmonar (según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Trombocitopenia por destrucción inmune |
| Puntaje de Predicción TxGNN | 99,53 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, reslizumab es un anticuerpo monoclonal que bloquea la interleucina-5 (IL-5), la principal señal de supervivencia de los eosinófilos, y su uso se relaciona con enfermedades eosinofílicas.

No existe un mecanismo establecido que vincule el bloqueo de IL-5 con la destrucción inmune de plaquetas. La trombocitopenia inmune (por ejemplo, la PTI) se debe principalmente a autoanticuerpos, desregulación de linfocitos T y aclaramiento mediado por macrófagos. Una posible conexión, de carácter especulativo, sería la reducción de la inflamación asociada a eosinófilos en trombocitopenias inmunes secundarias con eosinofilia.

Por tanto, el elevado puntaje de TxGNN (99,53 %) es solo una predicción computacional, sin respaldo clínico ni bibliográfico en los datos compilados. La similitud con la indicación original no ha sido evaluada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161125001 | CINQAERO 10 MG/ML (concentrado para solución para perfusión), Teva B.V. | Concentrado para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre el bloqueo de IL-5 y la destrucción inmune de plaquetas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), requisito bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisión de literatura específica sobre IL-5/eosinófilos en trombocitopenia inmune.
- Evaluar hipótesis mecanística (p. ej., trombocitopenia inmune secundaria con eosinofilia) y, de ser plausible, estudios preclínicos o de mecanismo.
- Evaluar la compatibilidad de la vía de administración (actualmente pendiente).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

