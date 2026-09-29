---
layout: default
title: Doxylamine
parent: Solo predicción del modelo (L5)
nav_order: 184
evidence_level: L5
indication_count: 4
---

# Doxylamine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Doxylamina: De Antihistamínico H1 de Primera Generación a Urticaria Alérgica

## Resumen en Una Frase

Doxilamina es un antihistamínico H1 de primera generación, comercializado en España en 18 autorizaciones, aunque los registros de la AEMPS recibidos no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones recibidas (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99,85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 18 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Lo que sigue proviene de farmacología general, no de los datos de entrada. Doxilamina es un antagonista del receptor H1 de la histamina, y la activación de los mastocitos mediada por histamina es un motor central de la urticaria. Por eso el vínculo mecanístico es muy plausible.

Hay una advertencia importante: el puntaje de 99,85% podría reflejar el redescubrimiento de un uso ya conocido de los antihistamínicos, y no un reposicionamiento genuino. Tampoco se puede distinguir si la señal es específica de doxilamina o un efecto de clase. Además, los antihistamínicos de primera generación se asocian a sedación y carga anticolinérgica, en comparación con los de segunda generación.

El modelo también predijo otras tres indicaciones, todas con evidencia L5 y sin ensayos ni literatura:

- **Urticaria por frío** (99,26%): mecanismo histaminérgico plausible. Se recomienda una búsqueda bibliográfica sobre antihistamínicos de primera generación en esta condición.
- **Enfermedad de la cavidad nasal** (99,36%): término demasiado amplio. Debe acotarse a una condición concreta antes de revisar evidencia. Estado: Hold.
- **Laringofaringitis aguda** (99,34%): vínculo débil e indirecto, ya que la causa suele ser infecciosa o irritativa, y la sequedad de mucosas podría ser contraproducente. Estado: Hold.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 18 autorizaciones.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 83322 | Doximax 12,5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No registrada en los datos |
| 80704 | Doxilamina Sandoz Care 25 mg comprimidos recubiertos con película | Comprimido recubierto con película | No registrada en los datos |
| 77281 | Doxilamina Esteve 12,5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No registrada en los datos |
| 60154 | Dormidina Doxilamina 12,5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No registrada en los datos |
| 77517 | Normodorm 25 mg comprimidos recubiertos con película | Comprimido recubierto con película | No registrada en los datos |

También existe una forma de polvo oral en el conjunto de autorizaciones.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se obtuvieron advertencias, contraindicaciones ni interacciones farmacológicas de la AEMPS o DrugBank. La consulta de interacciones no devolvió resultados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en un mecanismo plausible de clase. No hay ensayos, literatura, datos de seguridad ni indicación original documentada, por lo que la evidencia es de nivel L5.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas) para completar el cribado de seguridad.
- Obtener el mecanismo de acción desde DrugBank.
- Realizar una búsqueda bibliográfica de antihistamínicos H1 de primera generación en urticaria alérgica y por frío, para determinar si la señal es específica de doxilamina.
- Comparar la relación beneficio-riesgo (sedación, efecto anticolinérgico) frente a los antihistamínicos de segunda generación.
- Verificar la compatibilidad de vía y forma farmacéutica con la nueva indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

