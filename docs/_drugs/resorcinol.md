---
layout: default
title: Resorcinol
parent: Solo predicción del modelo (L5)
nav_order: 694
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Resorcinol: nueva indicación predicha, Acné queloideo (nivel de evidencia L5). Indicación original: Acné…"
monitor_inn: "resorcinol"
predicted_indications: ["acne keloid", "amyopathic dermatomyositis", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial"]
---

# Resorcinol
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

# Resorcinol: De Acné y Dermatitis a Acné Queloideo

## Resumen en Una Frase

Resorcinol es un queratolítico y antiséptico leve de uso tópico, comercializado en España como solución bucal (RESORBORINA SOLUCION) y asociado en el grafo de conocimiento a acné y dermatitis.
El modelo TxGNN predice que podría ser efectivo para **acné queloideo** (foliculitis queloidea de la nuca),
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Acné, dermatitis y dermatitis acneiforme (según el grafo de conocimiento; el texto de indicación autorizado en AEMPS no está disponible) |
| Nueva Indicación Predicha | Acné queloideo |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, resorcinol es un queratolítico tópico con efecto antiséptico leve, utilizado en acné y cuadros inflamatorios cutáneos relacionados, y mecanísticamente podría ser aplicable al acné queloideo.

El acné queloideo es una afección inflamatoria folicular crónica que se solapa con la patología del acné. El vínculo plausible sería la acción queratolítica y antiséptica sobre la obstrucción e inflamación folicular. De las seis predicciones analizadas, es la más coherente biológicamente.

Aun así, existen limitaciones importantes: la predicción se apoya solo en el modelo, no hay ensayos ni literatura, y el queloide es un proceso fibrótico dérmico sobre el que es poco probable que influya una queratólisis superficial a las bajas concentraciones de uso tópico.

Otras predicciones del modelo (dermatomiositis amiopática, dermatomiositis neonatal, enfermedad pulmonar intersticial infantil asociada a enfermedad del tejido conectivo, acrodermatitis crónica atrófica e hidroa vacciniforme familiar) carecen de vínculo mecanístico creíble y probablemente reflejan artefactos del grafo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 45563 | RESORBORINA SOLUCION (Laboratorios Ern S.A.) | Solución bucal | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): epilepsia, infección anogenital por virus del papiloma humano, verrugas comunes, enfermedad renal, piouréter, exantema, diabetes mellitus, cetoacidosis diabética, metahemoglobinemia (incluida la debida a déficit de metahemoglobina reductasa), sulfohemoglobinemia, paro cardíaco súbito, enfermedad del sistema de conducción cardíaco, déficit de G6PD, enfermedad por depósito de glucógeno, cistinuria, galactosemia, foliculitis, dermatitis seborreica, dermatitis, insuficiencia respiratoria, enfermedad vascular periférica, claudicación intermitente, enfermedad arterial periférica y déficit de piruvato deshidrogenasa E3.
- **Poblaciones de riesgo**: la absorción sistémica y la toxicidad del resorcinol tópico en lactantes (por ejemplo, metahemoglobinemia) desaconsejan cualquier uso en población neonatal.
- **Interacciones farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el mecanismo de acción no está documentado. Además, las contraindicaciones del grafo incluyen la foliculitis y la dermatitis, lo que exige cautela. El acné queloideo es la candidata más coherente, pero sigue sin respaldo empírico.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación autorizada), un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Realizar una búsqueda sistemática de literatura y registros de ensayos sobre resorcinol en acné queloideo/foliculitis queloidea.
- Evaluar la compatibilidad de vía y formulación: el producto autorizado es una solución bucal, no una formulación dérmica.
- Valorar estudios preclínicos o piloto sobre el efecto en inflamación folicular y fibrosis dérmica antes de considerar avanzar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

