---
layout: default
title: Rufinamide
parent: Solo predicción del modelo (L5)
nav_order: 479
evidence_level: L5
indication_count: 5
---

# Rufinamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Rufinamida: De Indicación Original No Registrada a Síndrome de Epilepsia Relacionada con Infección Febril (FIRES)

## Resumen en Una Frase

Rufinamida se comercializa en España como INOVELON (Eisai), pero los datos de autorización recibidos no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de epilepsia relacionada con infección febril (FIRES)**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción solo del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización recibidos |
| Nueva Indicación Predicha | Síndrome de epilepsia relacionada con infección febril (FIRES) |
| Puntaje de Predicción TxGNN | 99.57% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información recibida. Rufinamida se describe de forma general como un modulador de canales de sodio, lo que ofrece una lógica antiepiléptica plausible. Esta descripción no está confirmada por los datos del expediente.

FIRES es un síndrome epiléptico refractario asociado a inflamación. La predicción del modelo proviene de asociaciones en el grafo de conocimiento con fenotipos epilépticos. Los datos disponibles no muestran que modular los canales de sodio actúe sobre el componente inflamatorio del síndrome, por lo que la plausibilidad mecanística sigue sin verificarse.

En resumen, el puntaje del modelo es muy alto (99.57%), pero sin ensayos, literatura ni MOA confirmado, esta hipótesis debe tratarse como una señal para investigar y no como un hallazgo respaldado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 06378009 | INOVELON 200 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |
| 06378001 | INOVELON 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |
| 06378017 | INOVELON 40 mg/ml suspensión oral | Suspensión oral | No especificada en los datos |
| 06378015 | INOVELON 400 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |

Titular: Eisai GmbH.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin mecanismo de acción ni datos de seguridad confirmados. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un requisito bloqueante antes del cribado de seguridad.
- Confirmar el mecanismo de acción (por ejemplo, consultando DrugBank) y analizar su vínculo con la fisiopatología de FIRES.
- Confirmar la indicación aprobada de INOVELON en España, ausente en los datos actuales.
- Buscar casos clínicos, series de casos o estudios preclínicos sobre rufinamida en FIRES.
- Evaluar la compatibilidad de vía y forma farmacéutica (suspensión oral y comprimidos disponibles), hoy pendiente.

**Otras predicciones del modelo (todas L5, Hold, sin ensayos ni literatura):** mioclonías perioorales con ausencias (99.51%), epilepsia del lóbulo occipital fotosensible (99.44%), espasmos epilépticos criptogénicos de inicio tardío (99.44%) y epilepsia infantil atípica con puntas centrotemporales (99.44%).

*Este informe es solo para referencia de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

