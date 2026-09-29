---
layout: default
title: Fostamatinib
parent: Solo predicción del modelo (L5)
nav_order: 248
evidence_level: L5
indication_count: 2
---

# Fostamatinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Fostamatinib: De Trombocitopenia Inmune Crónica a Trombocitopenia Autosómica con Plaquetas Normales

## Resumen en Una Frase

Fostamatinib es un inhibidor de SYK que se comercializa en España como Tavlesse. Según el conocimiento farmacológico general, se usa en la trombocitopenia inmune crónica.
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia autosómica con plaquetas normales**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los textos de autorización locales (según conocimiento farmacológico general: trombocitopenia inmune crónica) |
| Nueva Indicación Predicha | Trombocitopenia autosómica con plaquetas normales |
| Puntaje de Predicción TxGNN | 99.45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según el conocimiento farmacológico general, fostamatinib es un profármaco de R406, un inhibidor de la tirosina quinasa SYK. Reduce la destrucción de plaquetas mediada por receptores Fc en los macrófagos, y por eso se usa en la trombocitopenia inmune crónica.

La relación con la nueva indicación es débil. Las trombocitopenias hereditarias suelen deberse a defectos en la producción de plaquetas o en la función de los megacariocitos, no a un aclaramiento inmunitario. Solo sería plausible si en esta enfermedad participara la destrucción inmunitaria de plaquetas, y eso no está verificado.

El puntaje de 99.45% es únicamente una predicción computacional. Ningún dato clínico del paquete lo respalda.

Nota: el modelo también predijo, en segundo lugar, **malformación esofágica no sindrómica** (puntaje 99.05%). No se identifica un vínculo mecanístico plausible. La inhibición de SYK no tiene relevancia establecida en la embriogénesis del esófago, y la predicción podría deberse a artefactos de la topología del grafo de conocimiento. Tampoco tiene ensayos ni literatura de apoyo (nivel L5, Hold).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191405002 | TAVLESSE 150 MG comprimidos recubiertos con película | Comprimido recubierto con película | No consta en el registro |
| 1191405001 | TAVLESSE 100 MG comprimidos recubiertos con película | Comprimido recubierto con película | No consta en el registro |

Ambas autorizaciones pertenecen a Instituto Grifols S.A.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5), sin ensayos clínicos ni literatura. El vínculo mecanístico con una trombocitopenia hereditaria es débil, porque el mecanismo inmunitario de fostamatinib no encaja con un defecto de producción plaquetaria. Además, no se dispone de datos de seguridad locales.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de la AEMPS (advertencias y contraindicaciones), que es un vacío bloqueante para el cribado de seguridad
- Obtener datos del mecanismo de acción desde DrugBank
- Confirmar la indicación aprobada en España, ya que los textos de autorización están vacíos
- Buscar evidencia preclínica o clínica que vincule la vía SYK con la fisiopatología de esta trombocitopenia
- Revisar si la predicción de malformación esofágica es un artefacto del grafo antes de dedicarle más recursos

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

