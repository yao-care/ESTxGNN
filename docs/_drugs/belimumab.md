---
layout: default
title: Belimumab
parent: Solo predicción del modelo (L5)
nav_order: 65
evidence_level: L5
indication_count: 6
---

# Belimumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Belimumab: De Inhibidor de BLyS (BAFF) a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Belimumab es un anticuerpo monoclonal que inhibe BLyS (BAFF), reduce la supervivencia de los linfocitos B y disminuye la producción de autoanticuerpos. Está comercializado en España, pero los datos recibidos no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **trastorno primario de liberación plaquetaria**, pero esta predicción **no tiene respaldo directo**: hay **1 ensayo clínico** sin relación con la enfermedad y **0 publicaciones**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99,96 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Belimumab inhibe BLyS (BAFF), una molécula clave para la supervivencia de los linfocitos B. Al bloquearla, reduce la producción de autoanticuerpos. Los datos de mecanismo de acción de DrugBank no están disponibles, por lo que esta descripción proviene del análisis mecanístico del propio Evidence Pack.

Los trastornos primarios de liberación plaquetaria son defectos hereditarios en la secreción de gránulos y en la señalización de las plaquetas. No existe una vía establecida de linfocitos B o BLyS en estas enfermedades. Por eso la relación entre el mecanismo del fármaco y la nueva indicación es débil.

El puntaje alto de TxGNN (0,9996) refleja una asociación calculada sobre el grafo de conocimiento, no un mecanismo respaldado por estudios. **Por ahora la predicción no es razonable desde el punto de vista mecanístico.** Debe tratarse como una señal del modelo pendiente de validación, no como una hipótesis terapéutica sólida.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Fase 2 | Completado | 14 | Estudio abierto de medicina experimental sobre eficacia, seguridad y mecanismo de belimumab (10 mg/kg IV) en glomerulonefropatía membranosa idiopática con autoanticuerpos anti-PLA2R. |

Este ensayo estudia una enfermedad renal mediada por anticuerpos, no un trastorno plaquetario. Solo demuestra que belimumab se ha administrado en una enfermedad autoinmune, y no aporta evidencia para los trastornos de liberación plaquetaria (relevancia: C).

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 11700001 | BENLYSTA 120 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión |
| 11700002 | BENLYSTA 400 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión |
| 111700004 | BENLYSTA 200 mg solución inyectable en pluma precargada | Solución inyectable en pluma precargada |

Titular de las tres autorizaciones: Glaxosmithkline (Ireland) Limited.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5). El único ensayo registrado no guarda relación con la enfermedad, no hay literatura y no existe un vínculo mecanístico plausible entre la inhibición de BLyS y los defectos hereditarios de la función plaquetaria.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS con la indicación aprobada, las advertencias y las contraindicaciones, que hoy faltan y bloquean el cribado de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Aportar evidencia preclínica o clínica que conecte la vía BLyS/linfocitos B con la fisiopatología de esta enfermedad. Sin ella, no se justifica avanzar.

**Nota sobre otras predicciones:** de las seis predicciones del modelo, solo la trombocitopenia aloinmune fetal y neonatal (FNAIT) se marcó como "pregunta de investigación". Está causada por aloanticuerpos maternos, por lo que una terapia dirigida a linfocitos B es biológicamente plausible. Sin embargo, no hay evidencia clínica ni bibliográfica, y los datos de seguridad de belimumab en el embarazo son limitados.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

