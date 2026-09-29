---
layout: default
title: Moxifloxacin
parent: Solo predicción del modelo (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
---

# Moxifloxacin
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

# Moxifloxacino: De Infecciones Bacterianas a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

Moxifloxacino es un antibiótico de la familia de las fluoroquinolonas, utilizado en infecciones bacterianas. Los datos de autorización de la AEMPS recibidos no incluyen el texto de la indicación.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hiperviscosidad policlonal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción. Es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones bacterianas (el texto de indicación de las autorizaciones está vacío en los datos recibidos) |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Moxifloxacino inhibe la ADN girasa y la topoisomerasa IV bacterianas. Es un mecanismo antibacteriano, dirigido a procesos infecciosos.

El síndrome de hiperviscosidad policlonal no es una infección, sino un problema de viscosidad de la sangre. **No se identifica un vínculo mecanístico plausible** entre la acción antibacteriana del fármaco y esta enfermedad. El puntaje de 99.98% refleja únicamente la predicción del modelo y no está respaldado por ensayos ni literatura, por lo que no debe interpretarse como evidencia de eficacia.

Cabe señalar que otras predicciones del mismo fármaco sí tienen más plausibilidad biológica. La **peste bubónica** (posición 10 del ranking, puntaje 99.41%) cuenta con estudios preclínicos que muestran actividad contra *Yersinia pestis*. Se trata de una extensión dentro de la misma clase de antibióticos y no de un mecanismo nuevo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 82014 | Moxifloxacino Aurovitas 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos recibidos |
| 82282 | Moxifloxacino Macleods 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos recibidos |
| 77126 | Moxifloxacino Aurobindo 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos recibidos |
| 77662 | Moxifloxacino Cinfa 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos recibidos |
| 78336 | Abiox 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos recibidos |

Se muestran 5 de las 20 autorizaciones. En el conjunto de datos también figuran otras formas farmacéuticas: colirio en solución, colirio en envase unidosis y solución para perfusión.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre un antibiótico y un síndrome de hiperviscosidad. Además, las fluoroquinolonas tienen un perfil de riesgo conocido (tendinopatía, prolongación del QT, efectos en el sistema nervioso central y en el oído), que no compensa un beneficio no demostrado.

**Para avanzar se necesita:**
- Descargar el prospecto de la AEMPS para completar advertencias, contraindicaciones e indicaciones aprobadas, ya que sin ello no se puede pasar al cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Priorizar otras predicciones de este fármaco, como la **peste bubónica** (L4, etapa S1, "Research Question"), que tiene evidencia preclínica y mayor plausibilidad biológica. Requeriría evidencia clínica en humanos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

