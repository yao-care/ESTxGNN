---
layout: default
title: Letermovir
parent: Solo predicción del modelo (L5)
nav_order: 462
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
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

# Letermovir: De Infección por Citomegalovirus a Candidiasis Vulvovaginal

## Resumen en Una Frase

Letermovir es un antiviral originalmente utilizado para la infección por citomegalovirus (CMV).
El modelo TxGNN predice que podría ser efectivo para **candidiasis vulvovaginal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por citomegalovirus |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 99,88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado en las fuentes compiladas. No obstante, según el conocimiento farmacológico general, letermovir inhibe el complejo terminasa del CMV humano (pUL56/pUL51/pUL89), una diana esencial para el empaquetamiento del ADN viral.

**En este caso no se identifica un vínculo mecanístico creíble.** La candidiasis vulvovaginal está causada por especies de *Candida* (principalmente *C. albicans*), hongos eucariotas que carecen de un equivalente de la terminasa viral. Por tanto, no cabe esperar que el mecanismo antiviral de letermovir actúe sobre ellos. Tampoco existen datos antifúngicos in vitro ni observaciones clínicas que apoyen la hipótesis.

La puntuación tan elevada del modelo (0,9988) debe interpretarse con cautela: podría reflejar artefactos del grafo de conocimiento, como conexiones compartidas a través de nodos de interacciones farmacológicas o de CYP (por ejemplo, interacciones con antifúngicos azólicos), y no una relevancia terapéutica real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171245002 | PREVYMIS 480 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1171245003 | PREVYMIS 240 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 1171245001 | PREVYMIS 240 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1171245004 | PREVYMIS 480 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |

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
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible entre un inhibidor de la terminasa viral y un patógeno fúngico. La puntuación alta probablemente sea un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- Datos de actividad antifúngica in vitro de letermovir frente a *Candida* spp.
- Datos detallados del mecanismo de acción (MOA)
- Revisión del prospecto de la AEMPS para advertencias y contraindicaciones
- Análisis de los nodos del grafo que originan la puntuación para descartar artefactos
- Evaluación de la compatibilidad de vías de administración (las formas actuales son oral e intravenosa, no tópica/vaginal)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

