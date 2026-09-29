---
layout: default
title: Fenfluramine
parent: Solo predicción del modelo (L5)
nav_order: 229
evidence_level: L5
indication_count: 4
---

# Fenfluramine
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

# Fenfluramina: De Supresor del Apetito (Control de Peso) a Síndrome de Microdeleción 16p11.2 Proximal

## Resumen en Una Frase

La fenfluramina se usó originalmente como ayuda para adelgazar y fue retirada del mercado para ese fin. Hoy se emplea como anticonvulsivo en epilepsias de inicio pediátrico, como el síndrome de Dravet.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de microdeleción 16p11.2 proximal**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS (el texto de indicación está vacío). Según la farmacología: supresor del apetito, hoy anticonvulsivo (síndrome de Dravet) |
| Nueva Indicación Predicha | Síndrome de microdeleción 16p11.2 proximal |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, la fenfluramina es un agente liberador de serotonina con actividad sobre receptores 5-HT2 y sigma-1. Su eficacia anticonvulsiva está reconocida: la FDA la aprobó en 2020 para el síndrome de Dravet y en 2025 NICE la recomendó para el síndrome de Lennox-Gastaut. En el análisis farmacológico aparecen como posibles dianas las triptófano hidroxilasas 1 y 2 (TPH1 y TPH2), aunque no hay datos públicos de bioactividad que confirmen una diana primaria.

El vínculo con la nueva indicación es solo especulativo. La deleción 16p11.2 se asocia con epilepsia, obesidad y rasgos del neurodesarrollo, y la fenfluramina actúa sobre la serotonina y se ha usado tanto en control de peso como en epilepsia. Sin embargo, ninguna evidencia aportada respalda esta conexión.

Un puntaje alto en el grafo de conocimiento no demuestra relevancia clínica. Debe tratarse como una hipótesis a verificar, no como una indicación con respaldo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1201491001 | FINTEPLA 2,2 mg/ml SOLUCIÓN ORAL (Ucb Pharma) | Solución oral |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó con 2 registros. Son asociaciones farmacológicas con dianas enzimáticas, no interacciones con otros medicamentos, y no tienen nivel de gravedad asignado:
  - Triptófano hidroxilasa 1 (TPH1)
  - Triptófano hidroxilasa 2 (TPH2)

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (nivel L5), sin ensayos ni literatura. El vínculo mecanístico es especulativo y no hay datos de seguridad locales que permitan avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un requisito para cualquier cribado de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Una revisión de literatura sobre fenfluramina y el síndrome 16p11.2 (epilepsia, obesidad, neurodesarrollo).
- Evaluar la compatibilidad de vía de administración y la similitud con la indicación original, hoy pendientes.
- Tener en cuenta que las otras tres predicciones del modelo (hipervitaminosis, hipertelorismo obsoleto y frontorrinia) carecen de vínculo farmacológico plausible y probablemente son artefactos del grafo. También quedan en Hold.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

