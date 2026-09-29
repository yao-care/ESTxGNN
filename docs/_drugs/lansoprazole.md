---
layout: default
title: Lansoprazole
parent: Evidencia moderada (L3-L4)
nav_order: 304
evidence_level: L4
indication_count: 2
---

# Lansoprazole
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

# Lansoprazol: De Indicación Original No Registrada a Reflujo Duodenogástrico

## Resumen en Una Frase

Lansoprazol es un inhibidor de la bomba de protones (IBP) que reduce la secreción de ácido gástrico. Los datos recibidos no incluyen su indicación original ni su mecanismo de acción.
El modelo TxGNN predice que podría ser efectivo para **reflujo duodenogástrico**, pero actualmente hay **0 ensayos clínicos** y **2 publicaciones** relacionadas.
Una de ellas es un estudio en ratas que sugiere un riesgo, no un beneficio.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones de AEMPS están vacíos) |
| Nueva Indicación Predicha | Reflujo duodenogástrico |
| Puntaje de Predicción TxGNN | 99,69% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, lansoprazol pertenece a la clase de los inhibidores de la bomba de protones. Estos fármacos reducen el ácido gástrico y se usan de forma general en úlcera péptica, infección por *Helicobacter pylori*, enfermedad por reflujo gastroesofágico y síndrome de Zollinger-Ellison, según la revisión de Shi y Klotz (2008).

La relación con el reflujo duodenogástrico es **indirecta**. Suprimir el ácido puede aliviar el daño de la mucosa, pero no impide que la bilis y el contenido duodenal refluyan al estómago. El puntaje alto del modelo probablemente refleja la cercanía en el grafo de conocimiento entre lansoprazol y las enfermedades gástricas y duodenales relacionadas con el ácido. No indica un efecto terapéutico directo demostrado.

El único estudio específico para esta indicación apunta en sentido contrario. En ratas con reflujo duodenogástrico, lansoprazol **promovió la carcinogénesis gástrica**. Es una señal preclínica de seguridad que desaconseja este uso hasta que se aclare.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para reflujo duodenogástrico.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revisión | Eur J Clin Pharmacol | Actualización del uso clínico y la farmacocinética de los IBP. Son fármacos de primera elección en úlcera péptica, *H. pylori*, ERGE, lesiones por AINE y síndrome de Zollinger-Ellison. No trata el reflujo duodenogástrico. |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Estudio animal (rata) | Gastric Cancer | Evaluó el efecto combinado del reflujo gastroduodenal y la inhibición ácida sobre el carcinoma gástrico. Lansoprazol promovió la carcinogénesis gástrica en ratas con reflujo duodenogástrico. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 66127 | LANSOPRAZOL SANDOZ 15 mg CÁPSULAS GASTRORRESISTENTES EFG | Cápsula dura gastrorresistente |
| 67430 | LANSOPRAZOL VIR PHARMA 30 mg CÁPSULAS GASTRORRESISTENTES EFG | Cápsula dura gastrorresistente |
| 77014 | LANSOPRAZOL STADA 30 MG CÁPSULAS DURAS GASTRORRESISTENTES EFG | Cápsula dura gastrorresistente |
| 77739 | LANSOPRAZOL FLAS SALVAT 30 MG COMPRIMIDOS BUCODISPERSABLE | Comprimido bucodispersable |
| 69189 | LANSOPRAZOL VIR 30 mg CÁPSULAS DURAS GASTRORRESISTENTES EFG | Cápsula dura gastrorresistente |

---

## Consideraciones de Seguridad

- **Señal preclínica:** en un modelo de rata con reflujo duodenogástrico, lansoprazol promovió la carcinogénesis gástrica (PMID 15052437). No se ha confirmado su relevancia en humanos, pero es un motivo de cautela específico para esta indicación.

Para el resto de la información de seguridad (advertencias, contraindicaciones e interacciones), consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en un vínculo mecanístico indirecto (nivel L4). No hay ensayos clínicos, y el único estudio específico muestra una posible promoción del cáncer gástrico en ratas. También se predijo obstrucción duodenal (puntaje 99,68%), pero esa indicación tampoco tiene respaldo: es un problema mecánico o anatómico que la supresión ácida no resuelve.

**Para avanzar se necesita:**
- Obtener del prospecto de AEMPS la indicación original, las advertencias y las contraindicaciones (brecha de datos bloqueante para el cribado de seguridad).
- Completar el mecanismo de acción desde DrugBank.
- Evaluar si la señal de carcinogénesis en ratas es relevante para humanos, con revisión de estudios clínicos u observacionales de IBP en reflujo biliar o duodenogástrico.
- Buscar ensayos clínicos con lansoprazol en reflujo duodenogástrico. Hoy no hay ninguno registrado.
- Revisar la relevancia del ensayo de fase 3 NCT00175032, cuya condición no se pudo confirmar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

