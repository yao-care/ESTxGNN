---
layout: default
title: Aflibercept
parent: Solo predicción del modelo (L5)
nav_order: 21
evidence_level: L5
indication_count: 1
---

# Aflibercept
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Aflibercept: Hacia Esotropía (predicción de reposicionamiento)

## Resumen en Una Frase

Aflibercept es un fármaco biológico que se comercializa en España como solución inyectable (marcas como Eylea, Opuviz, Eydenzelt y Pavblu), pero los datos de autorización recibidos no incluyen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **esotropía**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, por lo que se trata únicamente de una hipótesis del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de autorización disponibles |
| Nueva Indicación Predicha | Esotropía |
| Puntaje de Predicción TxGNN | 99,38 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente consultada. Según la información complementaria del análisis, aflibercept actúa como una "trampa" de los factores de crecimiento VEGF-A, VEGF-B y PlGF. Este dato no está confirmado por el campo de mecanismo de acción del paquete de evidencia.

La esotropía es un trastorno de la motilidad y la alineación ocular. Su origen suele ser neuromuscular, acomodativo o sensorial, y no hay un mecanismo establecido impulsado por VEGF. La puntuación alta de TxGNN (0,994) proviene solo de un modelo de grafo de conocimiento. Puede reflejar la cercanía en el grafo entre los usos oftálmicos de los anti-VEGF y los nodos de enfermedades oculares, y no necesariamente un vínculo biológico real.

Por ello, cualquier justificación mecanística es especulativa y los datos recibidos no la respaldan. No se ha podido evaluar la similitud con la indicación original ni la compatibilidad de vía de administración.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1241895001 | EYDENZELT 40 mg/ml solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No consta en los datos disponibles |
| 1241865002 | OPUVIZ 40 mg/ml solución inyectable en vial | Solución inyectable | No consta en los datos disponibles |
| 112797001 | EYLEA 40 mg/ml solución inyectable en jeringa precargada | Solución inyectable | No consta en los datos disponibles |
| 1251909002 | PAVBLU 40 mg/ml solución inyectable en vial | Solución inyectable | No consta en los datos disponibles |
| 112797004 | EYLEA 114,3 mg/ml solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No consta en los datos disponibles |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas para este fármaco en la fuente consultada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, no hay un mecanismo biológico plausible que conecte la inhibición de VEGF con la esotropía, y faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que es un requisito bloqueante para el cribado de seguridad.
- Obtener los datos del mecanismo de acción y la indicación original aprobada (DrugBank y fichas técnicas).
- Realizar una revisión de literatura preclínica o clínica sobre anti-VEGF en esotropía o trastornos de motilidad ocular.
- Evaluar la compatibilidad de la vía de administración con la nueva indicación.
- Solicitar una valoración clínica experta que confirme o descarte la plausibilidad biológica antes de asignar más recursos.

---

*Este informe es solo de referencia para la investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

