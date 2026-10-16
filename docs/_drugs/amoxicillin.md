---
layout: default
title: Amoxicillin
parent: Solo predicción del modelo (L5)
nav_order: 53
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Amoxicillin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (nivel de evidencia L5). Indicación original: Infección del tracto urinario (según el grafo de conocimiento"
monitor_inn: "Amoxicillin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Amoxicillin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Amoxicilina: De Infección del Tracto Urinario a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

Amoxicilina es un antibiótico betalactámico, utilizado originalmente para tratar infecciones bacterianas como la infección del tracto urinario, la otitis media infecciosa, la faringitis y la neumonía bacteriana.
El modelo TxGNN predice que podría ser efectivo para **síndrome de hiperviscosidad policlonal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección del tracto urinario (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, la amoxicilina es un antibiótico betalactámico que inhibe la síntesis de la pared celular bacteriana, y su eficacia en infecciones bacterianas está bien establecida.

**En este caso, la predicción no es mecanísticamente plausible.** El síndrome de hiperviscosidad policlonal se debe a niveles elevados de inmunoglobulinas u otras proteínas séricas, algo sobre lo que la amoxicilina no actúa. No existe relación clara entre las indicaciones originales (infecciones bacterianas) y esta nueva indicación (un trastorno hematológico no infeccioso).

El puntaje alto (0.996) probablemente es un artefacto del grafo de conocimiento, sin respaldo en evidencia clínica ni bibliográfica. Otras predicciones del mismo ranking con puntajes similares (hiperamilasemia, analbuminemia congénita, entre otras) comparten la misma limitación.

Entre las predicciones evaluadas, la única biológicamente plausible es la **peste septicémica** (infección por *Yersinia pestis*), aunque los betalactámicos no son tratamiento de primera línea (se prefieren aminoglucósidos, fluoroquinolonas y tetraciclinas) y la evidencia disponible es indirecta (estudios in vitro, modelos animales y casos aislados).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para el síndrome de hiperviscosidad policlonal.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el síndrome de hiperviscosidad policlonal.

---

## Información de Mercado en España

La amoxicilina cuenta con 20 autorizaciones vigentes (todas de principio activo único, ninguna cancelada). Se listan las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62337 | Amoxicilina Pensa 1 g comprimidos recubiertos EFG | Comprimido recubierto | No disponible |
| 64117 | Amoxicilina Cinfa 1000 mg polvo para suspensión oral en sobres EFG | Polvo para suspensión oral | No disponible |
| 85966 | Amoxicilina Reiwa Healthcare 250 mg polvo para suspensión oral en sobre EFG | Polvo para suspensión oral | No disponible |
| 50239 | Clamoxyl 500 mg cápsulas duras | Cápsula dura | No disponible |
| 64390 | Amoxicilina Normon 1000 mg comprimidos EFG | Comprimido | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): síndrome de QT largo, torsades de pointes, taquicardia ventricular, insuficiencia hepática y enfermedad hepática, colestasis, porfiria, enfermedad renal, colitis por *Clostridium difficile*, miastenia gravis, osteoporosis, fractura ósea, mononucleosis infecciosa, entre otras.
- **Interacciones farmacológicas** (100 interacciones registradas; se muestran las de mayor relevancia):
  - **Mayor**: metotrexato; vacuna viva de *Vibrio cholerae* (cepa CVD 103-HgR).
  - **Moderada**: doxiciclina, minociclina, demeclociclina, etinilestradiol, estradiol, anisindiona, dicumarol, micofenolato de mofetilo, entecavir, balsalazida, probióticos (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*), indio In-111 oxiquinolina.
  - **Menor**: alopurinol, amilorida, azitromicina, claritromicina, eritromicina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para síndrome de hiperviscosidad policlonal es solo computacional (L5), sin ensayos clínicos ni literatura, y carece de plausibilidad mecanística; el puntaje alto parece un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y un vínculo mecanístico justificable con la nueva indicación (hoy inexistente).
- Advertencias y contraindicaciones del prospecto de la AEMPS, pendientes de obtener, para completar el cribado de seguridad.
- Si se desea priorizar una línea de investigación con amoxicilina, valorar la **peste septicémica** como pregunta de investigación (nivel L4, evidencia indirecta), comparándola con los tratamientos de primera línea.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

