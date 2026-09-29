---
layout: default
title: Fluocinonide
parent: Solo predicción del modelo (L5)
nav_order: 236
evidence_level: L5
indication_count: 7
---

# Fluocinonide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Fluocinonida: De Afecciones Cutáneas Inflamatorias y Pruriginosas a Alopecia Mucinosa

## Resumen en Una Frase

Fluocinonida es un glucocorticoide tópico de alta potencia, utilizado en cremas para tratar afecciones cutáneas inflamatorias y pruriginosas.
El modelo TxGNN predice que podría ser efectivo para **alopecia mucinosa**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que es solo una hipótesis del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Afecciones cutáneas inflamatorias y pruriginosas (según farmacología; el texto de la autorización de AEMPS está vacío) |
| Nueva Indicación Predicha | Alopecia mucinosa |
| Puntaje de Predicción TxGNN | 99.61% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, fluocinonida es un glucocorticoide sintético cuyo blanco farmacológico registrado es el receptor de glucocorticoides (NR3C1). Su eficacia en dermatosis inflamatorias y pruriginosas está establecida, y mecanísticamente podría ser aplicable a la alopecia mucinosa.

La alopecia mucinosa (mucinosis folicular) tiene un componente inflamatorio alrededor del folículo piloso. Por eso un corticoide tópico es mecanísticamente concebible. Esta relación se infiere de la clase del fármaco, no de datos aportados sobre fluocinonida en esta enfermedad.

El puntaje del modelo es muy alto, pero no constituye evidencia clínica. No hay ensayos ni literatura que prueben el uso de fluocinonida en esta enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Otras Predicciones del Modelo (Contexto)

Las demás indicaciones predichas también son alopecias. Solo una tiene un ensayo, y es de apoyo indirecto.

| Indicación Predicha | Puntaje | Nivel | Evidencia disponible | Recomendación |
|------|------|------|------|------|
| Telogen effluvium | 99.61% | L5 | Ninguna; vínculo mecanístico débil (alteración no inflamatoria del ciclo capilar) | Hold |
| Alopecia areata | 99.59% | L4 | Un ensayo indirecto: [NCT04207931](https://clinicaltrials.gov/study/NCT04207931), Fase 4, en reclutamiento, n=250, sobre alopecia cicatricial central centrífuga (no alopecia areata). El registro no indica si fluocinonida es un brazo de tratamiento. | Pregunta de investigación |
| Foliculitis decalvante (Quinquaud) | 99.58% | L5 | Ninguna; alopecia cicatricial inflamatoria, uso como coadyuvante plausible | Hold |
| Hipotricosis hereditaria con vesículas cutáneas recurrentes | 99.56% | L5 | Ninguna; trastorno genético sin diana inflamatoria clara | Hold |
| Alopecia con deficiencia de anticuerpos | 99.51% | L5 | Ninguna; la inmunosupresión podría ser contraproducente | Hold |
| Síndrome de alopecia, discapacidad intelectual e hipogonadismo hipergonadotrópico | 99.49% | L5 | Ninguna; etiología genética no inflamatoria | Hold |

De todas ellas, la alopecia areata es la más plausible. Es autoinmune y ataca el folículo, y los corticoides tópicos potentes son de uso habitual en ella.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 54036 | NOVOTER 0,5 MG/G CREMA | Crema | Teofarma S.R.L. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para alopecia mucinosa no hay ningún ensayo ni publicación, y la predicción se apoya solo en el puntaje del modelo (nivel L5). Para esta indicación no hay base clínica que justifique avanzar.

**Para avanzar se necesita:**
- Buscar literatura y ensayos específicos de corticoides tópicos potentes en mucinosis folicular
- Obtener el prospecto de AEMPS (advertencias y contraindicaciones), aún no incorporado
- Confirmar el mecanismo de acción en DrugBank
- Evaluar si la alopecia areata (rango 3, L4) merece priorizarse como pregunta de investigación. Habría que verificar si NCT04207931 incluye fluocinonida
- Verificar la compatibilidad de la vía (crema tópica) con la localización de la enfermedad, hoy pendiente
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

