# Roadmap

This document records the plan and progress for operator-authorized work. It does not establish product requirements or authorize later implementation work. [Product](product.md) defines the purpose and scope; [Architecture](architecture.md#article-production-flow) defines the article production flow.

Saved checkpoints: **Batch 1**, designated successful by Vikas after positive feedback from Alex and Peter, is preserved at Git tag `batch-1-successful`. **Batch 1A**, the operator-accepted local consistency retest after the governing-document migration, is preserved at `batch-1a` and will not be delivered to Alex. The [article index](../articles/README.md) links both batches and their records. Separate evaluator work remains on hold.

## Deliver Batch 2

**Status:** Goal and customer requests recorded on October 28, 2026. Reviewing feedback one item at a time with Vikas; production and governing-document changes have not started. Preserve the successful writing approach and focus on the requested additions.

- **Batch scope:** Four articles for DC Derm Docs. One must be “DC Derm Docs Laser Hair Removal,” the topic delivered in Batch 1 as DC Derm Docs prompt 3. The other three assignments remain to be selected; how to handle the repeated assignment remains to be decided.
- **Linking:** Address Alex's suggested insertion in the [Batch 1 DC Derm laser hair removal Doc](https://docs.google.com/document/d/1i9uxnKszs0DQmTut1d_mTf6wDeO6ykOEulV5jB5X-NA/edit): “Main service or services should be linked on first mention. Here, the main landing page for laser hair removal should be linked to that anchor text.” The first mention in the opening is currently unlinked; the service-page link appears later on “Splendor X for laser hair removal.” Inspection of all four Batch 1 Docs found no other linking changes or suggestions; their article links match the saved versions. Next action is to propose the corresponding change to [Writing Standards' Links](writing-standards.md#links) for approval before production. This item concerns first-mention placement, not a request for more links.
- **FAQ request and direction:** Alex wants an FAQ section at the end of every piece, including blogs and pages, with three or four questions. His example is the [AAD laser hair removal FAQ](https://www.aad.org/public/cosmetic/hair-removal/laser-hair-removal-faqs). Vikas agreed that the FAQ should primarily recap the article's most important patient questions; add a missing question only when it belongs within the assignment. His preferred sequence is to write the article as before, then use it as the main basis for the FAQ. Whether the FAQ is additional to the article's word allowance remains unresolved. Vikas understands Alex's search purpose to be helping the content appear in LLM answers about treatment options and locations; this is the working objective, not a confirmed explanation from Alex or a verified search outcome. Incorporation into the governing instructions remains pending a consolidated proposal and approval.
- **Other Batch 1 feedback:** Alex said: “Technically, the writing is really solid. I mostly added linking, keyword and spacing recommendations.” The DC Derm Doc also contains suggestions about the introduction's paragraph break and the placement and bolding of “long-lasting hair reduction.” These remain to be discussed separately with Vikas.

**Pending decisions and next action:** Discuss FAQ treatment next with Vikas. Before production, resolve the assignment set and FAQ treatment, address the linking item and other relevant feedback, and obtain approval for any resulting instruction changes. [Writing Standards](writing-standards.md#article-structure) currently makes a separate FAQ conditional and governs article length and the closing call to action; those requirements remain unchanged. The delivery goal uses the existing [assignment delivery and tracking experience](userdesign.md#assignment-delivery-and-tracking), with customer review and acceptance under [Product's goals](product.md#goals).

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
