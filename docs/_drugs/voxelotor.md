---
layout: default
title: Voxelotor
parent: Solo predicción del modelo (L5)
nav_order: 569
evidence_level: L5
indication_count: 7
---

# Voxelotor
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

# Voxelotor: De Enfermedad de Células Falciformes a Trombocitopenia Hereditaria con Plaquetas Normales

## Resumen en Una Frase

Voxelotor es un inhibidor de la polimerización de la hemoglobina S, utilizado para la enfermedad de células falciformes. Esta indicación se deduce del mecanismo descrito en el paquete de evidencia, porque el registro de AEMPS no incluye el texto de indicación.
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia hereditaria con plaquetas normales**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro de AEMPS (por mecanismo, enfermedad de células falciformes) |
| Nueva Indicación Predicha | Trombocitopenia hereditaria con plaquetas normales |
| Puntaje de Predicción TxGNN | 99.58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado (según los datos del paquete; ver nota en Conclusión) |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información del análisis de razonamiento, voxelotor inhibe la polimerización de la hemoglobina S y aumenta la afinidad de la hemoglobina por el oxígeno.

**No existe un vínculo mecanístico conocido** entre este mecanismo y la trombocitopenia hereditaria. Voxelotor no tiene acción conocida sobre la megacariopoyesis ni sobre la producción de plaquetas. El puntaje alto (99.58%) proviene solo de patrones en el grafo de conocimiento y no de evidencia biológica o clínica. La similitud con la indicación original aún no ha sido evaluada.

Las demás predicciones del modelo tienen puntajes entre 99.0% y 99.6%. Son otras alteraciones plaquetarias (macrotrombocitopenia con insuficiencia mitral, enfermedad de gránulos densos, trombocitopenia neonatal transitoria, trombocitopenia, trastorno primario de liberación plaquetaria) y el síndrome de Fanconi asociado a cadenas ligeras. Ninguna tiene vínculo mecanístico establecido ni evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1211622001 | OXBRYTA 500 mg comprimidos recubiertos con película (Pfizer Europe MA EEIG) | Comprimido recubierto con película | No especificada en los datos disponibles |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos disponibles.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos, no hay literatura y no existe un vínculo mecanístico plausible entre la inhibición de la polimerización de la HbS y la producción o función plaquetaria. Además, faltan los datos de seguridad de la ficha técnica, lo que impide pasar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS (advertencias y contraindicaciones), que es un vacío bloqueante.
- Consultar DrugBank para obtener el mecanismo de acción detallado.
- Verificar el estado regulatorio actual de Oxbryta. El paquete lo marca como comercializado, pero conviene confirmarlo en AEMPS/EMA, porque según mi conocimiento el producto fue retirado del mercado en septiembre de 2024 por preocupaciones de seguridad. Esto es una recomendación de verificación, no un dato del paquete.
- Realizar una revisión de literatura preclínica sobre megacariopoyesis y función plaquetaria antes de reconsiderar la hipótesis.

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

