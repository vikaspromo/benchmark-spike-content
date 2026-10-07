# Roadmap

This document records the plan and progress for operator-authorized work. It does not establish product requirements or authorize later implementation work. [Product](product.md) defines the purpose and scope; [Architecture](architecture.md#article-production-flow) defines the article production flow.

## Open Questions for Alex

These questions are for discussion, not current or optional production work. Record Alex's answers here. Propose a scope or governing-document change only if those answers establish work the operator wants to adopt.

1. What keywords or search queries led to each article assignment, identified by client and prompt number? Which is the primary keyword? If an assignment was not selected from keywords or search queries, how was the topic chosen, and what reader question or goal should it address? This context could guide the research approach. The style guide calls for the primary keyword in the article and its meta title and meta description, but this assignment supplies titles without explicit primary keywords. Should we also draft a proposed meta title and meta description for each article using the keywords you provide?

2. How do Benchmark’s writers distinguish SEO articles from AEO articles in practice? The assignment labels them separately, but the style guide does not explain a different writing approach, and the assignment asks every article to support both SEO and AEO discovery. What should change in research, structure, content, or review criteria based on the label? Can you provide an example of each and explain the differences you expect?

3. Can you confirm that articles may be delivered directly to you after substantial editing, fact checking, and verification, with your customer review providing human review after delivery? The style guide requires human review before submission; the proposed workflow has no human review before delivery.

## Establish the Method in Codex

Current work is to establish the article production method in Codex. This development work is distinct from the stages used to produce each article. Ideas for an unattended worker and hosted intake are deferred in [Icebox](icebox.md#unattended-and-hosted-article-production).

The production flow has been agreed and documented in Architecture. The first cold trial has an article-specific rule catalog and reproducible measurable checks. Automated editorial and dependency assessment reliability and unattended operation have not been validated.

The next work is to exercise the flow on real assigned articles, inspect the briefs, research, outlines, drafts, and check findings, and refine the method. Alex’s customer review and acceptance provide evidence of article quality.

Estar prompt 4 has research, an evidence-linked outline and draft artifacts with recorded checks. Vikas found that the first revised article did not serve the target reader and included padding despite passing measurable checks; the earlier claim of editorial completion was premature. A new 1,272-word draft focuses on the reader's comparison, adds qualified practical expectations and removes repeated consultation advice. Its Word file preserves the text, seven links and six anchored comments; all four rendered pages were inspected. A fresh independent AI editorial review returned Revise for the second draft, identifying thin practice customization, scanning and specific clinical wording. A focused third draft addressed those findings. The reviewer reassessed the exact final version and returned Send as Needs Information with no remaining material delivery defect. The final Word file matches the reviewed text, retains seven links and six anchored comments, and passed inspection of all four rendered pages. This is evidence of an editorial review cycle, not validation of review reliability or human clinical judgment. Provider associations remain unresolved, and supplied-keyword checks remain unavailable. The local draft is Needs Information. Native Google Docs import, comment verification, batch tracking and delivery remain pending personal Google Drive access. Customer acceptance and writer-quality parity remain unverified.

A fresh-context trial of Estar prompt 4 completed research, drafting, automatic checks and a separate fresh editorial review under the current Writing Standards, using only the original assignment inputs and new research. The reviewer found no material factual or editorial defect and required one package correction: a visible note for unknown keywords and metadata scope. The corrected 1,403-word candidate is Send as Needs Information; no provider-to-procedure association is needed for its supported wording. The original candidate and reviewed package are preserved separately. The four-page Word export matches the reviewed text, seven links and four comments; all pages were inspected. Comparison with the earlier draft identifies improved dependency handling, but does not establish better prose, customer acceptance or general method reliability. Native Google delivery remains pending. The proposed source-archive cleanup remains pending approval.

Vikas’s inspection of intermediate work during development helps establish and verify the method. It does not introduce a permanent review or approval gate for individual articles. The intended direct-delivery experience remains defined in [User Design](userdesign.md#assignment-delivery-and-tracking).

Establish the method through evidence from real assignments and customer feedback. Documenting the production flow alone does not establish that it works.

The approved scope correction removes keyword and metadata production from the current workload. Those subjects are tracked only in Open Questions for Alex. The fresh article's current package uses the unchanged 1,403-word candidate, removes the obsolete required-input marker and customer questions, and retains only the optional quote and pricing comments. Its current local status is Ready for Review under the revised requirements; the earlier Needs Information assessments remain historical trial evidence. Google delivery and Alex's acceptance remain pending.
