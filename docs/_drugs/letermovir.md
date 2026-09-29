---
layout: default
title: Letermovir
parent: Solo predicción del modelo (L5)
nav_order: 312
evidence_level: L5
indication_count: 1
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Letermovir: De Infección por Citomegalovirus (CMV) a Candidiasis Vulvovaginal

## Resumen en Una Frase

Letermovir es un antiviral comercializado en España como Prevymis, utilizado frente al citomegalovirus (CMV). El modelo TxGNN predice que podría ser efectivo para **candidiasis vulvovaginal** con una puntuación muy alta (99,88 %), pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Antiviral frente a CMV (el texto de indicación no figura en los registros de AEMPS recibidos) |
| Nueva Indicación Predicha | Candidiasis vulvovaginal |
| Puntaje de Predicción TxGNN | 99,88 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, letermovir es un antiviral que inhibe el complejo terminasa viral (pUL56) del CMV. Es una diana específica del virus.

Esa diana no tiene un homólogo conocido en *Candida*, un hongo. Por eso no se identifica una relación mecanística plausible entre la indicación original (una infección viral) y la nueva (una infección fúngica). Tampoco hay una vía o mecanismo declarado que explique la puntuación del modelo.

La alta puntuación de TxGNN (posición 2753) parece más bien un artefacto del grafo de conocimiento que una predicción con fundamento biológico. Debe validarse de forma independiente, por ejemplo con pruebas de sensibilidad *in vitro* frente a *Candida*, antes de cualquier interpretación clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1171245001 | PREVYMIS 240 MG comprimidos recubiertos con película | Comprimido recubierto con película | Merck Sharp & Dohme B.V. |
| 1171245002 | PREVYMIS 480 MG comprimidos recubiertos con película | Comprimido recubierto con película | Merck Sharp & Dohme B.V. |
| 1171245003 | PREVYMIS 240 MG concentrado para solución para perfusión | Concentrado para solución para perfusión | Merck Sharp & Dohme B.V. |
| 1171245004 | PREVYMIS 480 MG concentrado para solución para perfusión | Concentrado para solución para perfusión | Merck Sharp & Dohme B.V. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no hay un vínculo mecanístico plausible entre un inhibidor de la terminasa viral del CMV y la candidiasis. Con estos datos no hay base para avanzar.

**Para avanzar se necesita:**
- Pruebas de sensibilidad *in vitro* de letermovir frente a especies de *Candida*
- Datos detallados del mecanismo de acción (MOA), por ejemplo desde DrugBank
- Descarga y análisis del prospecto de AEMPS para completar advertencias y contraindicaciones
- Revisión de por qué el grafo de conocimiento asocia este fármaco con la candidiasis vulvovaginal
- Evaluación de la compatibilidad de vías de administración, ya que las presentaciones actuales son oral e intravenosa
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

