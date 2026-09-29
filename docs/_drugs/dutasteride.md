---
layout: default
title: Dutasteride
parent: Solo predicción del modelo (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasterida: De Hiperplasia Benigna de Próstata a Hipertricosis Universal Congénita Tipo Ambras

## Resumen en Una Frase

Dutasterida es un inhibidor dual de la 5-alfa reductasa (tipos 1 y 2) que reduce la dihidrotestosterona (DHT). Su uso original habitual es la hiperplasia benigna de próstata. Este dato no consta en el Evidence Pack ni en el texto de las autorizaciones de la AEMPS, y no está verificado.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita tipo Ambras**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción basada solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de autorización de la AEMPS (hiperplasia benigna de próstata según conocimiento general, no verificado) |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.998% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Dutasterida inhibe la 5-alfa reductasa tipos 1 y 2, las enzimas que convierten la testosterona en DHT. Al reducir la DHT en los tejidos, también actúa sobre el folículo piloso. Por eso se usa fuera de indicación en la alopecia androgenética.

El vínculo con el síndrome de Ambras es débil. Este síndrome es un trastorno congénito causado por reordenamientos genómicos en 8q22 que alteran la regulación de *TRPS1*. No es un cuadro principalmente androgénico, y no hay razón mecanística clara para que suprimir la DHT corrija el exceso de vello. El puntaje del modelo es muy alto (0.99998), pero ningún ensayo, publicación o reporte de caso lo respalda.

Las otras nueve predicciones del modelo tienen la misma limitación. Todas están en L5, salvo "alopecia areata difusa" en L4, y la mayoría en "Hold". La de "hipotricosis simple del cuero cabelludo" figura como "pregunta de investigación", por analogía con la alopecia androgenética. Sigue sin verificarse, porque la causa es genética y no androgénica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Hay 20 autorizaciones en total. Se listan las 5 principales. El texto de indicación aprobada no está disponible en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 83259 | Dutasterida Tarbis 0,5 mg cápsulas blandas EFG | Cápsula blanda | Tarbis Farma S.L. |
| 77635 | Dutasterida Ratiopharm 0,5 mg cápsulas blandas EFG | Cápsula blanda | Teva Pharma S.L.U. |
| 81431 | Dutasterida Sandoz 0,5 mg cápsulas blandas EFG | Cápsula blanda | Sandoz Farmacéutica S.A. |
| 79750 | Dutasterida Vir 0,5 mg cápsulas blandas EFG | Cápsula blanda | Industria Química y Farmacéutica Vir S.A. |
| 81153 | Dutasterida Pensa 0,5 mg cápsulas blandas EFG | Cápsula blanda | Towa Pharmaceutical S.A. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (L5), sin ensayos, literatura ni casos clínicos. El mecanismo de la dutasterida (supresión de DHT) no explica un síndrome genético que no depende de andrógenos, por lo que la predicción parece un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), que hoy bloquea el cribado de seguridad.
- Confirmar la indicación original aprobada en España, que no consta en los datos.
- Buscar evidencia directa: reportes de caso, estudios preclínicos o datos sobre la vía TRPS1/8q22 y su relación con la señalización androgénica.
- Priorizar las predicciones con racional androgénico más plausible, como la hipotricosis simple del cuero cabelludo, antes de invertir en esta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

