# Chat Log

Active project chat log. Weekly archives are stored under `logs/<year>/W<number>.md`.

## 2026-04-28 - Codex local skills setup

- 요청: 현재 프로젝트에서만 동작하는 Codex 로컬 skills와 hooks 구조를 만들고, Python 문서화 작업을 시작점으로 삼았다.
- 결정: repo-local skill 위치는 `.agents/skills/<skill-name>/`, hook 위치는 `.agents/hooks/<hook-name>/`로 정했다.
- 변경: Python 문서화 skill을 `$fileheader`, `$function`, `$class`, `$comment`로 분리했다.
- 변경: Docker, Kubernetes, React TypeScript, SQL, GitHub Actions, project README, Python test 관련 skill을 추가했다.
- 변경: `examples/calculator.py`를 만들고 한국어 모듈 docstring, class docstring, function docstring, type hint 예시를 작성했다.
- 변경: GitHub public repo `nobrain711_custom_codex_skills`를 생성하고 `main`에 초기 내용을 push했다.
- 결정: 이후 작업은 도메인별 브랜치(`python/...`, `react/...`, `sql/...`, `skills/...` 등)와 Conventional Commits를 따른다.
- 현재 작업: `log.md`에 대화 기록을 우선 저장하고, 매주 월요일 00:00에 `logs/<year>/W<number>.md`로 회전 저장하는 `$chat-log` skill과 hook schedule을 추가한다.
