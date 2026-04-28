# nobrain711 custom Codex skills

## 한국어

이 저장소는 프로젝트 로컬 Codex skill, hook, 작업 지침을 관리하기 위한 개인용 skill 모음입니다. Python 문서화, 테스트, Docker, Kubernetes, React TypeScript, SQL, GitHub Actions, README 작성, 채팅 로그 관리 워크플로우를 포함합니다.

### Skills

- `$fileheader`: Python 파일 상단 모듈 docstring 작성
- `$function`: Python 함수/메서드 docstring 및 type hint 작성
- `$class`: Python 클래스 문서화와 클래스 수준 type 문서화
- `$comment`: 한국어 Python 주석 작성
- `$chat-log`: 프로젝트 채팅 로그와 주간 아카이브 관리
- `$docker`: Dockerfile, compose, 컨테이너 워크플로우
- `$github-actions`: GitHub Actions workflow 파일
- `$k8s`: Kubernetes manifest와 배포 워크플로우
- `$project-readme`: 프로젝트 README 생성 및 개선
- `$python-test`: pytest 또는 unittest 기반 Python 테스트
- `$react-ts`: React TypeScript 작업
- `$sql`: SQL 쿼리, migration, schema 작업

### 구조

- `AGENTS.md`: 프로젝트 로컬 Codex 지침
- `.agents/skills/`: 프로젝트 로컬 skills
- `.agents/hooks/`: 프로젝트 로컬 hooks
- `examples/`: skill 검증용 작은 예제

### 로그 정책

- 활성 대화 로그는 로컬 `log.md`에 저장합니다.
- 주간 아카이브는 로컬 `logs/<year>/W<number>.md`에 저장합니다.
- `log.md`와 `logs/`는 개인 작업 기록이므로 Git에 커밋하지 않습니다.

## English

This repository contains personal project-local Codex skills, hooks, and workflow instructions. It covers Python documentation, testing, Docker, Kubernetes, React TypeScript, SQL, GitHub Actions, README writing, and chat-log maintenance workflows.

### Skills

- `$fileheader`: Python module docstrings
- `$function`: Python function/method docstrings and type hints
- `$class`: Python class documentation and class-level type documentation
- `$comment`: Korean Python comments
- `$chat-log`: project chat logs and weekly archives
- `$docker`: Dockerfiles, compose files, and container workflows
- `$github-actions`: GitHub Actions workflow files
- `$k8s`: Kubernetes manifests and deployment workflows
- `$project-readme`: project README creation and updates
- `$python-test`: Python tests with pytest or unittest
- `$react-ts`: React TypeScript work
- `$sql`: SQL queries, migrations, and schema work

### Layout

- `AGENTS.md`: project-local Codex instructions
- `.agents/skills/`: project-local skills
- `.agents/hooks/`: project-local hooks
- `examples/`: small examples for testing skills

### Log Policy

- The active chat log is stored locally in `log.md`.
- Weekly archives are stored locally under `logs/<year>/W<number>.md`.
- `log.md` and `logs/` are personal work history files and should not be committed.
