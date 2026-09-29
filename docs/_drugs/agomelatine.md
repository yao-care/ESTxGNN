---
layout: default
title: Agomelatine
parent: Solo predicción del modelo (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Agomelatine
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

# Agomelatina: De Trastorno Depresivo Mayor a Tortícolis Paroxística Benigna de la Infancia

## Resumen en Una Frase

Agomelatina es un antidepresivo comercializado en España (por ejemplo, como Valdoxan) y utilizado para el trastorno depresivo mayor en adultos.
El modelo TxGNN predice que podría ser efectivo para **tortícolis paroxística benigna de la infancia**, pero **no hay ningún ensayo clínico ni publicación** que respalde esta dirección, por lo que se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno depresivo mayor (según los datos farmacológicos y la literatura del paquete; los registros de autorización no incluyen texto de indicación) |
| Nueva Indicación Predicha | Tortícolis paroxística benigna de la infancia |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados del mecanismo de acción en DrugBank. Según la literatura del paquete, agomelatina es un agonista de los receptores melatoninérgicos MT1 y MT2 y un antagonista del receptor serotoninérgico 5-HT2C. Los datos farmacológicos también la vinculan con los receptores 5-HT2A y 5-HT2B. Este mecanismo permite resincronizar los ritmos circadianos y aumentar la liberación de dopamina y noradrenalina en la corteza prefrontal, lo que explica su efecto antidepresivo.

**No se identifica un vínculo mecanístico entre este perfil y la tortícolis paroxística benigna de la infancia.** Es un trastorno pediátrico episódico y agomelatina se ha estudiado en depresión del adulto. El puntaje alto del grafo de conocimiento no está respaldado por ningún ensayo ni publicación, y el análisis del paquete señala además una preocupación de seguridad pediátrica. Por ello, esta predicción debe considerarse una hipótesis sin fundamento clínico por ahora.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 83546 | AGOMELATINA STADA 25 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película |
| 83453 | AGOMELATINA ARISTO 25 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película |
| 08499003IP1 | VALDOXAN 25 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película |
| 08499008 | VALDOXAN 25 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película |
| 83521 | AGOMELATINA QUALIGEN 25 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película |

Se muestran 5 de las 20 autorizaciones. Todas son comprimidos de 25 mg, y los registros no incluyen el texto de la indicación aprobada.

## Consideraciones de Seguridad

- **Población pediátrica**: el análisis del paquete señala una preocupación de seguridad en niños, relevante porque la indicación predicha es infantil.

Para el resto de la información de seguridad (advertencias, contraindicaciones e interacciones farmacológicas), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura (nivel L5), carece de un vínculo mecanístico plausible y plantea una preocupación de seguridad pediátrica. Un puntaje alto del modelo no basta para avanzar.

**Para avanzar se necesita:**
- Una hipótesis mecanística que relacione la modulación MT1/MT2 y 5-HT2C con la fisiopatología de la tortícolis paroxística benigna.
- Datos de seguridad pediátrica, ya que la población objetivo son lactantes.
- Advertencias y contraindicaciones extraídas del prospecto de la AEMPS.
- Datos del mecanismo de acción desde DrugBank.

**Nota:** entre las otras predicciones del paquete, las de melancolía y depresión neurótica (nivel L3, "Proceed with Guardrails") son las mejor respaldadas. Sin embargo, probablemente se solapan con la indicación ya comercializada, por lo que no constituirían un reposicionamiento genuino.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

