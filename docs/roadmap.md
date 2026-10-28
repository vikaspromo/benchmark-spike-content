# Roadmap

This document records the plan and progress for operator-authorized work. It does not establish product requirements or authorize later implementation work. [Product](product.md) defines the purpose and scope; [Architecture](architecture.md#article-production-flow) defines the article production flow.

Saved checkpoints: **Batch 1**, designated successful by Vikas after positive feedback from Alex and Peter, is preserved at Git tag `batch-1-successful`. **Batch 1A**, the operator-accepted local consistency retest after the governing-document migration, is preserved at `batch-1a` and will not be delivered to Alex. The [article index](../articles/README.md) links both batches and their records. Separate evaluator work remains on hold.

## Review Batch 2 Language Feedback

**Status:** Vikas authorized fresh production and replacement of all four Batch 2 articles on October 28, 2026. Use the common committed agent version `7a21f9152b177506c3c44e2f8a5a12b264b66112`, which includes the approved Opening and FAQ question-framing changes. SEO 03 becomes v010; SEO 04, SEO 10 and AEO 15 become v002. Retain the earlier local versions and keep Batch 1 unchanged.

**In progress:** Research, write and verify each article in a fresh context under [Architecture](architecture.md#article-production-flow). Retain the new article and support-and-check record in its version subfolder within [Batch 2](../articles/batch-2-2026-10-28/README.md). Replace the existing customer Docs only after the new articles pass local checks; preserve their URLs, folder and access settings, and any newer reviewer work. Update filenames, the agent-version prefaces and the existing review-index rows; retain the gray divider between batches. No sharing notification emails are needed.

**Outstanding verification:** Establish the new Opening and FAQ requirements on the exact resulting articles, repeat the full local checks, and verify native Doc preservation, presentation, comments, access and review-index entries under [Engineering](engineering.md#customer-delivery-verification). Alex's positive assessment of Batch 1 remains the quality reference; agent checks do not establish acceptance of the replacements.

**Next action:** Complete the four local packages, perform guarded native replacement and verify delivery. Record remaining failures or required information explicitly. Customer review and acceptance follow [User Design](userdesign.md#review-revision-and-writing-feedback).

## Goal 3: Assess Client Dossiers and Test Resolution with Peter

**Status and sequence:** Vikas selected this goal on October 28, 2026, for work after the Batch 2 rerun. This entry captures the intended work and its decisions for discussion. Governing-document changes and implementation remain pending the consolidated proposal and approval required by [AGENTS](../AGENTS.md#review-and-approve-the-change). Batch 2 continues under its existing production instructions.

**Context supplied by Vikas:** Benchmark calls its internal account team's summary of an account a dossier. Peter owns dossiers for the company. There is one dossier per client, intended to be a Google Doc, with no dependable template. A dossier can contain both public information and internal client information unavailable on the public web. Vikas has received one dossier from Peter: [DC Derm Docs](https://docs.google.com/document/d/1-ec5aLWUHk7vDz4w23-iHSBMLdr9bG5Q/edit).

**Stage 1 — Dossier index:** Add a tab named **Dossiers** to the existing [review spreadsheet](https://docs.google.com/spreadsheets/d/19pXjqiOHhgViaEOoUtpAzk22LcQqLMmfHFLVjaxbq8Y/edit), with columns **Client** and **Dossier**. Start with DC Derm Docs and its supplied link; add more client links as Vikas receives them from Peter. Keep one row per client and preserve the article review tab. Before the pilot, verify the supplied file's format and comment behavior: Drive currently identifies it as a `.docx` opened in Google Docs. Resolve any conversion need while preserving Peter's authoritative document and access.

**Stage 2 — One-client assessment and resolution pilot:** Develop and test a process using the DC Derm Docs dossier. Reuse the source discovery, practice investigation and conflict checks in [Architecture](architecture.md#understand-the-practice), [Data Model's evidence distinctions](data-model.md#article-research-material) and [Engineering's factual-support checks](engineering.md#factual-support). The proposed investigation starts from the client's actual dossier content rather than an article assignment or assumed dossier layout. Assess useful client detail, support, uncertainty and conflicts; do not treat an internal fact as wrong merely because it is absent from the website. Check public sources where they can answer the question, retaining the exact dossier passage and source evidence needed to assess each discrepancy.

The intended output is a comment in the dossier for each supported discrepancy that needs Peter's attention. Use natural language that sounds like Vikas, explain what we found and where, identify the relevant dossier wording, and include a direct source link Peter can visit. Avoid citation-style comments or claims that either source is automatically authoritative. Peter should be able to update an outdated dossier and resolve the comment, or reply that the public source is outdated and instruct us to use the dossier. Leave unresolved disagreements explicit. Check the resulting document and reply when establishing what was resolved; a closed comment alone does not explain which information is current.

**Pilot completion evidence:** Verify the index row and link, the exact dossier content assessed, the evidence and posted comments, and whether Peter can use the correction-or-reply process. Report dossier quality, unresolved questions and the evidence from Peter's actual responses. Preparing comments alone does not establish that the resolution workflow works. This pilot does not establish the quality of dossiers for other clients.

**Future article use — blocked:** The longer-term intent is to combine dossiers with our own research as client-specific input to article writing. Do not use dossiers to write or revise article batches yet. That work depends on assessing dossier quality, demonstrating the resolution workflow with Peter, and Vikas's decision to proceed under approved governing requirements.

**Next action and dependencies:** Discuss the smallest reuse of current research capabilities for this pilot, then prepare the exact consolidated governing-document proposal. Address the supported dossier-review operation and Peter's role in User Design; the research and resolution flow in Architecture; source identity, internal information, uncertainty and resolution evidence in Data Model; verification in Engineering; and Product scope plus Writing Standards' source rules where affected. Current article rules route client questions to Alex, start research from an assignment, and rely on public sources for practice claims; do not silently extend those rules to dossier review or future dossier-based writing. Stage 1 and the Stage 2 pilot can follow approval; article integration remains separately blocked as stated above.

## Open Questions for Alex

These questions are for discussion, not current or optional production work. Record Alex's answers here. Propose a scope or governing-document change only if those answers establish work the operator wants to adopt.

1. How are these article topics chosen, and what SEO keywords or search queries is each article intended to address?

   Under “Primary Keyword,” the [original style guide](../sources/writing-standards/content_style_guide.md#primary-keyword) states:

   > Include naturally in:
   > - Title
   > - First 100 words
   > - At least one H2 heading
   > - Meta title
   > - Meta description
   > - URL (when applicable)

   The assignment supplies titles and reference URLs but does not identify primary keywords. For each client and prompt number, can you provide the primary keyword and any supporting terms or search queries used to select the topic? Should writers receive those terms or infer them from the title? If a topic was not selected from keyword research, how was it chosen, and what reader question or goal should it address? This context would help guide research and establish how to apply the quoted requirement.

   Does this assignment also include drafting a meta title, meta description, and proposed URL, or are those handled separately during publication?

2. How do Benchmark’s writers distinguish SEO articles from AEO articles in practice? The assignment labels them separately, but the style guide does not explain a different writing approach, and the assignment asks every article to support both SEO and AEO discovery. What should change in research, structure, content, or review criteria based on the label? Can you provide an example of each and explain the differences you expect?

3. Can you confirm that articles may be delivered directly to you after substantial editing, fact checking, and verification, with your customer review providing human review after delivery? The style guide requires human review before submission; the proposed workflow has no human review before delivery.

   This customer-workflow confirmation remains deferred by Vikas. [User Design](userdesign.md#review-revision-and-writing-feedback) defines the current direct-delivery and customer-review arrangement.
