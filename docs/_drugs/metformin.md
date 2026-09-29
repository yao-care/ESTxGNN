---
layout: default
title: Metformin
parent: Solo predicción del modelo (L5)
nav_order: 346
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Metformina: De Diabetes Mellitus Tipo 2 a Síndrome de la Persona Rígida Clásica

## Resumen en Una Frase

La metformina es un antidiabético oral ampliamente comercializado en España. La indicación original no figura en los datos de AEMPS del Evidence Pack; se cita diabetes tipo 2 por conocimiento general del fármaco.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de la persona rígida clásico**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS (conocimiento general: diabetes tipo 2) |
| Nueva Indicación Predicha | Síndrome de la persona rígida clásico |
| Puntaje de Predicción TxGNN | 99,45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la metformina es un antidiabético oral de uso muy extendido, con eficacia comprobada en el control glucémico. Mecanísticamente, podría ser aplicable al síndrome de la persona rígida solo de forma especulativa.

La hipótesis, no respaldada por ningún ensayo ni publicación del Evidence Pack, se basa en la activación de AMPK y en posibles efectos inmunomoduladores de la metformina. El síndrome de la persona rígida es una enfermedad autoinmune, asociada a anticuerpos anti-GAD. El puntaje de 99,45% es únicamente una predicción del modelo, sin validación clínica.

La variante **síndrome de la extremidad rígida focal** tiene exactamente el mismo puntaje. Probablemente no es una predicción independiente, sino parte del mismo espectro de la enfermedad.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones. El texto de indicación aprobada está vacío en los datos recibidos, por lo que no se incluye.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 89159 | Metformina Adair 850 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 84266 | Metformina Juta 850 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 83866 | Metformina Vir 1000 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 72221 | Metformina Viatris 850 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 73662 | Metformina Combix 850 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ningún ensayo clínico ni publicación (nivel L5), y no hay datos de mecanismo de acción ni de seguridad. No hay base para avanzar más allá del cribado inicial (S0).

**Otras predicciones del modelo (todas L5 y Hold):**
- Síndrome de la extremidad rígida focal (99,45%)
- Opsismodisplasia (99,40%)
- Síndrome de disfunción sensible a tiamina (99,40%)
- Lipodistrofia localizada inducida por fármacos (99,06%)

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que bloquea el cribado de seguridad
- Obtener el mecanismo de acción desde DrugBank
- Hacer una búsqueda sistemática de literatura y de ensayos en ClinicalTrials.gov e ICTRP sobre metformina en síndrome de la persona rígida
- Comprobar si el puntaje duplicado con la variante focal refleja una sola señal del modelo
- Evaluar la compatibilidad de vía de administración y la similitud con la indicación original, actualmente pendientes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

