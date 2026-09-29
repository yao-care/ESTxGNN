---
layout: default
title: Liothyronine
parent: Solo predicción del modelo (L5)
nav_order: 322
evidence_level: L5
indication_count: 10
---

# Liothyronine
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

# Liotironina: De Hormona Tiroidea (T3) a Hipodisplasia/Aplasia Renal

## Resumen en Una Frase

La liotironina es la forma sintética de la triyodotironina (T3), una hormona tiroidea. En España está comercializada como TRIYODOTIRONINA LEO en comprimidos.
El modelo TxGNN predice que podría ser efectiva para **hipodisplasia/aplasia renal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción. Es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Hipodisplasia/aplasia renal |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la liotironina es la hormona tiroidea activa (T3), que actúa sobre receptores nucleares y modifica la expresión génica de las células diana. La ficha de AEMPS no incluye texto de indicación, por lo que su uso habitual (sustitución hormonal tiroidea) proviene del conocimiento general y no del registro.

La hormona tiroidea participa en el desarrollo de varios órganos, incluido el riñón, y esa podría ser la base biológica de la predicción. Sin embargo, la hipodisplasia/aplasia renal es una malformación estructural congénita. Es muy poco probable que la T3 administrada después del nacimiento o en la edad adulta pueda revertirla.

El puntaje alto (99.95%) probablemente refleja cercanía en el grafo de conocimiento y no un mecanismo terapéutico real. La segunda predicción, agenesia renal bilateral, tiene el mismo problema.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 45503 | TRIYODOTIRONINA LEO (Byk Leo, S.L.) | Comprimido |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La consulta de interacciones farmacológicas no devolvió resultados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo, sin ensayos ni literatura, y el mecanismo es biológicamente poco plausible para una malformación congénita estructural.

**Para avanzar se necesita:**
- Un mecanismo plausible que explique un efecto terapéutico en el desarrollo renal, o evidencia preclínica que lo apoye.
- El prospecto de AEMPS con indicaciones, advertencias y contraindicaciones, para poder hacer el cribado de seguridad.
- Datos del mecanismo de acción desde DrugBank.
- Considerar otras predicciones del mismo fármaco. La mejor respaldada es el **bocio nodular** (L4), pero el estándar de tratamiento allí es la levotiroxina y no hay evidencia directa con liotironina, así que tampoco es una señal novedosa de reposicionamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

