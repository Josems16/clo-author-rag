# Guía de Usuario — clo-author-rag

Herramienta de investigación asistida por IA para redacción de artículos científicos.
Combina un pipeline multi-agente (clo-author) con una base de conocimiento local de PDFs (RAG).

---

## Índice

1. [¿Qué es esto?](#1-qué-es-esto)
2. [Instalación](#2-instalación)
3. [Configuración inicial del proyecto](#3-configuración-inicial-del-proyecto)
4. [El motor RAG — tu biblioteca local](#4-el-motor-rag--tu-biblioteca-local)
5. [Claude Code y los agentes](#5-claude-code-y-los-agentes)
6. [Flujo de trabajo de un artículo completo](#6-flujo-de-trabajo-de-un-artículo-completo)
7. [Comandos de referencia rápida](#7-comandos-de-referencia-rápida)
8. [Preguntas frecuentes](#8-preguntas-frecuentes)

---

## 1. ¿Qué es esto?

Esta herramienta tiene dos partes que trabajan juntas:

### El motor RAG (`rag-engine/`)
RAG significa *Retrieval-Augmented Generation*. En lugar de que Claude lea tus PDFs completos cada vez (lento, caro en tokens), los indexa una sola vez en una base de datos vectorial local. Cuando haces una pregunta, Claude recupera solo los fragmentos relevantes.

**Resultado:** Claude puede responder preguntas sobre 50 papers como si los tuviera en memoria, usando una fracción de los tokens.

### El pipeline clo-author (`.claude/`)
Un conjunto de agentes especializados que guían el proceso completo de investigación:

```
Idea → Literatura → Estrategia → Análisis → Redacción → Revisión → Envío
```

Cada etapa tiene un agente que crea y un crítico que revisa. Nada avanza sin pasar el control de calidad.

---

## 2. Instalación

### Requisitos previos

| Herramienta | Para qué | Cómo instalar |
|------------|----------|---------------|
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Todo | `npm install -g @anthropic-ai/claude-code` |
| Python 3.10+ | Motor RAG | [python.org](https://www.python.org/) |
| XeLaTeX | Compilar el paper | [TeX Live](https://tug.org/texlive/) |

### Clonar y configurar

```bash
# 1. Clonar con el submodule del motor RAG incluido
git clone --recurse-submodules https://github.com/Josems16/clo-author-rag.git mi-articulo
cd mi-articulo

# 2. Instalar dependencias del RAG
pip install -r requirements.txt

# 3. Abrir Claude Code
claude
```

> **Si ya tienes el repo clonado y falta el submodule:**
> ```bash
> git submodule update --init --recursive
> ```

---

## 3. Configuración inicial del proyecto

Antes de empezar a investigar, configura dos archivos con los datos de tu proyecto.

### 3.1 `CLAUDE.md` — configuración general

Abre `CLAUDE.md` y rellena los campos marcados con corchetes:

```markdown
**Project:** [TÍTULO DE TU ARTÍCULO]
**Institution:** [TU INSTITUCIÓN]
**Field:** [TU CAMPO — ej. Ingeniería Térmica / Manufactura Aditiva]
```

Este archivo es lo primero que lee Claude al abrir una sesión. Define el contexto de todo.

### 3.2 `.claude/references/domain-profile.md` — perfil de tu campo

Este archivo le dice a Claude qué journals apuntas, qué notación usas, y cuáles son las referencias clave de tu área. Puedes rellenarlo tú manualmente o dejar que Claude te guíe:

```
/discover interview
```

Claude te hará preguntas sobre tu campo y rellenará el perfil por ti.

---

## 4. El motor RAG — tu biblioteca local

### Cómo funciona

```
Tus PDFs → watcher.py → Extracción de texto → Chunks → ChromaDB (local)
                                                              ↓
                                               Claude consulta cuando necesita
```

El índice se guarda en `rag-data/` (nunca se sube a git). En cada PC nuevo se reconstruye en minutos.

### Añadir papers de referencia

1. Copia tus PDFs a la carpeta `papers/` (desde Google Drive, USB, etc.)
2. Ejecuta el watcher:

```bash
# Opción A: indexar y quedarse escuchando (cualquier PDF nuevo se procesa solo)
python watcher.py

# Opción B: indexar una vez y salir
python watcher.py --once
```

El watcher imprime el progreso por cada PDF:
```
10:23:14 [INFO] Procesando: Smith_2022_evaporative_cooler.pdf
10:23:18 [INFO] Listo: Smith_2022_evaporative_cooler.pdf
```

### Qué extrae el RAG de cada PDF

- **Texto completo** dividido en chunks con metadatos de página
- **Tablas** (en texto, legibles para Claude)
- **Imágenes** filtradas por tamaño (figuras reales, no logos ni iconos)
- **Metadatos académicos** (título, autores, año, DOI si están disponibles)

### Cómo usar la base de conocimiento en Claude

Una vez indexados los papers, simplemente pregunta en lenguaje natural:

> *"¿Qué métodos de medición de efectividad de bulbo húmedo se usan en los papers indexados?"*

> *"Resume los valores de COP reportados en los estudios experimentales de enfriadores evaporativos indirectos."*

Claude recupera los chunks relevantes y responde con citas precisas (paper, página).

### Cuándo reconstruir el índice

- Al clonar en un PC nuevo: `python watcher.py --once`
- Al añadir nuevos PDFs: basta con copiarlos si el watcher está corriendo; si no, `--once`
- Si el índice se corrompe: borrar `rag-data/` y ejecutar `--once`

---

## 5. Claude Code y los agentes

### Abrir una sesión

```bash
cd mi-articulo
claude
```

Claude lee automáticamente `CLAUDE.md` y el perfil de dominio al iniciar.

### Los agentes y sus roles

Cada tarea tiene un agente que **crea** y un crítico que **revisa**. El crítico no puede editar archivos; el creador no puede puntuarse a sí mismo.

| Fase | Agente creador | Crítico |
|------|---------------|---------|
| Literatura | Librarian | librarian-critic |
| Datos | Explorer | explorer-critic |
| Estrategia | Strategist | strategist-critic |
| Análisis/código | Coder | coder-critic |
| Redacción | Writer | writer-critic |
| Presentación | Storyteller | storyteller-critic |
| Revisión por pares | Editor → Referees | — |

**Ningún artefacto avanza a la siguiente fase con una puntuación inferior a 80/100.**

### El orquestador

Cuando usas `/new-project`, el Orchestrator gestiona el flujo completo: activa los agentes en orden, espera las puntuaciones de los críticos, y solo avanza cuando se supera el umbral. Puedes ver el estado en cualquier momento preguntando:

> *"¿En qué fase estamos? ¿Cuál es la puntuación actual?"*

---

## 6. Flujo de trabajo de un artículo completo

### Opción A: Pipeline completo automatizado

Para proyectos nuevos donde quieres que Claude gestione todo el proceso:

```
/new-project [tema de tu investigación]
```

Claude planifica, te presenta el plan para aprobación, y luego ejecuta fase a fase.

---

### Opción B: Comandos individuales (recomendado para empezar)

Más control, más aprendizaje. Usa cada comando cuando lo necesites.

#### Paso 1 — Revisión de literatura

```
/discover literature [tu tema]
```

El Librarian busca, anota y organiza la literatura relevante. El librarian-critic revisa la cobertura y las lagunas. **Aprovecha el RAG**: si tienes papers indexados, Claude los consulta primero antes de buscar en la web.

#### Paso 2 — Estrategia de investigación

```
/strategize [tu pregunta de investigación]
```

El Strategist diseña la estrategia metodológica: diseño experimental, métricas, supuestos clave. El strategist-critic la somete a escrutinio.

#### Paso 3 — Análisis de datos

```
/analyze [nombre del dataset o descripción]
```

El Coder escribe los scripts de análisis (Python/R/Julia). El coder-critic revisa la calidad, reproducibilidad y alineación con la estrategia.

#### Paso 4 — Redacción del paper

```
/write [sección]
```

Ejemplos: `/write introduction`, `/write methodology`, `/write results`.

El Writer produce el borrador en LaTeX. El writer-critic revisa el estilo, la notación, y el cumplimiento de los estándares del campo.

#### Paso 5 — Revisión por pares simulada

```
/review --peer [nombre del journal]
```

Simula una revisión completa:
1. **Desk review** del editor — verifica novedad y decide si pasa a referees
2. **Dos referees independientes** — puntuaciones en 5 dimensiones con comentarios
3. **Decisión editorial** — Accept / Minor / Major / Reject con lista de acciones

Modos adicionales:
- `/review --stress [journal]` — referees adversariales (prueba de fuego pre-envío)
- `/review --peer --r2 [journal]` — segunda ronda con memoria de comentarios previos

#### Paso 6 — Revisión de R&R

Cuando llegan los comentarios reales del journal:

```
/revise [informe del referee]
```

Clasifica cada comentario (nuevo análisis / aclaración / desacuerdo / menor) y lo enruta al agente correspondiente. Produce la carta de respuesta.

#### Paso 7 — Preparar envío

```
/submit
```

Verifica que todo cumple los criterios: puntuación >= 95, todos los componentes >= 80, paquete de replicación completo.

---

### Sesión típica de trabajo

```bash
# 1. Arrancar (si hay PDFs nuevos)
python watcher.py --once

# 2. Abrir Claude Code
claude

# 3. Retomar donde lo dejaste
/checkpoint   ← Claude lee el estado de la sesión anterior

# 4. Trabajar
/write results

# 5. Guardar estado antes de cerrar
/checkpoint
```

---

## 7. Comandos de referencia rápida

### Investigación

| Comando | Qué hace |
|---------|----------|
| `/new-project [tema]` | Pipeline completo orquestado |
| `/discover [modo] [tema]` | Modos: `interview`, `literature`, `data`, `ideation` |
| `/strategize [modo]` | Modos: `paper`, `pre-analysis`, `theory` |
| `/analyze [dataset]` | Análisis de datos de principio a fin |
| `/write [sección]` | Borrador de sección + pase de humanización |

### Revisión

| Comando | Qué hace |
|---------|----------|
| `/review [archivo]` | Revisión de código o paper |
| `/review --peer [journal]` | Revisión por pares simulada |
| `/review --stress [journal]` | Referees adversariales |
| `/revise [informe]` | Ciclo R&R — clasifica y enruta comentarios |

### Salida

| Comando | Qué hace |
|---------|----------|
| `/talk [modo]` | Crea presentación Beamer desde el paper |
| `/submit` | Gate final: verifica y empaqueta para envío |

### Utilidades

| Comando | Qué hace |
|---------|----------|
| `/tools compile` | Compila el LaTeX |
| `/tools validate-bib` | Valida la bibliografía |
| `/tools commit` | Commit con control de calidad |
| `/tools journal [nombre]` | Consulta el perfil de un journal |
| `/checkpoint` | Guarda el estado de la sesión |

---

## 8. Preguntas frecuentes

**¿Cuántos PDFs puede manejar el RAG?**
Sin límite práctico. El índice vectorial (ChromaDB) es eficiente hasta cientos de papers. El tiempo de indexación es ~5-15 segundos por PDF.

**¿Qué pasa si cambio de PC?**
Clona con `--recurse-submodules`, copia los PDFs desde Google Drive a `papers/`, ejecuta `python watcher.py --once`. En 10-15 minutos tienes el entorno completo.

**¿Puedo usar el RAG sin el pipeline de clo-author?**
Sí. Puedes abrir Claude Code y preguntar directamente sobre tus papers sin usar ningún slash command.

**¿Los papers de `papers/` se suben a GitHub?**
No. La carpeta `papers/` está en `.gitignore`. Los PDFs se sincronizan por Google Drive (u otro almacenamiento en la nube). Solo el índice RAG regenerado localmente.

**¿Puedo añadir mis propios journals al perfil?**
Sí. Edita `.claude/references/journal-profiles.md` — hay una plantilla al final del archivo.

**¿Qué significa una puntuación de 80/100?**
Es el umbral mínimo para commitear. Para enviar al journal se exige >= 95 en el agregado y >= 80 en cada componente individual.

**¿Puedo saltar fases del pipeline?**
Sí. Si ya tienes datos y estrategia, puedes entrar directamente en `/write` o `/review`. El orquestador verifica dependencias, no secuencia obligatoria.

**¿Cómo actualizo la plantilla cuando haya nuevas versiones?**
```bash
# Actualizar solo la infraestructura (.claude/)
git pull origin main

# Actualizar el motor RAG
git submodule update --remote rag-engine
```
Tus archivos de proyecto (paper, datos, scripts) nunca se tocan.

---

*Basado en [clo-author](https://github.com/hugosantanna/clo-author) de Hugo Sant'Anna (MIT License).*
