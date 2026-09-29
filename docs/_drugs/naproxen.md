---
layout: default
title: Naproxen
parent: Solo predicción del modelo (L5)
nav_order: 369
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Naproxeno: De Dolor e Inflamación (AINE) a Síndrome de Braquidactilia-Sindactilia

## Resumen en Una Frase

Naproxeno es un antiinflamatorio no esteroideo (AINE) utilizado en artritis reumatoide, artrosis, espondilitis anquilosante, tendinitis, bursitis, gota aguda y dismenorrea primaria.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de braquidactilia-sindactilia**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en las autorizaciones de AEMPS (texto vacío). Según farmacología: artritis reumatoide, artrosis, espondilitis anquilosante, tendinitis, bursitis, gota aguda y dismenorrea primaria |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia |
| Puntaje de Predicción TxGNN | 99.35% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Naproxeno es un inhibidor no selectivo de COX-1 (PTGS1) y COX-2 (PTGS2), según los datos de farmacología disponibles. Al bloquear la síntesis de prostaglandinas, reduce el dolor y la inflamación. No se dispone de un texto detallado del mecanismo de acción en DrugBank para este registro.

**Con la información actual, la predicción no tiene un vínculo mecanístico plausible.** Los síndromes de braquidactilia-sindactilia son malformaciones congénitas de las extremidades. Suelen deberse a defectos genéticos o de señalización del desarrollo, y la inhibición de prostaglandinas no corrige esas vías. El puntaje alto (0.994) proviene solo del grafo de conocimiento y no está respaldado por estudios reales.

Otras predicciones del modelo para este fármaco presentan el mismo problema. Son enfermedades congénitas estructurales sin relación mecanística con la inhibición de COX:
- Síndrome de microftalmía colobomatosa-displasia rizomélica (99.22%)
- Displasia acromesomélica tipo Hunter-Thompson (99.17%)
- Síndrome de braquiolmia-amelogénesis imperfecta (99.06%)

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 68435 | NAPROXENO NORMON 500 mg COMPRIMIDOS EFG | Comprimido | No especificada en los datos |
| 85570 | NAPROXENO AUROVITAS 500 MG COMPRIMIDOS EFG | Comprimido | No especificada en los datos |
| 80806 | NAPROXENO AUROBINDO 500 MG COMPRIMIDOS EFG | Comprimido | No especificada en los datos |
| 77727 | LIDET 500 MG COMPRIMIDOS GASTRORRESISTENTES EFG | Comprimido gastrorresistente | No especificada en los datos |
| 56267 | NAPROSYN 500 mg COMPRIMIDOS | Comprimido | No especificada en los datos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (L5), sin ensayos clínicos ni literatura. Además, no existe un vínculo mecanístico plausible entre la inhibición de COX y una malformación congénita del desarrollo.

**Para avanzar se necesita:**
- Una hipótesis mecanística que conecte la inhibición de prostaglandinas con la fisiopatología de la enfermedad
- Estudios preclínicos o de mecanismo que respalden la predicción
- Advertencias y contraindicaciones del prospecto de AEMPS
- Texto de indicaciones aprobadas de las autorizaciones españolas
- Datos detallados del mecanismo de acción (MOA) desde DrugBank
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

