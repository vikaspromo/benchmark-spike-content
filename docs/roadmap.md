# Roadmap

This document records the plan and progress for operator-authorized work. It does not establish product requirements or authorize later implementation work. [Product](product.md) defines the purpose and scope; [Architecture](architecture.md#article-production-flow) defines the article production flow.

Saved checkpoints: **Batch 1**, designated successful by Vikas after positive feedback from Alex and Peter, is preserved at Git tag `batch-1-successful`. **Batch 1A**, the operator-accepted local consistency retest after the governing-document migration, is preserved at `batch-1a` and will not be delivered to Alex. The [article index](../articles/README.md) links both batches and their records. Separate evaluator work remains on hold.

## Review Batch 2 Language Feedback

**Status:** Batch 2 production and native delivery are complete. All four fresh DC Derm Docs articles use agent version `193fa85`; first-mention service linking and FAQ execution were validated. The [Batch 2 package](../articles/batch-2-2026-10-28/README.md) links the delivered Docs, review index and detailed checks. Two first drafts missed the initial length aim; the records preserve this deviation. Alex's review and acceptance are pending.

Alex said: “Technically, the writing is really solid. I mostly added linking, keyword and spacing recommendations.” Review of his remaining Batch 1 suggestions and the Batch 2 introductions led to the approved [Opening revision](writing-standards.md#opening): paragraph separation at the shift to the practice, and natural topic-phrase placement and emphasis in the final introduction sentence. Two Batch 2 introductions retain the paragraph pattern he flagged; all four lack the requested final-sentence bolding. No additional distinct feedback pattern was found in the four Batch 1 Docs.

**Opening guidance — awaiting validation:** The approved instruction is applied; its effect on produced articles remains unverified. Validate it during the next production run Vikas authorizes. Batch 2 remains unchanged and will not be rerun. Customer acceptance follows [User Design](userdesign.md#review-revision-and-writing-feedback).

**FAQ question framing — awaiting validation:** The approved [FAQ wording](writing-standards.md#faq) now calls for natural reader questions and realistic result expectations. Check its effect during the next authorized production run. Vikas directed that Batch 2 remain unchanged and not be rerun.

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
