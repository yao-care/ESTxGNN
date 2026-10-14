---
layout: default
title: Avelumab
parent: Solo predicción del modelo (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: De Carcinoma Neuroendocrino Cutáneo a Tumor Relacionado con el Herpesvirus Humano 8

## Resumen en Una Frase

Avelumab es un anticuerpo anti-PD-L1, originalmente utilizado para el tratamiento del carcinoma neuroendocrino cutáneo (carcinoma de células de Merkel).
El modelo TxGNN predice que podría ser efectivo para **tumores relacionados con el herpesvirus humano 8**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma neuroendocrino cutáneo (según el grafo de conocimiento; el texto de indicación autorizado no está disponible) |
| Nueva Indicación Predicha | Tumor relacionado con el herpesvirus humano 8 |
| Puntaje de Predicción TxGNN | 99,97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, avelumab es un anticuerpo monoclonal que bloquea PD-L1, y su eficacia en el carcinoma de células de Merkel (un cáncer neuroendocrino cutáneo asociado a un virus) ha sido comprobada. Mecanísticamente podría ser aplicable a tumores relacionados con el VHH-8.

La relación con la indicación original es la siguiente: ambos son tumores asociados a virus. En tumores como el sarcoma de Kaposi se ha descrito agotamiento inmunitario del eje PD-1/PD-L1, por lo que el bloqueo de PD-L1 podría restaurar la respuesta inmunitaria antitumoral.

No obstante, este vínculo se apoya solo en la predicción de TxGNN y en un razonamiento biológico general. No se dispone de ensayos ni literatura que lo confirmen.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 171214001IP | BAVENCIO 20 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos |
| 1171214001 | BAVENCIO 20 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos |
| 171214001IP1 | BAVENCIO 20 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-PD-L1) |
| Riesgo de Mielosupresión | Bajo en general; no es un citotóxico convencional. Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto (habitualmente hemograma, función hepática, renal y tiroidea) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 3 interacciones de nivel *Mayor*, con los inmunomoduladores:
  - Lenalidomida
  - Pomalidomida
  - Talidomida

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Otras Indicaciones Predichas (Referencia)

Además de la predicción principal, el modelo propone otras indicaciones, todas sin ensayos ni literatura en los datos compilados:

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Comentario |
|------|------|------|------|
| Tumor neuroendocrino del oído medio | 99,97% | L5 | Relación biológica con la indicación original; tumor extremadamente raro |
| Tumor cutáneo maligno de células granulares | 99,97% | L5 | Predicción puramente computacional |
| Ectomesenquimoma | 99,97% | L5 | Sin dependencia de PD-L1 establecida |
| Déficit de adenosina desaminasa | 99,95% | L5 | Mecanísticamente improbable; probable artefacto de la red |
| Disgenesia reticular | 99,94% | L5 | Mecanísticamente improbable; probable artefacto de la red |
| Hipoplasia inmunoeritromieloide | 99,94% | L5 | Sin vínculo mecanístico |
| Inmunodeficiencia no combinada grave | 99,92% | L5 | Probable artefacto computacional |
| Carcinoma urotelial de la uretra prostática | 99,92% | L4 | Apoyo indirecto: avelumab está aprobado como mantenimiento en carcinoma urotelial (JAVELIN Bladder 100, Fase 3); es una inferencia del perfil conocido del fármaco |
| Carcinoma sarcomatoide de células transicionales de la pelvis renal | 99,91% | L4 | Apoyo indirecto por la indicación urotelial; extrapolación con cautela |

Las dos indicaciones uroteliales son las que cuentan con el razonamiento más sólido, aunque indirecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal tiene un puntaje alto en TxGNN, pero se encuentra en el nivel L5: no hay ensayos clínicos ni literatura que la respalden. Además, faltan datos de seguridad del prospecto, lo que bloquea el cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones) y confirmar las indicaciones autorizadas
- Obtener datos detallados del mecanismo de acción desde DrugBank
- Realizar una búsqueda sistemática de ensayos y literatura sobre avelumab en sarcoma de Kaposi y otros tumores relacionados con el VHH-8
- Valorar priorizar las indicaciones uroteliales (L4), que cuentan con apoyo indirecto
- Evaluar la gestión clínica de las interacciones mayores con lenalidomida, pomalidomida y talidomida (frecuentes en terapias del sarcoma de Kaposi y otras neoplasias)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

