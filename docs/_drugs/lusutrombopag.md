---
layout: default
title: Lusutrombopag
parent: Solo predicción del modelo (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
---

# Lusutrombopag
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

# Lusutrombopag: De Trombocitopenia en Hepatopatía Crónica a Trombocitopenia Hereditaria con Plaquetas Normales

## Resumen en Una Frase

Lusutrombopag es un agonista del receptor de trombopoyetina (TPO-R). Los datos de autorización de AEMPS no registran su indicación original, pero se conoce su uso en la trombocitopenia asociada a hepatopatía crónica.
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia hereditaria con plaquetas normales**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. La predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS (uso conocido: trombocitopenia en hepatopatía crónica antes de procedimientos invasivos) |
| Nueva Indicación Predicha | Trombocitopenia hereditaria con plaquetas normales |
| Puntaje de Predicción TxGNN | 99.995% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, lusutrombopag es un agonista del TPO-R que estimula la megacariopoyesis (la producción de plaquetas). Mecanísticamente podría aplicarse a trombocitopenias hereditarias, donde el objetivo sería aumentar el recuento plaquetario.

La razonabilidad es **plausible pero no verificada**. La etiqueta de la enfermedad es ambigua (trombocitopenia con "plaquetas normales") y la causa genética no está especificada. Por eso no se sabe si el defecto se sitúa antes de la señalización del TPO-R, lo que condiciona que el fármaco pueda actuar.

Las puntuaciones altas del modelo no equivalen a evidencia clínica. Para esta indicación no hay ensayos ni literatura que confirmen el beneficio.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 1181348001 | MULPLEO 3 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | Shionogi B.V. |

El texto de indicación aprobada no figura en los datos recibidos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5), sin ensayos ni literatura. La enfermedad está mal definida y no hay datos de seguridad locales. Las otras nueve predicciones tampoco tienen evidencia:
- Las trombocitopenias, como la macrotrombocitopenia con insuficiencia mitral y la trombocitopenia neonatal transitoria, son mecanísticamente coherentes pero tienen una relación beneficio-riesgo poco clara.
- Las enfermedades de función plaquetaria (enfermedad de gránulos densos y déficit del pool de almacenamiento) tienen un vínculo débil.
- La esclerosis lateral amiotrófica y las demás entidades neurológicas o esqueléticas no tienen vínculo mecanístico y probablemente son artefactos del grafo de conocimiento.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir con precisión la enfermedad predicha y su causa genética, para confirmar si el defecto es sensible a la señalización TPO-R.
- Hacer una búsqueda sistemática de literatura y de registros de ensayos (ClinicalTrials.gov, ICTRP) sobre trombocitopenias hereditarias.
- Evaluar el riesgo trombótico y los datos de seguridad en poblaciones especiales, incluida la pediátrica y neonatal.

*Este informe es solo para referencia de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

