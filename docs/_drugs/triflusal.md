---
layout: default
title: Triflusal
parent: Solo predicción del modelo (L5)
nav_order: 546
evidence_level: L5
indication_count: 5
---

# Triflusal
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Triflusal: De Antiagregante Plaquetario a Exceso de Factor V con Trombosis Espontánea

## Resumen en Una Frase

Triflusal es un antiagregante plaquetario comercializado en España. Los datos recibidos no incluyen su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **exceso de factor V con trombosis espontánea**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Exceso de factor V con trombosis espontánea |
| Puntaje de Predicción TxGNN | 99.60% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, triflusal es un antiagregante plaquetario que inhibe de forma irreversible la COX-1. Su metabolito HTB añade inhibición de fosfodiesterasas y preserva la prostaciclina del endotelio. Estos datos provienen del análisis de la hipótesis de reposicionamiento, no de un campo de MOA verificado.

El exceso de factor V es un defecto de la cascada de coagulación, no del funcionamiento plaquetario. El vínculo con triflusal es por tanto **indirecto**: el fármaco solo podría reducir la contribución de las plaquetas a la propagación del trombo. No corregiría el defecto de coagulación de fondo.

El puntaje de 99.60% refleja una asociación en el grafo de conocimiento de TxGNN, no evidencia clínica. Sin ensayos ni literatura, esta predicción debe tratarse como una hipótesis por verificar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 10 autorizaciones. El Evidence Pack no incluye el texto de indicación aprobada de ninguna de ellas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 68135 | DISGREN 600 mg polvo y disolvente para solución oral | Polvo y disolvente para solución oral |
| 65268 | Triflusal Ratiopharm 300 mg cápsulas EFG | Cápsula dura |
| 76110 | Triflusal Pensa 300 mg cápsulas duras EFG | Cápsula dura |
| 65248 | Anpeval 300 mg cápsulas duras EFG | Cápsula dura |
| 68092 | Triflusal Teva 300 mg cápsulas EFG | Cápsula dura |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni publicaciones (nivel L5), y el mecanismo es solo indirecto: triflusal actúa sobre las plaquetas y la indicación predicha es un defecto de la coagulación. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de la AEMPS (advertencias, contraindicaciones e indicación aprobada), un vacío bloqueante para el cribado de seguridad
- Obtener los datos de mecanismo de acción desde DrugBank
- Buscar estudios de mecanismo o casos clínicos sobre triflusal en trastornos trombofílicos
- Valorar candidatas alternativas del mismo modelo con algo de literatura, como **trombofilia** (1 estudio farmacodinámico de función plaquetaria, nivel L4), aunque la evidencia sigue siendo indirecta

*Este informe es solo una referencia de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

