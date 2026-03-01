---
description: Draft blog posts with ulysses app, from ulysses app connect to publish on personal ghost blog
argument-hint: "<content type and topic>"
---

# Draft Content

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate blog content drafts tailored to a specific content type, audience, and brand voice.

## Trigger

User runs `/draft-blog-post` or asks to draft, write, or create blog content.

## Inputs

Gather the following resaerch article from devonthink folder: `x-devonthink-item://8AB280B1-55E7-4B02-ABFE-3B761CC58B2`. If not provided, ask before proceeding:

1. **Content type**
   - Blog post for ghost blog
   
2. **Topic** — the subject or theme of the content

3. **Target audience** — `/content-creation-pipeline/references/writing-style.md`

4. **Key messages** — 2-4 main points or takeaways to communicate

5. **Tone** — `/content-creation-pipeline/references/writing-style.md`

6. **Length** — Length: 1,200–1,800 words (5–7 minutes reading time). Structure: Introduction (max. 150 words), 3–5 main sections with H2 subheadings, conclusion with concrete actionable recommendation. Each section max. 300 words.

## Brand Voice

- Use the brand voice: `/content-creation-pipeline/references/writing-style.md` Inform the user that brand voice settings are being applied.
- If no brand voice is configured, ask: "Do you have brand voice guidelines you'd like me to follow? If not, I'll use a neutral professional tone."
- Apply the specified or default tone consistently throughout the draft.

## Content Generation by Type

### Blog Post
- Use the skill workflow: `/content-creation-pipeline/workflows/blog-post-creation.md`  
- SEO considerations: suggest a primary keyword, include it in the headline and first paragraph, use related keywords in subheadings

## SEO Considerations (for web content)

For blog posts:
- Suggest a primary keyword based on the topic
- Recommend keyword placement: headline, first paragraph, subheadings, meta description
- Suggest internal and external linking opportunities
- Recommend a meta description (under 160 characters)
- Note image alt text opportunities

## Output

Create the draft in the Ulysses folder: 


