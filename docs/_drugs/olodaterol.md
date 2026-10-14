---
layout: default
title: Olodaterol
parent: Evidencia moderada (L3-L4)
nav_order: 587
evidence_level: L4
indication_count: 2
---

# Olodaterol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Olodaterol: De Enfermedad Pulmonar Obstructiva Crónica (EPOC) a Bronquitis

## Resumen en Una Frase

Olodaterol es un agonista beta2 de acción prolongada (LABA) que se usa como broncodilatador de mantenimiento en la enfermedad pulmonar obstructiva crónica (EPOC).
El modelo TxGNN predice que podría ser efectivo para **bronquitis**, pero actualmente no hay **ningún ensayo clínico** y solo **2 publicaciones**, que tratan sobre la EPOC en general y no evalúan la bronquitis como indicación propia.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad pulmonar obstructiva crónica (EPOC) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99,84 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, olodaterol pertenece a la clase de los agonistas beta2-adrenérgicos de acción prolongada. Estos fármacos relajan el músculo liso de las vías respiratorias activando el receptor beta2 y aumentando el AMPc. Su eficacia en la EPOC está respaldada por una amplia evidencia.

La bronquitis crónica es un fenotipo de la EPOC, por lo que existe un solapamiento claro entre la indicación aprobada y la predicha. El puntaje tan alto del modelo (0,998) refleja probablemente ese solapamiento de etiquetas de enfermedad, y **no constituye una verdadera señal de reposicionamiento**.

Para la bronquitis aguda, que suele ser autolimitada y de origen infeccioso, no existe una justificación mecanística para usar un LABA. Las dos publicaciones recuperadas se centran en la EPOC y no analizan la bronquitis como entidad independiente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para bronquitis.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Revisión | Am J Health-Syst Pharm | Revisión de la farmacología, farmacocinética, eficacia y seguridad de olodaterol, un LABA de una dosis diaria, en la EPOC |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guía clínica | Basic Clin Pharmacol Toxicol | Guía finlandesa sobre diagnóstico y tratamiento farmacológico de la EPOC estable, orientada a atención primaria |

Ninguna de las dos publicaciones evalúa la bronquitis como indicación independiente.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 78253 | STRIVERDI RESPIMAT 2,5 microgramos solución para inhalación | Solución para inhalación | No especificada en los datos compilados (en la base de conocimiento: EPOC) |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones potenciales, todas las mostradas de nivel moderado. Algunas de las principales son:
  - Simpaticomiméticos y estimulantes: epinefrina (incluidas las formas oftálmica y tópica), efedrina (incluida la nasal), isometepteno, fentermina, dietilpropión y fenfluramina.
  - Fármacos con posible efecto sobre el intervalo QT o la motilidad: claritromicina, cisaprida, dolasetrón, palonosetrón y granisetrón.
  - Otros: famotidina, loperamida, y los antidiabéticos canagliflozina, ertugliflozina, albiglutida y semaglutida.
- Se recomienda prestar atención al riesgo cardiovascular, especialmente con otros agonistas beta, fármacos que prolongan el QT y betabloqueantes.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción coincide en gran parte con la indicación ya aprobada (EPOC) y no hay ensayos clínicos ni literatura específica en bronquitis. La bronquitis aguda carece de justificación mecanística para un LABA, por lo que no se recomienda avanzar con esta indicación.

**Para avanzar se necesita:**
- Definir si la indicación de interés es la bronquitis crónica (ya incluida dentro de la EPOC) o la bronquitis aguda.
- Estudios específicos en bronquitis que no se limiten a poblaciones con EPOC.
- Datos detallados del mecanismo de acción y las advertencias y contraindicaciones del prospecto de la AEMPS.
- Plan de monitoreo cardiovascular y de interacciones farmacológicas.

**Nota:** la segunda predicción del modelo, enfermedad pulmonar obstructiva (puntaje 99,57 %), cuenta con varios ensayos de Fase 3 completados. Esa evidencia confirma la indicación ya existente en EPOC y no establece una indicación nueva. Un posible uso en asma requeriría evidencia propia, porque la monoterapia con LABA en asma plantea preocupaciones de seguridad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

