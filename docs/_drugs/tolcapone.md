---
layout: default
title: Tolcapone
parent: Solo predicción del modelo (L5)
nav_order: 534
evidence_level: L5
indication_count: 10
---

# Tolcapone
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

# Tolcapona: De Enfermedad de Parkinson a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

La tolcapona es un inhibidor de la enzima COMT que se utiliza como terapia adyuvante en la enfermedad de Parkinson. El modelo TxGNN predice que podría ser efectiva para la **encefalitis subaguda de Rasmussen**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción. Por ahora es solo una señal del modelo, sin evidencia real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (terapia adyuvante; según la ficha farmacológica, ya que las autorizaciones de la AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Los datos farmacológicos disponibles indican que la tolcapona actúa sobre la catecol-O-metiltransferasa (COMT, gen *COMT*) humana. Al inhibirla, prolonga el efecto de la levodopa y de la señalización dopaminérgica en el Parkinson.

La encefalitis de Rasmussen es una enfermedad neurológica rara, de base inflamatoria e inmunomediada, que suele afectar a un solo hemisferio cerebral y cursa con epilepsia. No se observa un vínculo mecanístico evidente entre la inhibición de COMT y esa patología inmune. El puntaje del modelo es muy alto, pero no está respaldado por ningún dato clínico, de literatura ni mecanístico. Por eso esta predicción debe tomarse con mucha cautela y podría ser un artefacto del grafo de conocimiento.

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
| 97044003 | TASMAR 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | Viatris Healthcare Limited |
| 97044006 | TASMAR 200 mg comprimidos recubiertos con película | Comprimido recubierto con película | Viatris Healthcare Limited |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

El paquete de evidencia no contiene advertencias ni contraindicaciones. La única entrada en interacciones es la diana farmacológica (COMT), no una interacción entre fármacos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.93%), pero es de nivel L5: no hay ensayos, no hay literatura y no existe un vínculo mecanístico plausible entre la inhibición de COMT y la encefalitis de Rasmussen. Además, faltan los datos de seguridad de la AEMPS, lo que impide cualquier avance.

**Para avanzar se necesita:**
- Obtener y analizar la ficha técnica de la AEMPS (advertencias y contraindicaciones). Conviene revisar en especial el riesgo hepático, conocido para la tolcapona pero ausente en los datos aportados.
- Completar los datos de mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida de literatura y ensayos sobre tolcapona y encefalitis de Rasmussen. Si no hay resultados, descartar la hipótesis.
- Priorizar otras predicciones del mismo fármaco con más base biológica:
  - **Demencia con cuerpos de Lewy** (nivel L4): hay 2 estudios preclínicos sobre α-sinucleína, pero ninguno prueba la tolcapona.
  - **Parkinsonismo juvenil de Hunt** (nivel L5): es coherente con el mecanismo dopaminérgico conocido, pero probablemente se debe a la cercanía con la indicación ya aprobada. Antes hay que confirmar su mapeo con la enfermedad de Parkinson en la ontología.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

