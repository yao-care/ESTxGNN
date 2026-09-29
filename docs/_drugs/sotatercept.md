---
layout: default
title: Sotatercept
parent: Solo predicción del modelo (L5)
nav_order: 500
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: De Indicación Original No Registrada a Leucemia Linfoblástica Aguda

## Resumen en Una Frase

Sotatercept se comercializa en España con el nombre Winrevair, pero los registros de autorización disponibles no incluyen el texto de la indicación original.
El modelo TxGNN predice que podría ser efectivo para **leucemia linfoblástica aguda**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Leucemia linfoblástica aguda |
| Puntaje de Predicción TxGNN | 99.78% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Como contexto general, que no proviene de los datos suministrados y no está verificado, sotatercept se describe como una trampa de ligandos basada en el receptor de activina tipo IIA fusionado a Fc. Modula la señalización de la superfamilia del TGF-beta, que podría tener alguna relación con la regulación de la hematopoyesis.

El puntaje de 0.998 refleja únicamente la proximidad en el grafo de conocimiento de TxGNN, no un estudio real. La similitud con la indicación original tampoco se ha podido evaluar. Además, el fármaco eleva la hemoglobina y el hematocrito, por lo que su uso en una neoplasia hematológica activa requeriría una revisión de seguridad específica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1241850001 | WINREVAIR 45 MG polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No consta en el registro |
| 1241850003 | WINREVAIR 60 MG polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No consta en el registro |

Titular: Merck Sharp & Dohme B.V.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5, etapa S0), sin ensayos ni publicaciones. Además, el aumento de hemoglobina y hematocrito plantea una preocupación de seguridad en una neoplasia hematológica.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicación autorizada), ya que sin él no se puede pasar al cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda bibliográfica dirigida sobre sotatercept y leucemia linfoblástica aguda.
- Revisar la seguridad hematológica específica de esta posible indicación.

**Otras predicciones del modelo (contexto):**
- Las 10 predicciones principales son todas L5, con puntajes entre 99.34% y 99.78%.
- Las entradas de retinopatía diabética (3, incluida la catarata diabética) y las de carcinoma urotelial (4) forman grupos redundantes. Sus puntajes no son señales independientes.
- **Osteoporosis inducida por fármacos** es la única marcada como "Research Question". Tiene la justificación biológica más coherente: los inhibidores de ligandos del receptor de activina pueden afectar la remodelación ósea. Merece una búsqueda bibliográfica dirigida sobre marcadores de recambio óseo y densidad ósea antes de avanzar de etapa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

