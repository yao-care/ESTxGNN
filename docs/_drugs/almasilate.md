---
layout: default
title: Almasilate
parent: Solo predicción del modelo (L5)
nav_order: 31
evidence_level: L5
indication_count: 5
---

# Almasilate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Almasilato: De Indicación Original No Registrada (Antiácido) a Enfermedad Ulcerosa Péptica Activa

## Resumen en Una Frase

Almasilato es un antiácido de silicato de aluminio y magnesio, comercializado en España como Dolcopin. El registro no incluye el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **enfermedad ulcerosa péptica activa**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta indicación concreta, por lo que es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el registro (el texto de indicación aprobada está vacío) |
| Nueva Indicación Predicha | Enfermedad ulcerosa péptica activa |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, almasilato es un antiácido tamponante de silicato de aluminio y magnesio. Mecanísticamente podría ser aplicable a la enfermedad ulcerosa péptica activa, porque neutralizar el ácido gástrico es una vía plausible para aliviar los síntomas de las úlceras relacionadas con el ácido.

Esta relación es una inferencia mecanística y no está respaldada por ensayos clínicos ni literatura para esta indicación. El puntaje TxGNN es muy alto (99.91%), pero solo refleja una predicción del modelo. Los antiácidos suelen actuar como control sintomático y no como tratamiento curativo de la úlcera.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

Para otras indicaciones predichas sí se recuperaron algunos artículos, pero ninguno demuestra eficacia:
- **Úlcera gastroyeyunal:** una revisión de antiácidos complejos (PMID [3888581](https://pubmed.ncbi.nlm.nih.gov/3888581/), 1985) y un estudio comparativo de cuatro antiácidos centrado en la aceptación por los pacientes (PMID [6091079](https://pubmed.ncbi.nlm.nih.gov/6091079/), 1984). Ambos son solo indirectamente relevantes.
- **Úlcera gástrica:** un caso clínico de cálculo renal de silicato tras uso prolongado de un antiácido de silicato (PMID [9188143](https://pubmed.ncbi.nlm.nih.gov/9188143/), 1997). No es evidencia de eficacia y se comenta en la sección de seguridad.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52255 | DOLCOPIN 1 g POLVO PARA SUSPENSION ORAL (Meda Pharma S.L.) | Polvo para suspensión oral | No disponible en el registro |

## Consideraciones de Seguridad

Consultar el prospecto para obtener la información de seguridad de advertencias, contraindicaciones e interacciones.

- **Señal de seguridad a largo plazo:** un caso clínico (PMID 9188143) describe un cálculo de silicato en un paciente con litiasis recurrente de oxalato de calcio. Este paciente había tomado un antiácido de silicato de magnesio y aluminio durante unos 17 años. Es un solo caso, pero sugiere vigilar el uso prolongado.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura para la enfermedad ulcerosa péptica activa. Faltan además los datos del mecanismo de acción y de seguridad del prospecto de la AEMPS, y este último es un vacío bloqueante para el cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica y el prospecto de la AEMPS (advertencias y contraindicaciones).
- Obtener el mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada de Dolcopin en España y su relación con la úlcera péptica.
- Buscar estudios clínicos de antiácidos de silicato de aluminio y magnesio en úlcera péptica.
- Evaluar la compatibilidad de la vía de administración (oral) con la nueva indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

