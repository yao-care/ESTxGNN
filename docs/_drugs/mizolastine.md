---
layout: default
title: Mizolastine
parent: Solo predicción del modelo (L5)
nav_order: 361
evidence_level: L5
indication_count: 10
---

# Mizolastine
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

# Mizolastina: De Uso Antialérgico (indicación no registrada) a Porfiria Aguda Intermitente

## Resumen en Una Frase

Mizolastina es un antihistamínico que actúa sobre el receptor H1 y se comercializa en España en comprimidos de liberación modificada. El modelo TxGNN predice que podría ser efectivo para **porfiria aguda intermitente**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: solo existe la predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el registro local (el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Porfiria aguda intermitente |
| Puntaje de Predicción TxGNN | 99,76 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, mizolastina es un antihistamínico de segunda generación que se une al receptor H1 (gen *HRH1*) y se usa en medicamentos antialérgicos. No está aprobada en EE. UU.

Con los datos aportados **no se puede establecer un vínculo mecanístico** entre el bloqueo del receptor H1 y la porfiria aguda intermitente, que es un trastorno de la biosíntesis del hemo. El único respaldo es el puntaje del modelo (0,998), que es alto pero no equivale a evidencia biológica ni clínica.

Las otras nueve predicciones del listado (trastornos del movimiento, tics, déficit de carbamoil fosfato sintetasa I, entre otras) tienen puntajes entre 0,995 y 0,997. Todas están en nivel L5, sin ensayos ni literatura, y no muestran un patrón mecanístico claro.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 61658 | MIZOLEN 10 mg comprimidos de liberación modificada | Comprimido de liberación modificada | Opella Healthcare Spain S.L. |
| 61976 | ZOLISTAN 10 mg comprimidos de liberación modificada | Comprimido de liberación modificada | Sanofi Aventis S.A. |

---

## Consideraciones de Seguridad

- **Farmacología / Interacciones**: la consulta se completó con 1 registro, que corresponde a la diana farmacológica (receptor H1 humano, *HRH1*) y no a una interacción con otro fármaco. No hay interacciones clínicas documentadas.
- **Precaución específica de la indicación**: la porfiria aguda es un trastorno metabólico en el que cualquier fármaco debe evaluarse por separado para determinar si es porfirinogénico. Esto no se ha evaluado.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos, sin literatura y sin mecanismo plausible documentado. Además, la seguridad en porfiria no se ha evaluado.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción y el prospecto de la AEMPS (advertencias y contraindicaciones), para poder pasar al cribado de seguridad.
- Revisar la literatura preclínica sobre antihistamínicos H1 y la vía del hemo, para comprobar si existe un vínculo mecanístico.
- Evaluar el potencial porfirinogénico de mizolastina con bases de datos especializadas en porfiria.
- Confirmar la indicación original aprobada en España.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

