---
layout: default
title: Piroxicam
parent: Solo predicción del modelo (L5)
nav_order: 644
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "PIROXICAM"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis", "juvenile idiopathic arthritis"]
description: "Piroxicam: nueva indicación predicha, Colobomatous microphthalmia-rhizomelic dysplasia syndrome (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Piroxicam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Piroxicam: Colobomatous microphthalmia-rhizomelic dysplasia syndrome
{: .text-alpha }

## Resumen en Una Frase

Piroxicam es un antiinflamatorio no esteroideo (AINE) utilizado originalmente para la artritis reumatoide, la artrosis y otras artropatías.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmía colobomatosa-displasia rizomélica**, una displasia ocular y esquelética muy rara, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 3 de 9) |
| Número de Autorizaciones | 9 (vigentes: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, piroxicam es un AINE inhibidor no selectivo de la ciclooxigenasa (COX), con eficacia sintomática establecida en artritis reumatoide y artrosis. Reduce la inflamación y el dolor al disminuir la síntesis de prostaglandinas.

**En este caso no se identificó un vínculo mecanístico plausible.** La enfermedad predicha es un síndrome genético raro del desarrollo, con alteraciones esqueléticas y oculares. La inhibición de COX no tiene un papel conocido en su patogenia. El puntaje del modelo TxGNN (aprendizaje profundo) es muy alto (1,0000), pero puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni una relación terapéutica real.

Como el mecanismo de acción original tampoco está documentado en los datos disponibles, la predicción no puede verificarse mecanísticamente. Debe considerarse una hipótesis generada por el modelo, sin respaldo clínico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 9 autorizaciones vigentes (todas de principio activo único).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55382 | FELDENE 10 mg cápsulas duras (Pfizer) | Cápsula dura | No especificada en los datos disponibles |
| 55806 | FELDENE 20 mg cápsulas duras (Pfizer) | Cápsula dura | No especificada en los datos disponibles |
| 58085 | FELDENE 20 mg/ml solución inyectable (Pfizer) | Solución inyectable | No especificada en los datos disponibles |
| 60070 | FELDENE FLAS 20 mg liofilizado oral (Pfizer) | Liofilizado oral | No especificada en los datos disponibles |
| 62418 | PIROXICAM CINFA 20 mg comprimidos dispersables EFG | Comprimido dispersable | No especificada en los datos disponibles |

Las demás autorizaciones corresponden a formulaciones tópicas (geles y crema): SASULEN 5 mg/g gel, SALVACAM 5 mg/g gel, IMPRONTAL 5 mg/g crema y FELDEGEL 5 mg/g gel.

---

## Consideraciones de Seguridad

- **Condiciones de riesgo asociadas (grafo de conocimiento, no texto del prospecto):** el grafo asocia piroxicam con contraindicación o precaución en las siguientes condiciones:
  - **Cardiovasculares:** hipertensión, insuficiencia cardíaca congestiva, infarto de miocardio, trombosis coronaria, enfermedad cardiovascular y cardíaca, ictus, trastornos cerebrovasculares e infarto cerebral.
  - **Hepáticas y biliares:** enfermedad hepática, insuficiencia hepática aguda, hepatitis, lesión hepática inducida por fármacos y enfermedad de la vesícula biliar.
  - **Renales:** enfermedad renal y piouréter.
  - **Hematológicas:** trastornos de la coagulación, enfermedad trombótica, hemoglobinopatías y anemias.
  - **Gastrointestinales:** úlcera péptica activa.
  - **Otras:** trastornos de la visión y ceguera, y abuso o dependencia de sustancias.
- **Interacciones farmacológicas:** se identificaron 100 interacciones en total. Entre las principales (muestra de 20):
  - **Moderadas:** corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), ácido acetilsalicílico, metformina, glimepirida, clorpropamida, aprepitant, mesalazina, balsalazida, citrato y bicarbonato de potasio, ácido picosulfúrico y polietilenglicol con electrolitos.
  - **Menores:** famotidina, ranitidina, cimetidina y linaclotida.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no hay un mecanismo plausible que vincule la inhibición de COX con esta displasia genética. Además, el perfil de seguridad de un AINE, con riesgos cardiovasculares, renales, hepáticos y gastrointestinales, no se justifica sin un beneficio terapéutico demostrable.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de piroxicam y un análisis mecanístico formal frente a la fisiopatología de la enfermedad.
- Evidencia preclínica o clínica específica de la nueva indicación. Hasta ahora no existe.
- Las advertencias y contraindicaciones del prospecto de la AEMPS, para completar la evaluación de seguridad.

**Nota complementaria:** entre las predicciones del modelo, la **artritis idiopática juvenil** (puntaje 0,9993) es la única con literatura recuperada. Incluye estudios pediátricos de los años 80 y 90, como un estudio multicéntrico de piroxicam frente a naproxeno y un estudio farmacocinético en niños, además de metaanálisis en red de AINE. Su nivel de evidencia sería L3, pero solo como opción sintomática, no modificadora de la enfermedad. Podría valorarse como pregunta de investigación aparte, sin alterar la decisión de este informe.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

