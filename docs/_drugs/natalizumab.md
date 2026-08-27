---
layout: default
title: Natalizumab
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 5
---

# Natalizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# NATALIZUMAB: De Esclerosis Multiple y Enfermedad de Crohn a Bronquitis

## Resumen en Una Frase

Natalizumab es un anticuerpo monoclonal anti-integrina α4, utilizado clinicamente en el tratamiento de la esclerosis multiple y la enfermedad de Crohn.
El modelo TxGNN predice que podria ser efectivo para **Bronquitis**,
pero actualmente **no existe ningun ensayo clinico ni publicacion cientifica** que respalde esta direccion — la puntuacion se basa unicamente en la prediccion del modelo.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Esclerosis multiple y enfermedad de Crohn (segun notas mecanisticas del Evidence Pack; no hay ficha tecnica formal disponible) |
| Nueva Indicacion Predicha | Bronquitis |
| Puntaje de Prediccion TxGNN | 99.46% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

No se dispone de datos verificados sobre el mecanismo de accion (MOA) procedentes de DrugBank — esta es actualmente una brecha de datos pendiente de resolucion. Segun las notas mecanisticas incluidas en el propio Evidence Pack, Natalizumab es un anticuerpo monoclonal dirigido contra la integrina α4 (VLA-4), que bloquea la migracion de leucocitos a traves del endotelio mediada por VCAM-1; clinicamente se emplea en esclerosis multiple y enfermedad de Crohn.

La bronquitis es, en la mayoria de los casos, un cuadro infeccioso o irritativo de la via aerea. El propio razonamiento mecanistico del Evidence Pack senala que la inmunosupresion sistemica de natalizumab **no coincide** con la necesidad terapeutica de la bronquitis, y que incluso podria **aumentar el riesgo de bronquitis de origen infeccioso** al reducir la vigilancia inmunitaria de la via respiratoria.

Por tanto, la puntuacion alta de TxGNN (99.46%) debe interpretarse como una asociacion estadistica del modelo y no como una hipotesis mecanisticamente solida: no existe ningun dato clinico, preclinico ni bibliografico especifico para bronquitis que la respalde.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion se sustenta unicamente en el score de TxGNN (Nivel de Evidencia L5), sin ningun ensayo clinico ni publicacion especifica para bronquitis. Ademas, el propio razonamiento mecanistico disponible en el Evidence Pack apunta en direccion contraria: la inmunosupresion sistemica de natalizumab podria agravar en lugar de tratar un cuadro de bronquitis infecciosa.

**Para avanzar se necesita:**
- Ficha tecnica/prospecto oficial de la AEMPS (advertencias y contraindicaciones) — actualmente bloqueante
- Datos verificados de MOA desde DrugBank
- Evidencia clinica real (ensayos o series de casos) especifica para bronquitis, actualmente inexistente
- Reevaluacion del perfil riesgo-beneficio considerando el riesgo de inmunosupresion sistemica (incluida la leucoencefalopatia multifocal progresiva, senalada en la literatura de otras indicaciones dentro de este mismo Evidence Pack)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

