# Python Project Guidelines

## Python Commands

```bash
# Virtual environment (using UV - preferred)
pip install uv
uv venv
uv sync

# Or using standard venv
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
pip install -r requirements.txt

# Run tests
pytest tests/
pytest tests/ -v                  # Verbose
pytest tests/ -k "test_name"      # Run specific test

# Linting and formatting (using ruff - preferred)
ruff check src/
ruff format src/

# Or using traditional tools
black src/
isort src/
flake8 src/
mypy src/

# Type checking
mypy src/
```

## Python Standards

### Project Structure

```
project/
├── src/
│   └── package_name/
│       ├── __init__.py
│       └── ...
├── tests/
│   ├── __init__.py
│   └── ...
├── pyproject.toml
├── requirements.txt (or uv.lock)
└── CLAUDE.md
```

### Code Style

- Follow PEP 8 style guidelines
- Use type hints for function signatures
- Prefer `pathlib.Path` over `os.path`
- Use f-strings for string formatting
- Use context managers (`with` statements) for resource handling

### Dependencies

- Pin dependency versions in `requirements.txt` or `pyproject.toml`
- Use virtual environments for isolation
- Prefer UV for faster dependency resolution

### Testing

- Use pytest as the test framework
- Name test files `test_*.py` or `*_test.py`
- Name test functions `test_*`
- Use fixtures for reusable test setup
- Aim for meaningful test coverage, not 100%

### Type Hints

```python
def process_data(items: list[str], limit: int = 10) -> dict[str, int]:
    """Process items and return counts."""
    ...
```

### Imports

- Group imports: standard library, third-party, local
- Use absolute imports over relative imports
- Avoid `from module import *`

### Error Handling

```python
# Prefer specific exceptions
try:
    result = process(data)
except ValueError as e:
    logger.error(f"Invalid data: {e}")
    raise
except KeyError as e:
    logger.error(f"Missing key: {e}")
    return default_value
```

### Logging

- Use the `logging` module, not `print()` for production code
- Use appropriate log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Include context in log messages

### Pydantic Models (when applicable)

- Use Pydantic for data validation and settings
- Define clear model schemas with field descriptions
- Use validators for complex validation logic

### Async Code (when applicable)

- Use `async`/`await` consistently
- Prefer `asyncio.gather()` for concurrent operations
- Handle cancellation gracefully
