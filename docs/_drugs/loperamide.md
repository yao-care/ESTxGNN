---
layout: default
title: Loperamide
parent: Solo predicción del modelo (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamida: De Diarrea a Conjuntivitis Contagiosa Aguda

## Resumen en Una Frase

Loperamida es un agonista opioide periférico, utilizado originalmente para tratar la diarrea.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis contagiosa aguda**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. El puntaje alto parece un artefacto del grafo de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diarrea (según la ficha farmacológica; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Conjuntivitis contagiosa aguda |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Por ahora **no es razonable**. Loperamida actúa como agonista del receptor opioide μ (gen *OPRM1*) a nivel periférico. Reduce la motilidad y la secreción intestinales, lo que explica su uso en la diarrea. No se conoce que tenga acción antiinfecciosa ni antiinflamatoria ocular.

La diarrea y la conjuntivitis contagiosa aguda no comparten órgano, fisiopatología ni mecanismo farmacológico plausible. Además, la vía de administración oral de los productos comercializados no es compatible con un tratamiento ocular. El puntaje TxGNN elevado probablemente proviene de asociaciones indirectas del grafo de conocimiento, sin base biológica verificable.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 88777 | LOPERAMIDA OPKO 2 MG CAPSULAS DURAS EFG | Cápsula dura |
| 89192 | LOPERAMIDA GRINDEKS 2 MG CÁPSULAS DURAS | Cápsula dura |
| 36747 | SALVACOLINA 0,2 mg/ml SOLUCIÓN ORAL | Solución oral |
| 9091IP | FORTASEC FLAS 2 MG LIOFILIZADO ORAL | Liofilizado oral |
| 67219 | DIARFIN 2 mg CAPSULAS DURAS | Cápsula dura |

Se muestran 5 de las 20 autorizaciones. Las formas registradas incluyen también comprimidos y comprimidos bucodispersables.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Las publicaciones asociadas a otras predicciones del modelo señalan dos riesgos:
- **Colitis amebiana fulminante** tras el uso de loperamida (PMID 17241255, caso clínico). Los antimotilidad suelen evitarse en disentería invasiva.
- **Depresión respiratoria** en pacientes con inflamación gastrointestinal grave por quimioterapia (PMID 41924411, caso clínico de 2026). Una mucosa dañada podría aumentar la absorción y la exposición central.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos, literatura ni mecanismo plausible para conjuntivitis contagiosa aguda. La predicción se basa solo en el modelo (L5) y se considera un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- No dedicar recursos a esta indicación ni a las otras variantes de conjuntivitis (rangos 3 y 5 a 9) salvo que aparezca una hipótesis mecanística nueva.
- Si se quiere explorar algo del listado, la única señal con evidencia es **gastroduodenitis** (L3, "Research Question"). Se apoya en un estudio clínico de 1986 de diseño no verificado y solo aliviaría síntomas, no la inflamación de fondo. Requeriría verificar el diseño del estudio y evaluar el riesgo de absorción sistémica.
- **Amebiasis/disentería amebiana** (rango 2) queda descartada por la señal de seguridad descrita.
- Obtener la ficha técnica de la AEMPS para completar advertencias, contraindicaciones e indicaciones aprobadas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

