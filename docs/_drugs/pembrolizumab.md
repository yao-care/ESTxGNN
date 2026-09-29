---
layout: default
title: Pembrolizumab
parent: Solo predicción del modelo (L5)
nav_order: 412
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

# Pembrolizumab: De Indicaciones Oncológicas a Fibromatosis Gingival

## Resumen en Una Frase

Pembrolizumab es un anticuerpo monoclonal inhibidor del punto de control inmunitario PD-1, comercializado en España como Keytruda y usado en oncología. El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, que por ahora es solo una señal del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible: los registros de autorización no incluyen el texto de indicación aprobada |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 99.40% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, pembrolizumab es un inhibidor de PD-1 que refuerza la respuesta de los linfocitos T contra las células tumorales. Su eficacia está establecida en cánceres como el pulmonar no microcítico, aunque el registro no detalla las indicaciones autorizadas en España.

La fibromatosis gingival es un sobrecrecimiento fibroso no neoplásico, generalmente hereditario o inducido por fármacos. No tiene relación conocida con el eje PD-1/PD-L1, y no se identificó ningún fundamento mecanístico que justifique el bloqueo de puntos de control en esta enfermedad.

El puntaje alto (99.40%) refleja proximidad en el grafo de conocimiento, no evidencia biológica ni clínica. Por eso esta predicción debe tratarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

El registro no incluye el texto de indicación aprobada para ninguna autorización. Se muestran las 5 autorizaciones principales, de un total de 7.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1151024002IP3 | KEYTRUDA 25 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión |
| 1151024001 | KEYTRUDA 50 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión |
| 115024001IP | KEYTRUDA 50 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión |
| 1151024002IP | KEYTRUDA 25 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión |
| 1151024002IP2 | KEYTRUDA 25 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión |

Titular de todas: Merck Sharp & Dohme B.V.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo anti-PD-1); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Bajo como efecto directo; pueden aparecer citopenias de origen inmunomediado |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma, función hepática, renal y tiroidea, glucemia. Vigilar eventos adversos inmunomediados |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y los protocolos del centro para preparación de medicamentos biológicos antineoplásicos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción está en nivel L5: solo hay una señal del modelo, sin ensayos, sin literatura y sin fundamento mecanístico plausible. Además, la fibromatosis gingival es una condición benigna en la que la toxicidad inmunomediada de un inhibidor de puntos de control difícilmente se justificaría.

**Para avanzar se necesita:**
- Completar los datos de mecanismo de acción (DrugBank).
- Obtener la ficha técnica de la AEMPS con indicaciones, advertencias y contraindicaciones.
- Encontrar evidencia biológica o preclínica que vincule PD-1 con la fibrosis gingival; sin ella no conviene seguir con esta candidata.
- Revisar el resto de las predicciones del modelo: la mayoría carece de respaldo, y las de carcinoma del hilio pulmonar, neoplasia del surco pulmonar y neoplasia benigna de pulmón se solapan con las indicaciones de cáncer de pulmón ya establecidas. Deberían evaluarse dentro de esas indicaciones y no como reposicionamientos nuevos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

