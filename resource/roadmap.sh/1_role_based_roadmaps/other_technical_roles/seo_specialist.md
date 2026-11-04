# SEO Specialist

## Metadata
- Type: Role
- Domain: Digital Marketing & Growth
- Source: roadmap.sh
- Source URL: https://roadmap.sh/seo
- Related Roles:
  - Frontend Developer
  - AI Engineer
  - Fullstack Developer

---

## 1. Beginner

### 1.1 Introduction
- **What is GEO**
  - GEO stands for Generative Engine Optimization. It is the practice of making content visible inside AI-generated answers, such as those produced by ChatGPT, Google AI Overviews, or Perplexity.
- **What is AEO**
  - AEO stands for Answer Engine Optimization. It focuses on structuring content so answer systems, such as featured snippets, voice assistants, and chat interfaces, can extract a direct answer from it.
- **Search Intent**
  - Search intent is the underlying goal behind a search query, such as wanting to buy something, learn something, or find a specific website. Two people can type different words but want the same thing, or type the same words and want different things.
- **Semantic Search**
  - Semantic search is a method of finding relevant content based on meaning rather than exact keyword matches. It allows a system to understand that "cheap flights" and "affordable plane tickets" refer to the same idea.
- **What is SEO**
  - SEO stands for Search Engine Optimization. It is the practice of improving a website so that search engines like Google can find it, understand it, and show it to people searching for related topics.

### 1.2 How Search Engines Work
- **Lexical vs Vector Search**
  - Lexical search matches the literal words in a query against the literal words in a document, similar to a find-and-replace function. Vector search instead converts text into numerical representations and matches based on meaning, so it can find relevant content even when no exact words overlap.
- **Retrieval vs Ranking**
  - Retrieval is the step where a search or AI system pulls a set of candidate documents that might answer a query, based on relevance matching. Ranking is a separate step that follows, ordering those retrieved candidates from most to least relevant.
- **Hybrid Search**
  - Hybrid search combines lexical and vector search in a single system, so it can catch exact matches, like product names or error codes, while also catching content that means the same thing but uses different words. This combination generally performs better than either method alone, since lexical search alone misses paraphrased content and vector search alone misses exact terms.
- **Crawling, Indexing, Ranking**
  - Search engines function by using automated programs called spiders or crawlers to scan the internet, discover web pages, and follow links from one site to another. Once these pages are found, the information is processed and stored in a massive database known as an index, where it is categorized based on content and relevance.
- **Personalization, Localization**
  - Personalization is when search results differ based on an individual user's history, preferences, or device. Localization is when results differ based on geographic location, showing nearby businesses or region-specific content.
- **Training Data vs Grounding**
  - Training data is the information an AI model learned from during its initial training process, baked into the model itself and not updated in real time. Grounding refers to an AI system retrieving current, external information at the moment it answers a question, rather than relying only on what it learned during training.
- **SERP, Index, Crawl**
  - A SERP, or Search Engine Results Page, is the page shown after someone runs a search. The index is the search engine's stored database of pages it has processed and can retrieve.

### 1.3 White, Black, Grey Hat SEO
- **Backlinks & Anchor Text**
  - A backlink is a link from one website pointing to another, treated by search engines as a signal of trust or endorsement. Anchor text is the clickable, visible text of that link, and its wording gives search engines additional context about what the linked page is about.
- **Canonical**
  - A canonical tag is a snippet of HTML code that tells search engines which version of a webpage is the primary or "master" version. When multiple pages on a website contain identical or very similar content, this tag prevents confusion by signaling to crawlers that they should treat these pages as one.
- **Nofollow, Noindex**
  - Nofollow, noindex, and disallow are instructions used to manage how search engines interact with your website. A "nofollow" tag tells search engines not to pass authority to a specific link, a "noindex" meta tag prevents a page from appearing in search results, and a "disallow" command in a robots.txt file instructs search engine crawlers to avoid scanning certain parts of your site entirely.

### 1.4 Spam Policies
- **Organic vs Paid vs Direct**
  - Organic traffic comes from unpaid search results. Paid traffic comes from search ads, marked separately from organic results.
- **Cloaking & Doorways**
  - Cloaking is showing search engines different content than what a real visitor sees, typically to manipulate rankings while displaying something else to users. Doorway pages are low-value pages created specifically to rank for narrow search terms and funnel visitors elsewhere, rather than serving as genuine destinations.
- **Link Schemes**
  - A link scheme is any pattern of link building designed to manipulate rankings rather than earned through genuine editorial merit, such as buying links, excessive link exchanges, or using automated programs to generate links at scale. Search engines explicitly prohibit these practices and can penalize sites found participating in them.
- **Scaled Content Abuse**
  - Scaled content abuse is producing large volumes of low-quality content, often with little to no human oversight, purely to manipulate search rankings rather than to genuinely help users. This has become a bigger focus for search engines as AI writing tools make it easier to generate content at scale without proportional quality.
- **Site Reputation Abuse**
  - Site reputation abuse is when a third party publishes low-quality content on a reputable site's subdomain or section, attempting to exploit that site's existing authority and trust for their own ranking gain. Google has specifically targeted this practice, since it previously let unrelated, low-quality content unfairly benefit from a trusted domain's reputation.
- **Expired Domain Abuse**
  - Expired domain abuse is buying a domain that previously had an established reputation and history, then repurposing it with unrelated content purely to exploit its existing authority and rankings. Search engines treat this as manipulative because the new content has no real connection to what earned that domain its original trust.

### 1.5 Manual Actions & Recovery
- **Manual Actions & Recovery**
  - A manual action is a penalty applied directly by a human reviewer at a search engine, usually for violating guidelines, which can significantly reduce or remove a site's visibility. Recovery means identifying and fixing the underlying issue, then submitting a reconsideration request asking the search engine to review and lift the penalty.

### 1.6 Algorithm Updates
- **Folders & URL Structure**
  - This is the organization of a website's URLs into logical folders that reflect the site's content hierarchy, such as grouping all blog posts under /blog/ and all products under /products/. Clear, readable URLs help both users and crawlers understand what a page is about before they even load it.
- **Core Updates**
  - A core update is a broad change to a search engine's overall ranking systems, intended to improve results generally rather than target a specific type of content or violation. Core updates can cause noticeable ranking shifts across many sites, and there is often no single fix beyond genuinely improving content quality and relevance over time.
- **Spam Updates**
  - A spam update is a change specifically targeting spam and manipulative practices, aiming to reduce the visibility of content that violates spam policies. Unlike core updates, spam updates are narrower and tend to affect only sites engaging in the targeted manipulative behavior.
- **Helpful Content System**
  - The Helpful Content System is a part of Google's ranking systems designed to reward content created primarily to help people, and demote content created primarily to rank in search engines. It evaluates signals like whether content demonstrates real experience and whether it exists mainly to attract search traffic rather than serve a genuine audience need.

### 1.7 Website Architecture
- **Site Hierarchy & Depth**
  - Site hierarchy is the structure of how pages relate to each other, from the homepage down through categories to individual pages. Depth refers to how many clicks it takes to reach a given page from the homepage.
- **Machine-Readable Content**
  - Machine-readable content is content structured in a way that a computer program can parse cleanly, rather than requiring visual interpretation the way a human reader would. This means using proper HTML structure, avoiding critical information hidden inside images or scripts, and keeping text in a form crawlers and AI systems can extract directly.
- **Internal Linking**
  - Internal linking is the practice of linking between pages on the same website. It helps crawlers discover new pages, distributes ranking authority across a site, and signals which pages are related to each other.
- **Tracking Volatility**
  - Tracking volatility means monitoring sudden, unexplained shifts in search rankings across a site or industry, which often signal that an algorithm update is rolling out. Practitioners use volatility tracking tools to distinguish a site-specific issue from a broader industry-wide ranking shift.

### 1.8 HTTP & Status Codes
- **Sitemaps**
  - A sitemap is a file that lists the pages on a website, helping search engines discover content that might otherwise be missed through normal crawling. It is typically submitted directly to a search engine through tools like Google Search Console.
- **Robots.txt**
  - Robots.txt is a text file placed at the root of a website that tells crawlers which parts of the site they are allowed or not allowed to visit. It can be used to block specific bots entirely, including AI crawlers, or to keep crawlers away from pages like admin panels or duplicate content.
- **Redirect Chains & Loops**
  - A redirect chain is a sequence of multiple redirects in a row before reaching the final destination page, which slows down loading and wastes crawl budget. A redirect loop is when a chain of redirects eventually points back to an earlier page in the sequence, creating an endless cycle that prevents the page from ever loading.

### 1.9 Crawling & Indexing
- **Crawl Budget**
  - Crawl budget is the amount of crawling capacity a search engine allocates to a given website within a certain time period. Large or poorly structured sites can burn through crawl budget on unimportant pages, leaving important pages crawled less often or not at all.
- **Googlebot**
  - Googlebot is the web crawler Google uses to discover and read pages across the internet, feeding the content it finds into Google's search index. It renders JavaScript reasonably well compared to most other crawlers, though heavy or slow-loading scripts can still cause parts of a page to be missed.
- **Bingbot**
  - Bingbot is the web crawler used by Microsoft's Bing search engine to discover and index web pages. It also supplies some of the underlying data used by other services built on Bing's index, so a page invisible to Bingbot can lose visibility beyond Bing itself.
- **GPTBot**
  - GPTBot is the crawler operated by OpenAI, used to gather web content for training AI models. A website can block it entirely through robots.txt if it does not want its content used for that purpose, though doing so may also reduce visibility in tools that rely on GPTBot for retrieval.
- **ClaudeBot**
  - ClaudeBot is a web crawler operated by Anthropic that browses the internet to collect data for training and improving its artificial intelligence models. It visits websites to read and process content, which allows Claude AI to understand and respond to user queries with updated information.
- **Google-Extended**
  - Google-Extended is a specific crawler control that lets a website choose whether Google can use its content to train Gemini and improve AI features like AI Overviews, separately from whether the site allows normal Googlebot crawling for search. Blocking it does not affect a site's regular search rankings, but can affect its visibility inside Google's AI-generated answers.
- **Index Coverage & Bloat**
  - Index coverage refers to how much of a website's content is actually included in a search engine's index versus excluded for various reasons. Index bloat is when a large number of low-value, thin, or duplicate pages get indexed, diluting a site's overall quality signals and making it harder for a search engine to focus on the pages that matter.
- **Log File Analysis**
  - Log file analysis is examining a website's raw server logs to see exactly how search engine crawlers are behaving, including which pages they visit, how often, and which ones they ignore. It gives a more accurate picture of actual crawler behavior than simulated crawls from third-party tools, since it reflects what really happened rather than what should happen.
- **Managing AI Crawlers**
  - Managing AI crawlers involves controlling how automated bots and large language model scrapers access and process the content on your website. This practice allows you to balance visibility for traditional search engines while maintaining control over how your proprietary data is consumed and utilized by emerging artificial intelligence technologies.
- **Controls & Pay-Per-Crawl**
  - Cloudflare offers tools that let website owners manage how AI crawlers access their content at the network level, including the ability to block known AI bots by default. Pay-per-crawl is a newer model where a site can charge AI companies for the right to crawl its content, rather than allowing free access or blocking it entirely.

### 1.10 Rendering & JavaScript SEO
- **Canonicalization**
  - Canonicalization is the process of telling search engines which URL is the official version of a page when the same content is reachable through more than one URL, such as with or without a tracking parameter. Without this, a search engine might treat duplicate versions of a page as separate, unrelated pages and split ranking signals between them.
- **Pagination**
  - Pagination is when content is split across multiple linked pages, such as page 1, page 2, and page 3 of a product listing. Handling it correctly means signaling to search engines that these pages are part of one continuous sequence, rather than unrelated content competing with each other.
- **Faceted Navigation**
  - Faceted navigation refers to filter and sort options on a website, such as filtering products by size or color, that can generate a huge number of similar or duplicate URLs. Without careful control, this can flood a crawler with near-identical pages and waste crawl budget on variations that add little unique value.
- **URL Parameters**
  - URL parameters are the extra pieces of a URL that follow a question mark, such as a sort order or tracking code. They can unintentionally create many different URLs that all lead to the same content, so managing how crawlers treat them helps avoid duplicate content issues.
- **Screaming Frog**
  - Screaming Frog is a desktop crawler tool that simulates how a search engine bot would crawl a website. It reports issues such as broken links, missing title tags, duplicate content, and pages blocked by robots.txt, and is one of the most widely used tools for technical SEO audits.
- **Sitebulb**
  - Sitebulb is a desktop crawler tool similar to Screaming Frog, used to audit a website's technical health. It is known for presenting results in a more visual, guided format, with prioritized issue lists and clearer explanations, making it a common alternative for practitioners who prefer a less raw, spreadsheet-style output.
- **SSR vs CSR vs Hydration**
  - Server-side rendering, or SSR, generates a page's full HTML on the server before sending it to the browser, so crawlers receive complete content immediately. Client-side rendering, or CSR, sends a mostly empty page and builds the content using JavaScript in the browser, which can be harder for some crawlers to process.
- **PerplexityBot**
  - PerplexityBot is the crawler operated by Perplexity, used to gather live web content when generating answers for its AI-powered search product. It can be allowed or blocked through a site's robots.txt file, similar to other AI crawlers.

### 1.11 Site Migrations
- **Planning & Checklists**
  - This is the preparation phase of a site migration, involving documenting the current site's structure, deciding what will change, and building a checklist to make sure nothing gets missed during the transition.

### 1.12 Core Web Vitals
- **PageSpeed Insights**
  - PageSpeed Insights is a free tool from Google that measures a page's loading speed and reports its Core Web Vitals scores. It gives specific, actionable suggestions for improving performance, such as compressing images or reducing unused code.
- **Domain & Protocol Changes**
  - A domain change is moving a website to an entirely new domain name. A protocol change is switching between HTTP and HTTPS, or between www and non-www versions of a URL.
- **Redirect Mapping**
  - Redirect mapping is the process of creating a complete list matching every old URL to its correct new destination during a site migration. Missing or incorrect mappings can cause pages to lose their rankings entirely, since search engines may treat an unmapped old URL as simply gone rather than moved.

### 1.13 Mobile Friendliness
- **Post-Migration Monitoring**
  - Post-migration monitoring is closely tracking a website's rankings, traffic, and crawl behavior in the period immediately following a migration, to catch and fix problems quickly before they cause lasting damage.

### 1.14 HTTPS & Security
- **HTTPS & Security**
  - HTTPS is a secure, encrypted version of the standard web protocol, shown to users as a padlock icon in the browser address bar. It is treated as a baseline trust signal by search engines rather than a major ranking factor on its own, and its absence can actively hurt user trust and conversion rates.

### 1.15 On-Page SEO
- **Formatting & Readibility**
  - Content formatting and readability covers how a piece of writing is structured for easy scanning and comprehension, including paragraph length, use of bullet points, and sentence complexity. Content that is easy to read tends to keep visitors engaged longer and is easier for both users and AI systems to extract information from.
- **Keyword Placement**
  - Keyword placement is where and how often target keywords appear within a page's content. Over-optimisation is repeating a keyword unnaturally often in an attempt to manipulate rankings, which can make content read awkwardly and may trigger a quality penalty rather than helping visibility.
- **Heading Structure**
  - Heading structure refers to how a page uses heading tags, from a single main heading down through subheadings, to organize content into a logical hierarchy. A clear heading structure helps both readers scan content quickly and helps search engines understand how a page's sections relate to each other.
- **URL Slugs**
  - A URL slug is the specific, readable part of a URL that identifies a particular page, such as the "best-running-shoes" portion of a product page's address. Short, descriptive slugs that reflect the page's content are generally easier for both users and search engines to understand than long or auto-generated ones.
- **Title Tags**
  - A title tag is the HTML element that defines the clickable headline shown in search results and browser tabs for a page. It is one of the most direct signals search engines use to understand what a page is about, and a well written title tag also directly affects whether someone clicks through from search results.
- **Meta Descriptions**
  - A meta description is a short summary in a page's HTML that search engines often display below the title in search results. It does not directly affect rankings, but a compelling meta description can improve click-through rate by giving searchers a clear reason to choose that result.
- **Internal Anchor Text**
  - Internal anchor text is the clickable, visible text used for links pointing between pages on the same website. Descriptive anchor text gives search engines additional context about the linked page's topic, while vague text like "click here" provides no useful signal.
- **Image Optimization**
  - Image optimisation is the practice of preparing images so they load quickly and remain accessible and understandable to both users and search engines, covering how images are described, named, compressed, and formatted.

---

## 2. Intermediate

### 2.1 Keyword Research
- **Semrush**
  - Semrush is an all-in-one SEO platform used for keyword research, rank tracking, competitor analysis, and backlink auditing. It also offers a dedicated AI Visibility Toolkit for tracking how a brand appears within AI-generated answers.
- **Ahrefs**
  - Ahrefs is an SEO platform widely used for backlink analysis, keyword research, and rank tracking. It maintains one of the largest independent indexes of backlinks on the web, making it a common choice specifically for link-building research.
- **Google Keyword Planner**
  - Google Keyword Planner is a free tool, originally built for Google Ads, that shows search volume estimates and keyword suggestions based on Google's own search data. It is often used as a baseline data source alongside paid third-party keyword tools.
- **Volume, Difficulty & Potential**
  - Search volume is an estimate of how many times a keyword is searched over a given period. Keyword difficulty estimates how hard it would be to rank for that term based on existing competition.
- **SERP Analysis**
  - SERP analysis is examining the actual search results page for a target keyword to understand what type of content currently ranks, what format it takes, and what features like snippets or panels appear alongside it. This informs decisions about what kind of content is likely to succeed for that specific query.

### 2.2 Topic Clusters
- **Topic Clusters**
  - A topic cluster is a group of related pages built around one core theme, usually with a central pillar page linking out to several supporting pages that go deeper into subtopics. This structure helps search engines and AI systems recognize a site as comprehensively covering a subject, rather than having just one isolated page on it.

### 2.3 Question Mining
- **People Also Ask**
  - People Also Ask is a feature in Google search results showing a list of related questions that expand to reveal short answers when clicked. It is a useful source of real, common questions people have around a topic, and getting featured in it can drive visibility even without a top-ranking position.
- **Forums & Communities**
  - Forums and communities, such as Reddit and Quora, are places where people ask questions and discuss topics in their own words, often more candidly than in polished articles. They are a valuable source of real questions and language for content research, and are increasingly pulled from directly by AI systems when forming answers.
- **AI Chat Prompts**
  - AI chat prompts are the actual questions and phrasings people type into AI assistants like ChatGPT when looking for information. Studying these gives insight into how people phrase requests conversationally, which often differs from how they type short keyword searches into a traditional search engine.

### 2.4 Competitor Gap Analysis
- **Competitor Gap Analysis**
  - Competitor gap analysis is the process of identifying the topics, keywords, and content formats that your competitors are ranking for but your website is not. By comparing your existing content against the top-performing pages in your industry, you can pinpoint specific areas where your site is missing information or failing to address user intent.

### 2.5 E-E-A-T
- **E-E-A-T**
  - E-E-A-T stands for Experience, Expertise, Authoritativeness, and Trustworthiness. It is a framework Google uses to judge the quality and credibility of content and its creator, rather than a direct, measurable ranking factor.

### 2.6 Information Gain
- **Information Gain**
  - Information gain is whether a piece of content adds something genuinely new, such as a fact, data point, or perspective, compared to what already exists in top search results. Content that only restates what is already widely available offers little reason for a search or AI system to prefer it over existing sources.

### 2.7 Primary Data & Visuals
- **Original Research & Surveys**
  - This means running your own study or survey instead of citing research that someone else already conducted. It produces original data that did not exist before, giving other sources, including AI systems, a reason to cite your content specifically as the origin.
- **Proprietary Datasets**
  - A proprietary dataset is information only you have access to, such as internal usage data, customer behavior, or transaction data, that a competitor cannot easily replicate. Publishing insights drawn from it gives content a form of information gain that is difficult for others to copy.
- **Case Studies & Benchmarks**
  - Case studies and benchmarks provide evidence-based insights by analyzing specific project outcomes and industry performance standards. A case study highlights the journey, challenges, and results of a particular initiative, while a benchmark compares performance metrics against established averages or competitor data.
- **Custom Charts & Images**
  - Custom charts and images are visuals created specifically for a piece of content, using original data rather than generic stock graphics. They give search and AI systems a unique visual asset tied to that content, rather than an image that could be found anywhere else.

### 2.8 Entity SEO
- **Entities vs Keywords**
  - A keyword is a string of text, such as "Nike shoes." An entity is the actual, specific thing behind it, such as Nike as a distinct company with a history and headquarters. Search and AI systems have moved from matching keyword strings toward understanding which entity a piece of content is actually about.
- **Attributes & Relationships**
  - Attributes are facts a system tracks about a specific entity, such as a company's founding year or industry. Relationships describe how entities connect to each other, such as a person founding a particular company.
- **Disambiguation & Salience**
  - Disambiguation is the process a system uses to determine which specific entity a piece of content refers to when multiple entities share a similar name, such as two different people named Michael Jordan. Salience describes how central an entity is within a given piece of content, distinguishing a page that is genuinely about that entity from one that only mentions it in passing.
- **Knowledge Graphs**
  - A knowledge graph is a database that stores entities and the relationships between them, used by search and AI systems to understand and connect real-world information. Google maintains its own, and Wikidata is a large, open, publicly editable one that many systems reference.

### 2.9 Structured Data & Schema
- **SameAs & Entity Linking**
  - The SameAs property in schema markup links a page's entity to that same entity's presence elsewhere on the web, such as its official social media profiles or Wikipedia page. This helps a system confirm that multiple different pages all refer to the same real-world entity.
- **Org. & Person Schema**
  - Organization schema and Person schema are structured data types used to explicitly identify a company or an individual on a web page. They can include details like name, logo, job title, or affiliation, giving search and AI systems clear, structured facts rather than requiring them to infer this from unstructured text.
- **Product & Place Schema**
  - Product schema and Place schema are structured data types used to explicitly describe a product, such as its price and availability, or a physical location, such as a business address and hours. They let search engines display rich details directly in results and give AI systems clear, structured facts to draw from.
- **Authors & Brands**
  - This refers to schema and structured data specifically identifying the author of a piece of content or the brand behind a product or business. Clearly marking authorship and brand ownership supports both credibility signals and entity recognition across the web.
- **Breadcrumb, Video & Review**
  - Breadcrumb schema marks up the navigational path shown above a page's title, such as Home > Category > Product. Video schema provides structured details about an embedded video, like its duration and thumbnail.
- **Article, FAQ & HowTo**
  - Article schema marks up a piece of content as a news article or blog post, with structured details like publish date and author. FAQ schema marks up a list of questions and answers, sometimes allowing them to display directly in search results.

### 2.10 Structuring for AI Extraction
- **TL;DRs**
  - A TL;DR is a short summary placed at the top of a piece of content, stating the main point before the reader, or an AI system, reads the full explanation. It gives a quick, extractable answer without requiring the entire article to be read or processed.
- **Data Tables**
  - Data tables present information in rows and columns rather than paragraphs of prose. They are easier for both humans scanning quickly and AI systems extracting specific facts to parse accurately, since the structure clearly separates individual data points.
- **Direct Answers**
  - A direct answer is a plainly stated response to a specific question, placed clearly in the content rather than buried inside a long explanation. Content written this way is more likely to be pulled out and used by featured snippets, AI Overviews, and other answer systems.

### 2.11 Featured Snippets
- **Featured Snippets**
  - A featured snippet is a highlighted answer box that sometimes appears at the very top of Google's search results, pulled directly from a page further down the results list. Winning a featured snippet often means writing a clear, direct answer near the top of a page in a format, like a short paragraph or list, that Google can extract cleanly.

### 2.12 SERP Features
- **Sitelinks**
  - Sitelinks are additional links shown beneath a main search result, pointing to other important pages on the same website, such as a contact page or specific product category. They typically appear automatically for well-established sites with a clear internal structure, and cannot be directly requested.
- **Knowledge Panels**
  - A knowledge panel is a box that appears in search results, usually on the right side, summarizing key facts about an entity like a person, company, or place, often pulled from a knowledge graph. Appearing accurately in one depends heavily on having clear, consistent entity information across the web.

### 2.13 Content Lifecicle
- **Content Freshness & Decay**
  - Content freshness is whether a piece of content still reads as current and up to date, which search and AI systems weigh when a query specifically benefits from recent information. Content decay is the gradual decline in a page's rankings and traffic over time as it ages or as competing content improves, requiring an ongoing process of auditing, updating, or consolidating older content to keep it performing.
- **Content Consolidation**
  - Content consolidation is the process of combining multiple low-performing or redundant pages on a website into a single, comprehensive piece of content. By merging similar topics, you reduce keyword cannibalization and create a more authoritative resource that provides greater value to readers.
- **Duplicate Content**
  - Duplicate content is when the same or nearly identical content exists across multiple pages, either on the same site or across different sites. It confuses ranking systems about which version should be shown, and can dilute the ranking signals that would otherwise concentrate on a single strong page.
- **Pruning & Deindexing**
  - Pruning is the practice of removing or merging low-performing, outdated, or thin content from a website rather than letting it accumulate indefinitely. Deindexing is the technical step of formally telling search engines to remove a page from their index, typically done once that content has been pruned or is no longer meant to be found in search.
- **Image & Video Packs**
  - An image pack or video pack is a horizontal row of image or video thumbnails shown within search results for queries where visual content is especially relevant. Appearing in these packs depends on proper image or video optimization and relevant structured data.

### 2.14 AI Tools for Content
- **Surfer SEO**
  - Surfer SEO is a content optimization tool that analyzes top-ranking pages for a target keyword and suggests changes to a draft, such as related terms to include or an appropriate content length, based on what is already performing well.
- **Clearscope**
  - Clearscope is a content optimization tool that grades a piece of writing against top-performing content for a given topic, suggesting relevant terms and concepts that may be missing.
- **MarketMuse**
  - MarketMuse is a content planning and optimization tool that uses AI to identify content gaps within a topic, suggesting what related subjects a site should cover to be seen as comprehensive on that subject.
- **Frase**
  - Frase is a content optimization tool that combines keyword research, content briefs, and AI-assisted writing suggestions, helping writers structure content to match what is already ranking well for a target topic.
- **Breadcrumb rich result**
  - A breadcrumb rich result is when the navigational path of a page, such as Home > Blog > Article, displays directly within its search result listing instead of the full URL. It is enabled through breadcrumb schema markup and gives searchers a clearer sense of where a page sits within a site.

### 2.15 How AI is Changing SEO
- **RAG**
  - RAG stands for Retrieval-Augmented Generation. It is a method where an AI system first retrieves relevant documents or passages from an external source, then uses that retrieved content to generate its answer, rather than relying only on what it learned during training.
- **Embeddings**
  - Embeddings are numerical representations of text that capture its meaning, allowing a computer to compare how similar two pieces of text are. Words or sentences with related meanings end up close together in this numerical space, even if they share no common words.
- **Chunking**
  - Chunking is the process of splitting a long document into smaller pieces before it gets indexed for retrieval. Systems typically search and retrieve at the chunk level rather than the whole-document level, since a smaller, focused piece of text is easier to match accurately to a specific question.

### 2.16 Citation Resources
- **Dense Retrieval**
  - Dense retrieval is a method of finding relevant documents using embeddings and vector similarity, rather than matching exact keywords. It compares the numerical representation of a query against the numerical representations of stored content to find the closest matches by meaning.

### 2.17 Preferred Sources
- **Query Fan-Out**
  - Query fan-out is when an AI system breaks a single user question into several smaller sub-questions before retrieving information to answer it. A question like "best CRM for a small SaaS company" might get split internally into separate queries about pricing, integrations, and reviews.

### 2.18 Agentic Search
- **AI Overviews**
  - AI Overviews are AI-generated summaries that Google shows directly at the top of search results, answering a query before the user scrolls down to individual links. They are built using retrieval from indexed web content, so being cited depends on many of the same technical and content factors as ranking well in normal search results.
- **Google AI Mode**
  - Google AI Mode is a search experience that generates a conversational, AI-written response to a query, going further than a standard AI Overview by allowing follow-up questions within the same session. It draws on retrieved web content, meaning visibility here depends on many of the same technical and content factors as ranking in standard search results.
- **Multi-Step AI Intent**
  - Multi-step AI intent describes how a single user question can require several rounds of reasoning and retrieval before an AI system produces a final answer, rather than one direct lookup. The system may retrieve information, evaluate whether it answers part of the question, then retrieve again to fill remaining gaps.
- **Domain Authority**
  - Domain Authority is a score developed by Moz that estimates how likely an entire website is to rank in search results, based largely on the quantity and quality of links pointing to it. It is measured on a relative scale and is most useful for comparing one site against another, rather than as an absolute number.
- **How Agents Browse**
  - This covers the technical process by which an AI agent navigates websites autonomously, including how it reads page content, follows links, and interprets forms or buttons to complete a task, generally without a human directing each individual step.
- **MCP & Structured Access**
  - MCP, or Model Context Protocol, is a standard that lets AI systems connect to external tools and data sources in a structured, predictable way, rather than only reading unstructured web pages. Structured access through protocols like this can give AI agents more reliable, direct access to a website's data than scraping its rendered HTML.

### 2.19 Link Building
- **ChatGPT Search**
  - ChatGPT Search is a feature that lets ChatGPT retrieve current information from the web when answering a question, rather than relying only on its training data. It presents a conversational answer along with linked sources, similar in concept to a dedicated answer engine.
- **Page Authority**
  - Page Authority is a Moz metric similar to Domain Authority, but measured for a single page instead of an entire website. It estimates how likely that specific page is to rank well, based on the links pointing directly to it.
- **Trust Flow**
  - Trust Flow is a metric from Majestic that estimates how trustworthy a website is, based on the quality of sites linking to it rather than just the quantity. A page linked to by a small number of highly trusted sites can score higher than one linked to by many low-quality sites.
- **Citation Flow**
  - Citation Flow is a metric from Majestic that estimates the raw link popularity of a website, based on how many sites link to it regardless of their quality. It is typically compared alongside Trust Flow, since a large gap between the two can indicate a site has many low-quality links.
- **Perplexity**
  - Perplexity is an AI-powered search product built specifically to answer questions directly, retrieving information from the web and presenting a synthesized response with citations, rather than showing a traditional list of links to click through.
- **Copilot & Gemini**
  - Copilot is Microsoft's AI assistant, integrated into Bing search and other Microsoft products, capable of retrieving web information to answer questions. Gemini is Google's AI assistant, offering similar conversational and retrieval capabilities as a separate product from Google's main search engine.
- **Chat-Based Search**
  - Chat-based search is when someone finds information by asking a conversational AI assistant, such as ChatGPT or Claude, instead of typing a query into a traditional search engine. The assistant may retrieve information from the web, its training data, or both, then respond in natural language rather than showing a results page.

### 2.20 Digital PR
- **Data-Driven PR**
  - Data-driven PR is a specific digital PR tactic where a brand runs original research or a survey, then pitches journalists the resulting statistics as the basis for a story. It gives journalists something concrete and citable to write about, increasing the odds of coverage compared to a generic pitch.
- **Nofollow, Sponsored, UGC**
  - The nofollow attribute tells search engines not to pass ranking credit through a link. The sponsored attribute specifically marks a link as paid or part of an advertising arrangement.

---

## 3. Advanced

### 3.1 Influencer Outreach
- **Ahrefs**
  - Ahrefs is an all-in-one software suite that provides data on backlinks, keyword rankings, and website performance. It works by crawling the web to map out how pages connect to one another, allowing users to analyze their own site’s link profile or research the backlink strategies of competitors.
- **BuzzStream**
  - BuzzStream is an outreach and relationship management tool used in link building and digital PR, helping practitioners track contacts, send pitches, and manage ongoing outreach campaigns at scale.
- **Majestic**
  - Majestic is a backlink analysis tool best known for producing the Trust Flow and Citation Flow metrics, which estimate the quality and quantity of links pointing to a website.
- **Pitchbox**
  - Pitchbox is an outreach automation platform used for link building and digital PR, helping teams find contacts, send templated pitches, and manage follow-ups across large outreach campaigns.

### 3.2 Entity Consistency
- **Author & Org. Consistency**
  - This is making sure the name, biography, and stated facts about an author or organization match wherever they appear, whether on the company's own site, a guest post, or a professional profile. Inconsistent details, such as different job titles or misspelled names, make it harder for a system to confirm it is looking at the same entity.
- **Directories & Databases**
  - Directories and databases are external listings of a business or brand, such as industry directories or structured data sources. They act as independent confirmations of a brand's existence and details, beyond what the brand claims about itself on its own website.
- **Social Profiles**
  - Social profiles are a brand or individual's presence on platforms like LinkedIn or X. They serve as another point of confirmation for a system trying to verify identity, and are often referenced when knowledge graphs cross-check who or what an entity actually is.
- **Unlinked Brand Mentions**
  - An unlinked brand mention is when a brand name is referenced somewhere online without an accompanying clickable link back to its website. These mentions carry little weight in traditional link-based ranking, but they still count as evidence that a brand exists and is being discussed, which matters to entity-based and AI retrieval systems.

### 3.3 Community Presence
- **Niche Forums**
  - Niche forums are smaller, topic-specific online communities focused on a particular industry, hobby, or interest, as opposed to large general platforms. They often contain highly specific, candid discussion that both search and AI systems draw on when answering detailed questions within that niche.

### 3.4 Local Search
- **Google Business Profile**
  - Google Business Profile is a free listing that shows a business's hours, photos, phone number, and reviews directly in Google Maps and local search results. It is typically the single most important asset for any business trying to appear in local search.
- **NAP Consistency**
  - NAP stands for Name, Address, and Phone number. NAP consistency means keeping these three details identical across every website and directory where a business appears, since inconsistencies, such as "St." in one place and "Street" in another, can confuse systems trying to confirm it is the same business.

### 3.5 International SEO
- **Local Citations**
  - A local citation is a mention of a business's name, address, and phone number on another website or directory, even without a clickable link. Citations act as independent confirmations of a business's legitimacy and location, similar to how backlinks confirm a website's authority.
- **Hreflang**
  - Hreflang is an HTML attribute that tells search engines which language and regional version of a page to show to users based on their location and language settings. It prevents search engines from showing the wrong language version, or treating translated versions of the same page as duplicate content.
- **ccTLD, Subfolder, Subdomain**
  - A ccTLD is a country-specific domain ending, like .de for Germany, giving the strongest signal of geographic targeting but requiring separate domains for each market. A subfolder keeps international content under one main domain, such as example.com/de/, while a subdomain places it on a separate address like de.example.com.
- **Geo-Targeting & Localization**
  - Geo-targeting is signaling to search engines which country or region a page is intended for, while localization is adapting the page itself for that audience, including language, currency, spelling, and units. Signals such as hreflang annotations, a country-specific domain or URL structure, and genuinely localized content help search engines serve the right version of a page to the right users.

### 3.6 Video SEO
- **Local Landing Pages**
  - Local landing pages are dedicated pages for each location or service area a business serves, containing details specific to that place such as address, opening hours, services offered, local reviews, and an embedded map. They work best when each page has genuinely unique content rather than a template with only the city name swapped, which risks being treated as thin or duplicate content.

### 3.7 E-commerce SEO
- **E-commerce SEO**
  - Ecommerce SEO is the practice of optimizing an online store's product and category pages so they rank well in search, addressing challenges specific to retail sites like large product catalogs and complex filtering systems.

### 3.8 News & Discovery SEO
- **Reviews & Velocity**
  - Review velocity is how steadily new customer reviews come in over time, not just the overall star rating. A business that suddenly receives many reviews in a single day can look suspicious to review platforms, while a steady, ongoing flow of reviews looks organic and healthy.
- **Local Links**
  - Local links are backlinks from other websites that are relevant to a specific geographic area, such as local news outlets, local business associations, or local bloggers. They typically carry more weight for local rankings than a generic link from an unrelated site with no local connection.
- **Google Discover**
  - Google Discover is a personalized content feed shown on mobile devices, surfacing articles based on a user's interests rather than a specific search query. Appearing in Discover depends on factors like content quality and image optimization, but there is no way to directly target it the way you can target a specific keyword.

### 3.9 Google Search Console
- **Local Pack & Maps**
  - The Local Pack is the block of three business listings, shown alongside a map, that appears at the top of Google's results for local searches such as "coffee shop near me." Appearing in this block depends on a combination of Google Business Profile completeness, reviews, and local relevance.
- **Multi-Location SEO**
  - Multi-location SEO covers strategies specific to businesses with more than one physical location, or businesses that serve a defined area without a fixed storefront, such as a mobile repair service. These businesses need dedicated pages and listings for each location or service area, rather than treating the business as a single generic entity.
- **GSC API & BigQuery Export**
  - The Google Search Console API allows programmatic access to search performance data, rather than only viewing it through the web interface. The BigQuery export sends this data automatically into Google's BigQuery platform, enabling larger scale analysis and longer data retention than Search Console's standard interface allows.

### 3.10 Visibility Metrics
- **Impressions, Clicks & CTR**
  - Impressions are how often a page appears in search results for a query, whether or not anyone clicks it. Clicks are how many people actually click through.
- **Position & Share of Search**
  - Average position is where a page typically ranks for a given query. Share of search measures what percentage of all search interest in a category or topic a brand is actually capturing, which gives a broader view of visibility than tracking individual keyword rankings alone.
- **Branded vs Non-Branded**
  - Branded queries are searches that include a company's name, such as "Nike running shoes," while non-branded queries are generic searches without it, such as "best running shoes." Tracking the split between the two shows whether traffic is coming mostly from people who already know the brand or from people discovering it for the first time.
- **Query & Topic Coverage**
  - Query coverage is how many relevant search queries a site actually appears for, out of all the queries related to its topic. Topic coverage looks at this at a broader level, checking whether a site comprehensively addresses a subject or only touches a small part of it.
- **BrightLocal**
  - BrightLocal is a local SEO platform used for tracking local rankings, auditing citation consistency, and managing reviews across multiple business locations.
- **Whitespark**
  - Whitespark is a local SEO tool focused specifically on citation building and local rank tracking, helping businesses find and correct inconsistent listings across directories.

### 3.11 Rank Tracking
- **Semrush**
  - Semrush is an all-in-one marketing software suite that provides tools for keyword research, competitor analysis, and position tracking. It allows users to monitor their search engine rankings across various devices and locations, offering detailed data on visibility trends and performance changes over time.
- **AccuRanker**
  - AccuRanker is a rank tracking tool built specifically for speed and accuracy at scale, commonly used by agencies and larger sites that need to track rankings for a large number of keywords.

### 3.12 Traffic Analysis
- **Google Analytics**
  - Google Analytics is a free web analytics platform that tracks website traffic, including where visitors come from, which pages they view, and whether they complete meaningful actions like purchases or sign-ups.
- **Microsoft Clarity**
  - Microsoft Clarity is a free analytics tool that provides heatmaps and session recordings, showing how visitors actually move through and interact with a page, rather than just reporting traffic numbers.
- **Google Data Studio**
  - Google Data Studio, now known as Looker Studio, is a free tool for building custom dashboards and reports by pulling data from sources like Google Analytics and Search Console into a single visual interface.
- **LLM Referral Traffic**
  - LLM referral traffic is website visits that originate specifically from a link clicked inside an AI chat assistant's response, such as a source cited by ChatGPT or Perplexity. Tracking it separately from other referral traffic shows how much real, measurable value AI visibility is actually generating.

### 3.13 Zero-Click Attribution
- **Ahrefs Brand Radar**
  - Ahrefs Brand Radar is a feature that tracks how often and how prominently a brand appears within AI-generated answers, extending Ahrefs' existing tracking capabilities from traditional search into AI visibility.

### 3.14 AI Visibility Measurement
- **Prompt Coverage & Mention**
  - Prompt coverage measures how often a brand appears across a representative set of prompts within its category, when tested against AI systems. Mention rate is the frequency of those appearances, whether or not the brand is directly cited as a source.
- **Citation Rate & Position**
  - Citation rate is how often an AI system cites a particular source when generating an answer. Citation position refers to how prominently that source appears within the citations, since being the first source listed generally carries more visibility and credibility than being buried further down.
- **Competitive Answer Share**
  - Competitive answer share measures a brand's presence in AI-generated answers relative to its competitors, across the same set of prompts. It shows whether a brand is winning, losing, or roughly matching its competitors for visibility inside AI systems.
- **Entity & Sentiment**
  - This tracks whether an AI system correctly associates a brand with the right topics and entities, and whether that association carries positive, neutral, or negative sentiment. A brand can be frequently mentioned by an AI system while still being associated with the wrong context or an unfavorable tone.
- **Profound**
  - Profound is a platform built specifically to track how often and how favorably a brand appears within AI-generated answers across different AI systems.
- **Otterly**
  - Otterly is a tool that monitors brand visibility and citations within AI search and chat platforms, tracking how often a brand appears and in what context.
- **Peec**
  - Peec is a platform for tracking a brand's presence and share of voice within AI-generated answers, comparing performance against competitors across a defined set of prompts.

### 3.15 GEO & SEO Testing
- **Content & Schema A/B Tests**
  - This is testing two versions of a page's content or structured data against each other to see which one performs better in search or AI visibility, rather than assuming a change is an improvement without checking.
- **Before/After Prompt Tests**
  - This means running the same set of AI prompts before and after making a change to a website, then comparing the answers to see whether the change actually affected how AI systems describe or cite the brand.
- **Competitor Benchmarking**
  - Competitor benchmarking is the practice of comparing a website's search and AI visibility performance directly against competitors, rather than only tracking its own metrics in isolation. It gives context for whether a given number is actually good or bad within the competitive landscape.

### 3.16 SEO Audits
- **SEO Audits**
  - An SEO audit is a structured review of a website's technical health, content quality, and backlink profile, identifying issues and opportunities across all of these areas at once. It is typically the first step in diagnosing why a site is underperforming or in establishing a baseline before starting new work.

---

## 4. Optional / Specialized Topics

- What is SEO
- Personalization, Localization
- Training Data vs Grounding
- SERP, Index, Crawl
- Site Reputation Abuse
- Expired Domain Abuse
- ClaudeBot
- Google-Extended
- Index Coverage & Bloat
- Log File Analysis
- Managing AI Crawlers
- Controls & Pay-Per-Crawl
- Screaming Frog
- Sitebulb
- SSR vs CSR vs Hydration
- PerplexityBot
- Title Tags
- Meta Descriptions
- Internal Anchor Text
- Image Optimization
- SERP Analysis
- Breadcrumb, Video & Review
- Article, FAQ & HowTo
- Image & Video Packs
- Breadcrumb rich result

---

## 5. References

- [SEO Specialist Roadmap](https://roadmap.sh/seo)

---

## 6. Related Roles / Topics

### Related Roles
- Frontend Developer
- AI Engineer
- Fullstack Developer

### Related Skills
- Html
- Css
- JavaScript
- System Design