---
layout: default
title: Ganirelix
parent: Solo predicción del modelo (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ganirelix: nueva indicación predicha, Hipertricosis (nivel de evidencia L5). Indicación original: No disponible en las autorizaciones de la AEMPS (el texto de indicaci…"
---

# Ganirelix
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

# Ganirelix: De Indicación Original No Registrada a Hipertricosis

## Resumen en Una Frase

Ganirelix es un antagonista del receptor de GnRH, utilizado en la práctica clínica para prevenir la ovulación prematura en mujeres sometidas a estimulación ovárica durante tratamientos de fertilidad.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones de la AEMPS (el texto de indicación está vacío). Según la farmacología conocida: prevención de la ovulación prematura en estimulación ovárica |
| Nueva Indicación Predicha | Hipertricosis |
| Puntaje de Predicción TxGNN | 99,98 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro compilado. Según la información farmacológica conocida, ganirelix es un péptido antagonista del receptor GnRH₁ (gen GNRHR). Al bloquear este receptor, suprime la liberación de LH y FSH y, en consecuencia, reduce los esteroides sexuales derivados.

La relación con la hipertricosis es **débil e indirecta**. La hipertricosis no está impulsada principalmente por gonadotropinas, por lo que cualquier vínculo pasaría por una modulación androgénica y es especulativo. El puntaje elevado de TxGNN refleja la proximidad en la red del grafo de conocimiento, no evidencia clínica ni de literatura.

Conviene interpretar esta predicción con cautela. Entre las diez primeras predicciones, las más plausibles biológicamente son otras: **pubertad precoz central** (el bloqueo del receptor GnRH se alinea con el mecanismo, aunque los agonistas de GnRH son el estándar de tratamiento y no hay datos de ganirelix), **pubertad precoz familiar limitada a varones** (la eficacia sería limitada porque la producción de testosterona es independiente de gonadotropinas) y el **síndrome de exceso de aromatasa** (los inhibidores de aromatasa son un enfoque más directo). Estas tres están clasificadas como "pregunta de investigación". El resto (síndrome de Ambras, malformaciones dentales, síndrome de Dandy-Walker, anomalías del tallo piloso, circulación fetal persistente y tricomegalia familiar) carece de un vínculo mecanístico identificable.

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
| 78205 | Fyremadel 0,25 mg/0,5 ml solución inyectable en jeringa precargada EFG | Solución inyectable | No especificada |
| 1221658001 | Ganirelix Gedeon Richter 0,25 mg/0,5 ml solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada | No especificada |
| 86368 | Astarte 0,25 mg/0,5 ml solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada | No especificada |
| 00130001 | Orgalutran 0,25 mg/0,5 ml solución inyectable | Solución inyectable en jeringa precargada | No especificada |
| 00130002 | Orgalutran 0,25 mg/0,5 ml solución inyectable | Solución inyectable en jeringa precargada | No especificada |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 7 registros. Seis son de gravedad **moderada**: gonadorelina, gonadotropina coriónica humana, menotropinas, triptorelina, folitropina y urofolitropina. El séptimo corresponde al propio receptor GnRH₁ (dato farmacológico de la diana, sin nivel de gravedad asignado).

Para el resto de información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertricosis se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un mecanismo plausible que conecte el antagonismo de GnRH con este trastorno. Aunque el fármaco está comercializado en España con 5 autorizaciones, esto no aporta respaldo para la nueva indicación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de la AEMPS (descargar y analizar el PDF)
- Textos de indicación aprobada de las autorizaciones, hoy vacíos
- Revisión de literatura y ensayos para hipertricosis, y valorar priorizar candidatas más plausibles (pubertad precoz central, exceso de aromatasa)
- Evaluación de compatibilidad de vía de administración (ganirelix es inyectable) y de similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

