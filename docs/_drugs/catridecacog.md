---
layout: default
title: Catridecacog
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 3
---

# Catridecacog
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# CATRIDECACOG: De Deficiencia Congenita del Factor XIII a Trastorno Primario de Liberacion Plaquetaria

## Resumen en Una Frase

Catridecacog es un Factor XIII A2 recombinante, cuyo uso conocido se asocia al tratamiento de reemplazo en la deficiencia congenita de la subunidad A del Factor XIII (segun la logica mecanicista disponible en los datos, ya que el campo estructurado de indicacion original no contiene informacion). El modelo TxGNN predice que podria ser efectivo para **Trastorno Primario de Liberacion Plaquetaria**, pero actualmente **no existe ningun ensayo clinico ni publicacion** que respalde esta direccion: la prediccion se sostiene unicamente en la cercania semantica dentro del grafo de conocimiento.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en registros de Espana (farmaco no comercializado); segun el contexto mecanistico aportado, se asocia a la deficiencia congenita de la subunidad A del Factor XIII |
| Nueva Indicacion Predicha | Trastorno Primario de Liberacion Plaquetaria |
| Puntaje de Prediccion TxGNN | 99.29% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en el registro estructurado. Segun la informacion contextual disponible, catridecacog es una subunidad A2 del Factor XIII recombinante cuya funcion farmacologica se situa al final de la cascada de coagulacion: entrecruza monomeros solubles de fibrina para formar una red estable y tambien puede entrecruzar proteinas de membrana plaquetaria (como vinculina y actina) para reforzar la contraccion y estabilidad del trombo.

El Trastorno Primario de Liberacion Plaquetaria, en cambio, es una alteracion a nivel de la senalizacion de activacion plaquetaria (liberacion defectuosa del contenido de los granulos densos/alfa), es decir, un nivel patologico distinto al de la estabilizacion de fibrina/plaquetas que realiza el Factor XIII. La puntuacion elevada de TxGNN probablemente refleja la cercania semantica entre conceptos de "coagulacion/hemostasia" en el grafo de conocimiento, mas que una relacion causal directa. No existe respaldo farmacologico directo que indique que el Factor XIII pueda corregir el defecto de activacion/liberacion plaquetaria en si mismo.

Cabe senalar que las otras dos indicaciones predichas por el modelo (enfermedad de von Willebrand tipo plaquetario y trombastenia de Glanzmann) presentan el mismo patron: puntuaciones TxGNN muy altas (>99%) pero vinculos mecanisticos igualmente indirectos, ya que ambas patologias se originan en defectos de receptores plaquetarios (GPIbα y GPIIb/IIIa respectivamente) y no en la etapa de estabilizacion de fibrina donde actua el Factor XIII.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion se apoya exclusivamente en el modelo TxGNN (Nivel de Evidencia L5), sin ningun ensayo clinico ni publicacion que la respalde, y el propio analisis mecanistico indica que la relacion entre la farmacologia del Factor XIII y la fisiopatologia del trastorno de liberacion plaquetaria es indirecta. Ademas, el farmaco no esta comercializado en Espana y faltan datos regulatorios basicos.

**Para avanzar se necesita:**
- Advertencias y contraindicaciones del prospecto de la TFDA (dato bloqueante actualmente ausente)
- Datos detallados del mecanismo de accion (MOA) via DrugBank u otra fuente primaria
- Confirmacion documental de la(s) indicacion(es) original(es) aprobada(s) del farmaco
- Estudios preclinicos o de mecanismo que evaluen especificamente el efecto del Factor XIII sobre la activacion/liberacion plaquetaria antes de considerar avanzar a fases de evaluacion posteriores
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

