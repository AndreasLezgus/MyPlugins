# Content Creation Plugin

A content creation plugin primarily designed for [Cowork](https://claude.com/product/cowork), Anthropic's agentic desktop application — though it also works in Claude Code. Analyze provided content, create a blog post, create a substack artikel, create substack notes, create linkedIn article. Maintain my brand voice consistency, my writing style, my quality gates and my visual style.

## Installation

```download plugin.zip file into claude Cowork Plugin directory
```

## Commands

| Command | Description |
|---|---|
| `/draft-blog-post` | Draft blog posts, social media, email newsletters, landing pages, press releases, and case studies |
| `/draft-substack-article` | Generate a full campaign brief with objectives, channels, content calendar, and success metrics |
| `/draft-substack-notes` | Review content against your brand voice, style guide, and messaging pillars |
| `/drafts-linkedin-article` | Research competitors and generate a positioning and messaging comparison |
| `/seo-audit` | Run a comprehensive SEO audit — keyword research, on-page analysis, content gaps, technical checks, and competitor comparison |

## Skills

| Skill | Description |
|---|---|
| `blog-post-creation` | Content type templates, writing best practices by channel, SEO fundamentals, headline formulas, and CTA guidance |
| `substack-article-creation` | Content type templates, writing best practices by channel, SEO fundamentals, headline formulas, and CTA guidance |
| `substack-notes-creation` | Content type templates, writing best practices by channel, SEO fundamentals, headline formulas, and CTA guidance |
| `linkedin-article-creation` | 
Content type templates, writing best practices by channel, SEO fundamentals, headline formulas, and CTA guidance |
| `brand-voice` | Brand voice documentation, voice attributes, tone adaptation, style guide enforcement, and terminology management |
| `visual-style` | visual style attributes, style guide enforcement, logos and hero-images |


## Example Workflows

### Drafting a Blog Post

```
> /draft-blog-post
Type: blog post
Topic: Research Gartner article
Audience: IT-Leadership Team, CEO, CIO, CTO, Governance Leaders
Key messages: AI saves time on repetitive tasks, improves personalization, requires human oversight
Tone: Authoritative but approachable
Length: 1200 words
```

Claude will generate a structured blog post draft with an engaging headline, introduction with a hook, organized sections, SEO-optimized subheadings, and a clear call to action.

### Drafting a substack article

```
> /draft-substack-article
Type: substack article
Topic: Research Gartner article
Audience: IT-Leadership Team, CEO, CIO, CTO, Governance Leaders
Key messages: AI saves time on repetitive tasks, improves personalization, requires human oversight
Tone: Authoritative but approachable
Length: 1200 words
```

Claude will generate a structured substack article with an engaging headline, introduction with a hook, organized sections, SEO-optimized subheadings, and a clear call to action.

### Drafting substack notes

```
> /draft-substack-notes
Type: substack notes
Topic: Research Gartner article
Audience: IT-Leadership Team, CEO, CIO, CTO, Governance Leaders
Key messages: AI saves time on repetitive tasks, improves personalization, requires human oversight
Tone: Authoritative but approachable
Length: 500 words
```

Claude will generate a structured substack note with an engaging headline, introduction with a hook, organized sections, SEO-optimized subheadings, and a clear call to action.

## Configuration

Configure your brand voice, style guide, and target personas in a local settings file for personalized output. This allows commands like `/draft-content` and `/brand-review` to automatically apply your brand standards without prompting each time.

## MCP Integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

This plugin works with the following MCP servers:

- **Devonthink** — Share content, pdf, research articles
- **Drafts** — Create and edit drafts
- **Ulysses** — Create and edit blog post, substack articles and notes, linkedIn articles
- **Noteplan** — Create and edit meeting notes, daily planning, weekly planning, special tasks

