---
layout: default
title: Sonidegib
parent: 僅模型預測 (L5)
nav_order: 262
evidence_level: L5
indication_count: 10
---

# Sonidegib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Sonidegib: De Carcinoma Basocelular Avanzado a Meduloblastoma con Nodularidad Extensa

## Resumen en Una Frase

Sonidegib es un inhibidor de la via Hedgehog (antagonista del receptor Smoothened, SMO) utilizado originalmente en el carcinoma basocelular localmente avanzado o metastasico. El modelo TxGNN predice que podria ser efectivo para el **Meduloblastoma con Nodularidad Extensa (MBEN)**, un subtipo tumoral pediatrico dependiente de la misma via SHH, pero actualmente **no existe ningun ensayo clinico ni publicacion** en este paquete de evidencia que respalde directamente esta direccion.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Carcinoma basocelular localmente avanzado/metastasico (dato obtenido de la literatura incluida en este paquete, no de licencias AEMPS — el farmaco no esta comercializado en España) |
| Nueva Indicacion Predicha | Meduloblastoma con Nodularidad Extensa |
| Puntaje de Prediccion TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en la ficha tecnica del farmaco. Segun la evidencia bibliografica incluida en este paquete (asociada a la indicacion "cancer de piel" dentro de las predicciones), sonidegib es un antagonista del receptor Smoothened (SMO) que inhibe la via de senalizacion Hedgehog (Hh), y ha sido aprobado a nivel mundial (Suiza, FDA, EMA) para el carcinoma basocelular localmente avanzado, una neoplasia cutanea impulsada por activacion aberrante de esta via.

El meduloblastoma con nodularidad extensa (MBEN) es un subtipo histologico pediatrico de meduloblastoma caracterizado por activacion constitutiva de la via Sonic Hedgehog (SHH), el mismo eje molecular que sonidegib inhibe en el carcinoma basocelular. Esta coincidencia mecanistica explica la puntuacion muy alta de TxGNN (99.90%) para este par farmaco-enfermedad.

Sin embargo, la aplicabilidad clinica real es incierta: el uso de inhibidores de SMO en tumores cerebrales pediatricos plantea retos especificos (penetracion de la barrera hematoencefalica, toxicidad sobre placas de crecimiento oseo en poblacion pediatrica, resistencia adquirida por mutaciones en SMO) que no estan evaluados en este paquete de evidencia. Al no existir ningun ensayo clinico ni publicacion que evalue directamente sonidegib en MBEN, la hipotesis mecanistica no debe considerarse validada.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Citotoxicidad

*(Se incluye esta seccion porque la indicacion original — carcinoma basocelular — es una neoplasia maligna.)*

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (antagonista del receptor Smoothened / inhibidor de la via Hedgehog) |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion para Meduloblastoma con Nodularidad Extensa se apoya unicamente en la puntuacion del modelo TxGNN y en un razonamiento mecanistico (ambos tumores dependen de la via Hedgehog/SMO), sin ningun ensayo clinico ni publicacion que la respalde directamente. Con nivel de evidencia L5, no es posible avanzar mas alla de la etapa de hipotesis.

**Para avanzar se necesita:**
- Datos de mecanismo de accion (MOA) verificados desde DrugBank o ficha tecnica oficial
- Busqueda dirigida de literatura y ensayos sobre inhibidores de SMO en meduloblastoma SHH-activado pediatrico (fuera del alcance de esta consulta)
- Datos de seguridad del prospecto TFDA/AEMPS (advertencias, contraindicaciones, interacciones), actualmente todos en falta
- Evaluacion especifica de farmacocinetica y seguridad en poblacion pediatrica

**Nota adicional:** dentro de este mismo paquete de evidencia, la indicacion "cancer de piel" (carcinoma basocelular) presenta un nivel de evidencia mucho mayor (L2, 10 ensayos clinicos incluido el estudio pivotal BOLT, 20 publicaciones, recomendacion "Proceed with Guardrails"), ya que corresponde en la practica a la indicacion ya aprobada del farmaco a nivel mundial. Se recomienda revisar esa via como comparacion de referencia al priorizar candidatos de reposicionamiento para este farmaco.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

