---
name: release
description: Tag, render, and publish a new version of the paper
disable-model-invocation: true
argument-hint: "<version, e.g. v0.8>"
---

# Release $ARGUMENTS

Execute the full release pipeline for version $ARGUMENTS. Follow each step in order — do not skip or parallelise steps that depend on prior output.

## Pre-flight

1. Confirm on `main` branch with clean working tree (`git status`)
2. Validate `$ARGUMENTS` looks like a version tag (v0.N or v0.N.N)
3. Check that the previous tag exists and this version is newer

## Update CLAUDE.md

4. Update the Status section: version reference, publish branch version
5. Update Next steps: mark current version done, add next version target if known
6. Commit: `Update CLAUDE.md for $ARGUMENTS`

## Tag and render

7. Create tag: `git tag $ARGUMENTS`
8. Render: `quarto render paper` (from repo root)
9. Verify version string in output: `grep` for `$ARGUMENTS` in `paper/docs/integration.html`
10. If version string is wrong, diagnose — do not proceed with a stale render

## Commit render

11. Stage rendered output: `git add paper/docs/`
12. Stage any version-injected files: `git add README.md CITATION.cff` (if changed)
13. Commit: `Re-render with $ARGUMENTS version string`
14. Move tag to final commit: `git tag -f $ARGUMENTS`

## Publish

15. `git checkout publish && git merge main --no-edit && git checkout main`
16. Push: `git push origin main publish $ARGUMENTS --force-with-lease`
    - Note: `--force-with-lease` is needed because the tag was moved

## Verify

17. Confirm push succeeded for all three refs (main, publish, tag)
18. Report the final tagged commit hash

## If something goes wrong

- If render fails: fix the issue, re-render, do not tag until render is clean
- If tag already exists: ask the user before overwriting
- If push fails: diagnose, do not force-push without asking
- If version string is stale in rendered output: the render did not pick up the tag — re-render after confirming `git describe --tags` shows the correct version
