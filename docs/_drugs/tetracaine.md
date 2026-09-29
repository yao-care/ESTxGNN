---
layout: default
title: Tetracaine
parent: Solo predicción del modelo (L5)
nav_order: 524
evidence_level: L5
indication_count: 9
---

# Tetracaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Tetracaína: De Anestesia Local a Acrodermatitis Crónica Atrófica

## Resumen en Una Frase

La tetracaína es un anestésico local (bloqueador de canales de sodio) que se comercializa en España en formas tópicas. El modelo TxGNN predice que podría ser efectivo para la **acrodermatitis crónica atrófica**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anestesia local tópica (inferida por la clase del fármaco y sus formas farmacéuticas; los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Acrodermatitis crónica atrófica |
| Puntaje de Predicción TxGNN | 99,93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, la tetracaína es un anestésico local que bloquea los canales de sodio y su uso está establecido en anestesia tópica.

Sin embargo, el análisis no encuentra un vínculo mecanístico plausible con la nueva indicación. La acrodermatitis crónica atrófica es una afección cutánea atrófica asociada a la infección por *Borrelia*. La tetracaína no tiene acción antimicrobiana ni antiinflamatoria conocida frente a ese proceso.

El puntaje alto del modelo (99,93%) refleja solo una asociación en el grafo de conocimiento. No hay ensayos ni literatura que lo respalden, por lo que esta predicción debe considerarse hipótesis de bajo respaldo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 80830 | TETRACAINA LAINCO 7,5 MG/G GEL | Gel |
| 15371 | ANESTESIA TÓPICA B. BRAUN 10 mg/ml SOLUCIÓN | Solución cutánea |
| 14534 | LUBRISTESIC 7,5 mg/g POMADA | Pomada |

Las tres autorizaciones son de uso tópico o cutáneo. Los textos de indicación aprobada no figuran en los datos recibidos.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no se encontraron registros de interacciones en la consulta realizada.
- **Señal de neurotoxicidad en uso espinal**: la literatura recuperada para otra predicción (síndrome de cola de caballo) describe casos de síndrome de cola de caballo tras anestesia espinal con tetracaína, incluidos informes de casos y estudios preclínicos. Esto es una señal de seguridad para la administración intratecal, no una oportunidad de reposicionamiento.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5, sin ensayos ni literatura, y carece de un vínculo mecanístico plausible entre un anestésico local y una afección cutánea atrófica de origen infeccioso. Las otras ocho indicaciones predichas también quedan en Hold. Ninguna tiene evidencia que respalde un reposicionamiento, y la de síndrome de cola de caballo es un signo de toxicidad.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío bloqueante para el cribado de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Obtener los textos de indicación aprobada de las tres autorizaciones.
- Buscar evidencia preclínica o clínica que vincule la tetracaína con la acrodermatitis crónica atrófica. Sin ella, no se recomienda avanzar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

