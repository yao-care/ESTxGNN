---
layout: default
title: Palivizumab
parent: Solo predicción del modelo (L5)
nav_order: 404
evidence_level: L5
indication_count: 10
---

# Palivizumab
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

# Palivizumab: De Prevención de la Infección por VRS a Neoplasia Benigna de Lengua

## Resumen en Una Frase

Palivizumab es un anticuerpo monoclonal humanizado dirigido contra la proteína F del virus respiratorio sincitial (VRS), utilizado para prevenir la enfermedad grave por este virus en lactantes de alto riesgo. El modelo TxGNN predice que podría ser efectivo para **neoplasia benigna de lengua**, pero **no hay ningún ensayo clínico ni publicación** que respalde esta predicción, por lo que se trata únicamente de un resultado del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Prevención de la enfermedad grave por VRS (información general del fármaco; los textos de indicación de las autorizaciones no constan en los datos recibidos) |
| Nueva Indicación Predicha | Neoplasia benigna de lengua |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, palivizumab es un anticuerpo monoclonal humanizado que neutraliza el VRS al unirse a su proteína de fusión F. Su eficacia como profilaxis frente al VRS está comprobada. Sin embargo, no existe un vínculo mecanístico plausible con la nueva indicación.

La proteína F es un antígeno viral. No se ha descrito su expresión ni ninguna vía relacionada en tumores benignos de la lengua. Por eso el puntaje de 99.94% debe interpretarse como una asociación del grafo de conocimiento, no como una señal biológica o clínica.

Las otras nueve predicciones principales (epiglotis, neuroblastoma cervical, hipofaringe, suelo de la boca, testículo y paratestículo, neoplasia quística, schwannoma del agujero yugular, mesenquimoma y quiste del conducto tirogloso) tienen puntajes similares (99.93–99.94%). Todas tienen nivel L5, ausencia de ensayos y de literatura, y ninguna cuenta con un mecanismo plausible. Esto sugiere que los puntajes altos reflejan un patrón general del modelo para este fármaco y no una señal específica.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 199117003 | SYNAGIS 50 mg/0,5 ml solución inyectable | Solución inyectable |
| 99117002 | SYNAGIS 100 mg polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable |
| 99117001 | SYNAGIS 50 mg polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable |
| 199117004 | SYNAGIS 100 mg/1 ml solución inyectable | Solución inyectable |

Titular de las cuatro autorizaciones: AstraZeneca AB. Los datos recibidos no incluyen el texto de la indicación aprobada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y sin un mecanismo biológico que conecte un anticuerpo anti-VRS con esta neoplasia benigna. No hay base para avanzar.

**Para avanzar se necesita:**
- Un mecanismo biológico plausible, por ejemplo evidencia de que exista una diana relevante en el tejido tumoral
- Estudios preclínicos o literatura que apoyen la hipótesis
- El prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada), que hoy falta en los datos
- Datos de mecanismo de acción de DrugBank, para completar el análisis
- Reevaluar solo si aparece evidencia independiente del puntaje del modelo

> Los resultados son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

