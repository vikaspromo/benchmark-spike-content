# User Design

User Design defines what Vikas can accomplish through the content production product and the experience he receives. It also defines Alex’s customer review and acceptance interactions. It owns product capabilities, required information, information presentation, layout, interactions, and product-user-facing language and voice. Writing Standards owns the content and writing standards of the articles themselves.

Read the sections governing the affected user experience and follow references to its dependencies. Product owns system purpose and scope; Data Model owns record meanings, identity and validity; Architecture owns component responsibilities, processing and serving; Engineering owns implementation discipline and verification; Release owns deployment and recovery; AGENTS owns agent responsibilities, authorization and governing-document changes. Those documents reference User Design for product-user behavior, language and voice.

## Article Content and Writing Standards

Articles must meet [Writing Standards](writing-standards.md), the consolidated content and writing specification. That document owns the style-guide baseline, assignment additions, their applicability, approved interpretations, material eligibility, and the product exception for human review after delivery.

Selected images appear within the article Doc at locations that help explain the relevant content. Each image has a nearby caption explaining its relevance using supported details. Images and relevant labels must be clear enough to read, with proportions preserved and without cropping that changes their meaning. An image link or placement note does not replace an embedded image in the completed article. Image selection and captions follow [Writing Standards](writing-standards.md#practice-research-and-provider-coverage); this does not require images in every article.

The system delivers articles directly to Alex under [Assignment Delivery and Tracking](#assignment-delivery-and-tracking). Missing required facts and optional material are presented through [Review, Revision, and Writing Feedback](#review-revision-and-writing-feedback). [Data Model](data-model.md#article-research-material) defines the source material and intended-use records, and [Client Information](data-model.md#client-information) defines valid client associations. [Architecture](architecture.md#article-production-flow) defines acquisition, production, and delivery; [Engineering](engineering.md#article-verification) defines verification before submission.

## Assignment Delivery and Tracking

The system prepares and delivers assigned articles directly to Alex without requiring Vikas to review or approve individual articles. Vikas can monitor assignment progress, delivered articles, and unresolved issues through the batch Sheet and article Docs.

Each assignment batch has a Google Drive folder containing one subfolder per client and one Google Doc per article.

Each Doc’s filename includes the client name, assignment prompt number, SEO or AEO type, and article title so Alex can match the article to its assignment. [Data Model](data-model.md#assignments-and-article-status) defines the fixed prompt number through revisions.

The batch folder contains a Google Sheet with one row per assigned article. Each row includes the client, prompt number, SEO or AEO type, article title, Doc link, and status. The initial batch tracks all 52 articles in [Product’s assignment scope](product.md#assignment-scope).

The supported status labels are Drafting, Needs Information, Ready for Review, Revising, and Accepted. [Data Model](data-model.md#assignments-and-article-status) defines their meanings. The [Review, Revision, and Writing Feedback](#review-revision-and-writing-feedback) section defines the review interactions and status changes.

## Review, Revision, and Writing Feedback

Delivered articles must meet the applicable company, client, and assignment requirements and match the quality of content produced by Benchmark’s writers. Alex reviews the articles as the customer. Acceptance depends on both compliance with the writing standards and Alex’s subjective judgment of the article’s content and quality. Alex’s acceptance determines whether the articles meet [Product’s quality goal](product.md#purpose-and-scope).

Alex reviews each article through comments and suggested edits in its Google Doc. Revisions use the same Doc and address his feedback. The batch Sheet records the article’s current status.

Alex is the contact for missing or conflicting client information.

For missing optional material, prepare the article without that material and add a comment at the relevant location explaining what could improve the article and asking Alex to supply it. Optional requests do not prevent Ready for Review.

For missing required facts, draft the supported content and place a clear marker where each missing fact belongs. Add a comment explaining what Alex must supply or confirm. Set the status to Needs Information. Alex can answer in the comment or suggest text directly.

When Alex supplies the required information, move the article to Revising while incorporating it. Once required facts are resolved and revisions are complete, move the article to Ready for Review.

Completing revisions does not itself establish acceptance. Alex confirms acceptance; unresolved required facts prevent Accepted status.

Alex’s feedback guides revisions to the current article and, where applicable, improvements to future writing for that client or across clients.
