# User Design

User Design owns the operator and customer experience: what Vikas can accomplish and inspect, how articles are presented and delivered to Alex, and how Alex provides information, feedback, and acceptance. It defines product interactions, presentation, and interface language. [Writing Standards](writing-standards.md) owns the articles’ content and writing voice.

[Product](product.md) owns the required outcomes and scope. [Architecture](architecture.md#article-production-flow) owns how production fulfills this experience; [Data Model](data-model.md) owns records and their meanings; [Engineering](engineering.md#article-verification) owns verification. [Release](release.md) owns product deployment and recovery. [AGENTS](../AGENTS.md) owns agent conduct, communication with the operator, and governing-document changes.

## Article Content and Writing Standards

Articles must meet [Writing Standards](writing-standards.md), the consolidated content and writing specification. That document owns the style-guide baseline, assignment additions, applicability, approved interpretations, material eligibility, and writing conventions.

Present each article using text and links in its Google Doc. Use [Blog Agent — Article Doc Template](https://docs.google.com/document/d/16J68VvFNHnmiE7MPop_gU0Xye-1tzMYwp_RdaedU3L0/edit) as the presentation template for current and future article Docs. Create new article Docs by copying this template. Match its fonts, heading sizes, compact spacing and intro order. Replace its assignment details, reference links, batch, date, agent version and article with those for the delivered assignment. Keep the review note separate from the article, without adding section labels or a page break.

Vikas receives the compact support-and-check record for the resulting article, including its final checklist outcome, remaining failures, and required facts awaiting Alex. This supports confidence in delivery without requiring Vikas to approve each article. [Data Model](data-model.md#assignments-and-article-status) defines the record and status meanings.

The system delivers articles directly to Alex under [Assignment Delivery and Tracking](#assignment-delivery-and-tracking). Missing required facts and optional material follow [Review, Revision, and Writing Feedback](#review-revision-and-writing-feedback). [Data Model](data-model.md#article-research-material) defines retained research evidence, and [Client Information](data-model.md#client-information) defines valid client associations. [Architecture](architecture.md#article-production-flow) owns production and the single evaluation and revision flow; [Engineering](engineering.md#article-verification) owns verification methods and evidence.

## Assignment Delivery and Tracking

The system prepares and delivers assigned articles directly to Alex without requiring Vikas to review or approve individual articles. Create each article Doc with Commenter access for Alex Burgos (alex@bmpteam.com) and Peter Psillos (peter@bmpteam.com), with sharing email notifications disabled. Vikas retains Owner access. The reusable article template remains private. Vikas can monitor assignment progress, delivered articles, and unresolved issues through the batch Sheet and article Docs.

Each assignment batch has a Google Drive folder containing one subfolder per client and one Google Doc per article.

Each Doc’s filename includes the client name, assignment prompt number, SEO or AEO type, and article title so Alex can match the article to its assignment. [Data Model](data-model.md#assignments-and-article-status) defines the fixed prompt number through revisions.

The batch folder contains a Google Sheet with one row per assigned article. Each row includes the client, prompt number, SEO or AEO type, article title, Doc link, and status. The initial batch tracks all 52 articles in [Product’s assignment scope](product.md#assignment-scope).

The supported status labels are Drafting, Needs Information, Ready for Review, Revising, and Accepted. [Data Model](data-model.md#assignments-and-article-status) defines their meanings. The [Review, Revision, and Writing Feedback](#review-revision-and-writing-feedback) section defines the review interactions and status changes.

## Review, Revision, and Writing Feedback

Delivered articles must meet the applicable company, client, and assignment requirements and match the quality of content produced by Benchmark’s writers. Alex reviews the articles as the customer. In the current product version, this provides human review after delivery; human review is not required before delivery. AI review does not establish human review or acceptance. Customer confirmation remains open in [Roadmap](roadmap.md#open-questions-for-alex). Acceptance depends on both compliance with the writing standards and Alex’s subjective judgment of the article’s content and quality. Alex’s acceptance determines whether the articles meet [Product’s quality goal](product.md#purpose-and-scope).

Alex reviews each article through comments and suggested edits in its Google Doc. Revisions use the same Doc and address his feedback. The batch Sheet records the article’s current status.

Alex is the contact for missing or conflicting client information. [Architecture's Research and Resolve](architecture.md#research-and-resolve) determines whether to omit a detail, resolve the article's direction before drafting, or deliver supported content with a required fact awaiting Alex. Use the following comments and status interactions for gaps that can remain in the delivered article.

For missing optional material, prepare the article without that material and add a comment at the relevant location explaining what could improve the article and asking Alex to supply it. Optional requests do not prevent Ready for Review.

For a required fact that can be inserted without changing the supported direction, place a clear marker where the fact belongs and add a Google Doc comment explaining what Alex must supply or confirm. Deliver as Needs Information only after the article passes the applicable checks apart from the permitted missing facts, under [Architecture](architecture.md#evaluate-and-revise). Alex can answer in the comment or suggest text directly.

When Alex supplies the required information, move the article to Revising while incorporating it. Once required facts are resolved and the revised article passes [Architecture's evaluation and revision flow](architecture.md#evaluate-and-revise), move the article to Ready for Review.

Completing revisions does not itself establish acceptance. Alex confirms acceptance; unresolved required facts prevent Accepted status.

Alex’s feedback guides revisions to the current article and, where applicable, improvements to future writing for that client or across clients.
