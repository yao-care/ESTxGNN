---
layout: default
title: Volanesorsen
parent: Solo predicción del modelo (L5)
nav_order: 567
evidence_level: L5
indication_count: 10
---

# Volanesorsen
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

# Volanesorsen: De Síndrome de Quilomicronemia Familiar a Anemia Megaloblástica

## Resumen en Una Frase

Volanesorsen es un oligonucleótido antisentido dirigido contra el ARNm de APOC3 que reduce los triglicéridos. Se comercializa en España como Waylivra, y su uso original conocido es el síndrome de quilomicronemia familiar (dato de conocimiento general, no incluido en los datos de AEMPS recibidos).
El modelo TxGNN predice que podría ser efectivo para **anemia megaloblástica**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome de quilomicronemia familiar (conocimiento general; el texto de indicación de AEMPS está vacío) |
| Nueva Indicación Predicha | Anemia megaloblástica |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según el conocimiento general, volanesorsen es un oligonucleótido antisentido que silencia el ARNm de APOC3 y reduce los triglicéridos plasmáticos. Su eficacia se ha establecido en trastornos lipídicos graves, no en enfermedades hematológicas.

**Sinceramente, no se identifica un vínculo mecanístico claro con la anemia megaloblástica.** Esta enfermedad se debe a la deficiencia de vitamina B12 o folato y a una síntesis de ADN alterada, procesos que la reducción de APOC3 no aborda. El puntaje alto de TxGNN (99.997%) es una predicción basada en el grafo de conocimiento, sin estudios que la respalden.

Además, la trombocitopenia es un riesgo conocido de volanesorsen. Esto sería un problema adicional en un paciente con compromiso hematológico previo.

Las otras nueve predicciones principales (colangitis esclerosante, distintos subtipos de enfermedad de células falciformes, infección meningocócica y hemoglobinuria paroxística nocturna) tampoco tienen ensayos ni literatura, y todas son de nivel L5. Los subtipos de células falciformes comparten exactamente el mismo puntaje, lo que sugiere una señal heredada del nodo padre en el grafo y no evidencia independiente.

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
| 1191360 | WAYLIVRA 285 MG SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA (Akcea Therapeutics Ireland Limited) | Solución inyectable en jeringa precargada | No disponible en el registro recibido |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos recibidos.

Como nota de conocimiento general, la trombocitopenia es un efecto adverso conocido de volanesorsen. Debe considerarse de forma prioritaria en cualquier población con enfermedad hematológica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5: solo hay una puntuación del modelo, sin ensayos ni literatura. No existe un vínculo mecanístico plausible con la anemia megaloblástica, y el riesgo conocido de trombocitopenia aumenta la preocupación de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que es un requisito bloqueante para el cribado de seguridad
- Confirmar el mecanismo de acción y la indicación original desde DrugBank o la ficha técnica
- Encontrar evidencia preclínica o clínica que vincule la reducción de APOC3 con la anemia megaloblástica
- Evaluar el riesgo de trombocitopenia en pacientes con enfermedad hematológica

*Este informe es solo una referencia de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

