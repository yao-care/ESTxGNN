---
layout: default
title: Levothyroxine
parent: Solo predicción del modelo (L5)
nav_order: 469
evidence_level: L5
indication_count: 4
monitor_inn: "Levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-10-31
description: "Levothyroxine: nueva indicación predicha, Hipodisplasia/aplasia renal (nivel de evidencia L5). Indicación original: Hipotiroidismo"
---

# Levothyroxine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Levotiroxina: De Hipotiroidismo a Hipodisplasia/Aplasia Renal
{: .text-alpha }

## Resumen en Una Frase

Levotiroxina es una hormona tiroidea sintética, utilizada originalmente para el tratamiento del hipotiroidismo y de otras enfermedades de la glándula tiroides.
El modelo TxGNN predice que podría ser efectiva para **hipodisplasia/aplasia renal**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipotiroidismo (relación registrada en el grafo de conocimiento; los textos de indicación de las autorizaciones locales no están disponibles en los datos compilados) |
| Nueva Indicación Predicha | Hipodisplasia/aplasia renal |
| Puntaje de Predicción TxGNN | 0,9967 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 11) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la levotiroxina es la forma sintética de la tiroxina (T4) y actúa sobre los receptores de hormona tiroidea alfa (THRA) y beta (THRB). Su uso en enfermedades tiroideas es la base de su perfil terapéutico.

La relación con la hipodisplasia/aplasia renal es débil. La hormona tiroidea participa en el desarrollo fetal en general, incluido el renal, y el hipotiroidismo congénito se ha asociado de forma laxa con otras anomalías congénitas. Sin embargo, la hipodisplasia o aplasia renal tiene un origen genético y del desarrollo (por ejemplo, genes como PAX2, RET o HNF1B), y el reemplazo con levotiroxina no se esperaría que revierta un defecto estructural de las nefronas.

El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, como las congénitas o del desarrollo, no evidencia biológica. No se identifica un vínculo mecanístico directo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las autorizaciones listadas (la lista total puede ser parcial). Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Estado |
|---------|------|------|-----------|
| 77802 | Levotiroxina Sanofi 100 microgramos comprimidos | Comprimido | Vigente |
| 89301 | Levotiroxina Aristo 137 microgramos comprimidos | Comprimido | Vigente |
| 85613 | Solsint 13 microgramos solución oral en envase unidosis | Solución oral en envase unidosis | Cancelado |
| 77114 | Levotiroxina Sanofi 500 microgramos polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | Vigente |
| 64013 | Eutirox 75 microgramos comprimidos | Comprimido | Vigente |

## Consideraciones de Seguridad

- **Contraindicaciones registradas en el grafo de conocimiento (no proceden del prospecto):** hipertensión, hipopituitarismo y déficits hormonales hipofisarios (incluidos el déficit aislado de hormona del crecimiento, el síndrome de Sheehan y el síndrome de Kallmann), osteoporosis (incluida la posmenopáusica), diabetes mellitus, cetoacidosis diabética, enfermedad coronaria, infarto de miocardio y enfermedad del timo.
- **Interacciones farmacológicas:** los datos compilados solo recogen dianas farmacológicas (receptores de hormona tiroidea alfa y beta), no interacciones con otros medicamentos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio clínico ni publicación que aborde la hipodisplasia/aplasia renal, y el mecanismo propuesto no es plausible, ya que la levotiroxina no puede restaurar tejido renal ausente o malformado. El puntaje del modelo parece un artefacto del modelo TxGNN (aprendizaje profundo).

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de la levotiroxina.
- Advertencias y contraindicaciones del prospecto de la AEMPS.
- Estudios preclínicos o clínicos que evalúen directamente la hipodisplasia/aplasia renal.
- Valorar si las otras predicciones (aplasia renal bilateral, secuencia de Potter y complejo de Carney) merecen revisión; el complejo de Carney es la más verosímil biológicamente, aunque también sin evidencia clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

