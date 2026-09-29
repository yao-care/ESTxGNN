---
layout: default
title: Norfloxacin
parent: Solo predicción del modelo (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Norfloxacin
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

# Norfloxacino: De Antibacteriano Fluoroquinolónico a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

Norfloxacino es un antibacteriano de la clase de las fluoroquinolonas, comercializado en España en comprimidos recubiertos.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hiperviscosidad policlonal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. La predicción parece un artefacto del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, norfloxacino inhibe la ADN girasa y la topoisomerasa IV bacterianas, y su uso establecido es antiinfeccioso.

El síndrome de hiperviscosidad policlonal se debe a un exceso de inmunoglobulinas en sangre. No es un proceso infeccioso, y ningún mecanismo antibacteriano actúa sobre él. La revisión del mecanismo concluye que **no hay un vínculo plausible**.

El puntaje alto (99.70%) es idéntico al de la segunda indicación predicha (hiperamilasemia), lo que refuerza la sospecha de un artefacto de los embeddings del grafo de conocimiento y no de una señal biológica real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Las autorizaciones no incluyen texto de indicación aprobada en los datos recibidos, por lo que esa columna se omite. También figura una presentación en colirio en solución.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 56901 | Norfloxacino Qualigen 400 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 62622 | Norfloxacino Sandoz 400 mg comprimidos EFG | Comprimido recubierto |
| 68627 | Norfloxacino Cinfa 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 63159 | Norfloxacino Normon 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto |
| 63202 | Norfloxacino Stada 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación para esta indicación, y no hay un mecanismo plausible que la explique. La predicción es solo del modelo (L5) y debe mantenerse en espera.

Entre las demás indicaciones predichas, dos tienen algo de literatura y nivel L4:
- **Queratoconjuntivitis epitelial punteada** (recomendación: pregunta de investigación). Requeriría una formulación oftálmica tópica. Los artículos recuperados tratan sobre microsporidios y no demuestran un efecto específico de norfloxacino.
- **Peste septicémica** (recomendación: Hold). Hay plausibilidad a nivel de clase, pero norfloxacino tiene baja biodisponibilidad oral y niveles sistémicos pobres.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS para completar advertencias y contraindicaciones (brecha bloqueante para el cribado de seguridad)
- Obtener el mecanismo de acción desde DrugBank
- Confirmar el texto de indicación aprobada de cada autorización
- Si se desea explorar alternativas, priorizar la queratoconjuntivitis epitelial punteada con una revisión específica de norfloxacino tópico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

