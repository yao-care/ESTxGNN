---
layout: default
title: Topiramate
parent: Solo predicción del modelo (L5)
nav_order: 535
evidence_level: L5
indication_count: 9
---

# Topiramate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Topiramato: De Epilepsia a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

Topiramato es un antiepiléptico que se usa para tratar la epilepsia y prevenir la migraña.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia y prevención de migraña (según datos farmacológicos; los registros de AEMPS del paquete no incluyen texto de indicación) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información farmacológica disponible, topiramato actúa sobre varias dianas: bloquea canales de sodio dependientes de voltaje, potencia los receptores GABA-A, antagoniza los receptores AMPA/kainato e inhibe la anhidrasa carbónica (se registran interacciones con CA1, CA4, CA7 y CA12).

Estas acciones explican su eficacia en la epilepsia, pero **no se identificó un vínculo mecanístico plausible con la biología tumoral**. El puntaje alto de TxGNN (0.997) proviene de asociaciones en un grafo de conocimiento y no está respaldado por ningún ensayo ni publicación. Un uso sintomático, por ejemplo contra el dolor neuropático asociado, sería una indicación distinta y no una acción antitumoral.

En resumen, la relación entre la indicación original (epilepsia, migraña) y la nueva (un tumor del nervio trigémino) es débil desde el punto de vista mecanístico, y esta predicción debe tratarse con cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones. Los registros no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 70753 | Topiramato Normon 25 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorios Normon S.A. |
| 69002 | Fagodol 50 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Arafarma Group S.A. |
| 69001 | Fagodol 25 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Arafarma Group S.A. |
| 69889 | Topiramato Tarbis 50 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Tarbis Farma S.L. |
| 68591 | Topiramato Stada 25 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorio Stada S.L. |

También existe la forma de cápsula dura entre las presentaciones registradas.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la base de datos registra 4 interacciones de tipo farmacológico. Son dianas de unión, no interacciones clínicas con otros medicamentos: anhidrasa carbónica 1 (CA1), anhidrasa carbónica 4 (CA4), anhidrasa carbónica 7 (CA7) y anhidrasa carbónica 12 (CA12).

Consultar el prospecto para información sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que respalde el uso de topiramato en la neoplasia del nervio trigémino, y no se identificó un vínculo mecanístico plausible. La evidencia es únicamente la predicción del modelo (L5).

**Para avanzar se necesita:**
- Estudios preclínicos que muestren un efecto de topiramato sobre este tipo de tumor
- Datos detallados del mecanismo de acción (MOA) y de las advertencias y contraindicaciones del prospecto de AEMPS
- Revisión de otras predicciones del mismo fármaco con mayor respaldo. Por ejemplo, para la **epilepsia visual** (rango 2) hay un ensayo de Fase 3 completado en epilepsia general (NCT00231556) y revisiones sistemáticas, con nivel L3 y recomendación "Research Question"
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

