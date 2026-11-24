---
layout: default
title: Letermovir
parent: Solo predicción del modelo (L5)
nav_order: 462
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Letermovir: nueva indicación predicha, Candidiasis vulvovaginal (nivel de evidencia L5). Indicación original: Infección por citomegalovirus"
monitor_inn: "LETERMOVIR"
predicted_indications: ["vulvovaginal candidiasis"]
---

# Letermovir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Letermovir: De Infección por Citomegalovirus a Candidiasis Vulvovaginal
{: .text-alpha }

## Resumen en Una Frase

Letermovir es un antiviral originalmente utilizado para la infección por citomegalovirus (CMV).
El modelo TxGNN predice que podría ser efectivo para **candidiasis vulvovaginal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por citomegalovirus |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 0,9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 4; autorizadas no comercializadas: 2) |
| Número de Autorizaciones | 4 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Letermovir (traducción no oficial): «PREVYMIS es un fármaco antiviral contra el CMV. […] El letermovir inhibe el complejo de la terminasa del ADN del CMV (pUL51, pUL56 y pUL89), que es necesario para el procesamiento y el empaquetamiento del ADN viral. La caracterización bioquímica y la microscopía electrónica demostraron que el letermovir afecta la producción de genomas de longitud unitaria adecuada e interfiere con la maduración de los viriones.» Texto original en inglés: "PREVYMIS is an antiviral drug against CMV. […] Letermovir inhibits the CMV DNA terminase complex (pUL51, pUL56, and pUL89) which is required for viral DNA processing and packaging. Biochemical characterization and electron microscopy demonstrated that letermovir affects the production of proper unit length genomes and interferes with virion maturation." ([DailyMed: Prevymis (letermovir) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1b49df80-be4f-47e0-a0b7-123f3e69395b), versión del 2026-01-14; consultado el 2026-11-19). No obstante, según el conocimiento farmacológico general, letermovir inhibe el complejo terminasa del CMV humano (pUL56/pUL51/pUL89), una diana esencial para el empaquetamiento del ADN viral.

**En este caso no se identifica un vínculo mecanístico creíble.** La candidiasis vulvovaginal está causada por especies de *Candida* (principalmente *C. albicans*), hongos eucariotas que carecen de un equivalente de la terminasa viral. Por tanto, no cabe esperar que el mecanismo antiviral de letermovir actúe sobre ellos. Tampoco existen datos antifúngicos in vitro ni observaciones clínicas que apoyen la hipótesis.

La puntuación tan elevada del modelo (0,9988) debe interpretarse con cautela: podría reflejar artefactos del modelo TxGNN (aprendizaje profundo), como conexiones compartidas a través de nodos de interacciones farmacológicas o de CYP (por ejemplo, interacciones con antifúngicos azólicos), y no una relevancia terapéutica real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1171245002 | PREVYMIS 480 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Merck Sharp & Dohme B.V. | Comercializada |
| 1171245001 | PREVYMIS 240 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Merck Sharp & Dohme B.V. | Comercializada |
| 1171245003 | PREVYMIS 240 MG CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Merck Sharp & Dohme B.V. | Autorizada, no comercializada |
| 1171245004 | PREVYMIS 480 MG CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Merck Sharp & Dohme B.V. | Autorizada, no comercializada |

Se muestran las 4 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Todas las autorizaciones están vigentes y pertenecen a Merck Sharp & Dohme B.V.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las mostradas, destacan las de nivel **mayor** con:
  - Eliglustat
  - Naloxegol
  - Cisapride

  También se registraron interacciones de nivel **moderado** con, entre otros:
  - Corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona)
  - Antidiabéticos (pioglitazona, glimepirida, saxagliptina, clorpropamida, acetohexamida)
  - Inhibidores de la bomba de protones (omeprazol, lansoprazol)
  - Claritromicina
  - Aprepitant
  - Naldemedina
  - Nitisinona

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible entre un inhibidor de la terminasa viral y un patógeno fúngico. La puntuación alta probablemente sea un artefacto del modelo TxGNN (aprendizaje profundo).

**Para avanzar se necesita:**
- Datos de actividad antifúngica in vitro de letermovir frente a *Candida* spp.
- Datos detallados del mecanismo de acción (MOA)
- Revisión del prospecto de la AEMPS para advertencias y contraindicaciones
- Revisión de que la puntuación procede del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, para descartar artefactos
- Evaluación de la compatibilidad de vías de administración (las formas actuales son oral e intravenosa, no tópica/vaginal)

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Prevymis (letermovir) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1b49df80-be4f-47e0-a0b7-123f3e69395b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

