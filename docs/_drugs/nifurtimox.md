---
layout: default
title: Nifurtimox
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 7
---

# Nifurtimox
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Nifurtimox: De Enfermedad de Chagas a Analbuminemia Congenita

## Resumen en Una Frase

Nifurtimox es un derivado nitrofurano antiparasitario, historicamente utilizado para el tratamiento de la enfermedad de Chagas (tripanosomiasis americana); no consta un registro de comercializacion en España en los datos disponibles.
El modelo TxGNN predice que podria ser efectivo para **Analbuminemia Congenita**, con un puntaje de 99.58%,
pero **no existe actualmente ningun ensayo clinico ni publicacion** que respalde esta direccion, y la propia racionalizacion del modelo señala que se trata probablemente de una asociacion espuria.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Enfermedad de Chagas (tripanosomiasis americana) — no consta en los registros estructurados de Taiwan/España, ya que el farmaco no esta comercializado; dato basado en conocimiento farmacologico general |
| Nueva Indicacion Predicha | Analbuminemia Congenita |
| Puntaje de Prediccion TxGNN | 99.58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en las fuentes estructuradas consultadas. Segun la informacion farmacologica general conocida, Nifurtimox es un derivado nitrofurano cuya actividad tripanocida depende de la reduccion de su grupo nitro, generando especies reactivas de oxigeno (ROS) que dañan el ADN y las membranas del parasito *Trypanosoma cruzi*; este mismo mecanismo oxidativo es el que se ha explorado experimentalmente en modelos de citotoxicidad celular.

Sin embargo, la indicacion predicha en este informe (analbuminemia congenita) es una enfermedad hereditaria autosomica recesiva causada por defectos en el gen *ALB*, sin relacion fisiopatologica conocida con la accion antiparasitaria/oxidativa de Nifurtimox.

Segun la propia racionalizacion del modelo TxGNN incluida en el Evidence Pack, esta prediccion carece de vinculo mecanistico verificable y es representativa de un patron conocido: puntajes altos del modelo para enfermedades raras/geneticas que suelen corresponder a falsos positivos por ruido en el grafo de relaciones, mas que a una hipotesis biologica solida. No se recomienda avanzar en la investigacion de esta indicacion especifica sin evidencia mecanistica adicional.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Informacion de Mercado en España

Nifurtimox no esta comercializado en España (0 autorizaciones registradas), por lo que no hay datos de productos, formas farmaceuticas ni indicaciones aprobadas localmente que reportar.

## Consideraciones de Seguridad

Los campos estructurados de seguridad (advertencias, contraindicaciones e interacciones) no contienen datos disponibles en este Evidence Pack.

- **Señal relevante detectada en el analisis de otra indicacion candidata (#7, "hematological disease associated with an acquired peripheral neuropathy")**: segun el prospecto referenciado por TFDA, Nifurtimox se asocia con neuropatia periferica como reaccion adversa grave, con una incidencia reportada de aproximadamente 18.5%. Este dato no forma parte de los campos estructurados de seguridad del informe, pero se documenta aqui por su relevancia clinica directa.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Las siete indicaciones predichas por TxGNN se encuentran en Nivel de Evidencia L5 (solo puntaje del modelo, sin ensayos clinicos ni literatura de respaldo), y varias de las racionalizaciones incluidas en el propio Evidence Pack señalan explicitamente que corresponden a asociaciones probablemente espurias (enfermedades geneticas raras sin vinculo mecanistico, o confusion entre relacion terapeutica y relacion de efecto adverso conocido). Ademas, el farmaco no esta comercializado en España y faltan datos criticos de seguridad y mecanismo de accion (ver brechas de datos DG001 y DG002).

**Para avanzar se necesita:**
- Obtener y analizar el prospecto TFDA/EMA completo (advertencias, contraindicaciones e interacciones) — actualmente bloqueante (DG001)
- Obtener datos estructurados del mecanismo de accion (DG002)
- Si se desea priorizar alguna via de investigacion, la indicacion #6 ("premalignant hematological system disease") presenta al menos una hipotesis mecanistica preliminar (citotoxicidad mediada por ROS observada in vitro en neuroblastoma, NCT00601003) que podria justificar una busqueda de evidencia mas dirigida, aunque tambien en nivel L5
- Descartar formalmente la indicacion #7 como candidata de reposicionamiento, dado que su racional corresponde a un efecto adverso conocido y no a una hipotesis terapeutica
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

