---
layout: default
title: Amikacin
parent: Solo predicción del modelo (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
monitor_inn: "amikacin"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "punctate epithelial keratoconjunctivitis", "typhoid fever", "epiglottitis", "salmonellosis", "congenital analbuminemia", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "meningococcemia"]
last_modified_at: 2026-11-24
description: "Amikacin: nueva indicación predicha, fiebre paratifoidea (paratyphoid fever) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 8 (comercializadas: 4; autorizadas no comercializadas: 3)"
---

# Amikacin
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

## Amikacina: aminoglucósido antibacteriano → fiebre paratifoidea (paratyphoid fever)
{: .text-alpha }

## Resumen en Una Frase

Amikacina es un antibiótico aminoglucósido con actividad frente a bacterias gramnegativas.
El modelo TxGNN predice que podría ser efectivo para **fiebre paratifoidea (paratyphoid fever)**,
pero hasta ahora no hay ensayos clínicos y solo existen **8 publicaciones**, casi todas de epidemiología o antibiogramas, que tocan el tema de forma indirecta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | fiebre paratifoidea (paratyphoid fever) |
| Puntaje de Predicción TxGNN | 0.9982 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 8; autorizadas no comercializadas: 3; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 8 (comercializadas: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Amikacin (traducción no oficial): «La amikacina, un aminoglucósido, se une al ribosoma procariota e inhibe la síntesis de proteínas en las bacterias sensibles. Es bactericida in vitro frente a bacterias grampositivas y gramnegativas.» Texto original en inglés: "Amikacin, an aminoglycoside, binds to the prokaryotic ribosome, inhibiting protein synthesis in susceptible bacteria. It is bactericidal in vitro against Gram-positive and Gram-negative bacteria." ([DailyMed: amikacin sulfate prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f260ff2a-76a0-4672-9516-91c344b67890), versión del 2026-07-27; consultado el 2026-11-19). Según la información conocida, amikacina pertenece a la clase de los aminoglucósidos, que actúan contra bacterias gramnegativas, entre ellas enterobacterias como *Salmonella*. Por tanto, existe un vínculo antibacteriano plausible con la fiebre paratifoidea, causada por *Salmonella* Paratyphi.

Sin embargo, el vínculo es débil en la práctica: *Salmonella* vive dentro de los macrófagos y los aminoglucósidos penetran mal en el interior de las células, por lo que en general no son eficaces en la fiebre entérica. Además, ninguno de los estudios aportados evalúa directamente la amikacina como tratamiento de la fiebre paratifoidea.

Por esta razón, aunque el puntaje del modelo es alto, el nivel de evidencia se limita a L5: la literatura disponible es indirecta (vigilancia epidemiológica, sensibilidad antibiótica y casos aislados) y no estudia la enfermedad con amikacina como intervención.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Reporte de caso | Pediatric Hematology and Oncology | Niño con leucemia linfoblástica y colecistitis alitiásica por *S.* Paratyphi B, tratado con cefepima, amikacina y factor estimulante de granulocitos con buena evolución (amikacina dentro de una combinación) |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Serie de casos | Mikrobiyoloji Bülteni | Tratamiento y antibiograma de 48 pacientes con infección por paratifoidea B resistente al tratamiento clásico |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Cohorte prospectiva | Journal of the Indian Medical Association | Perfil clínico y sensibilidad antibiótica de *S.* Typhi y Paratyphi en 145 niños con fiebre entérica |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Estudio microbiológico | Pakistan Journal of Biological Sciences | Aislamiento e identificación de *S.* Paratyphi en pacientes con fiebre entérica |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Epidemiología | Medical Journal, Armed Forces India | Patrón de sensibilidad in vitro de *S.* Typhi y Paratyphi A; reaparición de sensibilidad al cloranfenicol |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Epidemiología | The New Microbiologica | Presencia de *S.* Typhi y Paratyphi en casos de diarrea notificados en Jordania, 1988-2000 |
| [8354556](https://pubmed.ncbi.nlm.nih.gov/8354556/) | 1993 | Epidemiología | Indian Journal of Pathology & Microbiology | Cepas de *S.* Typhi multirresistentes, pero sensibles a aminoglucósidos y ciprofloxacino |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Encuesta de antibiogramas | JNMA | Frecuencia de aislamientos en hemocultivos y patrones de sensibilidad |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 57012 | AMIKACINA NORMON 500 MG/2 ML SOLUCION INYECTABLE Y PARA PERFUSIÓN EFG | SOLUCIÓN INYECTABLE | Laboratorios Normon S.A. | Comercializada |
| 63879 | AMICACINA B BRAUN 5 MG/ML SOLUCION PARA PERFUSION INTRAVENOSA | SOLUCIÓN PARA PERFUSIÓN | B Braun Medical S.A. | Comercializada |
| 63880 | AMICACINA B BRAUN 10 mg/ml SOLUCION PARA PERFUSION INTRAVENOSA | SOLUCIÓN PARA PERFUSIÓN | B Braun Medical S.A. | Comercializada |
| 58048 | AMICACINA BRAUN 500 MG/2ML SOLUCIÓN INYECTABLE | SOLUCIÓN INYECTABLE | B Braun Medical S.A. | Comercializada |
| 85160 | AMIKACINA KABI 5 MG/ML SOLUCION PARA PERFUSION | SOLUCIÓN PARA PERFUSIÓN | Fresenius Kabi España, S.A.U. | Autorizada, no comercializada |
| 90159 | AMIKACINA NORIDEM 125 MG/ML SOLUCIÓN INYECTABLE Y PARA PERFUSION EFG | SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Noridem Enterprises Limited | Autorizada, no comercializada |
| 90160 | AMIKACINA NORIDEM 250 MG/ML SOLUCIÓN INYECTABLE Y PARA PERFUSION EFG | SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Noridem Enterprises Limited | Autorizada, no comercializada |
| 67333 | AMIKACINA SALA 125 mg / 2 ml SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Laboratorio Reig Jofre, S.A. | Revocada |

Se muestran las 8 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 212 interacciones. Las de nivel mayor incluyen sulfato de magnesio y manitol. Entre las de nivel moderado figuran anfotericina B, kanamicina, neomicina, ácido acetilsalicílico, mesalazina y varios inhibidores de la bomba de protones (omeprazol, pantoprazol, esomeprazol, lansoprazol, rabeprazol).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y ningún estudio evalúa directamente la amikacina en la fiebre paratifoidea. La literatura es epidemiológica o de sensibilidad in vitro, y los aminoglucósidos no son una opción habitual en la fiebre entérica por su escasa penetración intracelular.

**Para avanzar se necesita:**
- Estudios clínicos que evalúen amikacina específicamente en fiebre paratifoidea, con comparación frente a los tratamientos habituales
- Datos del mecanismo de acción y de la penetración intracelular frente a *Salmonella*
- Información de advertencias y contraindicaciones del prospecto de las autorizaciones españolas
- Plan de monitorización de seguridad (función renal, audición y función neuromuscular), dado el perfil de riesgo de los aminoglucósidos

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: amikacin sulfate prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f260ff2a-76a0-4672-9516-91c344b67890) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

