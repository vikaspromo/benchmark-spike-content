# Roadmap

This document records the plan and progress for operator-authorized work. It does not establish product requirements or authorize later implementation work. [Product](product.md) defines the purpose and scope; [Architecture](architecture.md#article-production-flow) defines the article production flow.

## Open Questions for Alex

These questions are for discussion, not current or optional production work. Record Alex's answers here. Propose a scope or governing-document change only if those answers establish work the operator wants to adopt.

1. What keywords or search queries led to each article assignment, identified by client and prompt number? Which is the primary keyword? If an assignment was not selected from keywords or search queries, how was the topic chosen, and what reader question or goal should it address? This context could guide the research approach. The style guide calls for the primary keyword in the article and its meta title and meta description, but this assignment supplies titles without explicit primary keywords. Should we also draft a proposed meta title and meta description for each article using the keywords you provide?

2. How do Benchmark’s writers distinguish SEO articles from AEO articles in practice? The assignment labels them separately, but the style guide does not explain a different writing approach, and the assignment asks every article to support both SEO and AEO discovery. What should change in research, structure, content, or review criteria based on the label? Can you provide an example of each and explain the differences you expect?

3. Can you confirm that articles may be delivered directly to you after substantial editing, fact checking, and verification, with your customer review providing human review after delivery? The style guide requires human review before submission; the proposed workflow has no human review before delivery.

## Establish the Method in Codex

Current work is to establish the article production method in Codex. This development work is distinct from the stages used to produce each article. Ideas for an unattended worker and hosted intake are deferred in [Icebox](icebox.md#unattended-and-hosted-article-production).

The production flow has been agreed and documented in Architecture. Trials of Estar prompt 4 exercised research, outlining, drafting, automatic checks, revisions, independent AI editorial review, and local Word export. Operator feedback showed that passing measurable checks did not establish reader usefulness or substantive practice customization. Earlier trials improved required-versus-optional dependency handling but did not establish Benchmark writer-quality parity, customer acceptance, or general method reliability. Automated editorial assessment reliability and unattended operation remain unverified.

The approved governing revisions require heading-focused content, meaningful practice customization demonstrated through the substitution test, and a final 1,150–1,250-word body measured after quality assessment. Architecture now separates research, outlining, and drafting from one final checklist, focused correction pass, and recheck. Remaining failures keep an article incomplete; a general automated repair engine is not required. Writing Standards governs independently of historical sources, stored under sources/writing-standards/. Open questions above remain discussion topics rather than article work.

At Vikas's request, the previous 1,600-word article and its complete package were removed. That replacement article was later removed at Vikas's request before the three-practice trial below. Git retains tracked earlier work for historical lookup; previous draft packages are not current production inputs.

That earlier run used a fresh production context without prior drafts, research, critiques, historical writing instructions, or Estar's completed same-topic blog. It completed the assignment brief, practice-first research, a structured research plan, authoritative topic verification, observed organic Google competitor review, an evidence-supported outline, drafting, and automatic evaluation and revision. The Google observation used a site-exclusion query and personalized Washington, DC, results; it does not establish universal rankings. Quality review identified underdeveloped useful explanations before the final length was measured. The final count excludes headings, URLs, Markdown markup, and bullet markers.

Fresh independent AI review required two factual corrections: remove an unsupported injection-time comparison and restrict the FDA combination-study statement to safety. Both were applied, affected checks repeated, and the reviewer confirmed Send on the exact resulting article. The final article has 1,172 substantive body words, seven hyperlinks, and one optional clinician-quote comment, with no required facts unresolved. The reviewer assessed compliance, factual support, and reader usefulness separately and confirmed heading relevance and practice substitution. Estar's lip-specific options within its broader filler menu and its facial-balancing service require factual rewriting for another practice; names and links alone were not counted. That earlier run reported local Ready for Review; it is not a readiness assessment of the current three articles.

The three-page Word document preserves the exact reviewed text, all seven hyperlinks, and the anchored optional comment. All three rendered pages were inspected, and structural checks passed. This is evidence from one local run, not human clinical validation, Alex's acceptance, writer-quality parity, or demonstrated assessment reliability across assignments.

Native Google Docs import, real comment verification, batch tracking, delivery, Alex's acceptance, and Benchmark writer-quality parity remain pending. Further discussion of a repeatable practice-research method remains pending; this run's evidence does not establish that method across clients. Continue refining and exercising the method when the operator directs further work.

Vikas's inspection of intermediate work during development helps establish and verify the method. It does not introduce a permanent review or approval gate for individual articles. The intended direct-delivery experience remains defined in [User Design](userdesign.md#assignment-delivery-and-tracking).

Establish the method through evidence from real assignments and customer feedback. Documenting the production flow alone does not establish that it works.

## Three-Practice Trial of the Simplified Flow

At Vikas's direction, the remaining Estar draft package was removed and three articles were produced using the revised governing documents: DC Derm Docs prompt 3 (laser hair removal), La-Mon’e prompt 9 (first-time lip filler), and Estar prompt 4 (lip flip versus filler). Research excluded each practice's blogs and did not read previous draft packages. Service, provider, contact, and gallery pages supplied practice evidence; independent clinical sources supported medical claims. Observed Google results excluded the respective client domain and were personalized, so they do not establish universal rankings.

Each preserved v001 package in [articles/](../articles/README.md) contains article.md, a structured brief, source support, one source image, prepared optional comments, a local HTML preview, and the final checklist assessment. No candidate-material inventory, omission history, or persistent repair engine was created. After a focused correction pass, the final counts were 1,160 words for DC Derm Docs, 1,157 for La-Mon’e, and 1,172 for Estar. All three have four distinct internal content links, a separate CTA link, two authoritative external links, and an embedded source image. Final local editorial, evidence, mechanical, and image-presentation checks passed by agent assessment.

The practice-substitution evidence is stated in each assessment rather than inferred from name changes. La-Mon’e and Estar use their actual lip-gallery examples. DC Derm Docs uses a provider image in its clinical-context section, plus its named systems and package boundaries; these do not establish a unique treatment policy or comparative expertise. One optional approved clinician quote request is prepared per article; no required article facts remain unresolved.

The assessments identify the exact checked article versions. The run used agent review, not independent human review, and does not establish Benchmark writer-quality parity or general assessment reliability. Google Docs creation, native comments, batch Sheet tracking, actual delivery verification, and Alex's acceptance remain pending. Further article work follows Vikas's direction; this record does not add a permanent operator approval gate.

## Three-Article Rerun With Current Writing Standards

At Vikas's direction, DC Derm Docs prompt 3, La-Mon’e prompt 9, and Estar prompt 4 were drafted again as v002 using committed governing inputs at `780d1fb313aa862c3f861df20dcd9caaf0a471c5`. The [production record](../articles/runs/2026-10-07-writing-standards-v002/README.md) links the exact inputs and outputs. Previous packages and practice blogs were not read; v001 remains preserved for feedback. This was fresh drafting within the existing conversation, not an isolated model context.

Final body counts are 1,159, 1,171, and 1,166 words respectively. Each has a final checklist assessment identifying the exact article hash, source support, prepared comments, and a local HTML preview. Local PDF render inspection and text/link verification passed. HTML structure was checked, but actual HTML browser rendering was not verified. La-Mon’e and Estar include practice treatment images; DC Derm Docs uses supported systems and package boundaries without an image.

All three are locally Ready for Review by agent assessment, with no required facts unresolved. Native Google Docs comments, customer delivery, batch tracking, Alex's acceptance, Benchmark writer-quality parity, and assessment reliability across assignments remain unverified. One optional clinician-quote request is prepared per article. The latest drafts are linked from [the article index](../articles/README.md); feedback can refer to v002 and the passage.
