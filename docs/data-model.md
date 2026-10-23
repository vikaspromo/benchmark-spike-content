# Data Model

## Client Information

Client information can include multiple websites and physical locations. Keep each fact associated with the client, clinician, location or treatment it concerns. Distinguish physical locations from article target geography, and treatments from bookable appointments. Clinician roles, credentials and treatment associations must refer to the correct person.

## Article Research Material

Keep source links and the passages needed to verify the resulting article’s factual claims and practice associations in its support-and-check record under [Assignments and Article Status](#assignments-and-article-status). Retain material limits or conflicts when they affect those claims or unresolved issues. Sources can support several passages; do not repeat the same evidence for each occurrence. [Writing Standards](writing-standards.md#content-types) owns material eligibility.

Distinguish source statements from interpretation and unknown associations from confirmed ones. Evidence for one product does not establish another formulation or device model.

## Assignments and Article Status

Identify an assignment by its original assignment reference, client and supplied prompt number. The prompt number remains fixed through revisions. [User Design](userdesign.md#assignment-delivery-and-tracking) defines how assignment identity appears in article filenames and the review index.

An **article version** identifies a retained draft or revision of one assignment. The **agent version** is the repository commit identifying the governing requirements actually used to produce that article version. The customer Doc URL identifies the shared review document, which can contain later article versions under [User Design’s revision experience](userdesign.md#review-revision-and-writing-feedback).

Retain two items for each drafted article version: the article and one compact support-and-check record. Keep posted customer comments in the linked Google Doc. The record contains:

- **Identity:** A reference to the original assignment, the exact article version checked and the customer Doc URL once the Doc exists.
- **Article status:** The current status under the meanings below.
- **Production inputs:** The agent version. If relevant production inputs were uncommitted, include their exact diff; the commit alone does not identify those inputs.
- **Claim support:** The source evidence required by [Article Research Material](#article-research-material).
- **Final checks:** The outcome for every applicable requirement, concise evidence sufficient to establish each result, and the measured body-word count. A failure identifies the requirement, location, and correction needed. Keep required facts awaiting Alex, optional requests, and inapplicable requirements distinct from passes and other failures. Identify unperformed or unverified checks explicitly.
- **Unresolved issues:** Only issues that still affect verification, revision or delivery. Until a prepared comment is posted to the customer Doc, retain its text and intended location here.

The article assessment is the final-check portion of this record. [Engineering](engineering.md#checklist-and-evidence) owns how evidence establishes each result; [Architecture](architecture.md#evaluate-and-revise) owns checking and revision.

Preserve reviewed article versions with the evidence for their checks. Keep current status, customer Doc links and other delivery information up to date in the same record, replacing superseded delivery information.

Briefs, plans, outlines, research for assignments not yet drafted, investigation notes, intermediate checks and transfer files are working material. Keep that material while it is needed for authorized work under [AGENTS](../AGENTS.md#identify-the-required-changes). Once the article and support-and-check record contain the needed evidence and unresolved issues, separate working material is no longer required. Do not retain production histories or duplicate research, assessment and provenance records.

Article status has the following meanings, using the labels defined in [User Design](userdesign.md#assignment-delivery-and-tracking):

- Drafting: The article is being prepared for Alex's review; this includes unresolved checklist failures before delivery.
- Needs Information: A draft is available with required facts still missing and no other unresolved checklist failures.
- Ready for Review: Required facts are resolved and the resulting article has passed the applicable checks for Alex's editorial review.
- Revising: Alex's information or editorial feedback is being incorporated.
- Accepted: Alex has confirmed that the completed article meets his expectations, with no unresolved required facts.

[User Design](userdesign.md#review-revision-and-writing-feedback) defines the customer review interactions and status changes.
