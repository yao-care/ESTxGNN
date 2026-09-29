---
layout: default
title: Catumaxomab
parent: Solo predicción del modelo (L5)
nav_order: 108
evidence_level: L5
indication_count: 3
---

# Catumaxomab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Catumaxomab: De Indicación Original No Disponible a Retinopatía Diabética No Proliferativa Grave

## Resumen en Una Frase

Catumaxomab es un anticuerpo biespecífico (EpCAM × CD3) que redirige linfocitos T contra células tumorales; los datos recibidos no incluyen su indicación original.
El modelo TxGNN predice que podría ser efectivo para **retinopatía diabética no proliferativa grave**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (las autorizaciones de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Retinopatía diabética no proliferativa grave |
| Puntaje de Predicción TxGNN | 99.64% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

**No se encontró un vínculo mecanístico que respalde esta predicción.** El puntaje de TxGNN (0.996) es la única base, sin ensayos ni literatura de apoyo.

Catumaxomab es un anticuerpo biespecífico que se une a EpCAM y CD3, y redirige los linfocitos T hacia las células tumorales que expresan EpCAM. La retinopatía diabética, en cambio, depende de la fuga vascular mediada por VEGF, la inflamación y el daño neurovascular. Ninguna vía conecta ambos mecanismos. Además, la activación sistémica de linfocitos T y la liberación de citocinas supondrían una preocupación de seguridad en el ojo.

El modelo también predijo **osteoporosis inducida por fármacos** (99.58%) y **retinopatía diabética** (99.47%), ambas con nivel L5 y decisión Hold:

- **Retinopatía diabética:** solapa con la predicción principal, por lo que ambas no constituyen evidencia independiente. Las terapias establecidas actúan sobre VEGF, la inflamación o vías láser y quirúrgicas, ninguna relacionada con la activación de linfocitos T por EpCAM/CD3.
- **Osteoporosis inducida por fármacos:** la redirección de linfocitos T y la inducción de citocinas proinflamatorias (TNF-alfa, IL-6) harían esperar, en todo caso, más resorción ósea y no protección. Es una preocupación teórica, no evidencia documentada. Lo más probable es que sea un artefacto de los embeddings del grafo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1241826001 | KORJUNY 10 microgramos | Concentrado para solución para perfusión | No especificada en los datos |
| 1241826002 | KORJUNY 50 microgramos | Concentrado para solución para perfusión | No especificada en los datos |
| 09512001 | REMOVAB 10 microgramos | Concentrado para solución para perfusión | No especificada en los datos |
| 09512002 | REMOVAB 50 microgramos | Concentrado para solución para perfusión | No especificada en los datos |

Titulares: Atnahs Pharma Netherlands B.V. (KORJUNY) y Fresenius Biotech GmbH (REMOVAB).

## Citotoxicidad

Catumaxomab actúa sobre células tumorales que expresan EpCAM, por lo que se incluye esta sección. Los datos recibidos no contienen categorías de DrugBank ni datos de toxicidad.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo biespecífico que redirige linfocitos T) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (nivel L5), sin ensayos ni publicaciones. No existe una conexión mecanística plausible entre la activación de linfocitos T por EpCAM/CD3 y la retinopatía diabética, y la seguridad ocular de un anticuerpo que activa linfocitos T no está demostrada.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (advertencias y contraindicaciones), un vacío bloqueante para cualquier evaluación de seguridad
- Completar los datos del mecanismo de acción y de la indicación original desde DrugBank
- Evidencia preclínica o mecanística que conecte EpCAM/CD3 con la fisiopatología de la retinopatía diabética
- Evaluar la compatibilidad de vía de administración (una administración ocular no está definida ni respaldada)
- Reevaluar solo si aparecen ensayos o literatura independientes que respalden alguna de las tres predicciones
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

