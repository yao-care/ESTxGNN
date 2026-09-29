---
layout: default
title: Avatrombopag
parent: Solo predicción del modelo (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Avatrombopag
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

# Avatrombopag: De Indicación Original No Registrada a Macrotrombocitopenia con Insuficiencia de la Válvula Mitral

## Resumen en Una Frase

Avatrombopag es un agonista del receptor de trombopoyetina (TPO-R) comercializado en España como Doptelet. Los datos recibidos no incluyen su indicación aprobada original.
El modelo TxGNN predice que podría ser efectivo para **macrotrombocitopenia con insuficiencia de la válvula mitral**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación de la autorización de AEMPS está vacío) |
| Nueva Indicación Predicha | Macrotrombocitopenia con insuficiencia de la válvula mitral |
| Puntaje de Predicción TxGNN | 99.995% |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la farmacología general, avatrombopag es un agonista del TPO-R que estimula la megacariopoyesis, es decir, la producción de plaquetas en la médula ósea. Mecanísticamente, podría ser aplicable a trastornos con recuento plaquetario bajo.

El nombre de la enfermedad predicha parece una variante de "macrotrombocitopenia", un grupo de trastornos hereditarios con plaquetas bajas y de gran tamaño. Un agonista del TPO-R solo ayudaría si el defecto genético de fondo reduce la producción de plaquetas pero deja intacta la vía de la trombopoyetina. Ese defecto no se conoce en este caso. Además, el componente valvular cardíaco (insuficiencia mitral) no se aborda con este mecanismo.

El vínculo es indirecto y solo plausible. Sin ensayos ni literatura, el puntaje alto del modelo no basta para sustentar una decisión clínica.

### Otras Predicciones en el Top 10

| Enfermedad Predicha | Puntaje TxGNN | Plausibilidad Mecanística |
|------|------|------|
| Trombocitopenia hereditaria con plaquetas normales | 99.995% | Indirecta y plausible. El nombre de la enfermedad es internamente inconsistente y requiere aclarar fenotipo y genotipo. |
| Trombocitopenia neonatal transitoria | 99.995% | Encaja mecanísticamente, pero es autolimitada y no hay datos de seguridad ni dosificación neonatal. |
| Enfermedad de gránulos densos | 99.995% | Débil. Es un defecto de función plaquetaria, no de recuento. |
| Esclerosis lateral amiotrófica (ELA) y entidades afines (susceptibilidad a ELA, síndrome de neurona motora inferior de inicio tardío, síndrome de Mills, amiotrofia monomélica) | 99.991%–99.993% | Sin vínculo plausible. Probablemente son artefactos del grafo de conocimiento. |
| Polimicrogiria parasagital parieto-occipital bilateral | 99.992% | Sin vínculo plausible. Es una malformación cortical estructural. |

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
| 1191373 | DOPTELET 20 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA (Swedish Orphan Biovitrum AB) | Comprimido recubierto con película | No especificada en los datos recibidos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura. El fenotipo predicho es ambiguo y no hay datos de seguridad del prospecto de AEMPS. Esta falta de datos de seguridad impide pasar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), pendiente de forma bloqueante.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada original de Doptelet en España.
- Aclarar el fenotipo y el defecto genético de la enfermedad predicha, y verificar si responde a la vía TPO-R.
- Buscar literatura y ensayos sobre agonistas del TPO-R en macrotrombocitopenias hereditarias.

*Los resultados son solo para fines de investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

