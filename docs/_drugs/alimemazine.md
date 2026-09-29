---
layout: default
title: Alimemazine
parent: Solo predicción del modelo (L5)
nav_order: 28
evidence_level: L5
indication_count: 6
---

# Alimemazine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Alimemazina: De Prurito Alérgico y Cinetosis a Urticaria Alérgica

## Resumen en Una Frase

Alimemazina (trimeprazina) es un antihistamínico H1 de la familia de las fenotiazinas. Según la farmacología de referencia, se usa para el prurito alérgico y la cinetosis (mareo por movimiento). El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS (el texto de indicación está vacío). Según farmacología (IUPHAR): prurito alérgico y cinetosis |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, alimemazina es una fenotiazina con actividad antihistamínica H1. Su uso en cuadros alérgicos pruriginosos es conocido, y mecanísticamente podría ser aplicable a la urticaria alérgica. Un estudio en cerebro bovino describe efectos antihistamínicos y antimuscarínicos (Ki de 38 nM para la unión muscarínica). No se encontraron datos públicos de afinidad en el objetivo humano, por lo que el mecanismo no está confirmado en humanos.

La urticaria alérgica está mediada por la liberación de histamina en los mastocitos, que produce ronchas y picor. El bloqueo del receptor H1 actúa directamente sobre ese mecanismo, por lo que el vínculo biológico es plausible.

Esta predicción podría solaparse con un uso ya autorizado. Como el campo de indicaciones originales está vacío, el conjunto de datos no lo refleja. Conviene verificarlo en la ficha técnica antes de considerarla un verdadero reposicionamiento.

### Otras predicciones del modelo

| Indicación Predicha | Puntaje TxGNN | Nivel | Valoración |
|------|------|------|------|
| Urticaria por frío | 99.96% | L5 | Plausible: los antihistamínicos H1 son tratamiento de primera línea, pero sin evidencia específica de alimemazina |
| Recalcitrant atopic dermatitis (dermatitis atópica refractaria) | 99.59% | L5 | Posible alivio sintomático del picor y del sueño; la histamina influye poco en la enfermedad de fondo |
| Respuesta IgE atópica | 99.60% | L5 | Vínculo débil: es un fenotipo inmunológico, no una enfermedad tratable (Hold) |
| Enfermedad de la cavidad nasal | 99.60% | L5 | Término demasiado amplio; habría que concretar el subtipo (Hold) |
| Laringofaringitis aguda | 99.54% | L5 | Sin justificación clara; el efecto anticolinérgico secante podría empeorar los síntomas (Hold) |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 40002 | VARIARGIL 40MG/ML GOTAS ORALES EN SOLUCIÓN (Laboratorios Farmacéuticos Logogen S.A.) | Gotas orales en solución | No especificada en los datos |

La única vía disponible es la oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Por su perfil antimuscarínico, cabe esperar un efecto anticolinérgico (sequedad de mucosas). Esto debe evaluarse antes de proponer usos en patología de vías respiratorias altas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es biológicamente plausible y el puntaje del modelo es muy alto, pero no hay ensayos ni literatura (nivel L5). Además, falta la información de la ficha técnica, por lo que no se puede descartar que la indicación ya esté autorizada.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS (advertencias, contraindicaciones e indicaciones autorizadas) para confirmar si la urticaria ya está cubierta.
- Completar el mecanismo de acción desde DrugBank y datos de afinidad en el receptor H1 humano.
- Hacer una búsqueda dirigida de literatura y ensayos sobre alimemazina/trimeprazina en urticaria (aguda, crónica y por frío).
- Concretar las indicaciones amplias (cavidad nasal) o poco plausibles (IgE atópica, laringofaringitis) antes de plantearlas como preguntas de investigación.

*Los resultados son solo para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

