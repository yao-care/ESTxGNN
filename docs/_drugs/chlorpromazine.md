---
layout: default
title: Chlorpromazine
parent: Solo predicción del modelo (L5)
nav_order: 122
evidence_level: L5
indication_count: 10
---

# Chlorpromazine
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

# Clorpromazina: De Esquizofrenia a Distrofia Retiniana con o sin Anomalías Extraoculares

## Resumen en Una Frase

La clorpromazina es un antipsicótico de primera generación, utilizado originalmente en el tratamiento de la esquizofrenia y la fase maníaca del trastorno bipolar.
El modelo TxGNN predice que podría ser efectiva para la **distrofia retiniana con o sin anomalías extraoculares**, pero **no hay ensayos clínicos** y las **15 publicaciones** recuperadas son de oftalmología general y no mencionan el fármaco, por lo que no respaldan la predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia (según la farmacología de referencia; los registros de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99,95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información farmacológica conocida, la clorpromazina es un antagonista de múltiples receptores: dopaminérgicos (D1 a D5), serotoninérgicos (5-HT1A, 5-HT2A, 5-HT2C, 5-HT6 y 5-HT7), adrenérgicos alfa-2 (A, B y C) e histamínico H1. También actúa sobre el canal TRPC5 y sobre los canales de cloro de tipo Maxi. Su eficacia en esquizofrenia proviene sobre todo del bloqueo dopaminérgico D2.

**No se identificó un mecanismo plausible** que vincule estos blancos con la distrofia retiniana. El puntaje de 99,95% procede únicamente de la predicción del grafo de conocimiento. La literatura recuperada trata de enfermedades orbitarias y oculares en general y no menciona la clorpromazina, así que parece una coincidencia por palabras clave del nombre de la enfermedad.

Además, la clorpromazina puede causar depósitos oculares (córnea y cristalino), y existe un informe antiguo de retinopatía por fenotiazinas. Esto apunta a **precaución más que a beneficio** en enfermedades oculares.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Las publicaciones se ordenan por cercanía al tema. Ninguna evalúa la clorpromazina como tratamiento de la distrofia retiniana.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [5647013](https://pubmed.ncbi.nlm.nih.gov/5647013/) | 1968 | No clasificado | Ophthalmologica | Retinopatía asociada a fenotiazinas (sin resumen disponible); señal de toxicidad, no de beneficio |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | No clasificado | Am J Ophthalmol | Patogenia y tratamiento de la maculopatía asociada a anomalías cavitarias del disco óptico |
| [31359131](https://pubmed.ncbi.nlm.nih.gov/31359131/) | 2019 | No clasificado | Human Genetics | Arquitectura genética de los defectos del desarrollo ocular ligados a la señalización del ácido retinoico |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | No clasificado | Int J Mol Sci | Anomalías del nervio óptico y de la retina en la fibrosis congénita de los músculos extraoculares |
| [36892533](https://pubmed.ncbi.nlm.nih.gov/36892533/) | 2023 | No clasificado | Invest Ophthalmol Vis Sci | Mutaciones de MAB21L1 y un nuevo síndrome ocular autosómico dominante (BAMD) |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Revisión | Pediatr Radiol | Diagnóstico diferencial y hallazgos de imagen de las patologías oculares pediátricas |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Revisión | Taiwan J Ophthalmol | Anomalías congénitas de la forma del cristalino |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Revisión | J Binocul Vis Ocul Motil | Oftalmoplejía y trastornos congénitos de disinervación craneal |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Cohorte | Neuroradiology | Características neurorradiológicas y clínicas de la oftalmoplejía |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Revisión | Semin Neurol | Enfoque sistemático del paciente con diplopía |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 42934 | LARGACTIL 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | Neuraxpharm Spain S.L. |
| 23665 | LARGACTIL 25 mg comprimidos recubiertos con película | Comprimido recubierto con película | Neuraxpharm Spain S.L. |
| 19622 | LARGACTIL 5 mg/ml solución inyectable | Solución inyectable | Neuraxpharm Spain S.L. |
| 23661 | LARGACTIL 40 mg/ml gotas orales en solución | Gotas orales en solución | Neuraxpharm Spain S.L. |

---

## Consideraciones de Seguridad

- **Consideración relevante para la nueva indicación**: la clorpromazina puede producir depósitos oculares en córnea y cristalino, y existe un antecedente publicado de retinopatía por fenotiazinas.
- **Interacciones Farmacológicas**: la consulta se completó, pero los 16 registros corresponden a blancos farmacológicos (receptores y canales) y no a interacciones con otros fármacos.

Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos clínicos, sin mecanismo plausible y con una literatura que no menciona el fármaco. Las señales de toxicidad ocular sugieren precaución.

**Para avanzar se necesita:**
- Completar el mecanismo de acción del fármaco (DrugBank).
- Obtener las advertencias y contraindicaciones del prospecto de AEMPS.
- Documentar la indicación autorizada, ya que los registros de AEMPS no incluyen texto de indicación.
- Buscar estudios preclínicos que respalden algún efecto en distrofias retinianas.

**Nota sobre otras predicciones:** la única predicción de la lista con respaldo clínico es la **esquizofrenia de inicio temprano** (puesto 10, puntaje 99,47%, nivel L3). Probablemente no es un reposicionamiento real, porque la esquizofrenia ya es un uso establecido del fármaco. La evidencia disponible es observacional y farmacogenética, y no hay ECA en población pediátrica. Las demás predicciones (miopías, hidranencefalia, Charcot-Marie-Tooth, entre otras) no tienen mecanismo plausible ni evidencia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

