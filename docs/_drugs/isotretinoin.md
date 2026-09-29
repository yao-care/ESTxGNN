---
layout: default
title: Isotretinoin
parent: Solo predicción del modelo (L5)
nav_order: 293
evidence_level: L5
indication_count: 2
---

# Isotretinoin
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

# Isotretinoína: De Indicación Original No Registrada a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Los datos de autorización de AEMPS suministrados no incluyen el texto de indicación de la isotretinoína, por lo que no consta para qué se usa originalmente. El modelo TxGNN predice que podría ser efectiva para **hipertensión renovascular maligna**, con una puntuación alta (99,01 %). Sin embargo, actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, que es solo una hipótesis computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización suministrados |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99,01 % |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

Hay una segunda predicción, **enfermedad renal hipertensiva maligna**, con la misma puntuación (99,01 %), el mismo nivel L5 y la misma decisión Hold. Ambas enfermedades están estrechamente relacionadas y probablemente comparten vecindad en el grafo de conocimiento. Por eso no constituyen evidencia independiente.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción, y los datos suministrados tampoco incluyen indicaciones originales. Con la información disponible no se puede establecer un vínculo mecanístico entre el fármaco y la nueva indicación.

La isotretinoína es un retinoide, y la señalización de retinoides se ha estudiado en biología renal y vascular. Este dato es solo contexto general: no se aportó ningún mecanismo de respaldo y aquí no se ha verificado ninguno. La puntuación de TxGNN refleja únicamente la posición del fármaco en el grafo de conocimiento, no una demostración de eficacia.

Además, su perfil de seguridad conocido (teratogenicidad y efectos lipídicos y hepáticos) aconseja especial cautela en una enfermedad grave y de alto riesgo como la hipertensión maligna.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 67570 | ISOACNE 10 mg CÁPSULAS BLANDAS | Cápsula blanda |
| 67878 | DERCUTANE 40 mg CÁPSULAS BLANDAS | Cápsula blanda |
| 86649 | ISOTIORGA 40 MG CÁPSULAS BLANDAS | Cápsula blanda |
| 78326 | DERCUTANE 30 MG CÁPSULAS BLANDAS | Cápsula blanda |
| 82566 | ACNEMIN 10 MG CÁPSULAS BLANDAS EFG | Cápsula blanda |

Se muestran 5 de las 20 autorizaciones. El texto de indicación aprobada no está disponible en los datos suministrados, por lo que se omite esa columna.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos, sin literatura y sin mecanismo de acción verificado. Faltan además los datos de seguridad del prospecto de AEMPS, lo que impide el cribado de seguridad. El perfil de riesgo conocido del fármaco refuerza la necesidad de cautela.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), una carencia de datos bloqueante.
- Obtener el mecanismo de acción desde DrugBank (consulta a la API).
- Confirmar la indicación original aprobada de la isotretinoína a partir de la ficha técnica.
- Realizar una búsqueda dirigida de estudios preclínicos o de mecanismo sobre retinoides e hipertensión renovascular o nefropatía hipertensiva.
- Evaluar la compatibilidad de vías de administración (actualmente pendiente).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

