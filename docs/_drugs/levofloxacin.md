---
layout: default
title: Levofloxacin
parent: Solo predicción del modelo (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "Levofloxacin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
description: "Levofloxacin: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) (nivel de evidencia L5). Indicación original: No consta en los datos locale"
---

# Levofloxacin
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

## Levofloxacin: Queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Levofloxacino es un antibiótico fluoroquinolónico, utilizado originalmente para infecciones bacterianas como la neumonía, la sinusitis, la pielonefritis y la conjuntivitis bacteriana.
El modelo TxGNN predice que podría ser efectivo para la **queratoconjuntivitis epitelial punteada**, pero actualmente hay **0 ensayos clínicos** y **1 publicación** (un informe de brote de queratoconjuntivitis microsporidiana, sin relación directa con el uso del fármaco), por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 10) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la farmacología conocida, levofloxacino es una fluoroquinolona que inhibe la ADN girasa y la topoisomerasa IV bacterianas, con lo que impide la replicación del ADN y tiene efecto bactericida.

La relación con la indicación original es indirecta. Levofloxacino ya se usa en conjuntivitis bacteriana, por lo que existe una justificación antiinfecciosa ocular. El alto puntaje (0.9992) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Esta justificación tiene límites importantes. La única publicación recuperada describe un brote de queratoconjuntivitis por microsporidios, y las fluoroquinolonas no tienen actividad establecida contra estos organismos. No hay evidencia directa que respalde su uso en la queratoconjuntivitis epitelial punteada. La predicción debe considerarse una hipótesis computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Informe de brote | American Journal of Ophthalmology | Brote de queratoconjuntivitis microsporidiana asociado a contaminación del agua en piscinas de Taiwán. No evalúa levofloxacino como tratamiento |

---

## Información de Mercado en España

Los datos compilados no incluyen el texto de indicación aprobada de estas autorizaciones. Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 68868 | Levofloxacino Serraclinics 5 mg/ml solución para perfusión | Solución para perfusión |
| 74832 | Levofloxacino Aurobindo 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 72160 | Levofloxacino Kabi 5 mg/ml solución para perfusión EFG | Solución para perfusión |
| 69697 | Levofloxacino Normon 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 90054 | Neumax 750 mg comprimidos recubiertos con película | Comprimido recubierto con película |

Las formas farmacéuticas autorizadas son comprimidos y solución para perfusión. Ninguna es una formulación oftálmica.

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento, no el texto del prospecto)**: síndrome de QT largo (incluida la forma familiar) y torsades de pointes; epilepsia; enfermedad hepática y lesión hepática inducida por fármacos; enfermedad de la vesícula biliar; trombocitopenia, leucopenia, pancitopenia y anemia; deficiencia de potasio; tendinitis y otros trastornos tendinosos o periarticulares; diabetes mellitus y cetoacidosis diabética; neuropatía periférica y enfermedades del sistema nervioso periférico; rabdomiólisis; colitis por *Clostridium difficile*; deterioro de la función renal; miastenia gravis y enfermedades de la unión neuromuscular; isquemia miocárdica y enfermedad coronaria.
- **Interacciones farmacológicas**: se registraron 100 interacciones. En el listado revisado (20 de ellas) destacan dos de nivel **Mayor**, con **tramadol** e **hidrocortisona**. La mayoría del resto son de nivel moderado, por ejemplo con antidiabéticos (metformina, pioglitazona, alogliptina, acarbosa), AINE (ibuprofeno, ketorolaco) y broncodilatadores (salbutamol, formoterol). Hay otras de nivel menor, como paclitaxel y aldesleucina.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5). No hay ensayos clínicos, y la única publicación trata de un agente (microsporidios) frente al cual las fluoroquinolonas no tienen actividad establecida. No se identifica evidencia que respalde avanzar con esta indicación.

**Para avanzar se necesita:**
- Evidencia directa de eficacia en queratoconjuntivitis epitelial punteada: estudios in vitro frente a los agentes etiológicos relevantes y estudios clínicos.
- Evaluación de la compatibilidad de vía de administración, ya que las formas autorizadas en España son orales e intravenosas y no existe una formulación oftálmica entre ellas.
- Datos detallados del mecanismo de acción en los datos compilados y los textos oficiales de advertencias y contraindicaciones de las autorizaciones españolas.
- Para otras predicciones de este mismo análisis, como la profilaxis de infecciones en mieloma múltiple (ensayo de fase 3 TEAMM), existe evidencia mucho más sólida y podrían priorizarse en una evaluación aparte.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

