# PF2TiddlyWiki
TiddlyWiki based reference to Pathfinder 2e OGL material.

The objective of this repository is to build a PF2 reference, similar to the Archives of Nethys, within TiddlyWiki.

## Why bother, when there's already Nethys/Easytool/etc?

There are two advantages to using TiddlyWiki:

* The entire database is stored in a single .HTML file. This can then be used anywhere where there's a web browser, or loaded into standard apps for manipulating TiddlyWikis.
* The TiddlyWiki engine has very strong support for semantic annotations on pages - in other words, for allowing the wiki to understand the meanings of pages as well as just the text. This allows intelligent searches, like "all Barbarian feats above level 1" to be much more easily expressed.

In addition, a core goal of this reference is to make the rules more readable by two methods:

* Increasing the spacing of rules so that each key rule is a separate paragraph, making it much easier to "scan" to discover all rules - as is often necessary when looking things up quickly during a game.
* Collapsing backreferences. For example, in most references, the text on Step reads: "You can't step into difficult terrain." This one reads: "You can't step into difficult terrain unless you have Feather Step." Unless you happen to read through the entire section on Feats, you won't notice that modification. TiddlyWiki's database mechanic can help greatly in doing this, but ultimately it's a matter of writing.

## Sounds good! How do I do the thing?

If you just want to use the reference, just download `output/index.html`. This stores the entire reference and is completely self-contained. You can copy it, put it on the cloud, stick it on mobile devices, and so on.

Note that if you use the reference this way, your edits will **not** be saved, so this can't be used for contributing or updating the reference.

## And if I want to contribute?

If you want to contribute, you'll need to:

1. Install Node.js from `https://nodejs.org/en/`.
2. Install TiddlyWiki from npm (`npm -g install tiddlywiki`).
3. Clone the repository into a suitable directory, let's say `PF2TiddlyWiki`.
4. From the parent of that directory, run `tiddlywiki PF2TiddlyWiki --listen`.
5. Open `localhost:8080` in a web browser.

Your edits will now be saved into the `.tid` files, and you can make changes, then commit and pull request the GitHub repository in the normal way. When you're done, you can just Ctrl-C or otherwise halt the TiddlyWiki process; it doesn't cache edits, so just gunning it won't lose any changes.


