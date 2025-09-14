# What were done to have the current structure of data?
0. Created pdf splitter script to split pdf so that llm(claude) can see patterns in the pdf.
1. Extracted text from the constitution pdf using `https://tools.pdf24.org/pdf-to-hmtl` or `https://www.idrsolutions.dom/online-pdf-to-html5-converter`. One gave less boiler plate.
2. Cleaned up the text to ignore initial parts and later schedule parts.
3. Created script to extract structured json from the parts and articles. This took some iteration. Got `constitution.json`.
4. Generating Q&A was also somewhat manual, llms won't take all the content so I had to copy paste chunks of content to get Q&A. Stored in a json file as an array.
5. Created a script `build_webpage.py` to convert those jsons to html. Uses a template html. Had to iterate here for a good enough UI as well.
6. Used splitter to split out the schedules and asked llm to extract. Did pretty well. Needed very few manual steps - just did some cleanups. This gave `constitution_schedules.json`.
7. Merged schedules into `constitution.json`.
8. Updated the webpage to integrate schedules and search.
