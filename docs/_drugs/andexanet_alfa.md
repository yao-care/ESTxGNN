---
layout: default
title: Andexanet Alfa
parent: Solo predicción del modelo (L5)
nav_order: 43
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Andexanet alfa: De la reversión de inhibidores del factor Xa a la trombastenia de Glanzmann

## Resumen en Una Frase

Andexanet alfa es una proteína recombinante que neutraliza los anticoagulantes inhibidores del factor Xa. Se comercializa en España como ONDEXXYA, aunque el texto de indicación de la autorización no está disponible en los datos recibidos.
El modelo TxGNN predice que podría ser efectivo para la **trombastenia de Glanzmann**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. La predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Trombastenia de Glanzmann |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Andexanet alfa es un señuelo recombinante del factor Xa, catalíticamente inactivo. Se une a los inhibidores directos e indirectos del FXa y los neutraliza, y su uso conocido es revertir el efecto anticoagulante en caso de sangrado. No hay datos detallados del mecanismo de acción original en el Evidence Pack, así que este resumen se basa en la descripción farmacológica general.

**Con la información disponible, la predicción no parece razonable mecanísticamente.** La trombastenia de Glanzmann se debe a un defecto de la integrina plaquetaria αIIbβ3, y andexanet alfa no tiene efecto conocido sobre la agregación plaquetaria. El puntaje alto (0.998) probablemente refleja cercanía en el grafo de conocimiento de coagulación y trastornos hemorrágicos, no un mecanismo terapéutico real.

Las otras tres indicaciones predichas siguen el mismo patrón: trastorno primario de liberación plaquetaria, pseudo-enfermedad de von Willebrand y hemofilia. Todas tienen puntajes altos (99.1% a 99.8%), no muestran un vínculo mecanístico plausible y quedan en Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la trombastenia de Glanzmann.

Como referencia, la cuarta indicación predicha (hemofilia) tiene 11 publicaciones asociadas, pero se centran en la reversión de anticoagulantes anti-FXa, la interferencia de los DOAC en pruebas de laboratorio y agentes hemostáticos en general. Ninguna evalúa andexanet alfa en pacientes con hemofilia.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1181345001 | ONDEXXYA 200 MG POLVO PARA SOLUCION PARA PERFUSION | Polvo para solución para perfusión | Astrazeneca Ab |

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones del prospecto de la AEMPS, y no se encontraron interacciones farmacológicas registradas. Consultar el prospecto para información de seguridad.

Según el análisis mecanístico del Evidence Pack, andexanet alfa tiene un riesgo tromboembólico conocido. Esto pesa en contra de usarlo en trastornos hemorrágicos plaquetarios sin un fundamento sólido.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero no cuenta con ensayos clínicos ni literatura (nivel L5), y no hay un mecanismo plausible que la respalde. El fármaco tampoco corrige el defecto plaquetario de fondo y conlleva un riesgo tromboembólico.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), un vacío que bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Disponer de evidencia preclínica que justifique un efecto sobre la función plaquetaria antes de reconsiderar esta indicación.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

