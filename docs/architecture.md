# Architecture

Architecture defines how components work together to produce and maintain the content production product’s required outcomes. Each section establishes a distinct architectural responsibility. Read the sections governing the affected components and operations, and follow references to their dependencies.

Product owns system purpose and scope; User Design owns product-user behavior, language and voice; Writing Standards owns article content and writing standards; Data Model owns record meanings, identity and validity; Engineering owns implementation discipline and verification; Release owns deployment and recovery; AGENTS owns agent responsibilities, authorization and governing-document changes. Architecture references those requirements and defines how components fulfill them.

## Article Production Flow

Process each assigned article through the stages below. The production system carries out the research, drafting, checks, and revisions needed for direct customer delivery under [User Design](userdesign.md#assignment-delivery-and-tracking).

Review the client’s website as needed at different stages for different purposes. Keep unresolved questions explicit and carry them forward. Later evidence may change the working interpretation or require further investigation in an earlier stage. Follow the research order in [Writing Standards](writing-standards.md#practice-research-and-provider-coverage): research the client’s own website before using third-party sources.

### Understand the Assignment

Produce a structured assignment brief that gives the next stage a clear target for investigation.

Preserve the supplied client, prompt number, original title, SEO/AEO label, reference URLs, and special instructions so Alex can trace the article to its assignment. Keep the supplied assignment distinct from its interpretation. Preserve the prompt number through revisions as required by [Data Model](data-model.md#assignments-and-article-status).

Use the assignment and a focused review of the client’s website to infer the target reader and the main question or decision the article should address. Choose one working interpretation, record it as a hypothesis with its supporting evidence, and move forward. Do not maintain competing interpretations. Revise the hypothesis if later evidence warrants a change.

Flag claims implied by the title for verification, including claims about superiority, permanence, pricing, availability, or provider expertise. The assigned title does not establish that those claims are true. Record missing inputs and material uncertainties explicitly.

This stage is complete when the structured brief records the working audience and article purpose, supplied constraints, supporting evidence, claims to investigate, and explicit unknowns. Unresolved practice facts may remain open. Interpret the assigned topic without silently replacing it; a proposed topic change requires resolution with Alex.

### Understand the Practice

Produce supported, article-specific practice findings that establish the context needed to plan the topic research.

Use the assignment brief to research the relevant services, treatments, technology, providers, credentials, locations, practice approach, terminology, and differentiators on the client’s website. Identify relevant service, provider, educational, contact, and booking links. Investigate the practice-specific claims flagged in the brief.

Record supporting website evidence alongside the article’s research. Preserve the distinctions between physical locations and article target geography, between treatments and bookable appointments, and the correct provider associations defined in [Data Model](data-model.md#client-information).

Research the practice for this article. Completion does not require a general client model or a full inventory of the practice. This stage is complete when the findings establish the relevant practice context and identify any facts needed for the article that the website did not establish. State what fact is missing and why the article needs it. Revise the assignment hypothesis when the findings warrant it.

### Plan the Research

Produce a structured, article-specific research plan from the assignment brief and practice findings. Plan the investigation here; carry it out in Research and Resolve.

Identify the main and supporting questions the article must answer, the claims requiring verification, and the specific practice facts still needed. For each investigation, state the question or claim, why it matters to the article, what evidence would adequately resolve it, and which sources to consult. Identify questions that only Alex can resolve, using the missing-information process in [User Design](userdesign.md#review-revision-and-writing-feedback).

Include the supplied reference URLs and client website as research starting points, and authoritative third-party sources to verify relevant claims. Treat the supplied references as starting points rather than material to rewrite, as required by [Writing Standards](writing-standards.md#practice-research-and-provider-coverage).

Plan a review of the leading organic Google results for the same topic. Derive research queries from the assignment and working interpretation, including geography when relevant. Plan to examine the reader questions, treatments, comparisons, considerations, answer structure, omissions, and weak explanations in the competing articles to identify how this article can be more useful.

Search ranking identifies competing answers to examine; it does not establish medical accuracy. Plan authoritative verification of relevant claims and develop an original article. Researching competitor pages does not permit linking to direct competitors in the delivered article; the [Writing Standards for external links](writing-standards.md#links-and-closing-call-to-action) still apply.

This stage is complete when the plan gives Research and Resolve clear investigation questions, sources to consult, and criteria for determining whether each question has been answered. A plan is not a set of verified findings.

### Research and Resolve

Produce an article-specific research record that supports the article’s central answer and gives Build the Outline supported findings and explicit limits.

Carry out the research plan using the supplied references, relevant practice pages, authoritative sources, and leading organic Google results. Record answers with their supporting evidence. Identify useful reader questions and omissions in competing articles. Investigate conflicting information and revise the working assignment hypothesis when the evidence warrants it.

For each unresolved question, assess what the missing answer prevents the article from establishing. Record the missing fact, the planned claims or sections that depend on it, what would change under plausible answers, and the chosen next action. Apply [Writing Standards](writing-standards.md#medical-claims-and-optional-supporting-material) to distinguish required facts from optional enhancements. Assess the dependency of this article rather than assigning a fixed classification to a kind of fact.

Handle each unresolved question according to its effect on the article:

- If the material would improve the article but is not needed to answer the assigned question, plan to omit it and prepare the optional-material comment required by [User Design](userdesign.md#review-revision-and-writing-feedback).
- If a required fact needs Alex’s confirmation and can be inserted later without changing the supported explanation or outline, plan a visible marker and a Google Doc comment at the relevant location. The draft follows User Design’s Needs Information process.
- If the missing answer could change the premise, treatment focus, central answer, or recommendation, investigate further before committing to an outline. If only Alex can resolve the direction, record the specific question for him and keep that dependency unresolved.

Make the dependency assessment automatically from the assignment brief, research plan, and findings. Its reliability must be verified under [Engineering](engineering.md#article-verification) before relying on it for direct delivery; recording a decision does not establish that the judgment is correct.

This stage is complete when the central answer has supporting evidence and each remaining question has a clear disposition. A marker does not establish a supported direction when the article’s premise remains unresolved.

### Build the Outline

Produce a practice-specific outline that shows how the article will answer the assigned question for its intended reader. Select coverage for relevance, supported answers, and distinct reader value under [Writing Standards](writing-standards.md#reader-answer-and-substantive-content), rather than assigning section word budgets.

Use the assignment brief, practice findings, and research record to state the main answer and arrange the reader's questions into a useful sequence. For each planned section, record its heading, the reader question it answers, the supported answer and evidence, and the distinct information it adds beyond other sections. A section purpose alone is insufficient if the outline cannot yet state its answer.

Place practice and provider information where it adds relevant context under [Writing Standards](writing-standards.md#practice-research-and-provider-coverage). Identify which planned passages would need factual rewriting for another practice and connect them to supporting practice evidence. If the outline relies only on interchangeable names, credentials, locations, or links, return to practice research. Plan useful internal links, appropriate external links, and the closing call to action under [Writing Standards](writing-standards.md#links-and-closing-call-to-action).

Identify where unresolved required facts need markers and comments. If outlining exposes an unsupported central answer or a dependency that changes the direction, return to research. Merge or remove sections that repeat another answer, and exclude material that does not support its heading. If research cannot support the coverage needed to answer the assigned question, report the specific gap for an operator decision rather than invent material or silently change the assignment.

This stage is complete when the outline covers the assigned question, connects each planned answer to evidence, and identifies each section's distinct reader value and the article's meaningful practice context. It must give drafting a clear basis for writing the whole article. Evaluate and Revise measures the resulting draft's length and resolves findings.

### Write the First Draft

Produce a complete article from the outline and supported research, following the applicable standards owned by [Writing Standards](writing-standards.md).

Follow the outline while allowing changes that improve clarity and flow. Integrate practice and provider details naturally, include the planned links and customized call to action, and place visible markers for unresolved required facts. Prepare the associated questions for Google Doc comments. Flag any new factual claims introduced during writing for verification.

Use a machine-readable representation of the applicable writing standards to guide drafting and run basic checks automatically on the completed draft. Preserve the standards’ conditions, exceptions, and assignment overrides. Basic checks include word count, heading structure, link counts and repeated destinations, phone-number formatting, known business-name spelling, and listed generic phrases. Apply the active requirements in Writing Standards; do not turn unresolved customer questions into additional checks or delivery dependencies.

This stage is complete when the whole article is written and basic check findings and unresolved claims are available to Evaluate and Revise. The first draft need not pass every check before entering evaluation.

### Evaluate and Revise

Produce a revised article that satisfies the applicable quality standards and final length range, with any required facts still needing Alex's input handled under [User Design](userdesign.md#review-revision-and-writing-feedback).

Automatically evaluate the complete article against the applicable writing standards, assignment brief, practice findings, research evidence, and outline. Run deterministic checks and automated editorial and evidence assessments as part of the flow, without a manual trigger or Vikas's article-by-article review. Use the same applicable standards that guide drafting, and apply [Engineering's verification requirements](engineering.md#article-verification).

Assess substantive coverage, reader-question coverage, factual support, quotations and reviews, medical claims, natural terminology, links, localization, call to action, voice, readability, formatting, and proofreading. Verify that each paragraph, bullet, and example supports its heading and that sections add distinct reader value under [Writing Standards](writing-standards.md#reader-answer-and-substantive-content). Apply the [practice-substitution test](writing-standards.md#practice-research-and-provider-coverage); return to practice research and revision when customization fails. Counts and detected phrases establish only what those checks measure; they do not establish substantive content, medical accuracy, or editorial quality. Assessment methods and evidence of their reliability belong in Engineering.

After assessing article quality, measure the body-word count against the range defined in Writing Standards. If the draft exceeds the range, remove tangents, repetition and lower-value detail, and make useful explanations more concise. If it falls below the range, identify useful explanations or relevant practice context that remain underdeveloped; return to research when needed. Do not pad the article or cut necessary information merely to meet the range.

Automatically correct issues the system can resolve, returning to research or outlining when needed. Repeat affected checks after revisions, including quality and evidence assessments affected by length changes. Evaluate the resulting article version rather than treating checks on an earlier version as proof that the revised article passes. Repeat evaluation until the article satisfies both the quality standards and the length range. If those requirements cannot be reconciled, report the specific conflict to the operator and keep the article incomplete.

When a required fact needs Alex's input, retain supported content, the visible marker, and the question prepared for a Google Doc comment. Missing optional material follows User Design's optional-material process. Missing information does not excuse other failed checks. If the system cannot resolve another failure, keep the finding explicit and the article incomplete rather than mark it Ready for Review.

This stage is complete when the resulting article completes the applicable checks, apart from explicitly identified required facts awaiting Alex's input. Such facts follow the Needs Information process. Articles with required facts resolved proceed to delivery as Ready for Review under User Design. Verification does not establish customer acceptance.

### Deliver to Alex

Deliver the article directly to Alex through the Google Drive, Docs, and Sheet experience defined in [User Design](userdesign.md#assignment-delivery-and-tracking), without requiring Vikas’s review or approval of the individual article.

Put the article in its assigned Google Doc and preserve the content, headings, links, and markers that were evaluated. Add questions about missing required facts as Google Doc comments at the relevant locations, asking Alex to supply or confirm the facts. Add the comments for missing optional material required by [User Design](userdesign.md#review-revision-and-writing-feedback). Plain-text notes do not replace those comments.

Verify the delivered Doc preserves the evaluated article and its required comments. If delivery changes the article in a way that affects a check, repeat the affected check. Record the correct Doc link and status in the batch Sheet. Use Needs Information when required facts await Alex’s input; otherwise use Ready for Review after the production checks are complete. The status meanings are owned by [Data Model](data-model.md#assignments-and-article-status).

Delivery is complete when the article Doc, required comments, Doc link, and batch status are correct. Accepted status requires Alex’s confirmation under User Design’s review process. When Alex supplies information or editorial feedback, revise the same Doc, repeat affected research and checks, and update the status according to that process.
