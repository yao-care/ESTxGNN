---
layout: default
title: Moxifloxacin
parent: Solo predicción del modelo (L5)
nav_order: 544
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
description: "Moxifloxacin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (nivel de evidencia L5). Indicación original: Infecciones bacterianas (neumonía bacteriana, peritonitis…"
monitor_inn: "Moxifloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "hematopoietic and lymphoid system neoplasm"]
---

# Moxifloxacin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Moxifloxacino: De Infecciones Bacterianas a Síndrome de Hiperviscosidad Policlonal
{: .text-alpha }

## Resumen en Una Frase

Moxifloxacino es una fluoroquinolona antibacteriana, utilizada originalmente para tratar infecciones como la neumonía bacteriana, la peritonitis, la conjuntivitis y la peste.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hiperviscosidad policlonal**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones bacterianas (neumonía bacteriana, peritonitis, infecciones estreptocócicas y estafilocócicas, conjuntivitis, peste, entre otras) |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 10) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, moxifloxacino pertenece a la clase de las fluoroquinolonas. Su eficacia en infecciones bacterianas está bien establecida, y actúa inhibiendo la ADN girasa y la topoisomerasa IV bacterianas.

**Con los datos actuales, la predicción no resulta mecanísticamente plausible.** El síndrome de hiperviscosidad policlonal es un trastorno reológico causado por proteínas o inmunoglobulinas, y un antibacteriano no actúa sobre ese proceso. El puntaje alto de TxGNN (0.9998) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no hay ensayos ni literatura que lo sustenten.

Por ello, esta predicción debe considerarse una hipótesis sin respaldo. Otras predicciones del mismo modelo tienen una base más sólida. Un ejemplo es la **peste bubónica** (rango 10), que es una extensión cercana de usos ya existentes (peste y peste neumónica) y cuenta con estudios preclínicos in vitro y en modelos animales.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Hay 20 autorizaciones vigentes, todas de producto único (sin combinaciones) y ninguna cancelada. Se muestran las 5 principales, que cubren las distintas formas farmacéuticas (oral, oftálmica e intravenosa). Los textos de indicación aprobada no estaban disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 83222 | ACTIRA 400 mg/250 ml solución para perfusión | Solución para perfusión | Bayer Hispania S.L. |
| 77662 | Moxifloxacino Cinfa 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorios Cinfa S.A. |
| 78593 | Moxifloxacino Kern Pharma 5 mg/ml colirio en solución | Colirio en solución | Kern Pharma S.L. |
| 82031 | Moxifloxacino Krka 400 mg/250 ml solución para perfusión EFG | Solución para perfusión | Krka D.D. Novo Mesto |
| 78336 | ABIOX 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Tiedra Farmacéutica S.L. |

---

## Consideraciones de Seguridad

No se dispone de datos de advertencias ni de contraindicaciones extraídos del prospecto; consultar el prospecto para esa información.

- **Contraindicaciones o condiciones de riesgo según el grafo de conocimiento (no proceden del texto del prospecto):**
  - Cardiovasculares: síndrome de QT largo (incluido el familiar), torsades de pointes, parada cardíaca súbita, enfermedad de la conducción cardíaca, isquemia miocárdica y enfermedad coronaria.
  - Neurológicas y neuromusculares: epilepsia, miastenia gravis (incluida la del adulto), enfermedad de la unión neuromuscular, neuropatía periférica y enfermedad del sistema nervioso periférico.
  - Musculoesqueléticas: tendinitis, periartritis y exostosis.
  - Hepáticas: cirrosis hepática y daño hepático inducido por fármacos.
  - Digestivas: colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
  - Metabólicas: deficiencia de potasio.
- **Interacciones farmacológicas:** se registran 100 interacciones. Las clasificadas como **Mayores** incluyen hidrocortisona, dexametasona, betametasona, triamcinolona (corticosteroides), bupropión y clorpropamida. Entre las de nivel **Moderado** figuran antidiabéticos (metformina, pioglitazona, acarbosa, alogliptina, canagliflozina, albiglutida), famotidina, loperamida, ácido acetilsalicílico, bisacodilo y sales de calcio y potasio.

Para la indicación predicha, la seguridad merece especial atención en la neuropatía periférica y en la disglucemia, ya que las fluoroquinolonas se asocian a ambas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo cuenta con el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre un antibacteriano y un trastorno de hiperviscosidad causado por proteínas.

**Para avanzar se necesita:**
- Una hipótesis mecanística creíble y datos preclínicos que la respalden (hoy no hay ninguno).
- Una revisión dirigida de la literatura sobre hiperviscosidad policlonal y fluoroquinolonas.
- Los datos del mecanismo de acción y las advertencias y contraindicaciones del prospecto de la AEMPS, para completar la evaluación de seguridad.
- Priorizar otras predicciones con mayor respaldo, como la peste bubónica, antes de invertir recursos en esta indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

