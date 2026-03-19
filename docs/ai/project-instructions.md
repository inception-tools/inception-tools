# AI Project Instructions

This repository is a legacy-style Python package for generating Python project
archetypes.

## Scope

- Keep changes focused and incremental.
- Preserve the existing packaging approach unless the task explicitly asks for a
  modernization pass.
- Maintain compatibility with the current published constraints in
  `setup.cfg` (`python_requires >=3.6`) unless the task explicitly changes
  supported versions.

## Repository Map

- `inception_tools/`: main package implementation.
- `inception_tools/data/`: archetype templates and packaged resource files.
- `tests/unit/`: unit coverage for package modules.
- `tests/integration/`: CLI and higher-level behavior tests.
- `docs/`: Sphinx documentation.
- `.github/workflows/`: CI and release automation.
- `Makefile`: preferred developer entry points.

## Preferred Workflow

- Install development dependencies with `pipenv install --dev`.
- If the development environment has not been bootstrapped yet, prefer the
  repository's Make targets such as `make init-dev` or `make init-dev-3.8`.
- When not already operating inside the project's virtual environment, run
  repository commands through `pipenv run`.
- Run the main validation path with `make check`.
- Run formatting with `make pretty`.
- Build docs with `make docs`.
- Use `python setup.py test` only when following the existing Make targets or
  when a task specifically relies on the current legacy flow.

## Environment and Execution

- Do not assume `python`, `pip`, or other expected executables are available on
  the shell `PATH`; use the repository's documented environment setup path
  first.
- If required tooling is missing, bootstrap the project environment before
  treating validation as blocked.
- Prefer `pipenv run make check`, `pipenv run make pretty`, and similar
  commands when the shell is outside the project virtual environment.
- Ask before installing dependencies or bootstrapping the environment when the
  task did not already imply that setup work.

## Git Workflow Expectations

- Treat pull requests as the default path for all changes; do not assume direct
  pushes to protected branches are acceptable.
- Follow the repository's existing GitFlow convention from `README.rst`:
  branch feature work from `develop` and keep branch purpose narrow.
- Do not merge pull requests, rewrite shared history, or push directly to
  `develop`, `master`, or release branches unless the user explicitly asks.

## Issue, Branch, and PR Conventions

- Use GitHub Issues as the default ticket source unless the user explicitly
  directs work to another tracker.
- When an existing GitHub Issue is associated with the work, include the issue
  number in the branch name.
- Name branches using the repository's GitFlow-style prefixes and these
  formats:
  `feature/<issue-number>-<short-summary>`,
  `bugfix/<issue-number>-<short-summary>`, or
  `hotfix/<issue-number>-<short-summary>`.
- If no issue exists, use the same formats without the issue number:
  `feature/<short-summary>`, `bugfix/<short-summary>`, or
  `hotfix/<short-summary>`.
- Keep branch summaries short, lowercase, and hyphenated.
- Write commit messages in the imperative mood and include the issue number when
  practical.
- Pull requests should follow the repository PR template and include `Summary`,
  `Related Issue`, `Validation`, and `Risks / Notes` sections.
- Summarize validation by naming the commands that were run instead of pasting
  full console output unless the raw output is needed to explain a blocker.
- Use `Risks / Notes` only for material reviewer context such as validation not
  run, documentation or workflow impact, known limitations, or follow-up work.

## Validation Expectations

- Validate changes with the smallest relevant test scope during development.
- Run `make check` before considering a code change complete when practical.
- Consider work ready for human handoff only after all relevant local tests
  pass.
- Treat `make check` as the default handoff gate when it is practical to run in
  the current environment.
- If required validation cannot be run or does not pass, do not represent the
  work as complete; clearly report the failure or limitation and treat the work
  as blocked or partially complete.
- If full validation cannot be run, state what was not run and why.

## Code and Test Expectations

- Follow PEP 8 with an 88-character line length, matching the current
  `flake8` and `black` configuration.
- Keep module structure and naming consistent with the existing package.
- Prefer test-driven development for behavior changes and bug fixes: write or
  update tests before implementation when practical.
- Design classes and functions for testability, with clear boundaries and
  minimal hidden side effects.
- Add or update tests when behavior changes.
- Prefer unit tests for isolated logic and integration tests for CLI or
  end-to-end archetype generation behavior.
- If a change affects archetype output, inspect template/resource files under
  `inception_tools/data/` and verify any corresponding tests.

## Coverage Guidelines

- Use coverage as a minimum safety check, not as a substitute for thoughtful
  test design.
- Maintain at least 80% overall test coverage.
- Aim for strong coverage of changed code, edge cases, and failure paths.
- Prioritize meaningful unit coverage for core logic and integration coverage
  for CLI and archetype-generation workflows.
- Do not chase coverage percentages at the expense of useful assertions or
  clear test intent.

## Change Scope

- Keep changes narrowly scoped to the requested task.
- Avoid unrelated refactors or opportunistic modernization.
- Preserve existing CLI behavior and public interfaces unless the task
  explicitly requires a breaking change.
- Separate the requested change from optional cleanup; ask before expanding
  scope beyond what the task requires.

## Legacy Repository Conventions

- Prefer the repository's existing tooling and structure over introducing new
  packaging, dependency, or project layout conventions.
- Do not add `pyproject.toml`, Poetry, or a `src/` layout unless explicitly
  requested.

## Regression Expectations

- For bug fixes, add a regression test that would fail before the fix.
- For CLI or archetype-output changes, verify externally visible behavior, not
  only internal implementation details.

## Change Guidelines

- Do not rewrite the repository to a new packaging tool or project layout unless
  explicitly requested.
- Avoid introducing new runtime dependencies without a clear need.
- Prefer Make targets and existing project conventions over ad hoc commands.
- Keep documentation in sync when user-facing CLI behavior or project structure
  changes.
- Do not commit generated artifacts such as build outputs, packaged
  distributions, or documentation build products unless the task explicitly
  requires them.

## Repository State Awareness

- Inspect the current worktree before editing or committing so you understand
  whether unrelated user changes are already present.
- Do not modify, stage, or revert unrelated changes you did not make unless the
  user explicitly asks.

## Approval Boundaries

- Request human approval before adding or upgrading dependencies, changing CI or
  release workflows, modifying generated templates broadly, or making breaking
  changes to public interfaces.
- Request human approval before creating issues or pull requests that were not
  explicitly requested.
- Request human approval before pushing branches, merging pull requests,
  rewriting history, or using destructive git operations such as branch
  deletion or force-pushes.
- Request human approval before making changes that imply a version bump or
  alter release behavior.
- When repository policy is unclear, ask for direction instead of inventing a
  new convention.

## Human Guidance Triggers

- Request human guidance when task requirements are ambiguous, incomplete, or
  conflicting.
- Request human guidance when multiple reasonable implementation options exist
  and the tradeoffs materially affect scope, behavior, or maintenance.
- Request human guidance before changing public behavior, APIs, generated
  project structure, CI, release flow, or dependency policy unless the task
  clearly calls for it.
- Request human guidance when you encounter unexpected local changes, unrelated
  failing tests, or repository state that may affect the requested work.
- Request human guidance when a required issue, branch name, reviewer, or
  approval path is unclear.
- Request human guidance before creating a new GitHub Issue unless the user has
  asked for one or it is clear that no suitable existing issue applies.
- Request human guidance when required validation cannot be completed
  successfully.

## Handoff Expectations

- End each completed task with a concise handoff summary that states what
  changed, what validation ran, what validation did not run, and any remaining
  risks, follow-ups, or decisions needing human input.
- Do not describe work as ready for review or handoff unless the branch is in a
  reviewable state and the required validation has passed or any remaining
  blockers have been clearly disclosed.

## Documentation Expectations

- Update `README.rst` or relevant files under `docs/` when user-facing
  behavior, workflows, or generated project structure changes.
