# AI Project Instructions

This repository is a legacy-style Python package for generating Python project
archetypes.

## Scope

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

## Shared Developer Workflow

- Follow `README.rst` as the source of truth for repository-wide development
  workflow, including environment setup, issue usage, branch naming, pull
  request structure, validation, handoff readiness, and generated artifact
  policy.
- Apply those workflow rules to AI-authored changes exactly as they apply to
  human-authored changes.
- When repository workflow policy is unclear or missing from `README.rst`, ask
  the user instead of inventing a new convention.

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
