---
layout: default
title: Remdesivir
parent: Solo predicción del modelo (L5)
nav_order: 462
evidence_level: L5
indication_count: 6
---

# Remdesivir
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

# Remdesivir: De COVID-19 a Neoplasia Endocrina Múltiple

## Resumen en Una Frase

Remdesivir es un análogo de nucleótido (profármaco) con actividad antiviral, comercializado en España como Veklury y utilizado en COVID-19.
El modelo TxGNN predice que podría ser efectivo para **neoplasia endocrina múltiple**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | COVID-19 (según la literatura del paquete de evidencia; el texto de indicación de la AEMPS no está disponible) |
| Nueva Indicación Predicha | Neoplasia endocrina múltiple |
| Puntaje de Predicción TxGNN | 99.50% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, remdesivir es un profármaco análogo de nucleótido que inhibe la ARN polimerasa dependiente de ARN de los virus, y su eficacia en COVID-19 está respaldada por ensayos de Fase 3 (SIMPLE, ACTT).

**Esta predicción no tiene un vínculo mecanístico identificable.** La neoplasia endocrina múltiple (MEN) es un síndrome tumoral hereditario (por ejemplo, variantes de MEN1 o RET) sin ninguna diana viral. El puntaje alto de TxGNN (0.995) proviene únicamente de la proximidad en el grafo de conocimiento, sin estudios que lo confirmen. Como falta el dato de mecanismo de acción, tampoco es posible verificar el vínculo con mayor detalle.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Otras Predicciones del Modelo

| # | Enfermedad predicha | Puntaje | Nivel | Comentario |
|---|------|------|------|------|
| 2 | Infección por VIH | 99.32% | L4 | 20 ensayos y 20 publicaciones asociados, casi todos sobre remdesivir en COVID-19 (más un estudio en supervivientes de ébola). Ninguno evalúa eficacia anti-VIH. La coincidencia parece deberse a menciones conjuntas, por ejemplo pacientes con VIH y COVID-19, o antirretrovirales como cobicistat usados junto con remdesivir. Solo un estudio farmacocinético de fase 2 (NCT04385719, 24 voluntarios sanos) se acerca al tema, y no es un ensayo de eficacia. |
| 3 | Síndrome de inmunodeficiencia adquirida felina | 99.07% | L5 | Enfermedad veterinaria; no es una indicación humana. |
| 4 | Infección por virus de inmunodeficiencia simia | 99.07% | L5 | Modelo en primates no humanos; no es una indicación humana. |
| 5 | Trastorno del neurodesarrollo con marcha atáxica, ausencia de habla y disminución de sustancia blanca cortical | 99.03% | L5 | Trastorno genético raro sin mecanismo plausible. |
| 6 | Hipercolesterolemia familiar homocigota | 99.03% | L5 | Defecto de la vía del receptor de LDL; remdesivir no tiene efecto conocido. |

Ninguna de estas predicciones cuenta con evidencia directa. Los ensayos de Fase 3 asociados a VIH son de COVID-19 y no respaldan esa indicación.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1201459001 | VEKLURY 100 MG CONCENTRADO PARA SOLUCION PARA PERFUSION | Concentrado para solución para perfusión | Gilead Sciences Ireland Unlimited Company |
| 1201459002 | VEKLURY 100 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION | Polvo para concentrado para solución para perfusión | Gilead Sciences Ireland Unlimited Company |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia endocrina múltiple es solo una puntuación del modelo (L5): no hay ensayos, literatura ni mecanismo plausible. Las demás predicciones tampoco tienen respaldo directo, incluida la de VIH, cuya evidencia asociada es en realidad de COVID-19.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada)
- Obtener los datos de mecanismo de acción desde DrugBank
- Estudios preclínicos que justifiquen un vínculo mecanístico con la neoplasia endocrina múltiple antes de considerar cualquier avance
- Revisar manualmente las coincidencias de VIH para descartar los falsos positivos por menciones conjuntas

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

