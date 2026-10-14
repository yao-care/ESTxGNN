---
layout: default
title: Alimemazine
parent: Evidencia moderada (L3-L4)
nav_order: 35
evidence_level: L4
indication_count: 6
---

# Alimemazine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **6** 
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

# Alimemazina: De Urticaria y Rinitis Alérgica a Urticaria Alérgica

## Resumen en Una Frase

Alimemazina (trimeprazina) es un antihistamínico H1 de primera generación del grupo de las fenotiazinas, utilizado originalmente para urticaria, rinitis alérgica, dermatografismo familiar y otras afecciones alérgicas.
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; el apoyo es solo indirecto (efecto de clase e indicaciones ya existentes).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Urticaria, rinitis alérgica, angioedema y otras afecciones alérgicas (según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, alimemazina es una fenotiazina con actividad antihistamínica H1 y efectos antimuscarínicos (datos farmacológicos en tejido cerebral bovino indican una Ki de 38 nM para la unión muscarínica). Mecanísticamente podría ser aplicable a la urticaria alérgica, una condición mediada por la liberación de histamina de los mastocitos.

La urticaria alérgica queda esencialmente dentro del espacio de las indicaciones originales del fármaco (urticaria, dermatografismo familiar, rinitis alérgica). El puntaje tan alto de TxGNN es coherente con esta cercanía farmacológica, pero por ello no constituye un hallazgo nuevo de reposicionamiento, sino más bien una confirmación del uso ya establecido.

Cabe señalar que los datos de afinidad por el receptor H1 humano no están disponibles públicamente, por lo que el mecanismo se infiere por la clase del fármaco.

### Otras indicaciones predichas (todas sin ensayos ni literatura)

| Rank | Indicación Predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|------|
| 2 | Urticaria por frío | 99.96% | L4 | Plausible por bloqueo H1, pero las guías prefieren antihistamínicos de segunda generación; los sedantes tienen efectos anticolinérgicos y sedantes |
| 3 | Respuesta IgE atópica | 99.60% | L5 | Es un fenotipo y no una enfermedad tratable; solo predicción del modelo |
| 4 | Enfermedad de la cavidad nasal | 99.60% | L4 | Categoría muy inespecífica que incluye rinitis ya indicadas |
| 5 | Dermatitis atópica recalcitrante | 99.59% | L4 | Posible uso adyuvante para prurito y sueño; no modifica la inflamación Th2 |
| 6 | Laringofaringitis aguda | 99.54% | L4 | Solapa con faringitis y resfriado común; beneficio probado limitado |

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
| 40002 | VARIARGIL 40 MG/ML gotas orales en solución | Gotas orales en solución | No disponible en los datos compilados |

Titular: Laboratorios Farmacéuticos Logogen S.A. (autorización vigente, monofármaco, vía oral).

---

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados. Consultar el prospecto para esa información.

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): 
  - Cardiovasculares: síndrome de QT largo (familiar o no), torsades de pointes, parada cardíaca súbita, enfermedad de conducción cardíaca, infarto de miocardio, trombosis coronaria, hipotensión ortostática, síndrome de taquicardia postural ortostática, atrofia multisistémica.
  - Hematológicas: neutropenia, agranulocitosis, leucopenia, trombocitopenia, anemia (incluida la macrocítica), hemoglobinopatía.
  - Neurológicas: epilepsia, enfermedad de los ganglios basales, distonía focal de la mano, blefaroespasmo.
  - Otras: enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, hiperplasia prostática benigna, obesidad (incluida la monogénica), carcinoma de mama femenino, abuso o dependencia de sustancias.
- **Interacciones farmacológicas**: la consulta se completó sin interacciones clínicas con otros fármacos; solo se registró la farmacología del receptor H1 (sin nivel de gravedad).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de alta puntuación pero no aporta una indicación realmente nueva: la urticaria alérgica ya se solapa con las indicaciones existentes. No hay ensayos ni literatura (nivel L4), y falta información de seguridad del prospecto, lo que bloquea el cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS para obtener advertencias, contraindicaciones y el texto de la indicación autorizada.
- Obtener datos del mecanismo de acción (por ejemplo, mediante DrugBank).
- Revisar la literatura y los registros de ensayos específicos de alimemazina en urticaria.
- Evaluar el perfil de seguridad (sedación, efectos anticolinérgicos, prolongación del QT, discrasias sanguíneas) frente a los antihistamínicos de segunda generación, preferidos por las guías.
- Confirmar la compatibilidad de vías de administración y la similitud con la indicación original (pendientes).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

