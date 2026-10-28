# Roadmap

This document records the plan and progress for operator-authorized work. It does not establish product requirements or authorize later implementation work. [Product](product.md) defines the purpose and scope; [Architecture](architecture.md#article-production-flow) defines the article production flow.

Saved checkpoints: **Batch 1**, designated successful by Vikas after positive feedback from Alex and Peter, is preserved at Git tag `batch-1-successful`. **Batch 1A**, the operator-accepted local consistency retest after the governing-document migration, is preserved at `batch-1a` and will not be delivered to Alex. The [article index](../articles/README.md) links both batches and their records. Separate evaluator work remains on hold.

## Review Batch 2 Language Feedback

**Status:** Vikas authorized fresh production and replacement of all four Batch 2 articles on October 28, 2026. Use the common committed agent version `7a21f9152b177506c3c44e2f8a5a12b264b66112`, which includes the approved Opening and FAQ question-framing changes. SEO 03 becomes v010; SEO 04, SEO 10 and AEO 15 become v002. Retain the earlier local versions and keep Batch 1 unchanged.

**In progress:** Research, write and verify each article in a fresh context under [Architecture](architecture.md#article-production-flow). Retain the new article and support-and-check record in its version subfolder within [Batch 2](../articles/batch-2-2026-10-28/README.md). Replace the existing customer Docs only after the new articles pass local checks; preserve their URLs, folder and access settings, and any newer reviewer work. Update filenames, the agent-version prefaces and the existing review-index rows; retain the gray divider between batches. No sharing notification emails are needed.

**Outstanding verification:** Establish the new Opening and FAQ requirements on the exact resulting articles, repeat the full local checks, and verify native Doc preservation, presentation, comments, access and review-index entries under [Engineering](engineering.md#customer-delivery-verification). Alex's positive assessment of Batch 1 remains the quality reference; agent checks do not establish acceptance of the replacements.

**Next action:** Complete the four local packages, perform guarded native replacement and verify delivery. Record remaining failures or required information explicitly. Customer review and acceptance follow [User Design](userdesign.md#review-revision-and-writing-feedback).

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
