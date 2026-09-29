---
layout: default
title: Benralizumab
parent: Solo predicción del modelo (L5)
nav_order: 68
evidence_level: L5
indication_count: 5
---

# Benralizumab
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

# Benralizumab: De Asma Eosinofílica Grave a Trombocitopenia por Destrucción Inmune

## Resumen en Una Frase

Benralizumab es un anticuerpo monoclonal dirigido contra el receptor alfa de la IL-5, que en los datos disponibles aparece asociado al asma eosinofílica grave.
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia por destrucción inmune**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma eosinofílica grave (inferida del ensayo observacional NCT04126499 en España; los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Trombocitopenia por destrucción inmune |
| Puntaje de Predicción TxGNN | 99,34% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Benralizumab se une al receptor alfa de la IL-5 (IL-5Rα) y elimina eosinófilos y basófilos mediante citotoxicidad celular dependiente de anticuerpos (ADCC). No se dispone de datos detallados del mecanismo de acción en DrugBank; la descripción anterior procede del análisis mecanístico del propio Evidence Pack.

**Con los datos suministrados, la predicción no tiene respaldo mecanístico plausible.** No existe un vínculo establecido entre la depleción de eosinófilos y la destrucción inmune de plaquetas. El puntaje alto (99,34%) probablemente refleja similitudes de vecindad en el grafo de conocimiento y no un mecanismo validado. No se recuperaron ensayos ni literatura que lo apoyen.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1171252002 | FASENRA 30 mg solución inyectable en pluma precargada | Solución inyectable en pluma precargada | AstraZeneca AB |
| 1171252001 | FASENRA 30 mg solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | AstraZeneca AB |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos ni publicaciones, y no hay un mecanismo plausible que vincule la depleción de eosinófilos con la trombocitopenia inmune. Como contexto, la segunda predicción del modelo (dermatitis) sí cuenta con un ensayo de Fase 2 controlado (HILLIER), que resultó negativo, lo que refuerza la cautela con este tipo de predicciones.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre el papel de los eosinófilos o la IL-5 en la trombocitopenia inmune (PTI)
- Datos del mecanismo de acción desde DrugBank
- Prospecto de AEMPS (advertencias y contraindicaciones), imprescindible antes de cualquier cribado de seguridad
- Estudios preclínicos que justifiquen un vínculo biológico antes de plantear un ensayo clínico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

