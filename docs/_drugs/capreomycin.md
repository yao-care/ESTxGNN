---
layout: default
title: Capreomycin
parent: Solo predicción del modelo (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Capreomycin: nueva indicación predicha, Gota (nivel de evidencia L5). Indicación original: Tuberculosis pulmonar (según el grafo de conocimiento"
monitor_inn: "capreomycin"
predicted_indications: ["gout", "rheumatoid arthritis", "osteoarthritis", "osteoarthritis susceptibility", "sclerosing cholangitis", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "meningococcal infection", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type"]
---

# Capreomycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Capreomicina: De Tuberculosis Pulmonar a Gota
{: .text-alpha }

## Resumen en Una Frase

Capreomicina es un antibiótico inyectable de segunda línea, originalmente utilizado para el tratamiento de la tuberculosis pulmonar.
El modelo TxGNN predice que podría ser efectivo para **gota**, pero actualmente no hay **ningún ensayo clínico** ni **publicación** que respalde esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tuberculosis pulmonar (según el grafo de conocimiento; el texto de indicación de la autorización de AEMPS está vacío) |
| Nueva Indicación Predicha | Gota |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la capreomicina es un antibiótico peptídico cíclico de tipo aminoglucósido que inhibe la síntesis de proteínas bacterianas, y su utilidad en la tuberculosis (como fármaco de segunda línea) está establecida.

Sin embargo, no se identifica un vínculo mecanístico plausible con la gota. Nada en su mecanismo antibacteriano aborda el metabolismo del urato ni la inflamación gotosa. El puntaje alto (0.999) refleja únicamente una predicción del grafo de conocimiento, no una relación fármaco-diana demostrada.

Además, su conocida nefrotoxicidad y ototoxicidad serían un inconveniente en una población con frecuente deterioro renal, y existen alternativas establecidas y más seguras para la gota.

### Otras indicaciones predichas (todas sin evidencia clínica)

| Posición | Indicación | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|------|
| 2 | Artritis reumatoide | 99.85% | L5 | Sin mecanismo que lo respalde; existen FAME y biológicos más seguros |
| 3 | Osteoartritis | 99.74% | L5 | Sin vínculo plausible; perfil de toxicidad y vía parenteral desfavorables para una enfermedad crónica |
| 4 | Susceptibilidad a osteoartritis | 99.74% | L5 | Anotación genética, no una condición tratable; probable artefacto del grafo |
| 5 | Colangitis esclerosante | 99.65% | L5 | Hipótesis meramente especulativa; mala biodisponibilidad oral y nefrotoxicidad |
| 6 | Síndrome de braquidactilia-sindactilia | 99.63% | L5 | Malformación congénita; sin respaldo |
| 7 | Síndrome de microftalmia colobomatosa-displasia rizomélica | 99.63% | L5 | Trastorno ultrarraro; sin respaldo |
| 8 | Infección meningocócica | 99.57% | L4 | Único caso con racionalidad débil (antibacteriano), pero sin actividad demostrada frente a *Neisseria meningitidis* y con existencia de tratamientos de primera línea eficaces |
| 9 | Pseudoacondroplasia | 99.53% | L5 | Displasia esquelética genética; sin acción conocida |
| 10 | Displasia acromesomélica tipo Hunter-Thompson | 99.52% | L5 | Displasia genética; sin vínculo farmacológico plausible |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 45261 | CAPASTAT 1 G POLVO PARA SOLUCIÓN INYECTABLE (Vianex S.A.) | Polvo para solución inyectable | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad renal, piureter, enfermedad hepática, enfermedad de la vesícula biliar, déficit de potasio, pérdida de audición y sordera mixta ligada al X con gusher perilinfático.
- **Interacciones farmacológicas**: se identificaron 58 interacciones en total. Entre las 20 mostradas, las de mayor gravedad son:
  - **Mayor**: kanamicina, neomicina (riesgo aditivo de toxicidad, especialmente renal y auditiva).
  - **Moderada**: anfotericina B (y sus formulaciones lipídicas), corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, beclometasona), inhibidores de la bomba de protones (omeprazol, esomeprazol, lansoprazol, rabeprazol, dexlansoprazol), mesalazina, balsalazida, olsalazina y exenatida.
- Para advertencias y contraindicaciones del prospecto, consultar el prospecto de AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las indicaciones predichas se sustentan solo en el modelo (nivel L5; la infección meningocócica en L4 por razonamiento indirecto de clase antibacteriana), sin ensayos clínicos ni literatura. La falta de mecanismo plausible, junto con la nefrotoxicidad y ototoxicidad conocidas y la administración parenteral, hace desfavorable el balance beneficio-riesgo para la gota.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), actualmente un vacío de datos bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, consultando DrugBank).
- Realizar una revisión sistemática de literatura y estudios preclínicos que justifiquen un vínculo biológico con la gota u otra indicación predicha.
- Evaluar la compatibilidad de vía de administración y la similitud con la indicación original, hoy pendientes.
- Si se prioriza una segunda indicación, valorar la infección meningocócica solo como hipótesis exploratoria, comparándola con los tratamientos de primera línea.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

