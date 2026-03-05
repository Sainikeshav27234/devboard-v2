# Contributing to DevBoard v2

Thank you for your interest in contributing to **DevBoard v2**! We welcome contributions from everyone. Please follow these guidelines to ensure a smooth collaboration.

---

## 1. Branch Naming Conventions

To keep the repository organized, please follow these prefixes when creating branches:

| Prefix       | Purpose                           | Example                      |
|--------------|----------------------------------|------------------------------|
| `feature/`   | New features                      | `feature/add-task`           |
| `fix/`       | Bug fixes                         | `fix/delete-task-bug`        |
| `docs/`      | Documentation updates             | `docs/update-readme`         |
| `chore/`     | Maintenance or housekeeping tasks | `chore/update-gitignore`     |

> Always branch off from `main` when starting a new task.

---

## 2. Pull Request (PR) Checklist

Before opening a PR, make sure:

- [ ] You have a **clear description** of the changes.
- [ ] You **link the related GitHub Issue** (use `Closes #<issue_number>` if applicable).
- [ ] You include a **screenshot or code snippet** showing the feature or fix in action.
- [ ] You **assign at least one reviewer** (Team Lead or QA Engineer).
- [ ] Your branch is **up-to-date with `main`** before merging.

---

## 3. Commit Message Format

Please follow these conventions to keep commit history readable:

| Type     | Description                                   | Example                                     |
|----------|-----------------------------------------------|---------------------------------------------|
| `feat:`  | Adding a new feature                          | `feat: add add_task with priority support`  |
| `fix:`   | Fixing a bug                                  | `fix: correct update_task logic`            |
| `docs:`  | Documentation updates                         | `docs: add README and contributing guidelines` |
| `chore:` | Maintenance or housekeeping tasks             | `chore: add .gitignore for Python`          |

> Use **imperative mood** (e.g., “Add feature” instead of “Added feature”).

---

## 4. Code Review Process

- All feature branches must go through a **Pull Request review**.
- **No one merges their own PR**.
- Reviewers will:
  - Leave **inline comments** for suggestions or improvements.
  - Approve the PR if it meets quality standards.
  - Request changes if necessary.
- Contributors must **respond to all review comments**, either by:
  - Making the suggested change and pushing a new commit.
  - Or explaining clearly why the change was not applied.

---

## 5. Testing

- All new features must include tests (see `test_tasks.py` as a reference).
- Run tests locally before opening a PR:

```bash
pytest test_tasks.py -v