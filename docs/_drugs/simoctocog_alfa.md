---
layout: default
title: Simoctocog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 737
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "SIMOCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "thrombotic thrombocytopenic purpura"]
description: "Simoctocog Alfa: nueva indicación predicha, Pseudo-enfermedad de von Willebrand (pseudo-von Willebrand disease) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Simoctocog Alfa
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

## Simoctocog Alfa: Pseudo-enfermedad de von Willebrand (pseudo-von Willebrand disease)
{: .text-alpha }

## Resumen en Una Frase

Simoctocog alfa es un factor VIII de coagulación humano recombinante (con el dominio B eliminado), utilizado originalmente para el tratamiento de la **hemofilia**.
El modelo TxGNN predice que podría ser efectivo para la **pseudo-enfermedad de von Willebrand**, aunque actualmente no hay **ningún ensayo clínico** ni **ninguna publicación** en los datos compilados que respalden esta dirección. Se trata de una predicción puramente basada en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Pseudo-enfermedad de von Willebrand (pseudo-von Willebrand disease) |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 8) |
| Número de Autorizaciones | 8 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Simoctocog alfa es un factor VIII recombinante humano, con el dominio B eliminado y producido en una línea celular humana. Actualmente no se dispone de datos detallados sobre su mecanismo de acción en los datos compilados; sin embargo, por su naturaleza, actúa reponiendo el factor VIII, componente del complejo tenasa de la cascada de coagulación, y se utiliza en la hemofilia, donde existe un déficit de este factor.

La pseudo-enfermedad de von Willebrand (de tipo plaquetario) se debe a una ganancia de función del receptor plaquetario GPIbα, que aumenta su unión al factor von Willebrand (VWF) y provoca la pérdida de multímeros de alto peso molecular de VWF. La reposición de FVIII no corrige este defecto plaquetario. El único vínculo es indirecto, a través del eje VWF–FVIII (el VWF estabiliza el FVIII circulante).

Por tanto, la puntuación alta del modelo refleja una proximidad en la red de conocimiento y no una eficacia demostrada. La plausibilidad mecanística es débil.

**Otras indicaciones predichas (todas con nivel L5 y sin evidencia clínica ni bibliográfica):**

| Posición | Indicación | Puntaje TxGNN | Comentario |
|---|---|---|---|
| 2 | Trastorno primario de liberación plaquetaria | 1,0000 | Vínculo débil e indirecto; el FVIII no corrige la secreción plaquetaria |
| 3 | Trombastenia de Glanzmann | 1,0000 | Defecto de la integrina αIIbβ3; el tratamiento estándar es transfusión de plaquetas o FVIIa recombinante |
| 4 | Síndrome de Scott | 0,9997 | Conexión teórica con el complejo tenasa, pero el FVIII no restaura la superficie fosfolipídica ausente |
| 5 | Déficit adquirido de factores de coagulación | 0,9995 | Más plausible mecanísticamente (p. ej., hemofilia A adquirida), pero los inhibidores pueden neutralizar el producto y la indicación es demasiado amplia |
| 6 | Diátesis hemorrágica por defecto del receptor de colágeno | 0,9992 | Sin vínculo mecanístico directo |
| 7 | Trastorno hemorrágico por trombocitopenia constitucional | 0,9992 | El FVIII no corrige el recuento plaquetario |
| 8 | Trombocitopenia aloinmune fetal y neonatal | 0,9984 | Sin fundamento mecanístico |
| 10 | Púrpura trombótica trombocitopénica | 0,9972 | Posible riesgo de seguridad por aporte procoagulante en una microangiopatía protrombótica |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se identificaron 8 autorizaciones vigentes (todas de medicamento único, ninguna cancelada), todas del titular Octapharma AB. Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 114936001 | NUWIQ 250 UI | Polvo y disolvente para solución inyectable | No disponible |
| 114936002 | NUWIQ 500 UI | Polvo y disolvente para solución inyectable | No disponible |
| 114936003 | NUWIQ 1000 UI | Polvo y disolvente para solución inyectable | No disponible |
| 114936004 | NUWIQ 2000 UI | Polvo y disolvente para solución inyectable | No disponible |
| 114936005 | NUWIQ 2500 UI | Polvo y disolvente para solución inyectable | No disponible |

*Se muestran las 5 primeras de 8 autorizaciones; las restantes corresponden a las presentaciones de 1500, 3000 y 4000 UI.*

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

No obstante, cabe señalar una preocupación derivada del análisis mecanístico: en la púrpura trombótica trombocitopénica (TTP), aportar FVIII no se espera que sea beneficioso y podría ser perjudicial al añadir carga procoagulante en una microangiopatía protrombótica. En el resto de las indicaciones predichas no se identificó una señal de seguridad específica en los datos compilados. Tampoco se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura que la respalden, y el mecanismo de la pseudo-enfermedad de von Willebrand (defecto plaquetario GPIbα) no es corregible mediante reposición de FVIII. Ninguna de las diez indicaciones predichas presenta evidencia que justifique avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias y contraindicaciones) y el texto de indicaciones aprobadas de las autorizaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión bibliográfica dirigida del eje VWF–FVIII en la pseudo-enfermedad de von Willebrand.
- Si se desea priorizar, evaluar con clínicos el déficit adquirido de factores de coagulación (p. ej., hemofilia A adquirida), acotando la indicación y considerando el efecto de los inhibidores.
- Aclarar si «hemofilia A con anomalía vascular» queda dentro de la indicación ya autorizada, por lo que no sería un reposicionamiento real.
- Evaluar específicamente el riesgo de seguridad en TTP antes de cualquier consideración adicional.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

