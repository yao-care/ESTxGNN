---
layout: default
title: Pentoxyverine
parent: Solo predicción del modelo (L5)
nav_order: 625
evidence_level: L5
indication_count: 2
---

# Pentoxyverine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Pentoxiverina: De Rinitis y Faringitis a Laringofaringitis Aguda

## Resumen en Una Frase

Pentoxiverina es un fármaco comercializado en España como solución oral (Bisolvon Calmatos), cuyas indicaciones originales en el grafo de conocimiento incluyen rinitis alérgica, rinitis vasomotora, faringitis, resfriado común, rinitis y nasofaringitis.
El modelo TxGNN predice que podría ser efectivo para **laringofaringitis aguda**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
La predicción se basa únicamente en el puntaje del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica, rinitis vasomotora, faringitis, resfriado común, rinitis y nasofaringitis (según el grafo de conocimiento; el texto de indicación de la autorización de AEMPS no está disponible) |
| Nueva Indicación Predicha | Laringofaringitis aguda |
| Puntaje de Predicción TxGNN | 99,59% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según conocimiento general (no verificado con los datos aportados), la pentoxiverina es un antitusígeno de acción central, al que se atribuyen propiedades anticolinérgicas y anestésicas locales. Mecanísticamente, el alivio sintomático de la tos en la irritación laríngea o faríngea es plausible.

La laringofaringitis aguda está muy próxima a las indicaciones ya conocidas del fármaco (faringitis, nasofaringitis, resfriado común). Por ello, es probable que la predicción sea una reexpresión de un uso ya existente y no una oportunidad de reposicionamiento realmente nueva. El puntaje elevado no constituye evidencia independiente de novedad ni de eficacia.

Una segunda predicción, "enfermedad de la cavidad nasal" (puntaje 99,57%), es una categoría amplia que se solapa con la rinitis y la nasofaringitis ya listadas. Probablemente refleja la cercanía en el grafo con esos usos conocidos, y no permite establecer un vínculo mecanístico específico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 85498 | BISOLVON CALMATOS 2,13 MG/ML SOLUCION ORAL | Solución oral | No disponible en los datos compilados |

Titular: Opella Healthcare Spain S.L. (autorización vigente, monofármaco, vía oral).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): el grafo asocia el fármaco con contraindicación en diversas enfermedades, entre ellas:
  - Cardiovasculares: hipertensión, enfermedad coronaria, infarto de miocardio, aterosclerosis, parada cardíaca súbita y enfermedad de conducción cardíaca.
  - Respiratorias: EPOC.
  - Digestivas y metabólicas: pancreatitis, úlcera péptica, diabetes mellitus, cetoacidosis diabética y acidosis metabólica.
  - Psiquiátricas: trastornos psicóticos, esquizoafectivos y esquizofreniformes.
  - Otras: glaucoma de ángulo cerrado, hipertensión ocular, hiperplasia prostática benigna, rabdomiólisis y hemoglobinopatías.
- **Interacciones farmacológicas**: se identificaron 233 interacciones; en los datos compilados las 20 primeras son de nivel moderado. Destacan:
  - Opioides y derivados: morfina, codeína, dihidrocodeína, fentanilo, alfentanilo, tramadol, opio, difenoxina y difenoxilato.
  - Depresores del sistema nervioso central: etanol, alprazolam, prometazina, clorfeniramina, fenil­toloxamina y dicloralfenazona.
  - Otros: dronabinol, nabilona, metoclopramida y sibutramina.
  
  El riesgo principal a vigilar es la sedación y depresión del sistema nervioso central aditivas.

Las advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto de AEMPS para la información de seguridad oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura que respalden la indicación predicha (nivel L5), y esta se solapa con usos ya conocidos del fármaco, por lo que no aporta novedad demostrada. Además, falta la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Confirmar el mecanismo de acción mediante DrugBank u otras fuentes.
- Definir una indicación específica con un criterio de valoración clínico (por ejemplo, un subtipo concreto en lugar de "enfermedad de la cavidad nasal").
- Realizar una búsqueda sistemática de ensayos y literatura sobre pentoxiverina en laringofaringitis aguda.
- Verificar si la indicación predicha ya está cubierta por las indicaciones autorizadas, para distinguir un uso nuevo de uno ya existente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

