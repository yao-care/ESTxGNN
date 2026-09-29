---
layout: default
title: Anagrelide
parent: Evidencia moderada (L3-L4)
nav_order: 41
evidence_level: L4
indication_count: 2
---

# Anagrelide
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Anagrelida: De Trombocitemia Esencial a Trombocitosis Reactiva

## Resumen en Una Frase

Anagrelida es un fármaco que reduce el recuento de plaquetas y se usa para tratar la trombocitemia esencial, un trastorno mieloproliferativo clonal.
El modelo TxGNN predice que podría ser efectivo para **trombocitosis reactiva**, pero **no hay ensayos clínicos** y las **10 publicaciones** recuperadas tratan de la trombocitemia esencial u otros temas, no de esta nueva indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trombocitemia esencial (según los datos de farmacología; los registros de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Trombocitosis reactiva |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Anagrelida reduce las plaquetas al inhibir la maduración de los megacariocitos, con lo que disminuye la producción plaquetaria. También se describe una inhibición de la fosfodiesterasa 3A (PDE3A). No se dispone de datos detallados de mecanismo de acción en DrugBank, así que esta descripción se basa en la literatura y en los datos de farmacología recuperados.

Mecanísticamente, un fármaco que baja la producción de plaquetas es biológicamente plausible para cualquier trombocitosis. Sin embargo, la trombocitosis reactiva es distinta de la trombocitemia esencial. La reactiva es secundaria a citoquinas (como IL-6 o TPO) por inflamación, déficit de hierro, infección o esplenectomía. Su riesgo trombótico es bajo y se maneja tratando la causa de fondo. La esencial es un trastorno clonal de la célula madre que sí requiere citorreducción.

El puntaje tan alto (0.998) probablemente refleja la cercanía en el grafo de conocimiento con la trombocitemia esencial, donde anagrelida ya está establecida, y no una eficacia demostrada en la forma reactiva. Además, existen preocupaciones de seguridad cardiovascular (por ejemplo, un reporte de infarto de miocardio en 2024) que pesan en contra de usar un citorreductor en una condición habitualmente benigna.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna de estas publicaciones evalúa la eficacia de anagrelida en trombocitosis reactiva.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Revisión | Expert Rev Anticancer Ther | Actualización de los mecanismos de acción y el potencial terapéutico de anagrelida en trombocitosis clonal; señala que la trombocitosis reactiva no requiere intervención terapéutica |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Revisión | Leuk Lymphoma | Revisión crítica de anagrelida en trombocitemia esencial y trastornos afines; la citorreducción se reserva para la trombocitosis clonal |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Revisión | Med J Aust | La trombocitemia esencial se diagnostica excluyendo otros trastornos mieloproliferativos y la trombocitosis reactiva; se recomienda tratamiento con más de 1000 x 10⁹/L plaquetas |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Revisión | Leuk Res | Papel de la trombocitaféresis en la hipertrombocitosis de neoplasias mieloproliferativas; la citorreducción médica sigue siendo la base del tratamiento |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Revisión | Rinsho Ketsueki | Diagnóstico diferencial y tratamiento de la trombocitemia esencial (busulfán, hidroxiurea, interferón alfa y anagrelida) |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Revisión | Am J Med Sci | Espectro clínico de la trombocitosis y la trombocitemia, y regulación de la producción plaquetaria por citoquinas |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Cohorte retrospectiva | Pediatr Blood Cancer | Análisis de 12 casos pediátricos de trombocitemia esencial frente a reactiva; no aporta datos de eficacia de anagrelida en la forma reactiva |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Reporte de caso | Eur J Case Rep Intern Med | Infarto agudo de miocardio en un paciente con trombocitemia esencial tratado con anagrelida |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Reporte de caso | Srp Arh Celok Lek | Trombocitemia esencial con espondilitis anquilosante tratada con anagrelida, FAME y etanercept |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Reporte de caso | Medicine | Reimplante exitoso de 2 dedos en un paciente con trombocitosis tras esplenectomía |

## Información de Mercado en España

Se muestran 5 de las 13 autorizaciones. Los registros no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 82766 | Anagrelida Pharmavic 0,5 mg cápsulas duras EFG | Cápsula dura | Pharmavic Iberica S.L. |
| 82672 | Anagrelida Teva 0,5 mg cápsulas duras EFG | Cápsula dura | Teva B.V. |
| 83063 | Anagrelida Uriach 0,5 mg cápsulas duras EFG | Cápsula dura | Grupo J Uriach S.L. |
| 83207 | Anagrelida Bluefish 0,5 mg cápsulas duras EFG | Cápsula dura | Bluefish Pharmaceuticals AB (Publ) |
| 84711 | Anagrelida Aurobindo 0,5 mg cápsulas duras EFG | Cápsula dura | Laboratorios Aurobindo S.L.U. |

## Consideraciones de Seguridad

- **Seguridad cardiovascular**: la literatura recuperada incluye un reporte de infarto agudo de miocardio en un paciente tratado con anagrelida (2024). Esto pesa en contra de su uso en una condición normalmente benigna como la trombocitosis reactiva.
- **Interacciones y dianas**: la única entrada de interacción disponible es la inhibición de la fosfodiesterasa 3A (PDE3A), que corresponde a su diana farmacológica y no a una interacción con otro fármaco.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en la cercanía con la trombocitemia esencial. No hay ensayos clínicos ni estudios que evalúen anagrelida en trombocitosis reactiva. Esta condición tiene bajo riesgo trombótico y se maneja tratando la causa, por lo que el riesgo cardiovascular de anagrelida no está justificado sin evidencia.

**Para avanzar se necesita:**
- Obtener la ficha técnica de AEMPS para revisar advertencias y contraindicaciones (bloqueante para el cribado de seguridad).
- Completar el mecanismo de acción desde DrugBank.
- Buscar evidencia directa de anagrelida en trombocitosis reactiva, o justificar un subgrupo (por ejemplo, trombocitosis extrema con riesgo trombótico demostrado).
- Evaluar la relación beneficio-riesgo cardiovascular en esta población.

La segunda predicción del modelo (síndrome de Klippel-Trenaunay inverso, puntaje 99.59%) no tiene ensayos, literatura ni vínculo mecanístico creíble con anagrelida. Queda en Hold con nivel L5.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

