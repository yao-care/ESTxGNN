---
layout: default
title: Calcitriol
parent: Solo predicción del modelo (L5)
nav_order: 96
evidence_level: L5
indication_count: 7
---

# Calcitriol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Calcitriol: De Indicación Original No Registrada a Deficiencia de Vitamina D (término obsoleto)

## Resumen en Una Frase

Calcitriol es la forma activa de la vitamina D y está comercializado en España en cápsulas, solución inyectable y pomada, aunque los datos de autorización no recogen su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de vitamina D (término obsoleto)**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de autorización de la AEMPS |
| Nueva Indicación Predicha | Deficiencia de vitamina D (término obsoleto) |
| Puntaje de Predicción TxGNN | 99,96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, calcitriol es la forma activa de la vitamina D. Su relación biológica con la deficiencia de vitamina D es, por tanto, plausible. La indicación original no está registrada en los datos recibidos, así que no se puede comparar formalmente con la nueva indicación.

Hay una advertencia importante. La etiqueta de la enfermedad figura como «obsoleta», y el puntaje tan alto (0,9996) probablemente sea un artefacto de la predicción y no una señal terapéutica real. Antes de cualquier evaluación, este término debe asignarse a un concepto de enfermedad vigente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55973 | ROCALTROL 0,25 mcg CAPSULAS BLANDAS | Cápsula blanda | No disponible |
| 68934 | CALCITRIOL KERN PHARMA 1 microgramo/ml SOLUCION INYECTABLE EFG | Solución inyectable | No disponible |
| 55974 | ROCALTROL 0,50 mcg CAPSULAS BLANDAS | Cápsula blanda | No disponible |
| 64527 | SILKIS 3 microgramos/g POMADA | Pomada | No disponible |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos ni literatura para esta predicción y la etiqueta de la enfermedad está obsoleta. Solo se sostiene sobre la plausibilidad biológica, así que no puede pasar de L5.

**Otras predicciones del mismo farmaco con más respaldo:**

| Posición | Indicación predicha | Puntaje TxGNN | Nivel | Recomendación |
|------|------|------|------|------|
| 7 | Raquitismo hipofosfatémico hereditario | 99,28% | L3 | Proceed with Guardrails |
| 2 | Acidosis tubular renal | 99,93% | L4 | Research Question |
| 6 | Síndrome de Dahlberg-Borer-Newcomer | 99,76% | L4 | Hold |

- **Raquitismo hipofosfatémico hereditario:** hay dos ensayos que evalúan directamente calcitriol o vitamina D activa en hipofosfatemia ligada al X. Son NCT03748966 (fase 1 temprana, en curso) y NCT03820518 (fase 4, estado desconocido). Ninguno tiene resultados en el paquete. Probablemente ya sea tratamiento estándar, y la ausencia de indicación original en los datos es una laguna y no prueba de novedad.
- **Acidosis tubular renal:** la literatura es sobre todo casos clínicos y estudios fisiológicos, y un estudio concluye que la enfermedad no altera el calcitriol circulante. El beneficio probable se limitaría a la enfermedad ósea secundaria.
- **Síndrome de Dahlberg-Borer-Newcomer:** la evidencia es indirecta y ninguna publicación aborda el síndrome ni el tratamiento con calcitriol.

**Para avanzar se necesita:**
- Asignar «deficiencia de vitamina D (obsoleta)» a un concepto de enfermedad vigente y volver a evaluarlo.
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones) y obtener las indicaciones aprobadas de cada autorización.
- Consultar el mecanismo de acción en la API de DrugBank.
- Para raquitismo hipofosfatémico hereditario, buscar los resultados de los ensayos NCT03748966 y NCT03820518, y definir un plan de monitoreo de hipercalciuria, nefrocalcinosis e hiperparatiroidismo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

