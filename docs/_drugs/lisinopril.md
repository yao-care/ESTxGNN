---
layout: default
title: Lisinopril
parent: Solo predicción del modelo (L5)
nav_order: 324
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: De Inhibidor de la ECA a Infarto de Miocardio Posterolateral

## Resumen en Una Frase

Lisinopril es un inhibidor de la enzima convertidora de angiotensina (ECA), comercializado en España en comprimidos. El modelo TxGNN predice que podría ser efectivo para el **infarto de miocardio posterolateral**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta indicación concreta. La predicción se apoya solo en el puntaje del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Infarto de miocardio posterolateral |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, lisinopril pertenece a la clase de los inhibidores de la ECA. Mecanísticamente podría ser aplicable al infarto de miocardio, porque el bloqueo del sistema renina-angiotensina-aldosterona (SRAA) puede reducir la remodelación cardíaca adversa posterior al infarto.

Hay una limitación importante. El infarto posterolateral es un subtipo anatómico del infarto de miocardio, no un objetivo de reposicionamiento distinto. Además, el puntaje es idéntico al del infarto posteroinferior (rank 2). Esto sugiere que proviene de una señal compartida de la ontología de enfermedades y no de evidencia independiente para este subtipo.

En resumen, la plausibilidad farmacológica es razonable, pero no hay estudios en el paquete que la confirmen para esta indicación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones registradas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 64562 | LISINOPRIL CINFA 20 mg COMPRIMIDOS EFG | Comprimido |
| 65530 | LISINOPRIL VIATRIS 5 MG COMPRIMIDOS EFG | Comprimido |
| 88814 | LISINOPRIL GRINDEKS 20 MG COMPRIMIDOS EFG | Comprimido |
| 59129 | PRINIVIL 20 mg COMPRIMIDOS | Comprimido |
| 63961 | LISINOPRIL TEVA-RATIOPHARM 5 mg COMPRIMIDOS EFG | Comprimido |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura para esta indicación (nivel L5). Además, es un subtipo anatómico de infarto y no un objetivo de reposicionamiento independiente. El puntaje alto del modelo no basta por sí solo para avanzar.

**Para avanzar se necesita:**
- Obtener del prospecto de la AEMPS las advertencias, contraindicaciones y las indicaciones aprobadas, que hoy están vacías en el paquete.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Reformular la pregunta a nivel de infarto de miocardio en general y no de un subtipo, y buscar ensayos y literatura específicos de lisinopril.
- Revisar las otras predicciones del paquete. La más avanzada es la **enfermedad cardíaca pulmonar crónica** (nivel L3, etapa S1), con dos publicaciones clínicas específicas de lisinopril (PMID 14524095 y 17047621). Su diseño y tamaño aún no están confirmados. El **infarto de miocardio septal** (L4) tiene una publicación indirecta.

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

