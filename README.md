
# QA Playwright Demo (Python)

Manual QA 2+ года → первый шаг в автоматизацию.
Автор: ttolmacheva-qa

## Что внутри
- Playwright + pytest
- Page Object для demoqa.com
- 1 smoke-тест (легко расширить до 5)
- GitHub Actions для CI

## Репозиторий
https://github.com/ttolmacheva-qa/playwright-qa-demo

## Запуск локально
```bash
pip install -r requirements.txt
playwright install
pytest --html=report.html
```

## CI
См. .github/workflows/playwright.yml — отчет сохраняется как артефакт после каждого push
