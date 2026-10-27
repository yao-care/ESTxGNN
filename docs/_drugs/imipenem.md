---
layout: default
title: Imipenem
parent: Solo predicción del modelo (L5)
nav_order: 409
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Imipenem: nueva indicación predicha, Esclerodermia difusa (nivel de evidencia L5). Indicación original: Neumonía bacteriana, peritonitis, neumonía estreptocócica…"
monitor_inn: "imipenem"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "staphylococcus aureus infection", "eosinophilia-myalgia syndrome"]
---

# Imipenem
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

## Imipenem: De Neumonía Bacteriana a Esclerodermia Difusa
{: .text-alpha }

## Resumen en Una Frase

Imipenem es un antibiótico carbapenémico de amplio espectro (comercializado junto con cilastatina), utilizado originalmente para infecciones bacterianas graves como neumonía bacteriana, peritonitis, endocarditis y endometritis.
El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa**, aunque no existen ensayos clínicos ni publicaciones que respalden esta predicción (evidencia solo del modelo).
Entre las demás predicciones, la que cuenta con más respaldo es la **infección por Staphylococcus aureus** (2 ensayos clínicos de Fase 4 y 19 publicaciones), seguida de la **fiebre tifoidea** (18 publicaciones, principalmente observacionales).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Neumonía bacteriana, peritonitis, neumonía estreptocócica, endocarditis, endometritis (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Esclerodermia difusa |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Hold |

> **Nota:** la predicción con mayor puntaje (esclerodermia difusa) carece de respaldo. Las candidatas con más evidencia se detallan en la sección de predicciones alternativas.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, imipenem es un carbapenémico bactericida que inhibe la síntesis de la pared celular bacteriana mediante la unión a proteínas de unión a penicilina (PBP), y es estable frente a muchas beta-lactamasas.

**Para esclerodermia difusa, la predicción no resulta mecanísticamente razonable.** La esclerodermia difusa es una enfermedad autoinmune y fibrótica, y no existe un vínculo mecanístico aparente con un antibacteriano. El puntaje elevado es una predicción basada en el grafo, sin ensayos ni literatura de apoyo. Las complicaciones infecciosas (por ejemplo, pulmonares o intestinales) se tratarían bajo las indicaciones antibacterianas ya existentes, no como reposicionamiento para la enfermedad en sí.

**Predicciones alternativas con mayor plausibilidad biológica:**

| Predicción | Puntaje TxGNN | Nivel | Valoración |
|------|------|------|------|
| Infección por *Staphylococcus aureus* | 99.95% | L2 | Sinergia con fosfomicina frente a SARM; imipenem en monoterapia no es adecuado para SARM |
| Fiebre tifoidea | 99.98% | L4 | Los carbapenémicos se usan como última línea en *Salmonella* Typhi XDR |
| Fiebre paratifoidea | 99.99% | pendiente | Solo estudios de sensibilidad antimicrobiana |
| Salmonelosis | 99.99% | L4 | Evidencia indirecta; papel de rescate como máximo |
| Sinusitis / rinosinusitis crónica / sinusitis etmoidal crónica | 99.98% | L4 / L4 / L5 | Actividad plausible, pero sin datos clínicos específicos de imipenem; preocupaciones de uso racional de antibióticos |
| Neoplasia de seno paranasal; síndrome de eosinofilia-mialgia | 99.98% / 99.85% | L5 | Sin vínculo mecanístico |

---

## Evidencia de Ensayos Clínicos

Para esclerodermia difusa: actualmente no hay ensayos clínicos relacionados registrados.

Como referencia, ensayos de la predicción alternativa con más respaldo (infección por *S. aureus*):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00871104](https://clinicaltrials.gov/study/NCT00871104) | Fase 4 | Completado | 50 | Fosfomicina + imipenem frente a vancomicina (tratamiento estándar) en endocarditis infecciosa por SARM; evalúa eficacia y seguridad |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Fase 4 | Desconocido | 60 | Linezolid solo o combinado con carbapenémico frente a SARM en neumonía asociada a ventilación mecánica; el carbapenémico no es necesariamente imipenem |

---

## Evidencia de Literatura

Para esclerodermia difusa: actualmente no hay literatura relacionada disponible.

Como referencia, publicaciones seleccionadas de las predicciones alternativas:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39991360](https://pubmed.ncbi.nlm.nih.gov/39991360/) | 2025 | Cohorte | Cureus | Carbapenémicos como última línea de defensa en fiebre tifoidea MDR/XDR (Peshawar) |
| [40212028](https://pubmed.ncbi.nlm.nih.gov/40212028/) | 2025 | Cohorte | Open Forum Infect Dis | Tendencias de fiebre entérica y aparición de tifoidea XDR en Pakistán |
| [15707075](https://pubmed.ncbi.nlm.nih.gov/15707075/) | 2003 | Reporte de caso | J Med Liban | Rabdomiólisis e insuficiencia renal por *S. typhi* tratadas con éxito con imipenem/cilastatina y hemodiálisis |
| [19208884](https://pubmed.ncbi.nlm.nih.gov/19208884/) | 2009 | Estudio in vitro (MIC) | J Med Microbiol | CMI de carbapenémicos, incluido imipenem, frente a 210 aislados de *Salmonella* spp. |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Reporte de caso | Antimicrob Agents Chemother | Imipenem/cilastatina más fosfomicina en infección refractaria por SARM |
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Cohorte | Antimicrob Agents Chemother | Imipenem-cilastatina en infecciones por *S. aureus* sensible y resistente a meticilina (23 pacientes) |
| [6421794](https://pubmed.ncbi.nlm.nih.gov/6421794/) | 1983 | Estudio animal | J Antimicrob Chemother | Imipenem en endocarditis experimental por *S. aureus* y *S. faecalis* |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | In vitro/animal | J Antimicrob Chemother | Efecto sinérgico de vancomicina e imipenem frente a SARM |
| [32013798](https://pubmed.ncbi.nlm.nih.gov/32013798/) | 2020 | Metaanálisis | Pathog Glob Health | Prevalencia de *Salmonella* resistente a fluoroquinolonas en Irán |
| [9044641](https://pubmed.ncbi.nlm.nih.gov/9044641/) | 1996 | Serie de casos / revisión | Enferm Infecc Microbiol Clin | Celulitis orbitaria grave: imipenem como opción terapéutica válida |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 71285 | Imipenem/Cilastatina Kabi 500 mg/500 mg | Polvo para solución para perfusión | No disponible |
| 82045 | Imipenem/Cilastatina ELC 250 mg/250 mg | Polvo para solución para perfusión | No disponible |
| 84189 | Imipenem/Cilastatina Hikma 500 mg/500 mg | Polvo para solución para perfusión | No disponible |
| 90726 | Enaros 500 mg/500 mg | Polvo para solución para perfusión | No disponible |
| 72637 | Imipenem/Cilastatina Aurovitas 500 mg/500 mg | Polvo para solución para perfusión | No disponible |

Hay 9 autorizaciones vigentes en total (todas de principio activo único, ninguna cancelada); se muestran las 5 principales. Entre las restantes figura Recarbrio (imipenem/cilastatina/relebactam, Merck Sharp & Dohme B.V.).

---

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo según el grafo de conocimiento** (no proviene del texto del prospecto): epilepsia, enfermedad renal, piouréter, colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones farmacológicas** (15 identificadas):
  - **Gravedad mayor:** bupropión, iohexol, iopamidol.
  - **Gravedad moderada:** polietilenglicol 3350 con electrolitos, dicumarol, warfarina, lindano, aminofilina, difilina, oxtrifilina, teofilina, ciclosporina, etinilestradiol, ácido micofenólico, pemetrexed.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (esclerodermia difusa) no tiene ensayos, literatura ni vínculo mecanístico plausible; es un artefacto del grafo y corresponde a un nivel de evidencia L5. Las líneas con algo de respaldo (infección por *S. aureus* en combinación con fosfomicina, y fiebre tifoidea XDR como opción de rescate) son indirectas o de tamaño pequeño, y se consideran preguntas de investigación, no candidatas para avanzar.

**Para avanzar se necesita:**
- Revisar el prospecto oficial de la AEMPS para completar advertencias, contraindicaciones e indicaciones aprobadas (bloqueante para el cribado de seguridad).
- Obtener los datos del mecanismo de acción desde DrugBank.
- Si se desea explorar reposicionamiento, priorizar las líneas infecciosas: un estudio prospectivo comparativo en tifoidea XDR y un ensayo mayor de imipenem + fosfomicina en infecciones refractorias por SARM.
- Descartar esclerodermia difusa, neoplasia de seno paranasal y síndrome de eosinofilia-mialgia salvo que aparezca una hipótesis mecanística nueva.
- Considerar la restricción por uso racional de antibióticos (carbapenémico parenteral de amplio espectro) en cualquier nueva indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

