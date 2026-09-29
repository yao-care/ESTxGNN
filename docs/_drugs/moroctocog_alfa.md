---
layout: default
title: Moroctocog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 365
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Moroctocog Alfa: De Factor VIII Recombinante a Trastorno de Liberación Plaquetaria Primario

## Resumen en Una Frase

Moroctocog alfa es un factor VIII de coagulación recombinante (con el dominio B eliminado), comercializado en España como ReFacto AF. El modelo TxGNN predice que podría ser efectivo para el **trastorno primario de liberación plaquetaria**, pero **ninguno de los 7 ensayos clínicos** asociados evalúa este fármaco en esta enfermedad y no hay **ninguna publicación** que lo respalde. La predicción carece de sustento mecanístico y clínico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99,97 % |
| Nivel de Evidencia | L5 (el pack asigna L4, pero ningún estudio evalúa el fármaco en esta enfermedad, por lo que aquí se aplica L5) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en el pack. Según la información conocida, moroctocog alfa es factor VIII recombinante y actúa reponiendo este factor plasmático de la coagulación.

**Esta predicción no resulta razonable desde el punto de vista mecanístico.** El trastorno de liberación (secreción) plaquetaria es un defecto funcional propio de la plaqueta, y la reposición de factor VIII no lo corrige. El puntaje alto probablemente refleja la cercanía del fármaco a la región de trastornos hemorrágicos en el grafo de conocimiento, no una razón biológica.

Los ensayos vinculados son estudios de fase 3 de otros productos de factor VIII en hemofilia A, o estudios sin relación con esta enfermedad.

**Nota:** entre las 8 predicciones del modelo, la más plausible es la n.º 4, **deficiencia adquirida de factores de coagulación** (relacionada con la hemofilia A adquirida). Su respaldo es solo indirecto, porque proviene de otros productos (sobre todo factor VIII porcino, susoctocog alfa/Obizur). Además, el moroctocog alfa es de secuencia humana y se esperaría que los mismos autoanticuerpos lo inhiban. Merece evaluarse aparte como pregunta de investigación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Fase 3 | Completado | 159 | rFVIIIFc-VWF-XTEN (BIVV001) como profilaxis en hemofilia A grave, ≥12 años. Otro producto y otra enfermedad |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Fase 3 | Completado | 74 | BIVV001 en pacientes pediátricos <12 años con hemofilia A grave. Otro producto y otra enfermedad |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Fase 3 | Completado | 30 | FVIII pegilado (BAX 855) en cirugía o procedimientos invasivos en hemofilia A. Otro producto y otra enfermedad |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | En reclutamiento | 25 | Soporte hepático artificial en insuficiencia hepática aguda sobre crónica. Sin relación |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | En reclutamiento | 45 | Exploración de la hemostasia en pacientes con derivación portosistémica transyugular (TIPS). Observacional, sin relación |
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | En reclutamiento | 200 | Evaluación de laboratorio y síntomas en el síndrome post-vacunación COVID-19. Sin relación |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Aún sin reclutar | 80 | Perfil de coagulación en leucemia mieloide aguda de nuevo diagnóstico. Observacional, sin relación |

Los 7 ensayos fueron clasificados con relevancia baja (grado C).

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 9 autorizaciones. Todas pertenecen a Pfizer Europe MA EEIG. El registro no incluye el texto de la indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 99103003 | ReFacto AF 1000 UI | Polvo y disolvente para solución inyectable | Pfizer Europe MA EEIG |
| 99103002 | ReFacto AF 500 UI | Polvo y disolvente para solución inyectable | Pfizer Europe MA EEIG |
| 99103004 | ReFacto AF 2000 UI | Polvo y disolvente para solución inyectable | Pfizer Europe MA EEIG |
| 99103007 | ReFacto AF 1000 UI | Polvo y disolvente para solución inyectable en jeringa precargada | Pfizer Europe MA EEIG |
| 99103008 | ReFacto AF 2000 UI | Polvo y disolvente para solución inyectable en jeringa precargada | Pfizer Europe MA EEIG |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene respaldo mecanístico, porque la reposición de factor VIII no corrige un defecto funcional de la plaqueta, y ningún ensayo ni publicación evalúa este fármaco en esta enfermedad. El puntaje alto del modelo parece reflejar proximidad en el grafo, no eficacia esperable.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de la AEMPS (advertencias y contraindicaciones), cuya ausencia bloquea el cribado de seguridad.
- Obtener los datos de mecanismo de acción desde DrugBank.
- Considerar reorientar la evaluación hacia la deficiencia adquirida de factores de coagulación (predicción n.º 4), que es la única con plausibilidad mecanística parcial.
- Verificar en la ontología el término ambiguo "flood factor deficiency" (predicción n.º 8) antes de cualquier revisión.

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

