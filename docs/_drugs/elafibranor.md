---
layout: default
title: Elafibranor
parent: Solo predicción del modelo (L5)
nav_order: 280
evidence_level: L5
indication_count: 1
---

# Elafibranor
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Elafibranor: De Colangitis Biliar Primaria a Amenorrea

## Resumen en Una Frase

Elafibranor es un agonista dual de los receptores PPARα y PPARδ, desarrollado inicialmente para la esteatohepatitis no alcohólica (NASH) y reposicionado después para la colangitis biliar primaria, indicación autorizada por la FDA (junio de 2024) y la EMA (septiembre de 2024).
El modelo TxGNN predice que podría ser efectivo para **amenorrea**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Colangitis biliar primaria (según los datos farmacológicos compilados; el texto de indicación de la autorización española está vacío) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Elafibranor es un agonista dual de PPARα y PPARδ (genes *PPARA* y *PPARD*). Se convierte en el hígado en su principal metabolito activo, GFT-1007. En estudios preclínicos redujo la acumulación de grasa hepática, la inflamación y la fibrosis. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco; la información anterior procede de los datos farmacológicos de los dianas.

La relación con la amenorrea es especulativa. La señalización PPAR influye en el metabolismo de lípidos y glucosa y en la inflamación, y posiblemente en la función ovárica e hipotálamo-hipofisaria. Esto podría ser relevante para causas metabólicas y endocrinas de amenorrea, como la disfunción ovulatoria asociada al síndrome de ovario poliquístico. Ningún dato compilado respalda este vínculo.

Además, el puntaje tan alto (99.86%) puede reflejar artefactos de la topología del grafo de conocimiento, como vecinos compartidos con otros agonistas PPAR o fármacos metabólicos. Debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1241855001 | IQIRVO 80 MG comprimidos recubiertos con película (Ipsen Pharma) | Comprimido recubierto con película | No disponible en el texto de la autorización |

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología**: la consulta se completó y devolvió 2 registros, ambos de naturaleza farmacológica (dianas) y no interacciones con otros fármacos con nivel de gravedad: PPARα (*PPARA*) y PPARβ/δ (*PPARD*). En los ensayos de fase 1/2 no se detectaron señales de seguridad específicas.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y con vínculo mecanístico especulativo. Además, faltan los datos de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), incluida la indicación aprobada
- Completar los datos del mecanismo de acción desde DrugBank
- Revisión de literatura y de registros de ensayos sobre PPAR y amenorrea/función ovárica (p. ej., síndrome de ovario poliquístico)
- Evaluar si el puntaje es un artefacto del grafo mediante análisis de los vecinos compartidos
- Evaluar la seguridad en mujeres en edad fértil (embarazo y fertilidad) antes de cualquier estudio exploratorio
- Estudios preclínicos o de mecanismo que respalden el vínculo con el eje reproductivo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

