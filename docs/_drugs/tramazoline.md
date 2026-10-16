---
layout: default
title: Tramazoline
parent: Solo predicción del modelo (L5)
nav_order: 810
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Tramazoline: nueva indicación predicha, Urticaria alérgica (nivel de evidencia L5). Indicación original: Rinitis alérgica (según el grafo de conocimiento"
monitor_inn: "Tramazoline"
predicted_indications: ["allergic urticaria", "acute laryngopharyngitis", "nasal cavity disease", "rosacea conjunctivitis", "rhinitis", "cold urticaria", "headache disorder", "trigeminal autonomic cephalalgia"]
---

# Tramazoline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Tramazolina: De Rinitis Alérgica a Urticaria Alérgica

## Resumen en Una Frase

Tramazolina es un descongestionante nasal y ocular de tipo imidazolina, utilizado originalmente en rinitis alérgica, rinitis vasomotora, faringitis, resfriado común y distintas formas de conjuntivitis.
El modelo TxGNN predice que podría ser efectiva para **urticaria alérgica**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99,95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la tramazolina es un agonista alfa-adrenérgico tópico de la clase de las imidazolinas, que produce vasoconstricción de la mucosa y se usa como descongestionante. Su eficacia sintomática en rinitis alérgica y conjuntivitis alérgica se basa en la reducción de la congestión y el enrojecimiento.

La relación con la urticaria alérgica es débil. La urticaria es una afección cutánea mediada por mastocitos e histamina, y un descongestionante nasal u ocular no tiene una vía de beneficio establecida en ella. El vínculo más plausible sería el síntoma común de «alergia», pero esto es solo una asociación del modelo.

Por ello, el puntaje elevado (99,95%) debe interpretarse con cautela: no hay evidencia clínica ni de literatura que lo confirme, y la exposición sistémica tras uso tópico es baja.

### Otras predicciones del modelo (para contexto)

| Indicación Predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Laringofaringitis aguda | 99,92% | L5 | Adyacente a las indicaciones de faringitis/nasofaringitis; sin evidencia directa |
| Enfermedad de la cavidad nasal | 99,91% | L5 | Categoría amplia, solapada con usos ya existentes |
| Conjuntivitis rosácea | 99,68% | L5 | Posible alivio sintomático de la hiperemia; riesgo de hiperemia de rebote |
| Rinitis | 99,53% | L4 | Cercana a la indicación actual; hay literatura de apoyo |
| Urticaria por frío | 99,45% | L5 | Sin vínculo mecanístico creíble |
| Trastorno de cefalea | 99,26% | L5 | Categoría demasiado amplia |
| Cefalalgia autonómica trigeminal | 99,17% | L5 | Vínculo especulativo; preocupación cardiovascular |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para urticaria alérgica.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para urticaria alérgica.

Como referencia, para la indicación predicha de menor distancia a las existentes (**rinitis**) se identificó la siguiente literatura:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26539289](https://pubmed.ncbi.nlm.nih.gov/26539289/) | 2015 | Estudio observacional multicéntrico sin control | Clinical and Translational Allergy | Efectividad y tolerabilidad de un spray nasal con tramazolina y aceites esenciales en rinitis aguda por resfriado común |
| [9745265](https://pubmed.ncbi.nlm.nih.gov/9745265/) | 1998 | Estudio clínico fisiológico | Nihon Jibiinkoka Gakkai Kaiho | Efecto descongestionante de la tramazolina sobre la permeabilidad nasal, medido por rinometría acústica en 30 sujetos alérgicos y 6 no alérgicos |
| [2874366](https://pubmed.ncbi.nlm.nih.gov/2874366/) | 1986 | Estudio controlado | Lancet | Spray tópico con dexametasona, tramazolina y neomicina en rinosinusitis mucopurulenta crónica (50 pacientes); relevancia específica de la tramazolina poco clara |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 56731 | Rhinospray Eucaliptus 1,18 mg/ml solución para pulverización nasal | Solución para pulverización nasal | No disponible en los datos compilados |
| 39574 | Rhinospray 1,18 mg/ml solución para pulverización nasal | Solución para pulverización nasal | No disponible en los datos compilados |

Ambas autorizaciones son monofármaco, están vigentes y pertenecen a Opella Healthcare Spain S.L.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**: hipertensión, enfermedad pulmonar obstructiva crónica (EPOC), enfermedad ulcerosa péptica, hiperplasia benigna de próstata, glaucoma de ángulo cerrado, hipertiroidismo (enfermedad de Graves, tirotoxicosis) y obstrucción del cuello vesical.
- **Consideraciones adicionales**: el uso crónico de vasoconstrictores puede causar hiperemia de rebote, y los simpaticomiméticos tienen efectos cardiovasculares relevantes en ciertas poblaciones.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para urticaria alérgica se basa únicamente en el modelo (L5), sin ensayos ni literatura, y carece de un vínculo mecanístico plausible para un descongestionante tópico nasal u ocular.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de la tramazolina.
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS.
- Evidencia preclínica o clínica que respalde un efecto en urticaria.
- Evaluación de la compatibilidad de vía de administración (forma nasal frente a necesidades de una afección cutánea).
- Si se busca una opción más viable, priorizar la indicación **rinitis** (L4), que es adyacente a la indicación autorizada y cuenta con literatura de apoyo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

