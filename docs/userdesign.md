# User Design

## Article Content and Writing Standards

Articles must meet [Writing Standards](writing-standards.md). Omit body-word counts from the customer article.

Present each article using text and links in a pageless Google Doc copied from [Blog Agent — Article Doc Template](https://docs.google.com/document/d/16J68VvFNHnmiE7MPop_gU0Xye-1tzMYwp_RdaedU3L0/edit). Match the template’s fonts, heading sizes, 12-point article body and spacing.

The preface contains only the client and SEO/AEO prompt number; batch, date and Agent version; original assignment title; and supplied reference links, in that order. Replace the template’s details with those for the delivered assignment. Start without a leading blank line and retain one blank paragraph between the preface and article.

## Assignment Delivery and Tracking

The system prepares and delivers assigned articles directly to Alex without requiring Vikas to review or approve individual articles. Give Alex Burgos (alex@bmpteam.com) and Peter Psillos (peter@bmpteam.com) Commenter access to each article Doc, with sharing email notifications disabled. Commenter access permits comments and suggested edits while preventing direct text changes. Vikas retains Owner access. The reusable article template remains private.

Keep the articles in a dedicated Benchmark folder on Vikas’s personal Google Drive, with a folder for each batch, client subfolders and one Google Doc per article. Each Doc’s filename includes the client name, assignment prompt number, SEO or AEO type, article title and article version. [Data Model](data-model.md#assignments-and-article-status) defines assignment identity and production inputs.

Use the same [review index](https://docs.google.com/spreadsheets/d/19pXjqiOHhgViaEOoUtpAzk22LcQqLMmfHFLVjaxbq8Y/edit) across batches so Alex can bookmark it. The index contains one row per article delivered for review, including permitted Needs Information drafts under [Review, Revision, and Writing Feedback](#review-revision-and-writing-feedback). Its columns, in order, are Batch, Client, Assignment, Draft article and Agent version. Assignment identifies the prompt number and SEO/AEO type. Draft article contains the article title as a blue, underlined link to its Doc. The final column shows the [agent version](data-model.md#assignments-and-article-status). Increment Batch for each new batch and sort complete rows by Batch descending so the newest batch appears first. The review index has no Status column.

Separate adjacent batches with one empty row filled light gray across all review-index columns.

Vikas receives the compact support-and-check record for each resulting article and uses it to monitor progress, the current article status, remaining failures and required facts awaiting Alex. The supported status labels are Drafting, Needs Information, Ready for Review, Revising and Accepted. [Data Model](data-model.md#assignments-and-article-status) defines the record and status meanings. The review index and article Docs provide access to delivered work; production status remains in the support-and-check record.

## Review, Revision, and Writing Feedback

Alex reviews delivered articles through comments and suggested edits in their Google Docs. His review provides human review after delivery; human review is not required before delivery. Alex’s review determines whether the articles meet [Product’s quality goal](product.md#goals). Acceptance depends on compliance with Writing Standards and Alex’s judgment of content and quality. AI review does not establish human review or customer acceptance. Completing revisions does not itself establish acceptance. Alex confirms acceptance; unresolved required facts prevent Accepted status.

Revisions address Alex’s feedback in the same Doc and follow [Architecture’s evaluation and revision flow](architecture.md#evaluate-and-revise). Update the article status in the support-and-check record as the revision progresses.

Alex is the contact for missing or conflicting client information. [Architecture’s Research and Resolve](architecture.md#research-and-resolve) determines which gaps must be resolved before drafting and which may remain in a delivered article. Use the following comments and status interactions for gaps permitted at delivery.

For missing optional material, prepare the article without it and add a comment at the relevant location explaining what could improve the article and asking Alex to supply it. Optional requests do not prevent Ready for Review.

For a required fact that can be inserted without changing the supported direction, place a clear marker where the fact belongs and add a Google Doc comment explaining what Alex must supply or confirm. Deliver as Needs Information only after the article passes the applicable checks apart from the permitted missing facts, under [Architecture](architecture.md#evaluate-and-revise). Alex can answer in the comment or suggest text directly.

When Alex supplies the required information, use Revising while incorporating it. Once required facts are resolved and the revised article passes Architecture’s evaluation and revision flow, use Ready for Review.

Alex’s feedback guides revisions to the current article and, where applicable, improvements to future writing for that client or across clients.
