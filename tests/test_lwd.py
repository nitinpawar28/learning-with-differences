"""Tests for the lwd generator. Run: python -m unittest discover -s tests"""

from __future__ import annotations

import shutil
import tempfile
import textwrap
import unittest
from datetime import date
from pathlib import Path

from lwd import mdscan, pipeline, yamlio

REPO = Path(__file__).resolve().parents[1]
TODAY = date(2026, 10, 24)

CONFIG = """\
[project]
site_name = "Fixture"
site_url = "https://example.org/fixture/"
exclude_docs = \"\"\"
/_data/
/_glossary/
/_study/
/_terms/
\"\"\"
not_in_nav = \"\"\"
/terms/
/glossary/browse/
/study/exams/
/study/paths/
\"\"\"
nav = [
  "index.md",
  { "Cloud" = ["cloud/azure/identity/managed-identities.md"] },
  { "Glossary" = ["glossary/index.md", "glossary/explorer.md", "glossary/a-z.md", "glossary/rosetta.md", "glossary/contrasts.md", "glossary/browse.md", "glossary/legend.md"] },
  { "Study" = ["study/index.md", "study/exams.md", "study/paths.md", "study/renewals.md", "study/reports/coverage.md", "study/reports/freshness.md", "study/reports/integrity.md", "study/reports/roadmap.md"] }
]
"""

TERMS = {
    "managed-identity": """\
        ---
        title: Managed Identity
        summary: An identity for an Azure resource whose credentials Azure creates, rotates and protects for you.
        acronyms: [MSI]
        aliases: [Managed identities for Azure resources]
        formerly:
          - { name: Managed Service Identity, acronym: MSIX }
        tracks: [security, cloud]
        domain: identity
        cloud: azure
        level: practitioner
        status: complete
        last_verified: 2026-10-01
        concept: workload-identity
        equivalents:
          - { term: iam-role, fidelity: close, note: "Both remove stored secrets; scope is assigned differently." }
        differs_from:
          - { term: workload-identity, note: "The Azure implementation versus the general idea." }
        covers: [az-104:1.1]
        sources:
          - { title: "What are managed identities?", url: "https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview", publisher: Microsoft Learn }
        ---
        ## Explanation

        A managed identity lets code running on Azure get tokens. See [the article](../cloud/azure/identity/managed-identities.md).

        ```text
        ## not a heading
        ```

        ## Examples

        Example text.

        ## Misconceptions

        - It is not a user.

        ## Exam notes

        Tested in AZ-104.

        ## Self-check

        ??? question "Does a managed identity have a password you rotate?"
            No. Azure manages the credential.
        """,
    "iam-role": """\
        ---
        title: IAM Role
        summary: An AWS identity with permissions that trusted principals assume to get temporary credentials.
        tracks: [security, cloud]
        domain: identity
        cloud: aws
        level: practitioner
        status: draft
        equivalents:
          - { term: managed-identity, fidelity: partial, note: "Roles are assumed; managed identities are attached." }
        differs_from: [workload-identity]
        ---
        ## Explanation

        Roles are assumed via STS.
        """,
    "workload-identity": """\
        ---
        title: Workload Identity
        summary: An identity issued by the platform to a running workload instead of a stored secret.
        tracks: [security]
        domain: identity
        cloud: neutral
        level: foundation
        status: draft
        differs_from:
          - { term: managed-identity, note: "General idea versus one implementation." }
        ---
        ## Explanation

        The general idea.
        """,
}

EXAM = """\
---
code: AZ-104
title: Microsoft Azure Administrator
credential: "Microsoft Certified: Azure Administrator Associate"
provider: microsoft
tracks: [cloud]
clouds: [azure]
level: associate
tier: core
stage: "2"
progress: planned
official_url: https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/
outline_version: "2026-04-17"
last_verified: 2026-10-01
objectives:
  - { id: "1", title: "Manage identities", weight: "50%" }
  - { id: "1.1", title: "Manage managed identities" }
  - { id: "1.2", title: "Manage RBAC" }
  - { id: "2", title: "Manage storage", weight: "50%" }
  - { id: "2.1", title: "Configure storage accounts" }
---
## Exam format

Facts.
"""

PATH = """\
---
title: Identity basics
summary: From workload identity to managed identities.
tracks: [security]
level: foundation
exams: [az-104]
steps:
  - term: workload-identity
  - page: cloud/azure/identity/managed-identities.md
  - objective: az-104:1.1
  - check: Explain the difference.
---
Intro.
"""

ARTICLE = """\
---
title: Managed identities in depth
description: How managed identities work.
status: draft
level: practitioner
tracks: [security, cloud]
clouds: [azure]
compares: [managed-identity, workload-identity]
covers: [az-104:1.2]
---

# Managed identities in depth

See [Managed Identity](../../../terms/managed-identity.md) and [IAM Role](../../../terms/iam-role.md#explanation).
"""


def build_fixture(root: Path) -> None:
    (root / "zensical.toml").write_text(CONFIG, encoding="utf-8")
    docs = root / "docs"
    (docs / "_data").mkdir(parents=True)
    shutil.copyfile(REPO / "docs" / "_data" / "taxonomy.yml", docs / "_data" / "taxonomy.yml")
    shutil.copyfile(REPO / "docs" / "_data" / "abbreviations.yml", docs / "_data" / "abbreviations.yml")
    (docs / "_terms").mkdir()
    for slug, text in TERMS.items():
        (docs / "_terms" / f"{slug}.md").write_text(textwrap.dedent(text), encoding="utf-8")
    (docs / "_study" / "exams").mkdir(parents=True)
    (docs / "_study" / "exams" / "az-104.md").write_text(EXAM, encoding="utf-8")
    (docs / "_study" / "paths").mkdir(parents=True)
    (docs / "_study" / "paths" / "identity-basics.md").write_text(PATH, encoding="utf-8")
    (docs / "cloud" / "azure" / "identity").mkdir(parents=True)
    (docs / "cloud" / "azure" / "identity" / "managed-identities.md").write_text(ARTICLE, encoding="utf-8")
    (docs / "index.md").write_text("---\ntitle: Home\n---\n\n# Home\n\n[Glossary](glossary/index.md)\n", encoding="utf-8")


class FixtureCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="lwd-test-"))
        build_fixture(self.tmp)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def run_pipeline(self) -> pipeline.Run:
        return pipeline.run(self.tmp, TODAY)

    def codes(self, run: pipeline.Run) -> set[str]:
        return {d.code for d in run.diags.items if d.severity == "error"}


class YamlTests(unittest.TestCase):
    def test_types_lines_and_duplicates(self) -> None:
        doc = yamlio.split("---\nlevel: 200\nid: 1.10\nflag: NO\nok: true\n---\nbody\n")
        self.assertEqual(doc.meta["level"], "200")
        self.assertEqual(doc.meta["id"], "1.10")
        self.assertEqual(doc.meta["flag"], "NO")
        self.assertIs(doc.meta["ok"], True)
        self.assertEqual(doc.meta.line_of("id"), 3)
        self.assertEqual(doc.body_line, 7)
        with self.assertRaises(yamlio.YamlError) as ctx:
            yamlio.split("---\na: 1\na: 2\n---\n")
        self.assertEqual(ctx.exception.line, 3)


class ScanTests(unittest.TestCase):
    def test_sections_ignore_fenced_headings(self) -> None:
        body = "## Explanation\n\ntext\n\n```md\n## not a heading\n```\n\n## Examples\n\nx\n"
        secs = mdscan.sections(body, 1, {"explanation": "explanation", "examples": "examples"})
        self.assertEqual([s.canonical for s in secs], ["explanation", "examples"])
        self.assertIn("## not a heading", secs[0].text)

    def test_links_wrapped_over_lines(self) -> None:
        links = mdscan.links("See [workload\nidentity](../terms/workload-identity.md) and `[x](nope.md)`.\n")
        self.assertEqual([l.target for l in links], ["../terms/workload-identity.md"])

    def test_questions(self) -> None:
        qs = mdscan.questions('??? question "Why?"\n    Because.\n\n    More.\n', 10)
        self.assertEqual(len(qs), 1)
        self.assertEqual(qs[0].question, "Why?")
        self.assertIn("More.", qs[0].answer)
        self.assertEqual(qs[0].line, 10)


class PipelineTests(FixtureCase):
    def test_clean_run_and_outputs(self) -> None:
        run = self.run_pipeline()
        errors = [d.format() for d in run.diags.items if d.severity == "error"]
        self.assertEqual(errors, [])
        out = run.outputs.docs
        for page in ("terms/managed-identity.md", "glossary/a-z.md", "glossary/rosetta.md", "study/exams/az-104.md", "study/paths/identity-basics.md"):
            self.assertIn(page, out)
        term = out["terms/managed-identity.md"]
        self.assertIn("## How it differs { #differs }", term)
        self.assertIn("## Azure ↔ AWS { #azure-aws }", term)
        self.assertIn("Partial", term)  # lower of close/partial wins
        self.assertNotIn("## not a heading {", term)

    def test_coverage_states(self) -> None:
        run = self.run_pipeline()
        cov = run.ctx["coverage"]["az-104"]
        self.assertEqual(cov.objectives["1.1"].state, "covered")   # complete term
        self.assertEqual(cov.objectives["1.2"].state, "partial")   # draft article
        self.assertEqual(cov.objectives["2.1"].state, "gap")
        self.assertAlmostEqual(cov.weighted, 0.5 * 0.5 / 1.0 * 1.0, places=3)

    def test_abbreviations_one_per_paragraph(self) -> None:
        run = self.run_pipeline()
        text = run.outputs.root["generated/includes/abbreviations.md"]
        self.assertIn("*[MSI]: Managed Identity", text)
        self.assertIn("*[MSIX]: Managed Service Identity — former name of Managed Identity", text)
        lines = text.strip().split("\n")
        self.assertTrue(all(lines[i] == "" for i in range(1, len(lines), 2)))

    def test_anki_has_stable_guids(self) -> None:
        run = self.run_pipeline()
        csv_text = run.outputs.docs["glossary/exports/anki-all.csv"]
        self.assertTrue(csv_text.startswith("#separator:Comma\n"))
        self.assertIn('"lwd-def-managed-identity"', csv_text)
        self.assertIn('"lwd-eq-managed-identity-iam-role"', csv_text)

    def test_deterministic(self) -> None:
        a = self.run_pipeline().outputs
        b = self.run_pipeline().outputs
        self.assertEqual(a.docs, b.docs)
        self.assertEqual(a.root, b.root)


class NegativeTests(FixtureCase):
    def edit(self, rel: str, old: str, new: str) -> None:
        path = self.tmp / rel
        path.write_text(path.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")

    def test_broken_link(self) -> None:
        self.edit("docs/cloud/azure/identity/managed-identities.md", "terms/iam-role.md", "terms/iam-rol.md")
        self.assertIn("LWD080", self.codes(self.run_pipeline()))

    def test_equivalent_same_cloud(self) -> None:
        self.edit("docs/_terms/iam-role.md", "cloud: aws", "cloud: azure")
        self.assertIn("LWD031", self.codes(self.run_pipeline()))

    def test_unknown_key_in_term(self) -> None:
        self.edit("docs/_terms/workload-identity.md", "level: foundation", "level: foundation\naliasses: [x]")
        self.assertIn("LWD010", self.codes(self.run_pipeline()))

    def test_reserved_slug(self) -> None:
        src = self.tmp / "docs/_terms/workload-identity.md"
        shutil.copyfile(src, self.tmp / "docs/_terms/aux.md")
        self.edit("docs/_terms/aux.md", "title: Workload Identity", "title: Aux")
        self.assertIn("LWD020", self.codes(self.run_pipeline()))

    def test_unquoted_colon(self) -> None:
        self.edit("docs/_study/exams/az-104.md", 'credential: "Microsoft Certified: Azure Administrator Associate"', "credential: Microsoft Certified: Azure Administrator Associate")
        self.assertIn("LWD001", self.codes(self.run_pipeline()))

    def test_unknown_objective(self) -> None:
        self.edit("docs/_terms/managed-identity.md", "covers: [az-104:1.1]", "covers: [az-104:9.9]")
        self.assertIn("LWD052", self.codes(self.run_pipeline()))

    def test_page_not_in_nav(self) -> None:
        (self.tmp / "docs/cloud/azure/identity/extra.md").write_text("---\ntitle: X\ndescription: Y\nlevel: foundation\ntracks: [cloud]\n---\n# X\n", encoding="utf-8")
        self.assertIn("LWD091", self.codes(self.run_pipeline()))


if __name__ == "__main__":
    unittest.main()
