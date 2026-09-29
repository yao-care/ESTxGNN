---
layout: default
title: Isoprenaline
parent: Solo predicción del modelo (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
---

# Isoprenaline
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

# Isoprenalina: De Bloqueo Cardíaco, Asma y Bronquitis Crónica a Enfermedad de la Cavidad Nasal

## Resumen en Una Frase

La isoprenalina (isoproterenol) es un agonista beta-adrenérgico no selectivo, utilizado clásicamente en el bloqueo cardíaco, el asma y la bronquitis crónica.
El modelo TxGNN predice que podría ser efectiva para la **enfermedad de la cavidad nasal**, pero **no hay ensayos clínicos** y la única publicación recuperada es un reporte de caso sin relación con la indicación, por lo que la predicción carece de respaldo real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Las autorizaciones de la AEMPS no incluyen texto de indicación. Según datos farmacológicos: bloqueo cardíaco, asma y bronquitis crónica |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 99,95 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La isoprenalina actúa sobre los receptores beta-adrenérgicos β1 (ADRB1), β2 (ADRB2) y β3 (ADRB3). Es un agonista no selectivo: la activación de β1 aumenta la frecuencia y la contractilidad cardíacas, y la de β2 relaja el músculo liso bronquial. De ahí proviene su uso en el bloqueo cardíaco y en las enfermedades obstructivas de las vías respiratorias.

Mecanísticamente, la estimulación beta-adrenérgica podría, en teoría, afectar la vasculatura de la mucosa nasal. Sin embargo, el análisis de evidencia concluye que **no existe un vínculo claro**. El único artículo recuperado es un reporte de caso sobre espasmo coronario y taquicardia ventricular perioperatoria. En ese caso se usó epinefrina en la cavidad nasal para la intubación, y no tiene relación con la isoprenalina ni con enfermedades nasales.

El puntaje alto de TxGNN (99,95 %) refleja la proximidad en el grafo de conocimiento entre los receptores adrenérgicos y las enfermedades de las vías respiratorias. No está respaldado por datos clínicos. Por ello, esta predicción debe tratarse como una hipótesis sin validar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14711196](https://pubmed.ncbi.nlm.nih.gov/14711196/) | 2003 | Reporte de caso | Japanese Heart Journal | Varón japonés de 26 años con taquicardia ventricular perioperatoria tras la aplicación nasal de epinefrina 1:100.000 durante la intubación; se halló espasmo coronario. No es relevante para la indicación predicha. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 89777 | LABRYCOR 0,2 MG/ML CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN EFG | Concentrado para solución para perfusión | Macure Healthcare Limited |
| 47131 | ALEUDRINA 0,2 mg/ml SOLUCIÓN INYECTABLE | Solución inyectable | Laboratorio Reig Jofre, S.A. |

Ambas presentaciones son de administración parenteral (perfusión o inyección). Los datos recibidos no incluyen el texto de la indicación aprobada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos clínicos, y la única publicación es un reporte de caso no relevante. Además, las presentaciones autorizadas en España son parenterales, lo que dificulta su aplicación en una enfermedad nasal.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que evalúen la isoprenalina o los agonistas beta-adrenérgicos en enfermedades de la cavidad nasal.
- Obtener el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones) y completar los datos de seguridad.
- Evaluar la compatibilidad de vías de administración, ya que solo hay formas parenterales autorizadas.
- Considerar otras predicciones del mismo fármaco con más respaldo. La más sólida es **enfermedad bronquial** (L3), con estudios históricos de 1966 a 1979 en asma y obstrucción de las vías aéreas. Su valor de reposicionamiento es bajo: es un uso ya conocido, desplazado por los agonistas β2 selectivos por sus efectos cardíacos. El único ensayo listado para esa indicación evalúa alendronato, no isoprenalina.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

