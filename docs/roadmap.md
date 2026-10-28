# Roadmap

This document records the plan and progress for operator-authorized work. It does not establish product requirements or authorize later implementation work. [Product](product.md) defines the purpose and scope; [Architecture](architecture.md#article-production-flow) defines the article production flow.

Saved checkpoints: **Batch 1**, designated successful by Vikas after positive feedback from Alex and Peter, is preserved at Git tag `batch-1-successful`. **Batch 1A**, the operator-accepted local consistency retest after the governing-document migration, is preserved at `batch-1a` and will not be delivered to Alex. The [article index](../articles/README.md) links both batches and their records. Separate evaluator work remains on hold.

## Review Batch 2 Language Feedback

**Status:** Vikas authorized fresh production and replacement of all four Batch 2 articles on October 28, 2026. Use the common committed agent version `7a21f9152b177506c3c44e2f8a5a12b264b66112`, which includes the approved Opening and FAQ question-framing changes. SEO 03 becomes v010; SEO 04, SEO 10 and AEO 15 become v002. Retain the earlier local versions and keep Batch 1 unchanged.

**In progress:** Research, write and verify each article in a fresh context under [Architecture](architecture.md#article-production-flow). Retain the new article and support-and-check record in its version subfolder within [Batch 2](../articles/batch-2-2026-10-28/README.md). Replace the existing customer Docs only after the new articles pass local checks; preserve their URLs, folder and access settings, and any newer reviewer work. Update filenames, the agent-version prefaces and the existing review-index rows; retain the gray divider between batches. No sharing notification emails are needed.

**Outstanding verification:** Establish the new Opening and FAQ requirements on the exact resulting articles, repeat the full local checks, and verify native Doc preservation, presentation, comments, access and review-index entries under [Engineering](engineering.md#customer-delivery-verification). Alex's positive assessment of Batch 1 remains the quality reference; agent checks do not establish acceptance of the replacements.

**Next action:** Complete the four local packages, perform guarded native replacement and verify delivery. Record remaining failures or required information explicitly. Customer review and acceptance follow [User Design](userdesign.md#review-revision-and-writing-feedback).

## Goal 3: Evaluate Research for Dossier Suggestions and Conflict Review

**Status and sequence:** Vikas selected this goal on October 28, 2026, for work after the Batch 2 rerun, then refined its first objective: evaluate whether the existing research method can support useful answers to dossier unknowns and identify factual conflicts. This entry captures the intended work for discussion. Governing-document changes and implementation remain pending the consolidated proposal and approval required by [AGENTS](../AGENTS.md#review-and-approve-the-change). Batch 2 continues under its existing production instructions.

**Context supplied by Vikas:** Benchmark calls its internal account team's summary of an account a dossier. Peter owns dossiers for the company. There is one dossier per client, intended to be a Google Doc, with no dependable template. A dossier can contain both public information and internal client information unavailable on the public web. Vikas has received one dossier from Peter: [DC Derm Docs](https://docs.google.com/document/d/1-ec5aLWUHk7vDz4w23-iHSBMLdr9bG5Q/edit). Its reliability as a writing source has not been established; it contains explicit unknowns and requests for confirmation as well as statements of fact.

**Dossier index:** Add a tab named **Dossiers** to the existing [review spreadsheet](https://docs.google.com/spreadsheets/d/19pXjqiOHhgViaEOoUtpAzk22LcQqLMmfHFLVjaxbq8Y/edit), with columns **Client** and **Dossier**. Start with DC Derm Docs and its supplied link; add more client links as Vikas receives them from Peter. Keep one row per client and preserve the article review tab.

**First objective — Research feasibility:** Evaluate the current research method on DC Derm Docs before committing to a broader dossier process. Reuse source discovery, practice investigation and conflict checks in [Architecture](architecture.md#understand-the-practice), [Data Model's evidence distinctions](data-model.md#article-research-material) and [Engineering's factual-support checks](engineering.md#factual-support). Adapt the investigation to this client's dossier coverage rather than an article assignment. Research the client using the existing method, then compare supported findings with the dossier's actual wording; the dossier's statements are claims to assess, not established research answers. Do not outline or draft articles. Identify which unknowns public research can answer, which need Peter or the client, which factual statements have conflicting evidence, and where research remains inconclusive. Absence from the website is not a contradiction, and general product information does not establish which product or model the practice uses. Keep exact source passages, links, timing where available, and material limits sufficient to assess each proposed answer or conflict.

**Pilot output 1 — Suggested answers:** Where research supports an answer to an explicit unknown or request for confirmation, propose the answer in the dossier using Google Docs **Suggesting mode**, so Peter can accept or reject the wording. Keep the supporting source link available beside the suggestion or in a linked comment. Preserve any qualification or remaining uncertainty. Leave questions unanswered when research cannot establish the answer; do not replace internal information with an inference from public sources. Verify that changes are actual suggestions, rather than direct edits to the dossier's accepted text.

**Pilot output 2 — Conflict comments:** Where research conflicts with a statement presented as fact, leave a natural-language comment that sounds like Vikas. Identify the relevant dossier wording, explain what we found and where, and include a direct source link Peter can visit. Distinguish a conflict from an existing unknown or a request the dossier already makes; avoid duplicate verification requests. Do not assume either source is automatically current. Peter can update an outdated dossier and resolve the comment, or reply that the public source is outdated and instruct us to use the dossier. Keep unresolved disagreements explicit and inspect the updated text or reply to establish the outcome; a closed comment alone does not explain which information is current.

**Technical dependency:** Before writing to the dossier, verify its format, permissions, Suggesting mode and comment behavior. Drive currently identifies the supplied file as a `.docx` opened in Google Docs. The connected Docs editing tool documents direct edits, not creation of suggestions; the route for actual suggestions remains to be verified. Preserve Peter's authoritative document and access, and resolve any conversion need explicitly. Do not substitute direct edits for suggestions or claim that proposed local wording is a posted suggestion.

**Completion evidence and decisions:** First produce an evidence-backed assessment of what the existing research method can and cannot answer, representative proposed answers and conflict comments, and a verified route or explicit blocker for actual suggestions and comments. That assessment determines whether and how to proceed with the one-client pilot. Verify the index row and link and, during the pilot, the exact dossier assessed, posted suggestions and comments, and Peter's actual acceptance, rejection, correction or reply. Preparing outputs alone does not establish that the resolution workflow works. Report unresolved questions and do not generalize one dossier's quality to other clients.

**Future article use — blocked:** The longer-term intent remains to combine dossiers with our own research as client-specific input to article writing. Do not let dossiers influence writing or revision of article batches yet. That work depends on assessing dossier quality, demonstrating the suggestion-and-resolution workflow with Peter, and Vikas's decision to proceed under approved governing requirements.

**Next action and dependencies:** Prepare the smallest consolidated governing-document proposal for the research-feasibility assessment and its intended pilot outputs. Address the supported dossier-review operation, suggestions, comments and Peter's role in User Design; the research and resolution flow in Architecture; source identity, internal information, uncertainty and resolution evidence in Data Model; verification in Engineering; and Product scope where affected. Current article rules route client questions to Alex and start research from an assignment; do not silently extend them to this operation. Changes to Writing Standards' source rules for future dossier-based writing remain outside this assessment and blocked with article integration. The index and assessment can follow approval; broader pilot execution depends on the assessment, and article integration remains separately blocked as stated above.

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
