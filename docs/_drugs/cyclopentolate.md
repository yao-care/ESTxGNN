---
layout: default
title: Cyclopentolate
parent: Solo predicción del modelo (L5)
nav_order: 149
evidence_level: L5
indication_count: 3
---

# Cyclopentolate
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

# Ciclopentolato: De Uso Oftálmico (Colirio Cicloplégico) a Síndrome de Cauda Equina

## Resumen en Una Frase

Ciclopentolato es un fármaco de uso oftálmico, comercializado en España como colirio cicloplégico.
El modelo TxGNN predice que podría ser efectivo para **síndrome de cauda equina**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Uso oftálmico como cicloplégico (según el nombre del producto; el registro no incluye texto de indicación) |
| Nueva Indicación Predicha | Síndrome de cauda equina |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según el conocimiento farmacológico general, el ciclopentolato es un antagonista muscarínico. En oftalmología se usa para dilatar la pupila y paralizar la acomodación.

El síndrome de cauda equina es una compresión de las raíces nerviosas de la parte baja de la médula. Es una urgencia quirúrgica. Un antimuscarínico, como mucho, podría aliviar síntomas vesicales o intestinales. No actúa sobre la compresión nerviosa que causa la enfermedad, así que no hay una justificación modificadora de la enfermedad. Este vínculo se infiere de la farmacología general, no de los datos aportados.

Además, el ciclopentolato es un agente oftálmico tópico con exposición sistémica limitada y riesgo conocido de toxicidad en el sistema nervioso central, sobre todo en niños. Por todo ello, la predicción se apoya solo en el puntaje del modelo.

**Otras predicciones del modelo (también sin evidencia clínica, nivel L5, Hold):**
- **Vejiga neurógena** (puntaje 99.40%): los antimuscarínicos son una clase establecida para la hiperactividad del detrusor, por lo que el vínculo de clase es plausible. Ya existen antimuscarínicos sistémicos aprobados, así que un fármaco oftálmico aportaría poco valor. El término de la enfermedad figura como obsoleto y debe mapearse a una ontología vigente antes de cualquier revisión.
- **Síndrome del intestino irritable** (puntaje 99.27%): antimuscarínicos antiespasmódicos como diciclomina o hiosciamina se usan para el dolor abdominal. No hay datos del ciclopentolato por vía sistémica o en uso gastrointestinal, y su perfil de efectos adversos centrales lo hace poco competitivo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 42117 | COLIROFTA CICLOPLÉJICO 10 MG/ML COLIRIO EN SOLUCIÓN | Colirio en solución | Alcon Healthcare S.A. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se dispone de advertencias, contraindicaciones ni interacciones farmacológicas registradas en el paquete de evidencia.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo cuenta con el puntaje de TxGNN (nivel L5), sin ensayos ni publicaciones. Además, el mecanismo no explica un beneficio sobre la causa del síndrome de cauda equina, y la formulación oftálmica y su perfil de toxicidad central la hacen poco adecuada.

**Para avanzar se necesita:**
- Prospecto de AEMPS con advertencias y contraindicaciones, para poder hacer el cribado de seguridad
- Datos del mecanismo de acción desde DrugBank
- Reasignar la vejiga neurógena a un término vigente de la ontología
- Evidencia clínica o preclínica de ciclopentolato en las indicaciones predichas
- Evaluación de la compatibilidad de vía de administración, ya que un colirio no cubre un uso sistémico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

