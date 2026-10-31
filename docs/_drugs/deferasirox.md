---
layout: default
title: Deferasirox
parent: Evidencia moderada (L3-L4)
nav_order: 229
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-31
monitor_inn: "DEFERASIROX"
predicted_indications: ["HIV infectious disease", "chronic hepatitis C virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "dermatofibrosarcoma protuberans"]
description: "Deferasirox: nueva indicación predicha, Infección por VIH (HIV infectious disease) (nivel de evidencia L4). Indicación original: No consta en los datos locales"
---

# Deferasirox
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

## Deferasirox: Infección por VIH (HIV infectious disease)
{: .text-alpha }

## Resumen en Una Frase

Deferasirox es un quelante de hierro utilizado originalmente en enfermedades hematológicas asociadas a la betatalasemia y otras hemoglobinopatías.
El modelo TxGNN predice que podría ser efectivo para **infección por VIH**, pero actualmente no hay **ningún ensayo clínico** y solo **2 publicaciones** (una revisión general del fármaco y un estudio preclínico) que lo respaldan de forma indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Infección por VIH (HIV infectious disease) |
| Puntaje de Predicción TxGNN | 0.9940 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 7) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Deferasirox es un quelante de hierro. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, su función como quelante de hierro ha sido comprobada en la sobrecarga de hierro asociada a la betatalasemia, y mecanísticamente podría ser aplicable a procesos en los que la homeostasis del hierro influya en la biología de una infección.

La única pista mecanística proviene de un estudio preclínico (PMID 34550543, 2021). Este describe que el hierro endolisosomal restringe la transactivación del LTR del VIH-1 mediada por Tat, al aumentar la oligomerización de Tat y la expresión de β-catenina. Esto sugiere que el hierro puede modular la transcripción del VIH-1.

Conviene ser prudente: se trata de evidencia indirecta y preclínica, y no está establecido en qué dirección actuaría la quelación del hierro (podría incluso ser desfavorable). La otra publicación (PMID 16529348) es una reseña general de nuevos fármacos sin datos específicos sobre VIH. El puntaje alto de TxGNN es solo una predicción computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Preclínico/Mecanístico | Journal of Neurovirology | El hierro endolisosomal restringe la transactivación del LTR del VIH-1 mediada por Tat, al aumentar la oligomerización de Tat y la expresión de β-catenina |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Revisión | Journal of the American Pharmacists Association | Reseña general de nuevos fármacos (ramelteón, tipranavir, nepafenac y deferasirox); sin evidencia específica sobre VIH |

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de fármaco único). Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 06356001 | Exjade 125 mg comprimidos dispersables | Comprimido dispersable | No disponible |
| 106356011 | Exjade 90 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 84909 | Deferasirox Stada 180 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 86261 | Deferasirox Aurovitas 90 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 89130 | Deferasirox Sun 360 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia hepática, enfermedad renal y función renal alterada, cirrosis, hiperbilirrubinemia y síndrome de Gilbert, trombocitopenia, neutropenia (incluidas las formas congénitas) y agranulocitosis, anemia, enfermedad de la vesícula biliar, hipertensión ocular, úlcera péptica activa, síndrome de disfunción multiorgánica y cáncer.
- **Interacciones farmacológicas**: se identificaron 100 interacciones; entre las de nivel **Mayor** figuran hidrocortisona, dexametasona, betametasona, triamcinolona, ácido acetilsalicílico, mesalazina, balsalazida y las formulaciones de anfotericina B. Entre las de nivel **Moderado** figuran rabeprazol, pioglitazona, alosetrón, aprepitant, claritromicina, saxagliptina, hidróxido de aluminio, cisaprida y dexfenfluramina.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo TxGNN y en un estudio preclínico indirecto cuya dirección de efecto es incierta. No hay ensayos clínicos, por lo que la hipótesis es, por ahora, una pregunta de investigación.

**Para avanzar se necesita:**
- Estudios in vitro y en modelos animales que evalúen directamente el efecto de deferasirox sobre la replicación del VIH.
- Datos del mecanismo de acción y clarificación de si la quelación del hierro favorece o perjudica la replicación viral.
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones), dado que el perfil renal, hepático y hematológico exige especial atención en personas con VIH.
- Evaluación de interacciones con los antirretrovirales.
- Revisión de las demás indicaciones predichas (hepatitis C crónica, etc.), todas con nivel L5, si se desea ampliar el análisis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

