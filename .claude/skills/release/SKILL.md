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

## Update version references

11. Update `README.md`: set `note = {Living document, $ARGUMENTS}` in the bibtex block
12. Update `CITATION.cff`: set `version:` to the version number without the `v` prefix

## Commit render

13. Stage rendered output and version references: `git add paper/docs/ README.md CITATION.cff`
14. Commit: `Re-render with $ARGUMENTS version string`
15. Move tag to final commit: `git tag -f $ARGUMENTS`

## Publish

16. `git checkout publish && git merge main --no-edit && git checkout main`
17. Push branches: `git push origin main publish --force-with-lease`
18. Push tag (force needed because tag was moved): `git push origin $ARGUMENTS --force`

## Verify

19. Confirm push succeeded for all three refs (main, publish, tag)
20. Report the final tagged commit hash

## If something goes wrong

- If render fails: fix the issue, re-render, do not tag until render is clean
- If tag already exists: ask the user before overwriting
- If push fails: diagnose, do not force-push without asking
- If version string is stale in rendered output: the render did not pick up the tag — re-render after confirming `git describe --tags` shows the correct version
