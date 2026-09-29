---
layout: default
title: Emicizumab
parent: Solo predicción del modelo (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: De Hemofilia A a Enfermedad de von Willebrand Pseudo (Tipo Plaquetario)

## Resumen en Una Frase

Emicizumab es un anticuerpo biespecífico que se usa en la hemofilia A, aunque los textos de autorización en España no detallan la indicación.
El modelo TxGNN predice que podría ser efectivo para **pseudo-enfermedad de von Willebrand**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia A (según la literatura del paquete de evidencia; los textos de autorización en España no la especifican) |
| Nueva Indicación Predicha | Pseudo-enfermedad de von Willebrand (pseudo-von Willebrand disease) |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, emicizumab es un anticuerpo biespecífico que imita la función del factor VIII activado (FVIIIa) al unir los factores IXa y X. Su eficacia en la hemofilia A está bien establecida.

**Esta predicción es débil desde el punto de vista biológico.** La pseudo-enfermedad de von Willebrand es un trastorno plaquetario causado por una ganancia de función del receptor GPIb-alfa. No es una deficiencia del cofactor FVIII, así que no existe un fundamento mecanístico directo para que emicizumab sea útil. La similitud con la indicación original no se ha evaluado.

El puntaje alto del modelo (99.99%) refleja probablemente una cercanía dentro del grafo de conocimiento entre trastornos hemorrágicos, no una relación farmacológica demostrada. No hay ensayos ni literatura que la respalden.

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
| 1181271001 | HEMLIBRA 30 MG/ML SOLUCION INYECTABLE | Solución inyectable | No especificada en el registro |
| 1181271002IP | HEMLIBRA 150 MG/ML SOLUCION INYECTABLE | Solución inyectable | No especificada en el registro |
| 1181271002IP1 | HEMLIBRA 150 MG/ML SOLUCION INYECTABLE | Solución inyectable | No especificada en el registro |
| 1181271002 | HEMLIBRA 150 MG/ML SOLUCION INYECTABLE | Solución inyectable | No especificada en el registro |
| 1181271002IP2 | HEMLIBRA 150 MG/ML SOLUCION INYECTABLE | Solución inyectable | No especificada en el registro |

Titular de todas las autorizaciones: Roche Registration GmbH.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como señal de alerta de la evaluación mecanística (asociada a otra indicación predicha, la púrpura trombótica trombocitopénica): se ha notificado microangiopatía trombótica con emicizumab combinado con concentrado de complejo protrombínico activado (aPCC). Esto sugiere prudencia en trastornos con tendencia trombótica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura para esta indicación, y el mecanismo de emicizumab (mimetismo del FVIIIa) no corrige el defecto plaquetario de la pseudo-enfermedad de von Willebrand. La predicción se apoya solo en el modelo (nivel L5).

**Para avanzar se necesita:**
- Datos de mecanismo de acción del registro (DrugBank) y advertencias/contraindicaciones del prospecto de la AEMPS, que hoy faltan.
- Evidencia preclínica que muestre si el aumento de la generación de trombina con emicizumab tiene algún efecto en defectos de GPIb-alfa.
- Considerar priorizar otra predicción del mismo análisis: la **hemofilia A adquirida** (puesto 5) cuenta con estudios prospectivos, entre ellos GTH-AHA-EMI (Fase 2) y AGEHA (Fase III), aunque el paquete de evidencia aún no los ha clasificado ni puntuado formalmente.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

