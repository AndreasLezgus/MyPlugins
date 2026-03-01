# Content Creation Plugin

A content creation plugin primarily designed for [Cowork](https://claude.com/product/cowork), Anthropic's agentic desktop application — though it also works in Claude Code. Analyze provided content, create a blog post, create a substack artikel, create substack notes, create linkedIn article. Maintain my writing style consistency, my visual design and my quality gates.

## Installation

```download plugin.zip file into claude Cowork Plugin directory
```

## Commands

| Command | Description |
|---|---|
| `/draft-blog-post` | Draft blog posts for my ghost blog. Publish with ulysses app. Content from Devonthink Research |
| `/draft-substack-article` | Draft substack article. Publish with ulysses app. Content from Devonthink Research |
| `/draft-substack-notes` | Draft substack notes. Publish with ulysses app. Content from Devonthink Research |
| `/drafts-linkedin-article` | Draft linkedin article. Publish with ulysses app. Content from Devonthink Research |

## Skills

| Skill | Description |
|---|---|
| `content-creation-pipeline` | Content type writing-style,visual-design, quality-gates, Content type workflows, writing best practices by channel, SEO fundamentals, headline formulas, and CTA guidance |



## Example Workflows

### Drafting a Blog Post

```
> /draft-blog-post
Type: blog post
Topic: Research from Gartner article oder PDF-Research
Audience: IT-Leadership Team, CEO, CIO, CTO, Governance Leaders
Key messages: AI without governance is shadow ai, requires human oversight and minimum vaiable policies
Tone: Authoritative but approachable
Length: 1200 words
```

Claude will generate a structured german blog post draft with an engaging headline, introduction with a hook, organized sections, SEO-optimized subheadings, and a clear call to action. Claude create the draft in ulysses app to edit and curate in a special folder.

### Drafting a substack article

```
> /draft-substack-article
Type: substack article
Topic: Research from Gartner article oder PDF-Research
Audience: IT-Leadership Team, CEO, CIO, CTO, Governance Leaders
Key messages: AI without governance is shadow ai, requires human oversight and minimum vaiable policies
Tone: Authoritative but approachable
Length: 1200 words
```

Claude will generate a structured english substack article with an engaging headline, introduction with a hook, organized sections, SEO-optimized subheadings, and a clear call to action. Claude create the draft in ulysses app to edit and curate in a special folder.

### Drafting substack notes

```
> /draft-substack-notes
Type: substack notes
Topic: Research from Gartner article oder PDF-Research
Audience: IT-Leadership Team, CEO, CIO, CTO, Governance Leaders
Key messages: AI without governance is shadow ai, requires human oversight and minimum vaiable policies
Tone: Authoritative but approachable
Length: 500 words
```

Claude will generate 30 english structured substack notes with an engaging headline, introduction with a hook, organized sections, SEO-optimized subheadings, and a clear call to action. Claude create the drafts in ulysses app to edit and curate in a special folder.

## Configuration

Configure your writing style, visual style, and quality gates in a local settings file for personalized output. This allows commands like `/content-creation-pipeline` to automatically apply your brand standards without prompting each time.

## MCP Integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

This plugin works with the following MCP servers:

- **Devonthink** — Share content, pdf, research articles
- **Drafts** — Create and edit drafts
- **Ulysses** — Create and edit blog post, substack articles and notes, linkedIn articles
- **Noteplan** — Create and edit meeting notes, daily planning, weekly planning, special tasks

