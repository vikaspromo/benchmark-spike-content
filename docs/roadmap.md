# Roadmap

This document records the plan and progress for operator-authorized work. It does not establish product requirements or authorize later implementation work. [Product](product.md) defines the purpose and scope; [Architecture](architecture.md#article-production-flow) defines the article production flow.

## Open Questions for Alex

These questions are for discussion, not current or optional production work. Record Alex's answers here. Propose a scope or governing-document change only if those answers establish work the operator wants to adopt.

1. What keywords or search queries led to each article assignment, identified by client and prompt number? Which is the primary keyword? If an assignment was not selected from keywords or search queries, how was the topic chosen, and what reader question or goal should it address? This context could guide the research approach. The style guide calls for the primary keyword in the article and its meta title and meta description, but this assignment supplies titles without explicit primary keywords. Should we also draft a proposed meta title and meta description for each article using the keywords you provide?

2. How do Benchmark’s writers distinguish SEO articles from AEO articles in practice? The assignment labels them separately, but the style guide does not explain a different writing approach, and the assignment asks every article to support both SEO and AEO discovery. What should change in research, structure, content, or review criteria based on the label? Can you provide an example of each and explain the differences you expect?

3. Can you confirm that articles may be delivered directly to you after substantial editing, fact checking, and verification, with your customer review providing human review after delivery? The style guide requires human review before submission; the proposed workflow has no human review before delivery.

## Establish the Method in Codex

Current work is to establish the article production method in Codex. This development work is distinct from the stages used to produce each article. Ideas for an unattended worker and hosted intake are deferred in [Icebox](icebox.md#unattended-and-hosted-article-production).

The production flow has been agreed and documented in Architecture. Trials of Estar prompt 4 exercised research, outlining, drafting, automatic checks, revisions, independent AI editorial review, and local Word export. Operator feedback showed that passing measurable checks did not establish reader usefulness or substantive quality. The fresh trial improved required-versus-optional dependency handling; it did not establish better prose, customer acceptance, or general method reliability. Automated editorial assessment reliability and unattended operation remain unverified.

Only the latest Estar prompt 4 article and the artifacts needed to support and verify it remain in the working tree. Earlier drafts and comparison artifacts were removed at Vikas's request; Git retains their history.

The revised-flow run completed fresh practice and topic research, a supported distinct-value outline, drafting, automatic checks, and separate compliance, factual-support and reader-usefulness assessments. An initial research context was stopped before writing after a search surfaced the completed Estar topic article; the replacement context used direct practice pages and exclusion queries, and reported no excluded-source exposure. The independent reviewer returned Send with no required corrections and confirmed that verdict after two optional wording refinements. The final article has 1,600 body words, seven hyperlinks, and one optional clinician-quote comment. All four rendered Word pages and the preserved text, links and comment were verified. It was locally Ready for Review under the standards used for that run. The newly approved length range and practice-substitution test supersede that readiness assessment: the 1,600-word draft is outside the range, and operator inspection found insufficient substantive customization. Its current status is Drafting; prior checks and reviewer findings remain evidence for the earlier standards, not a pass under the revised requirements. This is evidence from one run, not clinical validation, customer acceptance or demonstrated method reliability across assignments.

The approved governing changes are applied: supported answers precede referrals, each outline section has distinct value, practice details contribute relevant context, and usefulness is assessed separately from counts and factual support. Writing Standards governs independently of historical sources, now stored under sources/writing-standards/. Open questions above remain discussion topics rather than article work.

The approved revisions now require heading-focused content, meaningful practice customization demonstrated through the substitution test, and a final 1,150–1,250-word body measured after quality assessment. Architecture requires revision and repeated checks until quality and length both pass. Further discussion of the practice-research method remains pending; no new article run has been performed under these revisions.

Native Google Docs import, real comment verification, batch tracking, delivery, Alex's acceptance, and Benchmark writer-quality parity remain pending. Continue refining and exercising the method when the operator directs further work.

Vikas’s inspection of intermediate work during development helps establish and verify the method. It does not introduce a permanent review or approval gate for individual articles. The intended direct-delivery experience remains defined in [User Design](userdesign.md#assignment-delivery-and-tracking).

Establish the method through evidence from real assignments and customer feedback. Documenting the production flow alone does not establish that it works.
