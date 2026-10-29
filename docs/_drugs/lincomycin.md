---
layout: default
title: Lincomycin
parent: Solo predicción del modelo (L5)
nav_order: 472
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-29
monitor_inn: "lincomycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
description: "Lincomycin: nueva indicación predicha, Hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Lincomycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Lincomycin: Hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Lincomicina es un antibiótico lincosamida, originalmente utilizado para tratar infecciones neumocócicas, estafilocócicas y estreptocócicas.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0.9914 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 3 de 3) |
| Número de Autorizaciones | 3 (vigentes: 0) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la lincomicina es una lincosamida que inhibe la síntesis de proteínas bacterianas al unirse a la subunidad ribosomal 50S, y su eficacia en infecciones por cocos grampositivos está bien establecida.

**En este caso la predicción no resulta razonable desde el punto de vista mecanístico.** No se identifica ningún vínculo plausible entre la inhibición ribosomal bacteriana y la regulación de la amilasa. La hiperamilasemia es un hallazgo de laboratorio, no una enfermedad con una diana terapéutica clara, por lo que el puntaje proviene del modelo TxGNN (aprendizaje profundo) y podría reflejar similitudes que el modelo aprendió entre enfermedades relacionadas (por ejemplo, con pancreatitis inducida por fármacos o elevación de amilasa), no evidencia biológica ni un potencial terapéutico real.

Las otras dos predicciones de mayor puntaje tampoco tienen sustento: el **síndrome de hiperviscosidad policlonal** (0,9914, idéntico puntaje, lo que sugiere una similitud compartida aprendida por el modelo TxGNN, no evidencia biológica) y la **analbuminemia congénita** (0,9906, un trastorno genético por mutaciones del gen ALB que un antibiótico no puede corregir). Ninguna cuenta con ensayos ni literatura.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 41468 | LINCOCIN 600 mg INYECTABLE (Pfizer S.L.) | Solución inyectable | No disponible |
| 46655 | LINCOMICINA NORMON 600 mg SOLUCIÓN INYECTABLE (Laboratorios Normon S.A.) | Solución inyectable | No disponible |
| 41290 | LINCOCIN 500 MG CÁPSULAS DURAS (Pfizer S.L.) | Cápsula dura | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del texto del prospecto): insuficiencia hepática, colitis por *Clostridium difficile*, enterocolitis necrotizante perinatal, colitis, enfermedad del sistema digestivo y enfermedad intestinal.
- **Interacciones Farmacológicas**: se identificaron 21 interacciones potenciales. Las de nivel **moderado** son balsalazida, ácido picosulfúrico, attapulgita, caolín, eritromicina y etinilestradiol. Otras (clotrimazol, cimetidina, morfina, metformina, omeprazol, lactulosa, triamcinolona, simvastatina, ranitidina, warfarina, lidocaína, cetirizina, montelukast, salmeterol) figuran con nivel de gravedad desconocido.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible; además, el perfil de contraindicaciones gastrointestinales y hepáticas añade cautela.

**Para avanzar se necesita:**
- Revisión de la literatura para comprobar si existe alguna señal real entre lincomicina y las alteraciones de amilasa (incluida la posibilidad de que sea un efecto adverso y no un beneficio).
- Datos del mecanismo de acción desde DrugBank.
- Advertencias y contraindicaciones del prospecto de la AEMPS, necesarias para cualquier cribado de seguridad.
- Evidencia preclínica que justifique un mecanismo antes de reconsiderar la indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

