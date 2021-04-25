##### Table of Contents  
[Headers](#headers)  
[Emphasis](#emphasis)  
[Lists](#lists)  
[Links](#links)  
[Images](#images)  
[Code and Syntax Highlighting](#code)  
[Tables](#tables)  
[Blockquotes](#blockquotes)  
[Inline HTML](#html)  
[Horizontal Rule](#hr)  
[Line Breaks](#lines)  
[YouTube Videos](#videos)  

<a name="headers"/>

## Headers

```no-highlight
# H1
## H2
### H3
#### H4
##### H5
###### H6

Alternatively, for H1 and H2, an underline-ish style:

Alt-H1
======

Alt-H2
------
```

# H1
## H2
### H3
#### H4
##### H5
###### H6

Alternatively, for H1 and H2, an underline-ish style:

Alt-H1
======

Alt-H2
------

<a name="emphasis"/>

## Emphasis

```no-highlight
Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~
```

Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~


<a name="lists"/>

## Lists

(In this example, leading and trailing spaces are shown with with dots: ⋅)

```no-highlight
1. First ordered list item
2. Another item
⋅⋅* Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.

⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses
```

1. First ordered list item
2. Another item
  * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
  1. Ordered sub-list
4. And another item.

   You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

   To have a line break without a paragraph, you will need to use two trailing spaces.  
   Note that this line is separate, but within the same paragraph.  
   (This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses

<a name="links"/>

## Links

There are two ways to create links.

```no-highlight
[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com
```

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com

<a name="images"/>

## Images

```no-highlight
Here's our logo (hover to see the title text):

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style: 
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"
```

Here's our logo (hover to see the title text):

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style: 
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

<a name="code"/>

## Code and Syntax Highlighting

Code blocks are part of the Markdown spec, but syntax highlighting isn't. However, many renderers -- like Github's and *Markdown Here* -- support syntax highlighting. Which languages are supported and how those language names should be written will vary from renderer to renderer. *Markdown Here* supports highlighting for dozens of languages (and not-really-languages, like diffs and HTTP headers); to see the complete list, and how to write the language names, see the [highlight.js demo page](http://softwaremaniacs.org/media/soft/highlight/test.html).

```no-highlight
Inline `code` has `back-ticks around` it.
```

Inline `code` has `back-ticks around` it.

Blocks of code are either fenced by lines with three back-ticks <code>```</code>, or are indented with four spaces. I recommend only using the fenced code blocks -- they're easier and only they support syntax highlighting.

<pre lang="no-highlight"><code>```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
No language indicated, so no syntax highlighting. 
But let's throw in a &lt;b&gt;tag&lt;/b&gt;.
```
</code></pre>



```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```

```
No language indicated, so no syntax highlighting in Markdown Here (varies on Github). 
But let's throw in a <b>tag</b>.
```


<a name="tables"/>

## Tables

Tables aren't part of the core Markdown spec, but they are part of GFM and *Markdown Here* supports them. They are an easy way of adding tables to your email -- a task that would otherwise require copy-pasting from another application.

```no-highlight
Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3
```

Colons can be used to align columns.

| Tables        | Are           | Cool |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell. The outer pipes (|) are optional, and you don't need to make the raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

<a name="blockquotes"/>

## Blockquotes

```no-highlight
> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 
```

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 

<a name="html"/>

## Inline HTML

You can also use raw HTML in your Markdown, and it'll mostly work pretty well. 

```no-highlight
<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>
```

<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>

<a name="hr"/>

## Horizontal Rule

```
Three or more...

---

Hyphens

***

Asterisks

___

Underscores
```

Three or more...

---

Hyphens

***

Asterisks

___

Underscores

<a name="lines"/>

## Line Breaks

My basic recommendation for learning how line breaks work is to experiment and discover -- hit &lt;Enter&gt; once (i.e., insert one newline), then hit it twice (i.e., insert two newlines), see what happens. You'll soon learn to get what you want. "Markdown Toggle" is your friend. 

Here are some things to try out:

```
Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also a separate paragraph, but...
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.
```

Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also begins a separate paragraph, but...  
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.

(Technical note: *Markdown Here* uses GFM line breaks, so there's no need to use MD's two-space line breaks.)

<a name="videos"/>

## YouTube Videos

They can't be added directly but you can add an image with a link to the video like this:

```no-highlight
<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
```

Or, in pure Markdown, but losing the image sizing and border:

```no-highlight
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
```

Referencing a bug by #bugID in your git commit links it to the slip. For example #1. 

---

## Tools

A bigger list of tools (that probably negates the need for this page) can be found at [github.com/writekit/awesome-markdown](https://github.com/writekit/awesome-markdown).

### Editors

* [StackEdit](https://stackedit.io): In-browser MD document editor
* [Minimalist Online Markdown Editor](http://markdown.pioul.fr/)
* [Mou](http://25.io/mou/): macOS editor
* [Haroopad](http://pad.haroopress.com/user.html): Cross-platform editor


## Libraries

### JavaScript

* [Marked](https://github.com/chjj/marked)
* [Remarkable](https://github.com/jonschlinkert/remarkable)
* [PageDown](https://code.google.com/p/pagedown/) (and [PageDown Extra](https://github.com/jmcmanus/pagedown-extra))
* [markdown-it](https://github.com/markdown-it/markdown-it)
* [Gitdown](https://github.com/gajus/gitdown): GitHub markdown preprocessor
* [reMarked.js](https://github.com/leeoniya/reMarked.js): HTML-to-Markdown processor
* [Kramed](https://github.com/GitbookIO/kramed): Fork of Marked

License: [CC-BY](https://creativecommons.org/licenses/by/3.0/)

-
-
-
-

# Tips and Tricks

##### Table of Contents  

[Pasting from Clipboard (without tears)](#pasting)  
[Using an email signature](#sigs)  
[Footnotes](#footnotes)  
[Using other TeX math formulae renderers](#tex)  
[Changing the Main Font (and other overall styles)](#mainfont)  
[Getting fancy with inline HTML](#inlinehtml)  
[Cool CSS stuff](#css)  
[Creating more complex tables](#tables)  
[Getting original Markdown from sent email](#post-send-md)  
[Using Header Anchor Links](#header-anchors)

<a name="pasting" href="#"></a>
Pasting from Clipboard (without tears)
======================

If text is pasted from the clipboard with formatting intact, it can negatively impact the rendering of Markdown (i.e., it can make it super messed up). When pasting into an email that you plan on rendering with Markdown Here, you should try to paste as plain text.

### Windows and Linux

- **Chrome**: Context menu: "Paste as plain text". Hotkey: `Ctrl+Shift+V`.
- **Firefox**: There doesn't seem to be a menu item. Hotkey: `Ctrl+Shift+V`.
- **Thunderbird, Postbox**: _Edit_ menu and context menu: "Paste Without Formatting". Hotkey: `Ctrl+Shift+V`.

(Linux: Tested on Xubuntu.)

### Mac OS X

- **Chrome**: _Edit_ menu and context menu: "Paste and Match Style". Hotkey: ⇧⌘V (`Shift+Command+V`).
- **Firefox**: There doesn't seem to be a menu item. Hotkey: ⇧⌘V (`Shift+Command+V`).
- **Thunderbird, Postbox**: _Edit_ menu and context menu: "Paste Without Formatting". Hotkey: ⇧⌘V (`Shift+Command+V`).


<a name="sigs" href="#"></a>
Using email signatures
======================

Email signatures are automatically excluded from conversion. Specifically, anything after the semi-standard `'-- '` (note the trailing space) is left alone.

Note that Hotmail and Yahoo do not automatically add the `'-- '` to signatures, so you have to add it yourself.


<a name="footnotes" href="#"></a>
Footnotes
======================

Below is a copy-paste of a workaround described in the [feature request/issue](https://github.com/adam-p/markdown-here/issues/94) for adding footnotes:

I thought of a bit of a hack you can use to emulate your footnotes: put inline HTML `<sup>` tags<sup>1</sup>. What I just did there looks like this: `<sup>1</sup>`. Then you can put a numbered list<sup>2</sup> at the bottom with the actual footnotes. 

The numbered list in your original email had a larger left-side margin than mine will, but you could modify your "Primary Styling CSS" in the MDH options to and add something like `margin-left: 10em;` to the `ol` rule. But then it'd be like that for all your numbered lists.

You also have the carriage-return-ish icon in your footnotes at the bottom, but they're not links that lead back to the anchor, so... maybe you don't need them? If you want to add them by hand you can use the HTML entity<sup>3</sup> `&crarr;`. Like so: &crarr;

I haven't been using the square brackets around the footnote super numbers because there's a danger of them ending up being reference-style MD links<sup>4</sup>. Like this<sup>[11]</sup> but not like this<sup>[12]</sup>.

[11]: http://markdown-here.com

Anyway, maybe this will help you and maybe it won't. It's probably more hassle than you're happy with. I'll include the raw version of this email below so that you can see it.

1. Gratuitous link to info about the `<sup>` tag: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup
2. [MD cheatsheet entry for lists](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#wiki-lists)
3. [List of HTML entities](http://www.w3schools.com/tags/ref_symbols.asp)
4. https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links

---

```
I thought of a bit of a hack you can use to emulate your footnotes: put inline HTML `<sup>` tags<sup>1</sup>. What I just did there looks like this: `<sup>1</sup>`. Then you can put a numbered list<sup>2</sup> at the bottom with the actual footnotes. 

The numbered list in your original email had a larger left-side margin than mine will, but you could modify your "Primary Styling CSS" in the MDH options to and add something like `margin-left: 10em;` to the `ol` rule. But then it'd be like that for all your numbered lists.

You also have the carriage-return-ish icon in your footnotes at the bottom, but they're not links that lead back to the anchor, so... maybe you don't need them? If you want to add them by hand you can use the HTML entity<sup>3</sup> `&crarr;`. Like so: &crarr;

I haven't been using the square brackets around the footnote super numbers because there's a danger of them ending up being reference-style MD links<sup>4</sup>. Like this<sup>[11]</sup> but not like this<sup>[12]</sup>.

[11]: http://markdown-here.com

Anyway, maybe this will help you and maybe it won't. It's probably more hassle than you're happy with. I'll include the raw version of this email below so that you can see it.

1. Gratuitous link to info about the `<sup>` tag: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup
2. [MD cheatsheet entry for lists](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#wiki-lists)
3. [List of HTML entities](http://www.w3schools.com/tags/ref_symbols.asp)
4. https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links
```


<a name="svg" href="#"></a>
<a name="tex" href="#"></a>
Using other TeX math formulae renderers
======================

The default Google Charts service that Markdown Here uses for TeX math rendering doesn't support all math symbols (like [`\cong`](https://github.com/adam-p/markdown-here/issues/199)), and doesn't provide very crisp images. It was chosen because it was thought (by me) to be the least bad option, privacy-wise (because you're probably already using Google for your email). However, there are other possibilities, if you're willing to accept the implications. 

[CodeCogs](http://www.codecogs.com/) supports a wider range of symbols (I think) and provides more rendering targets. You can fool around with its [equation editor here](http://www.codecogs.com/latex/eqneditor.php). To use CodeCogs to produce PNG images, set this in Markdown Here's "TeX Mathematical Formulae Support" option:

```no-highlight
<img src="https://latex.codecogs.com/png.latex?{urlmathcode}" alt="{mathcode}">
```

Using this will give you nice smooth SVG images, but note that they will get stripped out of email:

```no-highlight
<img src="https://latex.codecogs.com/svg.latex?{urlmathcode}" alt="{mathcode}">
```

But please note a few important things:

- You're in charge of making sure that you're not violating [CodeCogs' terms of use](http://www.codecogs.com/pages/agreements/termsofuse.php). You should also check out [their privacy policy](http://www.codecogs.com/pages/agreements/privacy_policy.php).

- Understand that CodeCogs will be able to see all of your formulae. They can also do things map your IP address to your formulae. And then they can record the IP addresses of the people that read your email and view the formulae. And so they can draw some conclusions that someone at your IP address working with people at your friends' IP addresses.

For more discussion and technical info, see [issue #144](https://github.com/adam-p/markdown-here/issues/144).


<a name="mainfont" href="#"></a>
Changing the Main Font (and other overall styles)
======================

In the "Primary Styling CSS" section of the Markdown Here options page, there is a rule for `.markdown-here-wrapper` (that's empty by default). This rule should be used for styles that you want applied to your entire email (overridden by other styles, of course). 

So, if you wanted Verdana as your default font, you could set this:

```
.markdown-here-wrapper {
  font-family: Verdana, sans;
}
```
and this (if you want to apply the new font not only to the first row of your tables):
```
table tr th, table tr td {
  font-family: Verdana, sans;
  ...
}
```

![main font example](https://f.cloud.github.com/assets/425687/588697/75922c86-c992-11e2-8071-f42f40295e3c.gif)


<a name="inlinehtml" href="#"></a>
Getting fancy with inline HTML
======================

Markdown (and Markdown Here) allows for inline HTML tags to be used when writing the Markdown, and having them preserved when rendering. This provides you with the ability to add more powerful styling than is possible with Markdown or email alone.

You probably don't want to use these tricks too often, since they involve a lot more (and less natural) typing than normal Markdown, but they can let you do very powerful things that you can't otherwise.

**PLEASE NOTE:** _Always test_ to your fancy styles and HTML tags by sending an email that uses them to yourself and then viewing the email. Some email clients strip out some styles, so it might look good when you send it, but not when you receive it.

### HTML Tags

Some HTML tags that aren't available in a normal email client can be used if typed directly. For example, you can get superscripts and subscripts like this:

```
hi<sup>1</sup> low<sub>2</sub>
```

The result will look like this: hi<sup>1</sup> low<sub>2</sub>

TODO: More examples?

### Custom CSS classes

In Markdown Here's "Primary Styling CSS" you can create custom CSS classes that apply to `<span>` elements that you use inline. 

Let's say you want to the background color of some text in your email to be a nice gradient from light blue to light pink and have a big horrible border. You could create a CSS rule like this:

```
.hi {
  background: linear-gradient(225deg, lightpink, lightblue);
  border: thick dotted purple;
} 
```

And then use it in your email something like this:

```
Happy <span class="hi">Birthday</span> my friend!
```

(The preview of it won't show properly here, but try it out yourself in your email.)

TODO: More compelling, less ridiculous examples.


<a name="css" href="#"></a>
Cool CSS stuff
==================

### Different numbering for ordered lists

By defaults, ordered (aka numbered) lists use ordinary Arabic numbers (1, 2, 3, ...). But with a single CSS rule you can use Roman numerals, or Greek letters, or Thai numbers, and [lots of others](https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type):

```css
ol {
  list-style-type: lower-greek;
}
```

<a name="salutation" href="#"></a>
### Salutation Styling

If you want to style the salutation of your email differently from the rest of the email, you can add a CSS rule that applies to the very first paragraph like so:

```css
.markdown-here-wrapper > p:first-of-type {
  color: red;
}
```

(Note that this will apply to the first paragraph of all MDH-rendered chunks in an email. So if you're rendering multiple selections you'll get multiple red paragraphs. For my complex CSS to fix this, check out [this SO post](https://stackoverflow.com/questions/2717480/css-selector-for-first-element-with-class/8539107#8539107).)


<a name="tables" href="#"></a>
Creating more complex tables
======================

There is a [feature request](https://github.com/adam-p/markdown-here/issues/176) for adding the ability to span cells across rows and columns, but it hasn't yet been implemented. 

Probably the best way to do rowspan and colspan right now is to use this [online HTML table generator](http://www.tablesgenerator.com/html_tables) to create your table, and then paste it into your email (or whatever) and use MDH to render it. *Make sure* to check the boxes for "Do not generate CSS" (because MDH provides the CSS) and "Compact mode" (to avoid MDH's multi-line HTML [problem](https://github.com/adam-p/markdown-here/issues/157)).

### Header-less tables

See [this issue comment](https://github.com/adam-p/markdown-here/issues/266#issuecomment-85580214) for help on approximately creating a table without a header row (without using HTML).


<a name="post-send-md" href="#"></a>
Getting original Markdown from sent email
=========================================

There is an outstanding [feature request](https://github.com/adam-p/markdown-here/issues/252) to be able to get the original Markdown from a sent email, but for now there's an easy trick to get it:

1. Open the message.
2. Start a forward of it.
3. Markdown Toggle.
4. The forward content will be replaced with the original Markdown.

This has been tested in Gmail and Thunderbird. If the mail client quotes the forwarded content, then it won't work.


<a name="header-anchors" href="#"></a>
Using Header Anchor Links
=========================

[Stub. Someone (like me or Casey) should fill this in. Also, this section should probably not be at the bottom of the page -- it should probably be second or third.]
