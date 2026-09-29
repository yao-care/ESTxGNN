---
layout: default
title: Ziprasidone
parent: Solo predicción del modelo (L5)
nav_order: 573
evidence_level: L5
indication_count: 10
---

# Ziprasidone
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

# Ziprasidona: De Esquizofrenia a Tricotilomanía

## Resumen en Una Frase

Ziprasidona es un antipsicótico atípico, utilizado clínicamente en esquizofrenia y en episodios maníacos o mixtos del trastorno bipolar.
El modelo TxGNN predice que podría ser efectivo para **tricotilomanía**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción basada solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia y trastornos psicóticos relacionados (según la ficha farmacológica de referencia; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Tricotilomanía |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de una descripción formal del mecanismo de acción. Sin embargo, el perfil farmacológico de referencia muestra que ziprasidona se une a varios receptores serotoninérgicos (5-HT1A, 1B, 1D, 1E, 2A, 2C y 7), al receptor de dopamina D2 y al receptor de histamina H1. También actúa sobre los transportadores de noradrenalina (NET) y de serotonina (SERT).

La tricotilomanía es un trastorno del control de impulsos y de conductas repetitivas. Mecanísticamente, el antagonismo 5-HT2A/D2 podría guardar cierta relación con las conductas compulsivas o de control de impulsos. Es una hipótesis plausible, pero no está respaldada por ningún ensayo ni publicación recuperados.

La similitud con la indicación original aún no se ha evaluado. Además, el puntaje del modelo es muy alto (99.83%) pero no equivale a evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 64851 | ZELDOX 20 mg cápsulas duras | Cápsula dura | Viatris Healthcare Limited |
| 75683 | ZIPRASIDONA STADA 40 mg cápsulas duras EFG | Cápsula dura | Laboratorio Stada S.L. |
| 80957 | ZIPRASIDONA CINFA 80 mg cápsulas duras EFG | Cápsula dura | Laboratorios Cinfa S.A. |
| 78167 | ZIPRASIDONA AUROBINDO 60 mg cápsulas duras EFG | Cápsula dura | Laboratorios Aurobindo S.L.U. |
| 83770 | ZIPRASIDONA AUROVITAS 20 mg cápsulas duras EFG | Cápsula dura | Aurovitas Spain, S.A.U. |

Existe también una presentación en polvo para solución inyectable. El texto de indicación aprobada no figura en los registros recibidos.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

Las 11 entradas del apartado de interacciones del paquete de datos corresponden a dianas farmacológicas (receptores y transportadores), no a interacciones con otros fármacos. Por tanto, no se dispone de un listado de interacciones farmacológicas reales. Otras secciones del paquete señalan la vigilancia del intervalo QTc y del perfil metabólico como cuestiones de seguridad relevantes de ziprasidona.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para tricotilomanía es de nivel L5: solo puntaje del modelo, sin ensayos ni literatura que la respalden. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Una revisión de la literatura específica de ziprasidona en tricotilomanía y en trastornos de control de impulsos, para comprobar si existe algún estudio.
- Los textos de indicación y el prospecto de AEMPS (advertencias y contraindicaciones), aún no disponibles.
- Datos de mecanismo de acción de una fuente formal como DrugBank.
- Una evaluación de la similitud con la indicación original.

**Nota sobre otras predicciones del mismo paquete:**
- **Trastorno afectivo mayor** (puesto 3, puntaje 99.66%): cuenta con múltiples ensayos de Fase 3 completados y evidencia clasificada como L1, con recomendación "Proceed with Guardrails". Probablemente se solape con el uso ya conocido en manía bipolar, por lo que no sería un reposicionamiento genuino. Sería la línea más sólida para evaluar en un informe propio.
- **Síndrome de Tourette** (puesto 7, puntaje 99.63%): tiene un estudio piloto pediátrico y revisiones, con evidencia L3. Requiere prudencia por la seguridad cardíaca (QTc) en población pediátrica.

*Este informe es solo para referencia de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

