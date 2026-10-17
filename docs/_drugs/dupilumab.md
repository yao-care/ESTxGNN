---
layout: default
title: Dupilumab
parent: Solo predicción del modelo (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dupilumab: nueva indicación predicha, Bronquitis (nivel de evidencia L5). Indicación original: Dermatitis atópica (los datos de autorización de la AEMPS no incluyen…"
monitor_inn: "DUPILUMAB"
predicted_indications: ["bronchitis", "acne keloid", "exanthem (disease)", "neonatal dermatomyositis", "acrodermatitis chronica atrophicans", "amyopathic dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "hydroa vacciniforme, familial", "severe nonproliferative diabetic retinopathy"]
---

# Dupilumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Dupilumab: De Dermatitis Atópica a Bronquitis

## Resumen en Una Frase

Dupilumab es un anticuerpo monoclonal dirigido contra el receptor alfa de la interleucina-4 (IL-4Rα), utilizado originalmente para el tratamiento de la dermatitis atópica.
El modelo TxGNN predice que podría ser efectivo para **bronquitis** (primera predicción de la lista), con **1 ensayo clínico** (indirecto, en rinosinusitis crónica sin pólipos nasales) y **10 publicaciones** que actualmente respaldan esta dirección, de forma mayoritariamente indirecta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatitis atópica (los datos de autorización de la AEMPS no incluyen texto de indicación; se toma de las indicaciones originales del grafo de conocimiento) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L2 (según el análisis de los datos compilados; evidencia indirecta, ver nota) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

> **Nota:** el único ensayo (Fase 2, completado) corresponde a rinosinusitis crónica, no a bronquitis. La evidencia se limita en la práctica a fenotipos de inflamación tipo 2 (asma, EPOC tipo 2), por lo que se recomienda mantener la decisión en espera hasta contar con datos directos.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información conocida, dupilumab bloquea la subunidad IL-4Rα, inhibiendo así la señalización de IL-4 e IL-13, las citocinas centrales de la inflamación tipo 2. Su eficacia en dermatitis atópica está comprobada.

La dermatitis atópica y ciertas enfermedades de la vía aérea comparten una base inmunológica tipo 2. La literatura recopilada respalda la eficacia de dupilumab en asma (metaanálisis de ECA y extensión a largo plazo TRAVERSE) y en EPOC con fenotipo tipo 2 (series de práctica real). También hay reportes en bronquitis plástica eosinofílica pediátrica y bronquiolitis eosinofílica.

Sin embargo, "bronquitis" es una etiqueta genérica y heterogénea. El mecanismo es aplicable sobre todo a los fenotipos eosinofílicos o tipo 2, y no necesariamente a la bronquitis aguda o infecciosa. Por eso la evidencia para bronquitis como tal es indirecta.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Fase 2 | Completado | 33 | Dupilumab vs. placebo (doble ciego, aleatorizado) en rinosinusitis crónica sin pólipos nasales; relevancia indirecta (biología tipo 2 de la vía aérea), no es un ensayo de bronquitis |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | ECA (extensión abierta a largo plazo) | Lancet Respir Med | Seguridad y eficacia a largo plazo de dupilumab en asma moderada-grave (TRAVERSE) |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Metaanálisis de ECA | J Asthma | Eficacia y seguridad de dupilumab en asma no controlada |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Revisión | Tuberc Respir Dis | Terapias farmacológicas para prevenir exacerbaciones de EPOC |
| [42617837](https://pubmed.ncbi.nlm.nih.gov/42617837/) | 2026 | Comparación indirecta ajustada | Chest | Mepolizumab y dupilumab sin diferencias significativas en reducir exacerbaciones en EPOC eosinofílica |
| [42511891](https://pubmed.ncbi.nlm.nih.gov/42511891/) | 2026 | Cohorte (práctica real) | Biomedicines | Serie de 12 pacientes con EPOC tipo 2 tratados con dupilumab por uso compasivo |
| [42839285](https://pubmed.ncbi.nlm.nih.gov/42839285/) | 2026 | Cohorte multicéntrica | Respir Res | Efectividad de dupilumab en EPOC en práctica real en Alemania |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Revisión | Pediatr Pulmonol | Terapias novedosas para bronquitis plástica eosinofílica pediátrica |
| [41672525](https://pubmed.ncbi.nlm.nih.gov/41672525/) | 2026 | Reporte de casos | Intern Med | Dos casos de bronquiolitis eosinofílica tratados con éxito con biológicos, incluido dupilumab |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revisión | Expert Opin Pharmacother | Manejo del asma asociada a enfermedades de las vías aéreas inducidas por el tabaco |
| [42773542](https://pubmed.ncbi.nlm.nih.gov/42773542/) | 2026 | Revisión | Eur J Clin Invest | Novedades en el manejo de la EPOC, de vías inflamatorias a terapias dirigidas |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171229018 | DUPIXENT 300 MG solución inyectable en pluma precargada | Solución inyectable | No disponible en los datos compilados |
| 1171229014 | DUPIXENT 200 MG solución inyectable en pluma precargada | Solución inyectable | No disponible en los datos compilados |
| 1171229006 | DUPIXENT 300 MG solución inyectable en jeringa precargada | Solución inyectable | No disponible en los datos compilados |
| 1171229010 | DUPIXENT 200 MG solución inyectable en jeringa precargada | Solución inyectable | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 53 interacciones en total. Entre las visibles en los datos compilados:
  - **Mayor:** adalimumab, baricitinib, certolizumab pegol, cladribina.
  - **Moderada:** warfarina, roflumilast, alefacept, alemtuzumab, anakinra, azatioprina, canakinumab, ciclosporina, denosumab, dimetilfumarato, diroximilfumarato y la vacuna viva contra el cólera (Vibrio cholerae CVD 103-HgR).
  - **Menor:** sales de zinc (acetato, gluconato, sulfato, cloruro).
- **Efectos adversos descritos en la literatura:** conjuntivitis, erupciones psoriasiformes, dermatitis de cabeza y cuello, aumentos transitorios de eosinófilos y una posible señal de linfoma cutáneo de células T en evaluación.

Para advertencias y contraindicaciones formales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje TxGNN es muy alto, no hay ensayos en bronquitis y la evidencia proviene de asma y EPOC tipo 2, es decir, de fenotipos específicos. El único ensayo listado es de rinosinusitis crónica.

**Para avanzar se necesita:**
- Definir el fenotipo de bronquitis objetivo (por ejemplo, eosinofílica o tipo 2, o bronquitis crónica asociada a EPOC tipo 2).
- Ensayos clínicos específicos en ese fenotipo.
- Datos detallados del mecanismo de acción.
- Advertencias y contraindicaciones del prospecto de la AEMPS (actualmente no disponibles).
- Plan de monitoreo de seguridad (ocular, cutáneo y de eosinofilia).

### Otras predicciones del modelo (referencia)

| Enfermedad predicha | Puntaje TxGNN | Nivel de evidencia | Recomendación |
|------|------|------|------|
| Dermatitis | 99.71% | L1 | Proceed with Guardrails (señal que se solapa en gran parte con la indicación original; múltiples ECA de Fase 3 completados) |
| Queloide acneiforme | 99.61% | L4 | Hold |
| Exantema | 99.57% | L3 | Research Question |
| Dermatomiositis neonatal | 99.56% | L5 | Hold |
| Acrodermatitis crónica atrófica | 99.54% | L5 | Hold |
| Dermatomiositis amiopática | 99.53% | L5 | Hold |
| Enfermedad pulmonar intersticial infantil asociada a enfermedad del tejido conectivo | 99.52% | L5 | Hold |
| Hidroa vacciniforme familiar | 99.50% | L5 | Hold |
| Retinopatía diabética no proliferativa grave | 99.10% | L5 | Hold |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

