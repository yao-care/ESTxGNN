---
layout: default
title: Tropicamide
parent: Solo predicción del modelo (L5)
nav_order: 548
evidence_level: L5
indication_count: 3
---

# Tropicamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Tropicamida: De Midriasis para Exploración Oftalmológica a Síndrome de la Cola de Caballo

## Resumen en Una Frase

Tropicamida es un colirio antimuscarínico de acción corta, utilizado como midriático para facilitar la exploración del cristalino, el humor vítreo y la retina.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la cola de caballo**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Midriasis para exploración oftalmológica (según la base farmacológica; los registros de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Síndrome de la cola de caballo (cauda equina syndrome) |
| Puntaje de Predicción TxGNN | 99.53% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone del campo de mecanismo de acción (MOA) en el paquete de evidencia. Sin embargo, los datos farmacológicos indican que tropicamida se une a los receptores muscarínicos M2, M3, M4 y M5 (genes CHRM2, CHRM3, CHRM4 y CHRM5). Es decir, actúa como antagonista muscarínico tópico, con efecto midriático y cicloplégico.

La relación con el síndrome de la cola de caballo es débil. Se trata de una urgencia neurológica compresiva, cuyo tratamiento es la descompresión, generalmente quirúrgica. Un antimuscarínico solo podría, en el mejor de los casos, aliviar síntomas vesicales secundarios, y no trataría la causa. Además, tropicamida se administra en colirio y su exposición sistémica es mínima, lo que limita aún más la plausibilidad.

Por tanto, el puntaje alto de TxGNN (99.53%) debe interpretarse como una señal del modelo y no como evidencia de eficacia. Aún no se ha evaluado similitud con la indicación original ni compatibilidad de vía de administración.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 88867 | Minims Tropicamida 10 mg/ml colirio en solución en envase unidosis | Colirio en solución | Bausch + Lomb Ireland Limited |
| 57050 | Colirofta Tropicamida 10 mg/ml colirio en solución | Colirio en solución | Alcon Healthcare S.A. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Nota: los 4 registros de "interacciones" del paquete corresponden a dianas farmacológicas (receptores muscarínicos M2 a M5), no a interacciones entre medicamentos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ningún ensayo ni publicación (nivel L5). El vínculo mecanístico es débil, porque un antimuscarínico no trata la causa compresiva del síndrome y la exposición sistémica del colirio es mínima.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (advertencias y contraindicaciones), actualmente sin datos.
- Completar los datos de mecanismo de acción desde DrugBank.
- Realizar una revisión de literatura dirigida y una búsqueda de ensayos para confirmar la ausencia de evidencia.
- Evaluar viabilidad de vía de administración y farmacocinética, ya que solo existe la forma oftálmica.
- Como referencia, las otras dos predicciones del modelo (vejiga neurogénica, con término obsoleto que debe remapearse a la ontología vigente, y síndrome del intestino irritable) tienen un vínculo de clase antimuscarínica más plausible, pero también son solo predicciones (L5), sin evidencia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

