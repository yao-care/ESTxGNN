---
layout: default
title: Caplacizumab
parent: Solo predicción del modelo (L5)
nav_order: 139
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Caplacizumab: nueva indicación predicha, Trastorno primario de liberación plaquetaria (nivel de evidencia L5). Indicación original: Púrpura trombocitopénica"
monitor_inn: "CAPLACIZUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "hemophilia", "platelet-type bleeding disorder"]
---

# Caplacizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Caplacizumab: De Púrpura Trombocitopénica a Trastorno Primario de Liberación Plaquetaria
{: .text-alpha }

## Resumen en Una Frase

Caplacizumab es un nanocuerpo anti-factor von Willebrand (vWF), originalmente utilizado para el tratamiento de la púrpura trombocitopénica (púrpura trombocitopénica trombótica adquirida).
El modelo TxGNN predice que podría ser efectivo para el **trastorno primario de liberación plaquetaria**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, y el análisis mecanístico sugiere que la predicción probablemente sea un artefacto del modelo TxGNN (aprendizaje profundo).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Púrpura trombocitopénica |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, caplacizumab es un nanocuerpo humanizado dirigido al dominio A1 del vWF, que bloquea la interacción entre el vWF y el receptor plaquetario GPIb-IX-V, evitando la adhesión plaquetaria y la microtrombosis.

En la púrpura trombocitopénica trombótica (PTT), la deficiencia grave de ADAMTS13 deja multímeros ultragrandes de vWF que se unen a las plaquetas. Caplacizumab interrumpe este proceso, por lo que su eficacia en la indicación original está bien establecida.

Sin embargo, en los trastornos de liberación plaquetaria el defecto es intrínseco a la secreción plaquetaria y no depende de la unión vWF-A1. Bloquear la adhesión plaquetaria previsiblemente empeoraría, no mejoraría, la tendencia hemorrágica. El puntaje elevado proviene del modelo TxGNN (deep learning) y probablemente refleja similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para el trastorno primario de liberación plaquetaria.

*Nota:* para la púrpura trombocitopénica trombótica (indicación original, ya aprobada) sí existen ensayos clínicos que validan el uso autorizado, como HERCULES (NCT02553317, Fase 3, 145 pacientes) y TITAN (NCT01151423, Fase 2, 75 pacientes). No constituyen evidencia para la nueva indicación predicha.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el trastorno primario de liberación plaquetaria.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181305001 | CABLIVI 10 MG POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Polvo y disolvente para solución inyectable | No disponible en el registro |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones registradas; entre las principales de nivel **Mayor** figuran:
  - Ácido acetilsalicílico
  - Fondaparinux
  - Alteplasa
  - Abciximab
  - Anagrelida
  - Acalabrutinib
  - Deferasirox
  - Trastuzumab emtansina
  - Ibritumomab tiuxetán
  - Tositumomab (con y sin I-131)

  También hay interacciones de nivel **Moderado**, como ibuprofeno, celecoxib, ketorolaco (incluida la vía oftálmica), diclofenaco tópico, fluvoxamina, fenfluramina, dexfenfluramina y sibutramina. En general se trata de fármacos antitrombóticos, antiagregantes o que afectan la hemostasia, lo que sugiere un riesgo aditivo de sangrado.
- **Riesgo mecanístico**: al inhibir la adhesión plaquetaria dependiente de vWF, en trastornos hemorrágicos plaquetarios se esperaría un aumento del riesgo de sangrado.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura específica, y el mecanismo de acción de caplacizumab es contrario al necesario en un trastorno de la función plaquetaria, con riesgo de agravar la hemorragia.

**Para avanzar se necesita:**
- Datos de mecanismo de acción confirmados (p. ej., desde DrugBank)
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS
- Evidencia preclínica que justifique un beneficio en trastornos de liberación plaquetaria
- Evaluación formal del riesgo hemorrágico antes de considerar cualquier estudio clínico

*Observación adicional:* otras indicaciones predichas (pseudo-enfermedad de von Willebrand, trombastenia de Glanzmann, síndrome de Scott, hemofilia, entre otras) también carecen de evidencia y presentan preocupaciones de seguridad similares. La única con respaldo sólido es la púrpura trombocitopénica trombótica, que corresponde al uso ya autorizado y no a un reposicionamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

