---
layout: default
title: Methotrexate
parent: Solo predicción del modelo (L5)
nav_order: 347
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Metotrexato: De Uso Antineoplásico y Antirreumático a Blastoma Pulmonar

## Resumen en Una Frase

El metotrexato es un antifolato (agente antineoplásico e inmunosupresor) que se utiliza en leucemia linfoblástica aguda, otros tumores y enfermedades autoinmunes como la artritis reumatoide y la psoriasis grave.
El modelo TxGNN predice que podría ser efectivo para el **blastoma pulmonar**, con una puntuación muy alta (99,45 %).
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que es solo una hipótesis del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones de AEMPS (texto de indicación vacío). Según la base farmacológica: leucemia linfoblástica aguda, linfoma no Hodgkin, cáncer de mama, pulmón y cabeza y cuello, artritis reumatoide y psoriasis grave |
| Nueva Indicación Predicha | Blastoma pulmonar |
| Puntaje de Predicción TxGNN | 99,45 % |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. La base farmacológica sí indica que el metotrexato actúa sobre la **dihidrofolato reductasa (DHFR)**. También interactúa con el transportador de folato reducido 1 (SLC19A1) y con HMGB1. La inhibición de la DHFR frena la síntesis de nucleótidos y, con ello, la proliferación de células que se dividen rápidamente.

El metotrexato ya se usa contra varios tumores, entre ellos el cáncer de pulmón según la fuente farmacológica. Por eso es plausible que un modelo de grafo de conocimiento lo relacione con una neoplasia pulmonar. Sin embargo, no se recuperó ningún ensayo ni publicación sobre blastoma pulmonar, así que no hay una relación mecanística demostrada con esta enfermedad. Cualquier razonamiento basado en DHFR o antifolatos procede de farmacología general, no de este conjunto de datos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 80860 | METHOFILL 7,5 MG/0,15 ML solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada |
| 79558 | IMETH 25 MG/1 ML solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada |
| 85365 | METOTREXATO MEDAC 20 MG/0,40 ML solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada |
| 79126 | QUINUX 10 MG/0,4 ML solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada |
| 85363 | METOTREXATO MEDAC 15 MG/0,30 ML solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada |

Estas son 5 de las 20 autorizaciones. El texto de indicación aprobada no figura en los datos recibidos. En el conjunto de las autorizaciones también constan solución inyectable en pluma precargada, comprimidos y solución inyectable.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito/antifolato, inhibidor de DHFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto; aplicar las normas de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Dianas farmacológicas (no son interacciones clínicas entre fármacos):** DHFR, transportador de folato reducido 1 (SLC19A1) y HMGB1. El paquete de evidencia no incluye interacciones medicamentosas clínicas.
- **Toxicidad pulmonar:** la literatura recuperada para otra indicación describe lesión pulmonar inducida por metotrexato, con un estudio preclínico reciente (PMID 42185699). Esto es especialmente relevante al valorar el fármaco en una enfermedad pulmonar.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción (99,45 %) no tiene ningún ensayo clínico ni publicación que la respalde (nivel L5). Además, no se dispone del texto de indicaciones ni de las advertencias de AEMPS.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS para obtener indicaciones, advertencias y contraindicaciones.
- Confirmar el mecanismo de acción en DrugBank.
- Realizar una revisión de literatura específica sobre blastoma pulmonar (una neoplasia muy rara).
- Valorar la toxicidad pulmonar del metotrexato en pacientes con enfermedad pulmonar.
- Como alternativa, priorizar otras predicciones del mismo fármaco con más evidencia en el paquete:
  - Hodgkin (L3).
  - Rabdomiosarcoma (L3).
  - Linfoma pulmonar primario (L4).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

