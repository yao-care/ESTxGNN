---
layout: default
title: Adenosine
parent: Solo predicción del modelo (L5)
nav_order: 25
evidence_level: L5
indication_count: 1
monitor_inn: "Adenosine"
predicted_indications: ["obsolete bundle branch block"]
last_modified_at: 2026-10-27
description: "Adenosine: nueva indicación predicha, Bloqueo de rama (obsolete bundle branch block) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Adenosine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Adenosina: agonista de receptores de adenosina → bloqueo de rama (obsolete bundle branch block)
{: .text-alpha }

## Resumen en Una Frase

La adenosina es un agonista de los receptores de adenosina (A1, A2A, A2B y A3) que se utiliza en medicina cardiovascular para tratar taquicardias.
El modelo TxGNN predice que podría ser efectiva para **bloqueo de rama (obsolete bundle branch block)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Bloqueo de rama (obsolete bundle branch block) |
| Puntaje de Predicción TxGNN | 0,9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 7) |
| Número de Autorizaciones | 7 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Lo que sí consta es que la adenosina actúa sobre los receptores A1, A2A, A2B y A3, además de TRPM4 y las fosfatidilinositol 4-quinasas tipo 2 alfa y beta. Su efecto principal en el corazón, mediado por el receptor A1, es frenar la conducción del nodo auriculoventricular.

Ese efecto es una acción farmacológica sobre la conducción, no un fundamento terapéutico para el bloqueo de rama. Al contrario, la adenosina puede provocar o desenmascarar bloqueos de la conducción, por lo que un beneficio terapéutico no resulta plausible sin evidencia adicional.

Además, el término de la enfermedad predicha figura como obsoleto en la ontología, lo que sugiere una entrada desactualizada que puede corresponder mal con una entidad clínica actual. El puntaje alto del modelo (0,9994) es solo una predicción computacional y no sustituye a la evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

La adenosina está comercializada en España, con 5 autorizaciones vigentes y 2 canceladas. A continuación se muestran las autorizaciones principales (productos de un solo principio activo):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 36189 | Atepodin 100 mg polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable |
| 81545 | Adenosina Accord 6 mg/2 ml solución inyectable EFG | Solución inyectable |
| 86371 | Adenosina Hikma 6 mg/2 ml solución inyectable EFG | Solución inyectable |
| 81546 | Adenosina Accord 30 mg/10 ml solución para perfusión EFG | Solución para perfusión |
| 61732 | Adenoscan 30 mg/10 ml solución para perfusión | Solución para perfusión |

## Consideraciones de Seguridad

- **Interacciones farmacológicas y dianas**: la adenosina interactúa con los receptores A1, A2A, A2B y A3, con TRPM4 y con PI4K2A y PI4K2B (7 dianas farmacológicas registradas).

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos ni publicaciones. Además, la enfermedad predicha figura como obsoleta y el efecto conocido de la adenosina sobre la conducción auriculoventricular no respalda un beneficio en el bloqueo de rama.

**Para avanzar se necesita:**
- Aclarar a qué entidad clínica vigente corresponde el término obsoleto de la predicción
- Datos del mecanismo de acción que justifiquen un efecto terapéutico y no solo farmacológico sobre la conducción
- Evidencia preclínica o clínica que estudie directamente esta enfermedad
- Revisión de advertencias y contraindicaciones del prospecto de la AEMPS
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

