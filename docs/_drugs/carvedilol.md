---
layout: default
title: Carvedilol
parent: Solo predicción del modelo (L5)
nav_order: 106
evidence_level: L5
indication_count: 5
---

# Carvedilol
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

# Carvedilol: De Indicación Original No Registrada a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Carvedilol es un betabloqueante no selectivo con bloqueo alfa-1 que está comercializado en España, pero los datos recibidos no incluyen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (las autorizaciones de la AEMPS no traen texto de indicación) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.55% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, carvedilol es un betabloqueante no selectivo con bloqueo alfa-1. Esto sugiere un posible efecto antihipertensivo y vasodilatador, por lo que mecanísticamente podría ser aplicable a cuadros de hipertensión grave.

Sin embargo, este vínculo se basa únicamente en la puntuación de TxGNN (0.995). No se aportó ningún ensayo ni publicación que apoye su uso en hipertensión renovascular o maligna. Además, la hipertensión maligna es una emergencia hipertensiva que normalmente se maneja con fármacos intravenosos titulables, de modo que un betabloqueante oral no encaja de forma natural.

Otras predicciones del modelo (hipertensión maligna con daño renal, dos grupos de hipertensión pulmonar y síndrome de Braddock) tienen puntuaciones similares (0.994–0.995) y tampoco cuentan con evidencia clínica. Los dos primeros resultados tienen puntuaciones idénticas, lo que sugiere que provienen del mismo entorno del grafo y no de señales independientes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones. Ninguna incluye texto de indicación aprobada en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 59695 | COROPRES 25 mg COMPRIMIDOS | Comprimido | Cheplapharm Arzneimittel Gmbh |
| 65885 | CARVEDILOL CINFAMED 6,25 mg COMPRIMIDOS EFG | Comprimido recubierto con película | Laboratorios Cinfa S.A. |
| 66921 | CARVEDILOL TEVA 25 mg COMPRIMIDOS EFG | Comprimido | Teva Pharma S.L.U. |
| 61281 | COROPRES 6,25 mg COMPRIMIDOS | Comprimido | Cheplapharm Arzneimittel Gmbh |
| 70697 | CARVEDILOL TEVA-RATIOPHARM 25 mg COMPRIMIDOS EFG | Comprimido recubierto con película | Teva Pharma S.L.U. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como nota del análisis, el bloqueo beta podría reducir la contractilidad del ventrículo derecho y el gasto cardíaco en pacientes con hipertensión pulmonar. Esto sería una preocupación de seguridad si se explorara esa dirección.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene una puntuación alta (99.55%), pero no cuenta con ensayos clínicos ni literatura específica (nivel L5). Además, la hipertensión maligna se trata normalmente con fármacos intravenosos, y no hay datos de mecanismo ni de seguridad que respalden avanzar.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), lo cual bloquea el cribado de seguridad
- Obtener los datos del mecanismo de acción desde DrugBank
- Hacer una búsqueda dirigida de literatura sobre carvedilol en hipertensión renovascular y maligna, y revisar si existen ensayos
- Evaluar la compatibilidad de la vía de administración (oral frente a intravenosa) y la similitud con la indicación original
- Realizar una evaluación de seguridad específica antes de considerar cualquier predicción de hipertensión pulmonar

*Este informe es solo de referencia para la investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

