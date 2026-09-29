---
layout: default
title: Ravulizumab
parent: Solo predicción del modelo (L5)
nav_order: 459
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: De Inhibidor del Complemento C5 a Neutropenia Congénita Grave Autosómica Recesiva por Deficiencia de G6PC3

## Resumen en Una Frase

Ravulizumab es un anticuerpo monoclonal de acción prolongada que bloquea el componente C5 del complemento y está comercializado en España como Ultomiris.
El modelo TxGNN predice que podría ser efectivo para la **neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, que por ahora es solo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3 |
| Puntaje de Predicción TxGNN | 99,96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, ravulizumab es un anticuerpo monoclonal anti-C5 que bloquea la activación terminal del complemento.

La deficiencia de G6PC3 es un defecto metabólico: se acumula 1,5-anhidroglucitol-6-fosfato, lo que provoca apoptosis de los neutrófilos. No se conoce ningún papel del complemento terminal en esta vía, así que la relación mecanística **no está respaldada**. El puntaje alto de TxGNN proviene de asociaciones en el grafo de conocimiento, sin sustento clínico ni bibliográfico.

Las otras nueve predicciones del modelo (ciclos hematopoyéticos, hiperoxaluria primaria, neutropenia congénita grave, deficiencia de CXCR2, deficiencia de p14, pseudo-enfermedad de von Willebrand, neutropenia ligada al cromosoma X, trastorno de liberación plaquetaria y anemia megaloblástica) están en la misma situación. Todas son de nivel L5, sin ensayos ni literatura, y con vínculos mecanísticos débiles o hipotéticos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1191371003 | ULTOMIRIS 1100 mg/11 ml concentrado para solución para perfusión | Concentrado para solución para perfusión |
| 1191371002 | ULTOMIRIS 300 mg/3 ml concentrado para solución para perfusión | Concentrado para solución para perfusión |

Titular de ambas autorizaciones: Alexion Europe SAS. El texto de las indicaciones aprobadas no figura en los datos recibidos.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos, no hay literatura y el vínculo mecanístico entre el bloqueo de C5 y la deficiencia de G6PC3 no está establecido. Además, el fármaco puede aumentar el riesgo de infecciones, algo relevante en pacientes con neutropenia.

**Para avanzar se necesita:**
- Obtener del prospecto de la AEMPS las advertencias, contraindicaciones e indicaciones aprobadas, que hoy impiden el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar evidencia preclínica que relacione el complemento (C5/C5a) con la apoptosis de neutrófilos en la deficiencia de G6PC3.
- Reevaluar solo si aparece evidencia preclínica o clínica; sin ella, no avanzar.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

