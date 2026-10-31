---
layout: default
title: Risperidone
parent: Solo predicción del modelo (L5)
nav_order: 706
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
description: "Risperidone: nueva indicación predicha, Parálisis de la mirada horizontal familiar con escoliosis progresiva (nivel de evidencia L5). Indicación original: Esquizofrenia…"
monitor_inn: "Risperidone"
predicted_indications: ["gaze palsy, familial horizontal, with progressive scoliosis", "amelocerebrohypohidrotic syndrome", "Phelan-McDermid syndrome", "trichotillomania", "major affective disorder"]
---

# Risperidone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Risperidona: De Esquizofrenia y Trastorno Bipolar a Síndrome de Parálisis de la Mirada Horizontal Familiar con Escoliosis Progresiva
{: .text-alpha }

## Resumen en Una Frase

La risperidona es un antipsicótico atípico utilizado originalmente para la esquizofrenia, los episodios maníacos del trastorno bipolar y la irritabilidad asociada al autismo.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de parálisis de la mirada horizontal familiar con escoliosis progresiva**, una enfermedad neurológica rara.
Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia, trastorno bipolar (episodios maníacos) y trastornos del espectro autista (según las indicaciones registradas en el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Parálisis de la mirada horizontal familiar con escoliosis progresiva |
| Puntaje de Predicción TxGNN | 0.9976 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 15) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la risperidona es un antipsicótico atípico cuya eficacia en esquizofrenia, manía bipolar e irritabilidad en el autismo está establecida. El perfil de unión a receptores compilado muestra afinidad por receptores serotoninérgicos (5-HT1A, 1B, 1D, 1E, 1F, 2A, 2C, 6 y 7), dopaminérgicos (D2 y D3), adrenérgicos (α1A, α1B, α1D y α2A) e histaminérgicos H1. El bloqueo de D2 y 5-HT2A es el mecanismo clásicamente asociado a su acción antipsicótica.

La enfermedad predicha es un trastorno neurológico hereditario raro, relacionado con el gen ROBO3, que afecta al control de los movimientos oculares horizontales y a la columna vertebral. **No se ha establecido ningún vínculo mecanístico** entre el bloqueo dopaminérgico/serotoninérgico y la fisiopatología de esta enfermedad, que es de origen del desarrollo neurológico.

Por tanto, el puntaje alto (0.9976) debe interpretarse con cautela. En ausencia de ensayos, literatura o una hipótesis mecanística clara, la predicción no ofrece por sí sola una base suficiente para plantear un uso clínico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

La risperidona cuenta con 20 autorizaciones vigentes, todas de medicamentos con un único principio activo. No hay autorizaciones canceladas ni combinaciones. Los textos de indicación aprobada no están disponibles. Se muestran las 5 primeras:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 68798 | Risperidona Stada 1 mg/ml solución oral EFG | Solución oral |
| 81426 | Risperidona Aurovitas 1 mg/ml solución oral EFG | Solución oral |
| 71473 | Risperidona Viatris 1 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 71095 | Risperidona FLAS Krka 1 mg comprimidos bucodispersables EFG | Comprimido bucodispersable |
| 60336 | Risperdal 1 mg comprimidos recubiertos con película (Janssen Cilag) | Comprimido recubierto con película |

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento, no según el texto del prospecto):** el grafo asocia la risperidona con riesgo en las siguientes categorías:
  - **Cardiovasculares:** hipotensión ortostática, síndrome de taquicardia postural ortostática, infarto de miocardio, enfermedad cardíaca y de la conducción cardíaca, paro cardíaco súbito, ictus y enfermedad cerebrovascular.
  - **Metabólicas:** diabetes mellitus, hiperglucemia, cetoacidosis diabética, hiperlipidemia y obesidad.
  - **Hematológicas:** neutropenia y agranulocitosis.
  - **Hepáticas y biliares:** insuficiencia y enfermedad hepática, enfermedad de la vesícula biliar.
  - **Otras:** epilepsia, atrofia multisistémica y carcinoma de mama femenino.
- **Perfil receptorial relevante para la seguridad:** el bloqueo de receptores α1-adrenérgicos y H1 es coherente con los riesgos de hipotensión ortostática y sedación.

No se dispone de las advertencias del prospecto ni de interacciones farmacológicas con otros medicamentos. Consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para esta enfermedad rara carece de ensayos clínicos, literatura y vínculo mecanístico plausible (nivel L5). Además, la risperidona tiene un perfil de riesgo cardiometabólico y neurológico no trivial, por lo que no se justifica avanzar sin una hipótesis biológica fundamentada.

**Para avanzar se necesita:**
- Una hipótesis mecanística que relacione la vía ROBO3 con el bloqueo dopaminérgico/serotoninérgico, junto con estudios preclínicos.
- Datos detallados del mecanismo de acción (MOA).
- Las advertencias y contraindicaciones del prospecto de la AEMPS, necesarias para cualquier evaluación de seguridad.
- Una revisión de la relevancia clínica de esta predicción frente al riesgo de uso fuera de indicación en una población pediátrica con una enfermedad rara.

**Nota sobre otras predicciones del mismo análisis:** el modelo generó otras candidatas con mejor respaldo, que podrían evaluarse en informes separados.
- **Trastorno afectivo mayor / depresión resistente al tratamiento (nivel L1):** dos ensayos de Fase 3 completados (NCT00095134, n=630; NCT00044681, n=258) y varios metaanálisis respaldan la risperidona como tratamiento adyuvante.
- **Tricotilomanía (nivel L4):** solo informes y series de casos.
- **Síndrome de Phelan-McDermid (nivel L4):** solo evidencia indirecta y preclínica.
- **Síndrome de Asperger:** coincide en gran medida con la indicación original de autismo, por lo que no constituye reposicionamiento nuevo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

