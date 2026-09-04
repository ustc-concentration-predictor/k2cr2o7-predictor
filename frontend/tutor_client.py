"""Load the deployed tutor source without reusing a stale global ``tutor`` import."""
import hashlib
import importlib.util
import inspect
import logging
from functools import lru_cache
from pathlib import Path


logger = logging.getLogger(__name__)
TUTOR_PATH = Path(__file__).resolve().parents[1] / "backend" / "tutor.py"
EXPECTED_API_VERSION = 2


@lru_cache(maxsize=2)
def _load_source(path, source):
    name = "_k2cr2o7_tutor_" + hashlib.sha256(source).hexdigest()
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None:
        raise ImportError("Tutor module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    # Execute exactly the local bytes used as the cache key. Neither sys.modules
    # nor timestamp-based .pyc caches can select an earlier deployed implementation.
    exec(compile(source, path, "exec"), module.__dict__)
    if getattr(module, "HARNESS_API_VERSION", None) != EXPECTED_API_VERSION:
        raise RuntimeError("Tutor interface version mismatch")
    return module.ask_tutor


def ask_tutor(prompt, history, mode, context, api_key, base_url, model,
              learning_context=None, language="zh"):
    try:
        tutor = _load_source(str(TUTOR_PATH), TUTOR_PATH.read_bytes())
        args = (prompt, history, mode, context, api_key, base_url, model)
        kwargs = {"learning_context": learning_context, "language": language}
        inspect.signature(tutor).bind(*args, **kwargs)
        # Never drop new arguments or fall back to a harness without scope checks.
        return tutor(*args, **kwargs)
    except Exception as exc:
        # Exception strings may contain provider data or credentials; log only type.
        logger.error("Tutor loading/invocation failed (%s)", type(exc).__name__)
        return {
            "reply": ("The assistant could not start. Please update all app files and reboot the app; if it persists, contact the maintainer."
                      if language == "en" else
                      "助手暂时无法启动。请更新完整应用文件并重启应用；若仍出现此提示，请联系维护者。"),
            "configured": bool(api_key), "model": model, "error": True,
        }
