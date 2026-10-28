# Roadmap

This document records the plan and progress for operator-authorized work. It does not establish product requirements or authorize later implementation work. [Product](product.md) defines the purpose and scope; [Architecture](architecture.md#article-production-flow) defines the article production flow.

Saved checkpoints: **Batch 1**, designated successful by Vikas after positive feedback from Alex and Peter, is preserved at Git tag `batch-1-successful`. **Batch 1A**, the operator-accepted local consistency retest after the governing-document migration, is preserved at `batch-1a` and will not be delivered to Alex. The [article index](../articles/README.md) links both batches and their records. Separate evaluator work remains on hold.

## Deliver Batch 2

**Status:** Goal and customer requests recorded on October 28, 2026. The linking requirement is applied; FAQ governing changes are pending approval. Both items require validation on Batch 2. Language changes remain deferred until the resulting articles can be evaluated; production has not started.

- **Batch scope:** Four articles for DC Derm Docs. One must be “DC Derm Docs Laser Hair Removal,” the topic delivered in Batch 1 as DC Derm Docs prompt 3. The other three assignments remain to be selected; how to handle the repeated assignment remains to be decided.
- **Linking:** Address Alex's suggested insertion in the [Batch 1 DC Derm laser hair removal Doc](https://docs.google.com/document/d/1i9uxnKszs0DQmTut1d_mTf6wDeO6ykOEulV5jB5X-NA/edit): “Main service or services should be linked on first mention. Here, the main landing page for laser hair removal should be linked to that anchor text.” The first mention in the opening is currently unlinked; the service-page link appears later on “Splendor X for laser hair removal.” Inspection of all four Batch 1 Docs found no other linking changes or suggestions; their article links match the saved versions. The approved requirement is applied in [Writing Standards' Links](writing-standards.md#links). **Open — awaiting Batch 2 validation:** check that each main service links to the relevant practice page on its first body mention, with no repeated internal destination. Applying the instruction does not establish successful execution.
- **FAQ direction agreed; governing revision pending:** Add three or four questions to every piece, including blogs and pages, using the [AAD laser hair removal FAQ](https://www.aad.org/public/cosmetic/hair-removal/laser-hair-removal-faqs) as a format reference. Write the article using the successful approach, then derive the FAQ primarily from its most important patient questions. Add a missing question only when it belongs within the assignment. Use general treatment questions, practice-specific questions, or both, according to reader usefulness. Each answer should make sense independently, with practice and location details included naturally where relevant. Keep answers as short as the question permits and apply the existing factual-support, clarity and usefulness checks, preserving necessary qualifications. The FAQ is additional to the main article's word allowance, with no separate word target. Append it after the article's existing closing CTA. This placement is Vikas's agreed choice; Alex requested an FAQ at the end but did not specify its position relative to the CTA. Vikas understands the search purpose to be helping the content appear in LLM answers about treatment options and locations. Incorporation into the governing instructions remains pending a consolidated proposal and approval.
- **Language feedback — blocked by FAQ, linking and Batch 2 results:** Alex said: “Technically, the writing is really solid. I mostly added linking, keyword and spacing recommendations.” His DC Derm suggestions about the introduction's paragraph break and the placement and bolding of “long-lasting hair reduction” remain deferred. Implement the approved FAQ and linking changes and produce Batch 2 under the existing language instructions first. Then evaluate the resulting articles against this feedback and decide whether language instructions need to change. Do not include these language changes in the FAQ/linking governing revision. This deferred review does not block Batch 2 production.

**Pending decisions and next action:** Review and approve the FAQ governing proposal, and resolve the assignment set before production. The applied linking requirement remains open for validation on Batch 2. Reconcile [Writing Standards' Article Structure](writing-standards.md#article-structure), which currently makes a separate FAQ conditional, includes all body content in the word count and ends the article with a CTA. Current governing requirements remain unchanged until that revision is approved. The language-feedback review follows production of the resulting Batch 2 articles. The delivery goal uses the existing [assignment delivery and tracking experience](userdesign.md#assignment-delivery-and-tracking), with customer review and acceptance under [Product's goals](product.md#goals).

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
