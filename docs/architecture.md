# Architecture

Architecture defines how components work together to produce and maintain the content production product’s required outcomes. Each section establishes a distinct architectural responsibility. Read the sections governing the affected components and operations, and follow references to their dependencies.

Product owns system purpose and scope; User Design owns product-user behavior, language and voice; Writing Standards owns article content and writing standards; Data Model owns record meanings, identity and validity; Engineering owns implementation discipline and verification; Release owns deployment and recovery; AGENTS owns agent responsibilities, authorization and governing-document changes. Architecture references those requirements and defines how components fulfill them.

## Article Production Flow

Produce each assigned article through research, outlining, and drafting, then run the single evaluation and revision flow in [Evaluate and Revise](#evaluate-and-revise) before direct customer delivery under [User Design](userdesign.md#assignment-delivery-and-tracking). Writing Standards owns what the article must satisfy; Engineering owns verification methods and evidence.

The production stages provide working context for writing. Keep the structured assignment brief, source evidence needed to support the article, and unresolved dependencies that affect its answer. Research plans, notes, and outlines may be adjusted as useful without maintaining stage histories, candidate-material inventories, or reasons for each unused item. [Data Model](data-model.md#article-research-material) defines the retained research evidence; [Assignments and Article Status](data-model.md#assignments-and-article-status) defines the article assessment.

Review the client's website as needed for different purposes. Research the client's own website before using third-party sources; [Writing Standards](writing-standards.md#practice-specific-material) defines the relevant practice material. Later evidence may change the working interpretation or require more research. Production adjustments do not require separate compliance reviews at each stage.

### Understand the Assignment

Produce a structured assignment brief that gives research and writing a clear target.

Preserve the supplied client, prompt number, original title, SEO/AEO label, reference URLs, and special instructions so Alex can trace the article to its assignment. Keep the supplied assignment distinct from its interpretation. Preserve the prompt number through revisions under [Data Model](data-model.md#assignments-and-article-status).

Use the assignment and a focused review of the client's website to infer the target reader and main question or decision. Choose one working interpretation, record it as a hypothesis with supporting evidence, and move forward. Update that interpretation when later evidence warrants a change; do not maintain competing interpretations or an interpretation history.

Identify claims implied by the title that need investigation, including superiority, permanence, pricing, availability, and provider expertise. The title does not establish their truth. Keep missing inputs explicit when they affect the article's answer or an applicable requirement. The brief must establish the audience, purpose, and supplied constraints without silently replacing the assigned topic; resolve a proposed topic change with Alex.

### Understand the Practice

Establish the practice context and find supported material useful to this article under [Writing Standards](writing-standards.md#practice-specific-material).

Use the assignment brief to research relevant services, treatments, technology, providers, credentials, locations, practice approach, terminology, and differentiators on the client's website. Examine relevant text and images, including captions and text within images, using Writing Standards' material categories to guide the search. Find useful service, provider, educational, contact, and booking links, and investigate relevant practice claims from the brief.

Keep source evidence and limits needed to use the findings accurately under [Data Model](data-model.md#article-research-material). Preserve correct provider associations and distinguish physical locations from article target geography and treatments from bookable appointments under [Client Information](data-model.md#client-information). A website image does not establish who or what it depicts; product-brand evidence does not establish every formulation or model.

Investigate practice facts needed for the article's answer. Use the supported material available; this stage does not require material from every category, a general client model, or records of unused material.

### Plan the Research

Use the assignment brief and practice findings to plan an article-specific investigation of the questions the article must answer and the claims it needs to support. The plan is working guidance and may change as research develops.

Use supplied reference URLs and the client website as starting points, then consult authoritative third-party sources to verify relevant claims. Treat supplied references as starting points rather than material to rewrite or the only sources to consult.

Include a review of leading organic Google results for the same topic. Derive queries from the assignment and working interpretation, including geography when relevant. Examine reader questions, comparisons, considerations, answer structure, omissions, and weak explanations to inform a more useful original article. Search ranking does not establish medical accuracy, and competitor research does not permit competitor links in the delivered article under [Writing Standards](writing-standards.md#links-and-closing-call-to-action).

Identify questions that only Alex can resolve under [User Design](userdesign.md#review-revision-and-writing-feedback). Do not require a saved investigation record or completion status for every planned question.

### Research and Resolve

Establish a supported central answer using the supplied references, relevant practice pages, authoritative sources, and leading organic Google results. Keep the evidence needed to support the article under [Data Model](data-model.md#article-research-material). Investigate conflicting information and adjust the working interpretation when warranted.

Apply [Writing Standards](writing-standards.md#missing-information) to unresolved facts. Omit optional material when supported content answers the question without it, using User Design's optional-material comment process when applicable. For a required fact that Alex can supply without changing the supported direction, prepare a marker and Google Doc comment under [User Design](userdesign.md#review-revision-and-writing-feedback).

Resolve a missing answer before drafting when it could change the premise, treatment focus, central answer, or recommendation. Investigate further or bring the specific question to Alex when only he can resolve it. Keep the dependency explicit; a marker does not establish a supported direction. This judgment concerns the article's actual needs, not a fixed classification for a kind of fact. It does not require a separate dependency report or histories of possible answers.

### Build the Outline

Arrange the supported central answer and reader questions into a useful sequence. Plan headings and substantive answers, using supported practice material where it helps the article under [Writing Standards](writing-standards.md#reader-answer-and-substantive-content). Do not assign section word budgets.

Plan relevant provider context, useful internal links, appropriate external links, and the closing call to action under Writing Standards. Place useful practice material and images where they support an explanation, and identify locations for unresolved required facts and comments.

Adjust coverage or return to research when the outline lacks a supported answer. Combine repetitive sections and omit material that does not support its heading. If research cannot support the assigned answer, bring the specific gap to the operator rather than invent material or silently change the topic. The outline guides drafting; it does not require a selection record for every material item or a separate customization review.

### Write the First Draft

Produce a complete article from the outline and supported research under [Writing Standards](writing-standards.md). Adjust the outline and material choices when that improves the article.

Use relevant supported practice material, links, and a customized call to action. Acquire and embed images used in the article with supported captions under [User Design](userdesign.md#article-content-and-writing-standards). If an image or other optional material cannot be used, choose another supported approach; keep the evidence needed for the resulting article rather than a history of acquisition attempts or discarded choices.

Prepare markers and Google Doc comments for unresolved required facts and applicable optional-material requests under [User Design](userdesign.md#review-revision-and-writing-feedback). Preserve source support for factual claims, including claims introduced during writing and in captions.

Pass the completed article and supporting evidence to Evaluate and Revise. Drafting does not have its own compliance gate or checklist.

### Evaluate and Revise

Check the complete article against every applicable requirement in [Writing Standards](writing-standards.md), its assignment-specific instructions, and the presentation requirements in [User Design](userdesign.md#article-content-and-writing-standards). This is the single evaluation and revision flow before delivery. Run it as part of production without a manual trigger or Vikas's article-by-article approval.

Use [Engineering](engineering.md#article-verification) to perform mechanical checks and editorial and evidence assessment on the resulting text, images, and captions. Assess article quality before measuring the final body-word count under Writing Standards. Do not add checks or delivery dependencies for unresolved customer questions. Evaluate the article itself rather than auditing earlier plans, unused material, or reasons for changed selections.

Identify each failed requirement, its location, and the correction needed. For length failures, remove repetition and lower-value material or develop useful explanations and practice context, returning to research when needed. Preserve necessary information and medical qualifications; do not pad the article or cut essential answers to meet the range.

For the current method in Codex, make a focused correction pass that addresses the findings, including further research or outline changes when needed. Then recheck the resulting article against the full applicable checklist and retain its current assessment under [Data Model](data-model.md#assignments-and-article-status). A separate automated repair engine or open-ended retry loop is not required. If failures remain after the correction pass, report them to the operator and keep the article incomplete pending further work. Do not mark the article ready on the basis of checks against an earlier version.

Handle required facts awaiting Alex's input through User Design's markers, comments, and Needs Information process. The checklist must distinguish these facts from passed requirements, other failures, optional requests, and requirements that do not apply. Missing information does not excuse other failures.

Proceed to delivery only when no failures remain, apart from required facts permitted through the Needs Information process. With required facts resolved, the article may be delivered as Ready for Review. Verification does not establish customer acceptance.

### Deliver to Alex

Deliver the evaluated article directly through the Google Drive, Docs, and Sheet experience in [User Design](userdesign.md#assignment-delivery-and-tracking), without requiring Vikas's approval of the individual article.

Preserve the evaluated text, headings, links, images, captions, and markers in the assigned Google Doc. Embed images inline between paragraphs, place each caption immediately below its image, and add the source-link comment anchored to the caption under [User Design](userdesign.md#article-content-and-writing-standards). Deliver the images within the Doc without uploading separate original-image files to Drive. Add missing-information comments under [Review, Revision, and Writing Feedback](userdesign.md#review-revision-and-writing-feedback); plain-text notes do not replace Google Doc comments.

Verify that the actual customer Doc preserves the evaluated article and its required comments under [Engineering](engineering.md#article-verification). A local export or successful upload alone does not establish delivery. Correct transfer or rendering failures. If correction changes the evaluated article, use Evaluate and Revise to check the resulting version before claiming delivery complete.

Record the correct Doc link and status in the batch Sheet under [Data Model](data-model.md#assignments-and-article-status). Use Needs Information for required facts awaiting Alex; otherwise use Ready for Review after the checks pass. Delivery is complete when the Doc, comments, link, and status are correct.

When Alex provides information or feedback, revise the same Doc and use Evaluate and Revise before updating its status under User Design. Accepted requires Alex's confirmation.
