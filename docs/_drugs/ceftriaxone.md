---
layout: default
title: Ceftriaxone
parent: Solo predicción del modelo (L5)
nav_order: 159
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-31
monitor_inn: "Ceftriaxone"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "infectious otitis media", "blood group incompatibility", "suppurative otitis media", "chronic otitis media"]
description: "Ceftriaxone: nueva indicación predicha, Hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Ceftriaxone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Ceftriaxone: Hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Ceftriaxona es un antibiótico cefalosporínico de tercera generación, utilizado originalmente para infecciones bacterianas como neumonía, meningitis, gonorrea y salmonelosis.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia** (puntaje de 0,9939), pero esta predicción **no cuenta con ensayos clínicos** y solo con **3 publicaciones** de relevancia indirecta.
Entre las demás predicciones, la **otitis media infecciosa** es la mejor respaldada (1 ensayo registrado, aunque no evalúa ceftriaxona, y 18 publicaciones), por lo que se comenta como alternativa más plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0.9939 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 17) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, ceftriaxona es una cefalosporina de tercera generación con acción antibacteriana, y su eficacia en infecciones bacterianas está bien establecida.

Para la hiperamilasemia, la predicción **no es mecanísticamente plausible**. La elevación de amilasa es un hallazgo de laboratorio y no una infección. La literatura recuperada trata sobre síndrome de Weil con hemorragia digestiva, enzimas pancreáticas en hemorragia intracraneal y profilaxis tras papilosfinterotomía endoscópica; ninguna demuestra que ceftriaxona trate la hiperamilasemia. El puntaje alto del modelo es solo una predicción.

Otras predicciones del modelo siguen el mismo patrón. Las de síndrome de hiperviscosidad policlonal, analbuminemia congénita e incompatibilidad de grupo sanguíneo carecen de vínculo mecanístico. En cambio, las predicciones de **otitis media** (infecciosa, supurativa y crónica) sí son coherentes con la actividad antibacteriana del fármaco, aunque se acercan más a un uso ya conocido que a un reposicionamiento genuino.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para hiperamilasemia.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | Estudio clínico | Bratislavske lekarske listy | Profilaxis con 1 g de ceftriaxona tras papilosfinterotomía endoscópica en 30 pacientes frente a 30 controles; las bacterias biliares fueron sensibles a ceftriaxona |
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | Cohorte | Southern Medical Journal | Hiperamilasemia/hiperlipasemia de origen pancreático en 38 pacientes con hemorragia intracraneal, sin pancreatitis; no involucra ceftriaxona |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | Reporte de caso | Revista Española de Enfermedades Digestivas | Síndrome de Weil con hemorragia digestiva alta; sin relación terapéutica demostrada |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 83903 | Ceftriaxona Qilu 1 g | Polvo para solución inyectable y para perfusión | No disponible |
| 63251 | Ceftriaxona LDP Torlan 500 mg | Polvo y disolvente para solución inyectable | No disponible |
| 88920 | Ceftriaxona Kalceks 1 g | Polvo para solución inyectable y para perfusión | No disponible |
| 64950 | Ceftriaxona Sala 2 g | Polvo para solución para perfusión | No disponible |
| 62635 | Ceftriaxona Normon 1000 mg | Polvo y disolvente para solución inyectable | No disponible |

Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único).

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: enfermedad hepática, enfermedad de la vesícula biliar, ictericia neonatal, colitis por *Clostridium difficile*, enterocolitis necrotizante perinatal y anemia hemolítica.
- **Interacciones Farmacológicas** (100 registradas en total):
  - **Mayores**: cloruro de calcio, glucoheptonato de calcio y gluconato de calcio.
  - **Moderadas**: kanamicina, neomicina, estreptomicina y ácido picosulfúrico.
  - Otras interacciones, como calcitriol, epinefrina, anfotericina B y manitol, tienen nivel desconocido.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (hiperamilasemia) es solo del modelo (L5), sin ensayos ni mecanismo plausible, por lo que no justifica avanzar. La otitis media infecciosa (L3, S2) podría avanzar como "Proceed with Guardrails": hay un ensayo comparativo de ceftriaxona frente a trimetoprim-sulfametoxazol y guías con ceftriaxona intramuscular en dosis única. Sin embargo, el único ensayo registrado evalúa tubos de timpanostomía, no ceftriaxona, y no se verificó ningún ECA de Fase 3. La otitis media supurativa y la crónica quedan como preguntas de investigación (L3 y L4), con evidencia antigua, no controlada o microbiológica.

**Para avanzar se necesita:**
- Prospecto de AEMPS con advertencias, contraindicaciones e indicaciones aprobadas.
- Datos del mecanismo de acción desde DrugBank.
- Para otitis media: ECA de Fase 3 de ceftriaxona y verificación de su estatus frente a la indicación ya autorizada.
- Para otitis media: salvaguardas de uso restringido (fracaso terapéutico, vómitos o imposibilidad de vía oral) y de control de resistencias antimicrobianas.
- Separar las formas aguda y crónica de otitis media supurativa en futuros análisis.
- Descartar la hiperamilasemia, la hiperviscosidad, la analbuminemia y la incompatibilidad de grupo sanguíneo como candidatas terapéuticas, salvo nueva evidencia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

