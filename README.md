# Alfred - Google Search

<p align="center">
<img src="https://github.com/aviaryan/alfred-google-search/raw/master/src/icon.png">
</p>

**Tested with Alfred 3**

This workflow allows you to do in-line Google searches right from the Alfred bar.
It gives you the flexibility to either open the result URL or copy it to clipboard.


## IMPORTANT

Adapted from [gsearch's README](https://github.com/aviaryan/python-gsearch)

> Overusing this workflow might lead to your IP being blocked by Google Search servers.
Searches through Chrome or another browser might still work but this workflow will stop working.
I recommend keeping a 10-15 seconds gap after each usage of this workflow.
In most cases, much lower gaps or even continuous use of the workflow will still work but still this is something to be kept in mind.
If you see a 'rate limit' or a 503 error, it's best to stop using the workflow and try back after some time (~1 minute).


## Installing

Download [Google Search workflow file](https://github.com/aviaryan/alfred-google-search/raw/master/GoogleSearch.alfredworkflow) 
and double click to open it with Alfred.


## Using

```sh
# search, ENTER to open result in browser
gs search query
# search, ENTER to copy URL to clipboard
gs search query$
```

Ending the search query with a '$' changes the workflow behavior to copy URL instead of opening the URL.


## Screenshots

![Default UI](https://i.imgur.com/8fGcx4j.png)

![Search 1](https://i.imgur.com/WeBLxZp.png)

![Search 2 with Clipboard](https://i.imgur.com/Ob5QyrU.png)

![Unicode](https://i.imgur.com/h6Pe6IK.png)


## Inspiration

[Vinta's workflow](https://github.com/vinta/alfred-google-inline-workflow). 
It doesn't work right now and probably it never will, 
and this gave me the motivation to create this workflow with a different approach.
I hope this workflow will continue working for some time to come.


----

⭐️ [Donate](https://www.paypal.me/aviaryan) ⭐️
