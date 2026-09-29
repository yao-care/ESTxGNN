---
layout: default
title: Avapritinib
parent: Solo predicción del modelo (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib: De Inhibidor de Quinasas KIT/PDGFRA a Displasia Espondilometafisaria Axial

## Resumen en Una Frase

Avapritinib es un inhibidor de quinasas de las familias KIT/PDGFRA, comercializado en España con el nombre Ayvakyt. Los datos de autorización recibidos no detallan su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para la **displasia espondilometafisaria axial**, una displasia esquelética rara, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección. La predicción es puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de autorización de la AEMPS recibidos |
| Nueva Indicación Predicha | Displasia espondilometafisaria axial |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, avapritinib es un inhibidor de quinasas KIT/PDGFRA de uso oncológico. No hay datos que permitan trazar un vínculo mecanístico con la displasia espondilometafisaria axial.

Con la información disponible, **no se ha establecido ningún vínculo mecanístico**. Se trata de una displasia esquelética rara sin conexión conocida con las rutas de KIT o PDGFRA. El único respaldo es el puntaje elevado del grafo de conocimiento de TxGNN (0.9992), que es una predicción computacional y no evidencia.

Además, la similitud con la indicación original queda pendiente de evaluación. Conviene interpretar el puntaje con cautela: entre las 10 primeras predicciones, siete pertenecen al grupo de esclerosis lateral amiotrófica (ELA) y enfermedades de la motoneurona. Esto sugiere que los puntajes reflejan agrupamiento por vecindad en el grafo y no señales independientes.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1201473004 | Ayvakyt 25 mg | Comprimido recubierto con película |
| 1201473005 | Ayvakyt 50 mg | Comprimido recubierto con película |
| 1201473001 | Ayvakyt 100 mg | Comprimido recubierto con película |
| 1201473002 | Ayvakyt 200 mg | Comprimido recubierto con película |
| 1201473003 | Ayvakyt 300 mg | Comprimido recubierto con película |

Titular de todas las autorizaciones: Blueprint Medicines (Netherlands) B.V.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de quinasas KIT/PDGFRA) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Señales neurológicas**: el análisis de las predicciones señala eventos adversos del sistema nervioso central asociados a avapritinib (hemorragia intracraneal y efectos cognitivos). Esto es relevante para cualquier uso neurológico. Esta información no proviene de las advertencias del prospecto de la AEMPS, que no se recibieron.
- **Interacciones farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.

Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible. Las señales de seguridad del sistema nervioso central añaden cautela.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), que es un requisito bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar evidencia preclínica que relacione KIT/PDGFRA con la displasia espondilometafisaria axial.
- Revisar el agrupamiento de predicciones en torno a ELA y enfermedades de la motoneurona antes de darles peso.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

