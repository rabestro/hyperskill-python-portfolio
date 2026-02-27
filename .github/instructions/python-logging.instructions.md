---
applyTo: '**/*.py'
description: 'Python logging standards enforced by Ruff in evo-fraud-core'
---
# Logging Standards (Enforced by Ruff)

Follow these rules when writing or modifying Python code.
Violations will fail linting (`flake8-logging-format`, `flake8-logging`).

---

## 1. Lazy Logging (Required)

Logging MUST use lazy `%s` formatting.

Why:
- Prevents unnecessary formatting when log level is disabled
- Required by Ruff

Correct:
    logger.info("Processed frame %s in %ss", frame_id, time)

Incorrect (will fail lint):
    logger.info(f"Processed frame {frame_id}")
    logger.info("Processed frame {}".format(frame_id))

---

## 2. Logger Initialization

Each module defines its own logger.

Rules:
- Create immediately after imports
- Name it `logger`
- Use `logging.getLogger(__name__)`
- Do not import loggers from other modules

Correct:
    import logging
    logger = logging.getLogger(__name__)

---

## 3. Exception Logging

Inside `except` blocks:

- Use `logger.exception("message")`
- Do not manually append the exception object

Correct:
    except Exception:
        logger.exception("Failed to process frame")
