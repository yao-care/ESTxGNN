---
layout: default
title: Loprazolam
parent: Solo predicción del modelo (L5)
nav_order: 329
evidence_level: L5
indication_count: 1
---

# Loprazolam
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

# Loprazolam: De Indicación No Registrada en AEMPS a Trastorno del Sueño (Inicio y Mantenimiento)

## Resumen en Una Frase

Loprazolam es una benzodiazepina con propiedades hipnóticas, comercializada en España como comprimidos de 1 mg. El registro de AEMPS incluido en el paquete de evidencia no especifica su indicación original.
El modelo TxGNN predice que podría ser efectivo para el **trastorno del sueño con dificultad para iniciar y mantener el sueño** (insomnio), con **0 ensayos clínicos registrados** y **20 publicaciones**, entre ellas varios ensayos aleatorizados de los años 80, que respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el registro de AEMPS (texto de indicación vacío) |
| Nueva Indicación Predicha | Trastorno del sueño, inicio y mantenimiento del sueño (insomnio) |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L2 (según el paquete de evidencia; se apoya en ECAs publicados, sin ensayos registrados) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Según la clase farmacológica, loprazolam es una benzodiazepina que actúa como modulador alostérico positivo de los receptores GABA-A. Potencia la neurotransmisión inhibitoria GABAérgica y produce efectos sedantes e hipnóticos. Este vínculo mecanístico proviene de la clase del fármaco y no del registro proporcionado.

Ese mecanismo es coherente con el tratamiento de los trastornos de inicio y mantenimiento del sueño. La literatura describe a loprazolam como un hipnótico para el insomnio agudo o crónico. Su semivida de 7 a 8 horas en adultos sanos podría ofrecer ventajas frente a hipnóticos de acción más larga cuando se quiere evitar la sedación residual al día siguiente.

La indicación predicha coincide en la práctica con el uso hipnótico ya descrito para el fármaco. Por tanto, más que un reposicionamiento clásico, la predicción confirma un uso terapéutico conocido, y el principal hueco es documentar formalmente la indicación autorizada en España.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6141896](https://pubmed.ncbi.nlm.nih.gov/6141896/) | 1983 | ECA | Curr Med Res Opin | 40 pacientes hospitalizados con insomnio por ansiedad; loprazolam 1 mg fue superior a placebo (7 noches de tratamiento) |
| [6147285](https://pubmed.ncbi.nlm.nih.gov/6147285/) | 1984 | ECA | J Int Med Res | 190 sujetos con insomnio; loprazolam 1 mg frente a nitrazepam 5 mg y placebo durante 7 noches |
| [6142463](https://pubmed.ncbi.nlm.nih.gov/6142463/) | 1983 | ECA | Pharmatherapeutica | 40 pacientes ancianos; loprazolam 1 mg y nitrazepam 5 mg mejoraron significativamente el patrón de sueño |
| [6141114](https://pubmed.ncbi.nlm.nih.gov/6141114/) | 1984 | ECA (simple ciego) | J Int Med Res | 197 pacientes en atención primaria; loprazolam 1 mg comparado con temazepam 20 mg y placebo |
| [6132929](https://pubmed.ncbi.nlm.nih.gov/6132929/) | 1983 | ECA (dosis única) | J Clin Pharmacol | 60 pacientes con insomnio; 0.5 y 1.0 mg de loprazolam con potencia similar a flurazepam 15 mg y superiores a placebo |
| [2569239](https://pubmed.ncbi.nlm.nih.gov/2569239/) | 1989 | ECA (cruzado) | Therapie | 67 pacientes ambulatorios; comparación de loprazolam 1 mg con triazolam 0.25 mg en insomnio común |
| [6340977](https://pubmed.ncbi.nlm.nih.gov/6340977/) | 1983 | Estudio clínico (cruzado) | Curr Med Res Opin | 16 pacientes; loprazolam 1 mg frente a nitrazepam 5 mg y placebo en medicina general |
| [2874007](https://pubmed.ncbi.nlm.nih.gov/2874007/) | 1986 | Revisión | Drugs | Revisión de propiedades farmacodinámicas y farmacocinéticas; con dosis superiores a 1 mg puede aparecer sedación residual |
| [15252823](https://pubmed.ncbi.nlm.nih.gov/15252823/) | 2004 | Revisión sistemática y metaanálisis | Hum Psychopharmacol | Compara la eficacia de fármacos Z con benzodiazepinas (incluido loprazolam) en el manejo del insomnio a corto plazo |
| [1336776](https://pubmed.ncbi.nlm.nih.gov/1336776/) | 1992 | Revisión | J Clin Psychiatry | Compara triazolam con otros hipnóticos de acción corta, entre ellos loprazolam, en eficacia y seguridad |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 57017 | SOMNOVIT 1 mg COMPRIMIDOS (Teofarma S.R.L.) | Comprimido | No especificada en el registro |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos del registro no incluyen advertencias, contraindicaciones ni interacciones.

La literatura aportada señala riesgos propios de los hipnóticos benzodiazepínicos:
- **Sedación residual**: puede aparecer con dosis superiores a 1 mg (PMID 2874007).
- **Efectos "resaca"**: somnolencia diurna y deterioro psicomotor y cognitivo al día siguiente, con riesgo de accidentes (PMID 15089115).
- **Equilibrio y caídas**: los hipnóticos afectan el equilibrio corporal y se asocian a caídas y fracturas de cadera (PMID 20171127).
- **Duración del tratamiento**: las guías recomiendan limitar su uso en insomnio transitorio o de corta duración (PMID 7525193).

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos aleatorizados publicados que comparan loprazolam 1 mg con placebo y con otros hipnóticos, y el mecanismo de clase es coherente con la indicación predicha. Sin embargo, los estudios son antiguos, no hay ensayos registrados y falta la información de seguridad del prospecto, por lo que se recomienda avanzar con salvaguardas.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS para obtener advertencias y contraindicaciones, ya que sin esto no se puede completar el cribado de seguridad.
- Confirmar la indicación autorizada de SOMNOVIT 1 mg en la ficha técnica de AEMPS.
- Obtener el mecanismo de acción desde DrugBank.
- Establecer medidas de protección para poblaciones vulnerables, especialmente ancianos (sedación residual, caídas) y limitar la duración del tratamiento.
- Revisar la relevancia de las publicaciones pendientes de clasificación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

