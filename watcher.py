"""
Watcher de papers para clo-author-rag.

Monitoriza la carpeta papers/ y procesa automáticamente cualquier PDF nuevo
usando el motor RAG incluido en rag-engine/ (submódulo de Proyecto-RAG).
Los datos indexados se guardan en rag-data/ (excluido de git).

Uso:
    python watcher.py            # modo watcher (corre en background)
    python watcher.py --once     # procesa todos los PDFs sin watch

En nuevo PC tras git clone --recurse-submodules:
    pip install -r requirements.txt
    python watcher.py --once     # reconstruye el índice desde papers/
"""

from __future__ import annotations

import argparse
import logging
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).parent
PAPERS_DIR   = PROJECT_ROOT / "papers"
RAG_DATA_DIR = PROJECT_ROOT / "rag-data"
RAG_ENGINE   = PROJECT_ROOT / "rag-engine"   # submódulo git

if not RAG_ENGINE.exists():
    print("ERROR: rag-engine/ no encontrado.")
    print("Ejecuta: git submodule update --init --recursive")
    sys.exit(1)

# Add rag-engine to sys.path so we can import its modules
sys.path.insert(0, str(RAG_ENGINE))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Core: ingest a single PDF
# ---------------------------------------------------------------------------
def ingest(pdf_path: Path) -> None:
    try:
        from src.config import Config
        from src.ingestor import ingest_pdf

        cfg = Config(
            data_dir=RAG_DATA_DIR,
            # Reuse default config.yaml from Proyecto-RAG but override data path
        )
        # Override data directories to point inside this project
        cfg.raw_dir       = RAG_DATA_DIR / "raw"
        cfg.processed_dir = RAG_DATA_DIR / "processed"
        cfg.reports_dir   = RAG_DATA_DIR / "reports"
        cfg.index_dir     = RAG_DATA_DIR / "index"
        cfg.chroma_dir    = RAG_DATA_DIR / "chroma"
        cfg.ensure_dirs()

        logger.info("Procesando: %s", pdf_path.name)
        ingest_pdf(pdf_path, config=cfg)
        logger.info("Listo: %s", pdf_path.name)
    except Exception as exc:
        logger.error("Error procesando %s: %s", pdf_path.name, exc)


# ---------------------------------------------------------------------------
# Batch: process all PDFs in papers/
# ---------------------------------------------------------------------------
def process_all() -> None:
    pdfs = sorted(PAPERS_DIR.glob("*.pdf"))
    if not pdfs:
        logger.info("No hay PDFs en papers/")
        return
    logger.info("Procesando %d PDF(s)...", len(pdfs))
    for pdf in pdfs:
        ingest(pdf)


# ---------------------------------------------------------------------------
# Watcher: monitor papers/ for new files
# ---------------------------------------------------------------------------
def watch() -> None:
    try:
        from watchdog.events import FileSystemEventHandler
        from watchdog.observers import Observer
    except ImportError:
        logger.error("Instala watchdog: pip install watchdog")
        sys.exit(1)

    class PDFHandler(FileSystemEventHandler):
        def on_created(self, event):
            if not event.is_directory and event.src_path.endswith(".pdf"):
                time.sleep(1)  # wait for file to finish copying
                ingest(Path(event.src_path))

        def on_moved(self, event):
            if not event.is_directory and event.dest_path.endswith(".pdf"):
                time.sleep(1)
                ingest(Path(event.dest_path))

    PAPERS_DIR.mkdir(exist_ok=True)
    process_all()  # index any existing PDFs on startup

    observer = Observer()
    observer.schedule(PDFHandler(), str(PAPERS_DIR), recursive=False)
    observer.start()
    logger.info("Escuchando papers/ — Ctrl+C para parar")
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF watcher and RAG indexer for clo-author-rag")
    parser.add_argument("--once", action="store_true", help="Procesar todos los PDFs y salir")
    args = parser.parse_args()

    if args.once:
        process_all()
    else:
        watch()
