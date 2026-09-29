---
layout: default
title: Brolucizumab
parent: Solo predicción del modelo (L5)
nav_order: 83
evidence_level: L5
indication_count: 4
---

# Brolucizumab
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

# Brolucizumab: De Anti-VEGF Intravítreo (indicación original no registrada) a Trastorno Mitocondrial de la Fosforilación Oxidativa por Anomalías del ADN Nuclear

## Resumen en Una Frase

Brolucizumab es un fragmento de anticuerpo de cadena única anti-VEGF-A que se administra por vía intravítrea. Los datos recibidos no incluyen su indicación original aprobada.
El modelo TxGNN predice que podría ser efectivo para el **trastorno mitocondrial de la fosforilación oxidativa por anomalías del ADN nuclear**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Trastorno mitocondrial de la fosforilación oxidativa por anomalías del ADN nuclear |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se ha identificado un vínculo mecanístico plausible. Brolucizumab bloquea VEGF-A y se administra en el ojo. La inhibición de VEGF no tiene un papel conocido en los defectos de fosforilación oxidativa causados por el ADN nuclear. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia.

El puntaje alto (0.997) proviene solo de la predicción del grafo de conocimiento, sin ensayos ni literatura de apoyo. Por eso debe interpretarse como una señal computacional y no como evidencia de eficacia.

Otras predicciones del modelo para este fármaco tampoco cuentan con evidencia (todas L5, decisión Hold):
- **Várices esofágicas con sangrado y sin sangrado** (puntaje 99.12%): existe una lógica biológica indirecta, ya que la angiogénesis dependiente de VEGF contribuye a la hipertensión portal. Sin embargo, la vía intravítrea implica una exposición sistémica mínima, por lo que es poco probable que el fármaco llegue a la circulación esplácnica. Ambos nodos comparten el mismo puntaje, lo que sugiere que son nodos duplicados o hermanos y no señales independientes.
- **Insuficiencia pancreática exocrina** (puntaje 99.07%): no hay vínculo mecanístico creíble, porque el bloqueo de VEGF-A no corrige la pérdida de secreción de enzimas digestivas.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191417 | BEOVU 120 MG/ML SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA (Novartis Europharm Limited) | Solución inyectable en jeringa precargada | No disponible en los datos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como referencia, el análisis mecanístico señala que brolucizumab conlleva advertencias de inflamación intraocular y vasculitis retiniana. No se han consultado los datos oficiales de la AEMPS, y no se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni publicaciones. Además, no hay un vínculo mecanístico plausible con la enfermedad mitocondrial, y falta información básica de seguridad e indicación.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto/ficha técnica de la AEMPS (advertencias, contraindicaciones e indicación aprobada), que hoy bloquea el cribado de seguridad.
- Obtener el mecanismo de acción desde DrugBank.
- Evaluar la compatibilidad de la vía de administración (intravítrea) con el tejido diana de cada indicación predicha.
- Buscar evidencia preclínica o clínica independiente antes de reconsiderar cualquier indicación.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

