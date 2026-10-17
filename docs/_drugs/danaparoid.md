---
layout: default
title: Danaparoid
parent: Solo predicción del modelo (L5)
nav_order: 218
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Danaparoid: nueva indicación predicha, Trombastenia de Glanzmann (nivel de evidencia L5). Indicación original: No disponible en la autorización (el texto de indicación está vacío)"
monitor_inn: "danaparoid"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "Scott syndrome"]
---

# Danaparoid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Danaparoid: De Anticoagulación (indicación original no especificada en la licencia) a Trombastenia de Glanzmann

## Resumen en Una Frase

Danaparoid es un heparinoide anticoagulante comercializado en España. El texto de indicación de su autorización no está disponible en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **Trombastenia de Glanzmann**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Además, el mecanismo del fármaco apunta a lo contrario (empeoramiento del sangrado).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la autorización (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Trombastenia de Glanzmann |
| Puntaje de Predicción TxGNN | 99,88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información conocida, danaparoid es una mezcla de heparinoides (heparán sulfato, dermatán sulfato y condroitín sulfato) que actúa principalmente mediante la inhibición del factor Xa mediada por antitrombina. En la práctica clínica se emplea como anticoagulante alternativo, por ejemplo en la trombocitopenia inducida por heparina.

La trombastenia de Glanzmann es un trastorno hemorrágico causado por la deficiencia o disfunción de la integrina plaquetaria αIIbβ3. Un anticoagulante cabría esperar que **empeore, y no mejore**, el fenotipo hemorrágico. Por lo tanto, **no se identifica un vínculo mecanístico plausible**.

El alto puntaje de TxGNN (0,9988) probablemente refleja asociaciones en el grafo de conocimiento con las vías de coagulación y plaquetas, y no un mecanismo terapéutico real. Las demás predicciones de mayor rango comparten el mismo problema: son trastornos hemorrágicos plaquetarios (trastorno primario de liberación plaquetaria, pseudo-enfermedad de von Willebrand, defecto del receptor de colágeno, trombocitopenia constitucional y síndrome de Scott), en los que un anticoagulante sería contraproducente.

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
| 86436 | TRALEUSIN 750 U ANTI-XA/0,6 ML SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN (Viatris Limited) | Solución inyectable y para perfusión | No especificada en los datos disponibles |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 139 interacciones registradas. Entre las de nivel **Mayor** figuran:
  - Ácido acetilsalicílico
  - Ketorolaco
  - Ibuprofeno
  - Alteplasa
  - Abciximab
  - Acalabrutinib
  - Deferasirox
  - Trastuzumab emtansina
  - Ibritumomab tiuxetán
  - Tositumomab (I-131)

  También hay interacciones de nivel Moderado, por ejemplo con fenfluramina, sibutramina, aliskireno, amilorida, celecoxib, sugammadex y los yoduros I-123/I-131. En general, se trata de fármacos que aumentan el riesgo hemorrágico o afectan a la hemostasia.
- **Riesgo específico de la nueva indicación**: por su efecto anticoagulante, danaparoid podría aumentar el riesgo de hemorragia en pacientes con trastornos hemorrágicos plaquetarios.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el mecanismo anticoagulante del fármaco es contrario al que requeriría un trastorno hemorrágico, por lo que existe un riesgo de daño.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de la literatura que justifique un posible mecanismo; de no encontrarse, considerar descartar esta predicción.
- Evaluar si alguna de las otras indicaciones predichas tiene un fundamento mecanístico distinto, antes de invertir más recursos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

