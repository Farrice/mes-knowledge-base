# videos-watchlist — source: https://help.sandcastles.ai/How-to-Use-the-videos-watchlist-tool-Sandcastles-MCP-35eacc48f1da8184ae51e16da2e98968 — captured 2026-08-27

Page title: How to Use the /videos-watchlist tool (Sandcastles MCP in Claude)
Category: MCP
Last Updated: August 9, 2026 1:39 PM

## Understanding the /videos-watchlist Tool

The `/videos-watchlist` tool within Sandcastles is designed to help video creators analyze their content's performance. It allows you to quickly see the top-performing videos from your watchlist.

## Key Features:

- Performance Ranking: Identifies your best-performing videos based on engagement.
- Customizable Filters: You can specify criteria such as a minimum engagement rate (e.g., above 2%) and exclude boosted entries.
- Direct Links: Provides direct links to the videos and information about the creators.
- Data Analysis: Analyzes videos based on views, engagement rate (ER), and other relevant metrics.

## How to Use the /videos-watchlist Tool

1. Access the Tool: Navigate to the "Cowork" section and type `/videos-watchlist` into the prompt.
2. Specify Your Request: You can refine your search by adding parameters. For example, to see top-performing videos from your watch list in the last 28 days, with an engagement rate above 2% (excluding boosted entries), you would use the following prompt:

   ```
   /videos-watchlist Show me the top performing videos from my watch list in the last 28 days. Order them based on views, but don't show me any that have below a 2% engagement rate. Those have been boosted, and I don't want those. I just want them in order above 2%, and then I want you to give me the link to the video as well as the creator who made it.
   ```

3. Initiate the Search: Press Enter or click the send/queue button to run the query.

## Interpreting the Results

The tool will return a ranked list of videos based on your specified criteria. Each entry typically includes:

- The creator's handle (e.g., `@connectwithgrowth`)
- Key metrics such as views and engagement rate (ER)
- The video title or a brief description
- A direct link to the video

### Example Output:

```
Loaded tools, used sandcastles Integration
Top performing videos from your watchlist - last 28 days, sorted by views, with engagement >2% (boosted entries at 2% flat excluded).
1. @connectwithgrowth - 4.9M views, 8% ER - "He Deleted Social Media Because of This" -> video
2. @devinjatho - 3.48M views, 4% ER - "Comment GEAR For My Equipment List" -> video
3. @monthebrain - 1.79M views, 5% ER - "Your Beliefs Impact your dopamine system" -> video
...
```

## Further Analysis

For videos that haven't been analyzed by Sandcastles (e.g., "Oren's perfect size home", "Devin's trial reels", and "Oren's "Loneliness, friendship, and brands""), you can request deeper analysis on hooks, formats, and narrative structure.

## Support

If you have any questions or need further assistance with the `/videos-watchlist` tool, please contact us at support@sandcastles.ai
