---
layout: default
title: Tipranavir
parent: Solo predicción del modelo (L5)
nav_order: 530
evidence_level: L5
indication_count: 10
---

# Tipranavir
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

# Tipranavir: De Infección por VIH-1 a Infección por el Virus de la Inmunodeficiencia Simia (SIV)

## Resumen en Una Frase

Tipranavir es un inhibidor de la proteasa del VIH-1, autorizado en España en solución oral y cápsulas blandas. El texto de indicación aprobada no figura en los datos recibidos, así que la indicación original se toma del conocimiento general sobre el fármaco.
El modelo TxGNN predice que podría ser efectivo para la **infección por el virus de la inmunodeficiencia simia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los textos de autorización recibidos (infección por VIH-1, según el conocimiento general del fármaco) |
| Nueva Indicación Predicha | Infección por el virus de la inmunodeficiencia simia |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, tipranavir es un inhibidor de la proteasa del VIH-1. Su eficacia antirretroviral frente a este virus es la base de su uso clínico, y mecanísticamente podría ser aplicable a virus emparentados.

El VIH-1 y el SIV son lentivirus y sus proteasas son homólogas. Por eso existe una justificación mecanística plausible para que un inhibidor de la proteasa actúe también sobre el SIV.

Hay que interpretar el puntaje con cautela:
- El valor de 99.99% refleja la **cercanía en el grafo de conocimiento** con el VIH, no evidencia clínica.
- El SIV es una enfermedad de primates no humanos y **no es una indicación clínica en humanos**.
- Por tanto, la predicción tiene poco valor como reposicionamiento terapéutico en personas.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 05315002 | APTIVUS 100 MG/ML SOLUCIÓN ORAL | Solución oral | No especificada en los datos disponibles |
| 05315001 | APTIVUS 250 MG CÁPSULAS BLANDAS | Cápsula blanda | No especificada en los datos disponibles |

Ambas autorizaciones pertenecen a Boehringer Ingelheim International GmbH.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni literatura. Además, el SIV es una enfermedad de primates no humanos y carece de relevancia clínica humana directa.

Las otras predicciones de mayor puntaje tampoco tienen respaldo sólido:
- Las dos primeras (SIV y síndrome de inmunodeficiencia adquirida felina) son enfermedades veterinarias.
- Las predicciones de tumores benignos y trastornos del neurodesarrollo carecen de vínculo mecanístico y probablemente son artefactos del grafo.
- La hiperlipidemia combinada familiar (término obsoleto) podría reflejar una señal de efecto adverso, porque los inhibidores de proteasa suelen empeorar el perfil lipídico.
- "Congénito por VIH" tiene 9 ensayos asociados, pero los títulos visibles no confirman tipranavir como intervención.

**Para avanzar se necesita:**
- Confirmar la indicación aprobada en la ficha técnica de la AEMPS y descargar el prospecto para obtener advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Priorizar indicaciones con relevancia humana: verificar si "complejo relacionado con el SIDA" y "VIH congénito" son indicaciones ya existentes, y comprobar si los ensayos asociados incluyen realmente tipranavir y poblaciones pediátricas.
- Considerar las advertencias de hepatotoxicidad y hemorragia intracraneal en cualquier escenario pediátrico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

