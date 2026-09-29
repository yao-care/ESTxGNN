---
layout: default
title: Doravirine
parent: Solo predicción del modelo (L5)
nav_order: 181
evidence_level: L5
indication_count: 3
---

# Doravirine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Doravirina: De Infección por VIH-1 a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Doravirina es un inhibidor no nucleósido de la transcriptasa inversa (ITINN) utilizado para tratar la infección por VIH-1.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (el texto de indicación de la autorización no está disponible; se toma del conocimiento general sobre el fármaco) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, doravirina es un ITINN, es decir, inhibe la transcriptasa inversa del VIH-1 uniéndose a un sitio alostérico de la enzima. Su eficacia en VIH-1 está comprobada. Mecanísticamente, podría ser aplicable al virus de la inmunodeficiencia felina (VIF) por ser este también un lentivirus.

La relación entre ambas indicaciones es de vecindad en el grafo de conocimiento: el VIH-1 y el VIF pertenecen al mismo género viral. Esto explica el puntaje alto (0.9993), pero **no es evidencia de eficacia**.

Hay una limitación importante: los ITINN suelen tener poca actividad frente a transcriptasas inversas de lentivirus distintos del VIH-1, porque el bolsillo de unión difiere. No se aportaron datos específicos sobre VIF. Por eso el puntaje refleja probablemente la proximidad en el grafo y no una actividad antiviral demostrada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181332001 | PIFELTRO 100 mg comprimidos recubiertos con película (Merck Sharp & Dohme B.V.) | Comprimido recubierto con película | No especificada en los datos disponibles |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo, sin ensayos ni literatura (nivel L5). Además, hay razones farmacológicas para dudar de la actividad de los ITINN fuera del VIH-1. Las otras predicciones del modelo tampoco avanzan:
- **Infección por virus de inmunodeficiencia de simios:** el único artículo recuperado trata de islatravir en VIH-1 y no respalda a doravirina.
- **Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y reducción de sustancia blanca cortical:** no hay vínculo mecanístico creíble y probablemente es un artefacto del grafo.

**Para avanzar se necesita:**
- Datos de susceptibilidad *in vitro* de doravirina frente al VIF (y, si se explora el VIS, frente al VIS o en modelos de primates no humanos)
- Datos detallados del mecanismo de acción (MOA)
- Advertencias y contraindicaciones del prospecto de la AEMPS, hoy no disponibles, para completar el cribado de seguridad
- Evaluación de la relevancia veterinaria, porque la indicación predicha es una enfermedad animal y no humana
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

